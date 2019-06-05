import json
import sys
import datetime
import uuid
from collections import defaultdict
from pymongo import MongoClient
from bson.son import SON
from config.settings import DB_NAME, DB_URL, COLLECTION_NAME


class BaseMongoConnector(object):
    def __init__(self, parameters):
        self.parameters = parameters
        self.client = MongoClient(DB_URL)
        self.db = getattr(self.client, DB_NAME)
        self.collection = getattr(self.db, COLLECTION_NAME)

    def __str__(self):
        return f'Mongo Connector Class - Database: {self.db.name}, Collection: {self.collection.name}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.parameters})'
        

class InsertMongoConnector(BaseMongoConnector):
    
    def insert(self):
        self.collection.insert_one(self.parameters)
