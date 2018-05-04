# Put the use case you chose here. Then justify your database choice:

#I choose to use mongodb as my database for implementing photo app, 
#becuse MongoDB is a document database in which one collection holds different documents. 
#Number of fields, content and size of the document can differ from one document to another, which 
#provides a clear structure of a single object. The design of photo app is object oriented. Therefore, mongodb is 
#a good choice. It also provides the flexibility for future developmemt.

# Explain what will happen if coffee is spilled on one of the servers in your cluster, causing it to go down.

#The design of the database is atomic which means if there is one transaction in the middle and the server shut down, then the whole
#transaction will be canceled and the data in the server will be preserved. If the server is damaged, then it will switch to the 
#primary server which has been created before.


# What data is it not ok to lose in your app? What can you do in your commands to mitigate the risk of lost data?

# User's password and email address is not ok to lose in the app. We can create a new server to duplicate their password and 
# email address, which can prevent the accidental lose of data.
#


import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.finalProject
users = db.users_collection
photos = db.photos_collection


# Action 1: <A user signs up for an account>
users.insert(
	{ 
	  	'email': 'test4@gmail.com',
	  	'name': 'Yongmei Lai',
	  	'password': '123456',
	  	'follows':[],
	  	'follower':[]
	}) 


# Action 2: <A user uploads a new picture>
photos.insert(
	{	'name':'photo_7',
		'user_email':'test4@gmail.com',
		'likes':[],
		'comments':[],
		'description':'house'
	})

# Action 3: <A user starts following a new person>
users.update({'email':'test4@gmail.com'}, {'$push': {'follows': {'email': 'test1@gmail.com'}}})
users.update({'email':'test1@gmail.com'}, {'$push': {'follower': {'email': 'test4@gmail.com'}}})

# Action 4: <A user likes a photo>
photos.update({'$and': [{'name': 'photo_7'},{'user_email': 'test4@gmail.com'}]}, {'$push': {'likes': {'email': 'test1@gmail.com'}}})

# Action 5: <A user comments on another's photo>
photos.update({'$and': [{'name': 'photo_7'},{'user_email': 'test4@gmail.com'}]}, {'$push': {'comments': {'email': 'test1@gmail.com', 'content': 'The house is sweet !'}}})

# Action 6: <A user sees all the photos of one particular person they follow>
cursor = photos.find({'user_email':'test4@gmail.com'})
for doc in cursor:
	pic_name = (doc['name'])

# Action 7: <A user wants to see how many likes he gets in total>
photos.aggregate({'$group': { 'user_email': 'test1@gmail.com', 'totalSize': { '$sum': { '$size': '$likes'}} }})


# Action 8: <A user wants to change its email address>
users.update({'email':'test4@gmail.com'}, {'$set': {'email': 'test5@gmail.com'}})
photos.update({'user_email': 'test4@gmail.com'}, {'$set': {'email': 'test5@gmail.com'}})




