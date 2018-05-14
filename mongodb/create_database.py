import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.finalProject

users = db.users_collection
photos = db.photos_collection

users.insert([
	{ 
	  	'email': 'test1@gmail.com',
	  	'name': 'Chunlin Zhu',
	  	'password': '123456',
	  	'follows':[{'name': 'Chunyang Zhu', 'email': 'test2@gmail.com'}, {'name': 'Jack Ma', 'email': 'test3@gmail.com'}],
	  	'follower':[{'name': 'Chunyang Zhu','email': 'test2@gmail.com'}, {'name': 'Jack Ma', 'email': 'test3@gmail.com'}]
	}, 
	{ 
		'email': 'test2@gmail.com',
	  	'name': 'Chunyang Zhu',
	  	'password': '123456',
	  	'follows':[{'name': 'Chunlin Zhu', 'email': 'test1@gmail.com'}, {'name': 'Jack Ma', 'email': 'test3@gmail.com'}],
	  	'follower':[{'name': 'Chunlin Zhu', 'email': 'test1@gmail.com'}, {'name': 'Jack Ma', 'email': 'test3@gmail.com'}]
	},
	{
		'email': 'test3@gmail.com',
	  	'name': 'Jack Ma',
	 	'password': '123456',
	  	'follows':[{'name': 'Chunyang Zhu', 'email': 'test2@gmail.com'}, {'name': 'Chunlin Zhu','email': 'test1@gmail.com'}],
	  	'follower':[{'name': 'Chunlin Zhu', 'email': 'test1@gmail.com'}, {'name': 'Chunyang Zhu', 'email': 'test2@gmail.com'}]
	}]
	)

# I use subdocument to represent the comments and likes object in my schema.
photos.insert([
	{	'name':'photo_1',
		'user_email':'test1@gmail.com',
		'likes':[{'eamil':'test3@gmail.com'},{'eamil':'test2@gmail.com'},{'eamil':'test1@gmail.com'}],
		'comments':[{}],
		'description':'waterfall'
	},

	{	'name':'photo_2',
		'user_email':'test1@gmail.com',
		'likes':[{'eamil':'test3@gmail.com'},{'eamil':'test2@gmail.com'}],
		'comments':[{'email':'test3@gmail.com', 'content': 'beautiful!'}],
		'description':'mountain'
	},
	{	'name':'photo_3',
		'user_email':'test2@gmail.com',
		'likes':[{'eamil':'test3@gmail.com'}],
		'comments':[{'email':'test3@gmail.com', 'content': 'mordern!'}],
		'description':'city'
	},
	{	'name':'photo_4',
		'user_email':'test2@gmail.com',
		'likes':[{'eamil':'test3@gmail.com'},{'eamil':'test2@gmail.com'}],
		'comments':[{'email':'test3@gmail.com', 'content': 'peace!'}],
		'description':'sea'
	},
	{	'name':'photo_5',
		'user_email':'test3@gmail.com',
		'likes':[{'eamil':'test3@gmail.com'}],
		'comments':[],
		'description':'tower'
	},
	{	'name':'photo_6',
		'user_email':'test3@gmail.com',
		'likes':[{'eamil':'test3@gmail.com'},{'eamil':'test2@gmail.com'},{'eamil':'test1@gmail.com'}],
		'comments':[{'email':'test1@gmail.com', 'content': 'long!'}],
		'description':'bridge'
	}
	])
	



