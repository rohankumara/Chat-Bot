from random import choice

class PickStrategy:

    @classmethod
    def get_random(cls, answers_list):
        return choice(answers_list)