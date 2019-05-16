import mongomock
import unittest

from mongo_integration.retrieve import find_metadata
from mongo_integration.publish import publish_metadata


class mongoTest(unittest.TestCase):

    def setUp(self):
        self.testDoc = {"_id": "56", "firstname": "Bob"}
        self.collection = mongomock.MongoClient().db.collection


    def test_retrieve_meta(self):
        self.collection.insert_one(self.testDoc)
        result = find_metadata(self.collection, self.testDoc)
        self.assertDictEqual(result, self.testDoc)

    def test_publish_meta(self):
        result = publish_metadata(self.collection, self.testDoc)
        assert result == "56"

