#encoding=utf-8
from unittest import TestCase

from chatter_learning.brains.closest_mean import ClosestMean
from chatter_learning.store_adapters import Mongodb

class TestClosestMean(TestCase):

    def setUp(self):
        self.closest_mean = ClosestMean()
        self.closest_mean.set_store(Mongodb(database_name='test_database'))


    def tearDown(self):
        self.closest_mean.drop_store()

    def test_process(self):
        self.closest_mean.store.put_answer('你幾歲', '22')
        self.closest_mean.store.put_answer('你現在幾年級', '碩一')
        self.closest_mean.store.put_answer('你今年幾歲', '22')
        confidence, result = self.closest_mean.process('幾歲')
        self.assertEqual(confidence, 0.5)
        self.assertEqual(result, '22')

    def test_get_similarity(self):
        result = self.closest_mean.get_similarity('我目前就讀於台北科技大學', '台北')
        self.assertEqual(result, 1)
        result = self.closest_mean.get_similarity('我目前就讀於台北科技大學資工碩一', '資工碩一')
        self.assertEqual(result, 2)
