from chatter_learning.store_adapters import BaseStore
from pymongo import MongoClient
class Mongodb(BaseStore):

    def __init__(self, **kwargs):
        self.database_url = kwargs.get('database_url', 'mongodb://127.0.0.1:27017')
        self.database_name = kwargs.get('database_name', 'chatterLearning')
        self.client = MongoClient(self.database_url)
        self.database = self.client[self.database_name]
        self.conversations = self.database['conversations']

    def get(self, key):
        data = self.conversations.find_one({'ask': key})
        if not data:
            return None
        return data

    def put_answer(self, ask, answer):
        data = self.conversations.find_one({'ask': ask})
        if data is None:
            data = dict()
            data['answers'] = list()
        data['ask'] = ask
        data['answers'].append(answer)
        self.conversations.replace_one({'ask': ask}, data, True)

    def list(self):
        matches = self.conversations.find()
        matches = list(matches)
        return matches

    def list_answers(self):
        matches = self.conversations.find()
        matches = list(matches)
        answers_list = []
        for match in matches:
            answers_list += match['answers']
        return answers_list

    def filter(self, word = None):
        if word is None:
            matches = self.conversations.find()
        else:
            regex = ".*%s.*" % word
            matches = self.conversations.find({'ask': {"$regex" : regex}})
        matches = list(matches)
        return matches

    def drop(self):
        self.client.drop_database(self.database_name)
