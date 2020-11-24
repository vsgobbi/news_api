from pymongo import MongoClient
from json import loads
from bson import json_util

client = MongoClient(
    "mongodb+srv://teste:teste@cluster0.jeyvf.mongodb.net/news_portal?retryWrites=false&w=majority"
)

db = client.test
news_collection = db.news
authors_collection = db.authors


class PyMongoParser:

    @classmethod
    def parse_json(cls, data):
        return loads(json_util.dumps(data))
