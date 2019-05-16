import logging
from pyformance import time_calls
import pymongo

from core.managed import Managed
from mongo_integration.publish import publish_document, publish_metadata
from mongo_integration.retrieve import  find_document, find_metadata


class MongoManager(Managed):

    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger("MongoManager")

        self.username = self.config["username"]
        self.password = self.config["password"]
        self.host = self.config["host"]
        self.port = self.config["port"]
        self.dbName = self.config["database"]
        self.collectionName = self.config["collection"]
        self.namespace = self.config["namespace"]

        self.client = pymongo.MongoClient(self.host, self.port)
        self.dbInstance = self.client[self.dbName]
        self.collectionInstance = self.dbInstance[self.collectionName]

    def start(self):
        pass

    @time_calls
    def retrieve_metadata(self, query):
        retrievedMetadata = find_metadata(self.collectionInstance, query)
        return retrievedMetadata

    @time_calls
    def retrieve_document(self, documentName):
        retrieved = find_document(self.dbInstance, self.namespace, documentName)
        return retrieved

    @time_calls
    def store_metadata(self, dictionary):
        publishedMetadata = publish_metadata(self.collectionInstance, dictionary)
        return publishedMetadata

    @time_calls
    def store_document(self, document, documentName):
        publishedDocument = publish_document(self.dbInstance, self.namespace, document, documentName)
        return publishedDocument

