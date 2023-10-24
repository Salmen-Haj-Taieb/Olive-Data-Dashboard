
from dotenv import load_dotenv,find_dotenv
from pymongo import MongoClient
load_dotenv(find_dotenv())
connection_string = "mongodb+srv://salmen:azerty123456@stage.g7d1vqy.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)     
print(client.list_database_names())
smartGardenData=client.smartGarden
print(smartGardenData.list_collection_names())

row_0={
    "treeId":6010,
    "humidity": "19",
    "lunière":[400,360,600]
}
row_1={
    "treeId":6010,
    "temperature": "40",
    "humidity": "28",
}
rows=[row_0,row_1]
generalData=smartGardenData.generalData
"""result=generalData.insert_one({
    "NumberOfTrees" : 3
})"""
tree_0=smartGardenData.tree_0
result=tree_0.insert_many([row_0,row_1])
#result=generalData.insert_many()
#result=tree_0.find_one({"temperature":"40"})
#result=tree_0.find_one({"lunière":800})
#from bson.objectid import ObjectId
#result=tree_0.find_one({"_id":ObjectId("62dd09a1d90c6282f7362d09")})
"""results=tree_0.find({"lunière":400})
#print(list(results))
for result in results:
   print(result)"""
#print(tree_0.count_documents({}))   
#print(tree_0.count_documents({"temperature":"40"}))

#results=tree_0.find({"temperature":{"$gt":"28"}})
results=generalData.find_one({"NumberOfTrees":3})
print(results["NumberOfTrees"])
#results=tree_0.find({"temperature":{"$lt":"100"}}).sort("lunière")

"""for result in results:
    print(result)"""

#result=tree_0.delete_one({"temperature":"28"})
#result=tree_0.delete_many({"temperature":"28"})
#result=tree_0.delete_many({})

#result=tree_0.update_one({"temperature":"28"},{"$set":{"humidity":100}})
#result=tree_0.update_many({"temperature":"28"},{"$set":{"humidity":100}})
#result=tree_0.update_many({"temperature":"28"},{"$unset":{"humidity":None}})

