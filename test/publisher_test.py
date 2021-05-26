import unittest
from src.pubsub.publisher import Publisher


class PublisherTest(unittest.TestCase):

    def test_raise_exception_for_none_topic_name_and_project_id(self):
        self.assertRaises(Exception, Publisher)
