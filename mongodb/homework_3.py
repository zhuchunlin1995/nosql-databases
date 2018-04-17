import pymongo
from pymongo import MongoClient


# open database and set up connections.
client = MongoClient()
database = client.test
collection = database.movies

#find all documents that satisfy requirement
cursor = collection.find({"genres": "Drama", "rated": "NOT RATED"})
num = collection.find({"genres": "Drama"}).count()
print('before updating: %d' %(num))


#A
#update database  in-place and atomicly.
for doc in cursor:
	collection.update({"_id": doc["_id"]},{'$set':{"rated":"Pending rating"}})

#check if the database hase been updated
num = collection.find({"genres": "Drama", "rated": "NOT RATED"}).count()
print('after updating: %d' %(num))


#B
collection.insert_one({"title": "Baby Boom","year": 1987, "countries": ["United States"],"genres": ["Drama", "Comedy", "Romance"], "directors": ["Charles Shyer"], "imdb": {"id":8888888, "rating":10.0, "votes":152}})
collection.find({"title" : "Your mom boom", "genres" : "Drama"})


#C
collection.aggregate([{ '$match' : {'genres' : "Drama"} }, { '$group' : {'_id': "Drama", 'count': {'$sum': 1}}}])

#D
result = collection.aggregate([{'$match':{"countries" : "Hungary", "rated" : "Pending rating"}},{'$group':{"count":{'$sum': 1}, "_id" : {"countries" : "Hungary", "rating": "Pending rating"}}}])
print(list(result))

#E
database.test2.insert({'name':'Chunlin Zhu', 'age':'21'})
database.test3.insert({'name':'Chunlin Zhu', 'age':'21'})

database.test2.insert({'name':'Chunyang Zhu', 'age':'21'})
database.test3.insert({'name':'Chunyang Zhu', 'age':'21'})

result = database.test2.aggregate([{'$lookup':{'from': 'test3', 'localField':'name', 'foreignField': 'name', 'as': 'result'}}])
print(list(result))

