import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient(
    "mongodb+srv://japuerta:ABCDE54321@misiontic2022.nam7cyu.mongodb.net/results_db?retryWrites=true&w=majority",
    tlsCAFile=ca
)

db = client.test
print(db)

data_base = client['results_db']
print(data_base.list_collection_names())

collection = data_base.get_collection('candidate')
print(collection.find())
