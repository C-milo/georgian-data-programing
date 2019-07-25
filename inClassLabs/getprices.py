import json
from bson import BSON
from bson import json_util
import dns
from pymongo import MongoClient


client = MongoClient('mongodb+srv://dbuser:M4ng0357!@cluster0-ubk6k.azure.mongodb.net/test?retryWrites=true&w=majority')
db = client.test
collection = db['test']
cursor = collection.find({})

for document in cursor:
    final = json.dumps(document, indent=4, default=json_util.default)
    print(final)
exit()