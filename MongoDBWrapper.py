import pymongo
import gc
import traceback

class MongoDBWrapper(object):
    
  __db = None
  
  def open(self):
    if self.__db is None:
      mongoClient = pymongo.MongoClient("mongodb://localhost:27017")
      shieldClient = mongoClient["shielddb"]
      self.db = shieldClient["EDB"]
      return "created"
    return "existed"
  def close(self):
    try:
      if self.__db is not None:
          del self.__db
          gc.collect()
          return "deleted"
    except AttributeError:
      gc.collect()
      traceback.print_exc()
      return "exception"
          
  def put(self,key,value):
    if self.__db is not None:
      self.__db.insert_one({key: value})
  
  def get(self,key):
    if self.__db is not None:
      return self.__db.find(key)
    else:
      return None
      
  def delete(self,key):
    if self.__db is not None:
      self.__db.delete_many({key:{}})
  
  def getInfo(self):
    if self.__db is not None:
      #https://github.com/facebook/rocksdb/wiki/RocksDB-Tuning-Guide
      message = self.__db.get_property(pyrocksdb.ReadOptions(),b"rocksdb.estimate-num-keys").decode()
      message += "\n"
      message += self.__db.get_property(pyrocksdb.ReadOptions(),b"rocksdb.stats").decode()
      return message
    else:
        return None