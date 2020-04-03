from unittest import TestCase
from chatter_learning.store_adapters import Mongodb

class TestMongodb(TestCase):

    def setUp(self):
        self.mongodb = Mongodb(database_name='test_database')


    def tearDown(self):
        self.mongodb.drop()

    def test_get(self):
        self.mongodb.put_answer('how are you', 'im fine')
        actual = self.mongodb.get('how are you')
        self.assertEqual(actual['answers'], ['im fine'])

    def test_put_answer(self):
        self.mongodb.put_answer('how are you', 'im fine')
        actual = self.mongodb.get('how are you')
        self.assertEqual(actual, ['im fine'])
        self.mongodb.put_answer('how are you', 'cool')
        actual = self.mongodb.get('how are you')
        self.assertEqual(actual, ['im fine', 'cool'])

    def test_list(self):
        self.mongodb.put_answer('how are you', 'im fine')
        self.mongodb.put_answer('are you a boy or girl?', 'boy')
        self.mongodb.put_answer('are you a boy or girl?', 'girl')
        self.mongodb.put_answer('how old are you', '23')
        list = self.mongodb.list()
        self.assertEqual(len(list), 3)

    def test_filter(self):
        self.mongodb.put_answer('how are you', 'im fine')
        self.mongodb.put_answer('are you a boy or girl?', 'boy')
        self.mongodb.put_answer('are you a boy or girl?', 'girl')
        self.mongodb.put_answer('how old are you', '23')
        result = self.mongodb.filter('old')[0]
        self.assertEqual(result['answers'], ['23'])


