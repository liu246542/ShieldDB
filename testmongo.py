import pymongo

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient["shielddb"]
testcol = mydb["test"]
testcol.insert_one({"test1":"apple"})
testcol.insert_one({"test1":"pear"})
print([x for x in testcol.find()])
# print([x for x in testcol.find({"test1":{}})])