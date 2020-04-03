#encoding=utf-8
import os
from chatter_learning.brains import ClosestMean
from chatter_learning.brains.closest_method import ClosestMethod
from chatter_learning.store_adapters import Mongodb


class Chatter(object):
    def __init__(self, **kwargs):

        brain_name = kwargs.get('brain', 'closest_method')
        storage_name = kwargs.get('storage', 'mongodb')
        self.set_store(storage_name, **kwargs)
        self.set_brain(brain_name, **kwargs)
        self.connected_brain_on_store()
        self.recent_answers = []
    def set_store(self, store_adapter_name, **kwargs):
        if store_adapter_name == 'mongodb':
            self.store = Mongodb(**kwargs)

    def set_brain(self, brain_name, **kwargs):
        if brain_name == 'closest_mean':
            self.brain = ClosestMean(**kwargs)
        elif brain_name == 'closest_method':
            self.brain = ClosestMethod(**kwargs)

    def connected_brain_on_store(self):
        self.brain.set_store(self.store)

    def get_previous_answers(self):
        return self.recent_answers[-1]

    def append_answer_to_question(self, question, answer):
        self.store.put_answer(question, answer)


    def response_to(self, ask):
        confidence, response = self.brain.process(ask)
        current_conversation = {
            'ask': ask,
            'answers': []
        }
        conversation = self.store.get(ask)
        if conversation:
            current_conversation = conversation
        if len(self.recent_answers) > 0:
            previous_answer = self.get_previous_answers()
            self.append_answer_to_question(previous_answer, ask)
        self.recent_answers.append(response)
        return response

