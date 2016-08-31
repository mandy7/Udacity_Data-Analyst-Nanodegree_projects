import pymongo

"""
Your task is to sucessfully run the exercise to see how pymongo works
and how easy it is to start using it.
You don't actually have to change anything in this exercise,
but you can change the city name in the add_city function if you like.
Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB (see Instructor comments for link to installation information)
and uncomment the get_db function.
"""


def get_db():
    # For local use
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.cities
    return db

if __name__ == "__main__":
    # For local use
    db = get_db() # uncomment this line if you want to run this locally

   
    print db.newdelhi.find().count()
    print db.newdelhi.find( {"type":"node"} ).count()
    print db.newdelhi.find( {"type":"way"} ).count()
    print len(db.newdelhi.distinct( "created.user" ) )
    print db.newdelhi.count({"amenity" : {"$exists":1}})
    print db.newdelhi.count({"amenity" : "bank"})
    # Similiar to above query for bank, I checked other necessary amenities count such as school, hospital, police and noted an observations corresponding to them

    # Let's check how many of these documents were not updated post creation 
    print db.newdelhi.count({"created.version" : "1"})

    # Total count of postal codes available
    print db.newdelhi.count( {"address.ostcode" : {"$exists":1} } )

    # To find count of residents of New Delhi
    # New delhi's area pin code start with "11"
    print db.newdelhi.find( {"address.ostcode" : { "$regex" : "^11.+"} } ).count()



    # to find top 5 religion
    print list(db.newdelhi.aggregate([{"$match": {"religion":{"$exists":1}}}, {"$group":{"_id":"$religion", "count":{"$sum":1}}},{"$sort":{"count":-1}},{"$limit":5}]))


    #To find % of Hindus
    print db.newdelhi.count( {"religion" : {"$exists":1} } )
    print db.newdelhi.count({"religion" : "hindu"})


    # to find top 5 amenities
    print list(db.newdelhi.aggregate([{"$match": {"amenity":{"$exists":1}}}, {"$group":{"_id":"$amenity", "count":{"$sum":1}}},{"$sort":{"count":-1}},{"$limit":5}]))

    # Top 5 cuisines
    print list(db.newdelhi.aggregate([{"$match": {"amenity":"fast_food", "cuisine":{"$exists":1}}}, {"$group":{"_id":"$cuisine", "count":{"$sum":1}}},{"$sort":{"count":-1}},{"$limit":5}]))


    # Top 5 banks
    print list(db.newdelhi.aggregate([{"$match": {"amenity":"bank", "name":{"$exists":1}}}, {"$group":{"_id":"$name", "count":{"$sum":1}}},{"$sort":{"count":-1}},{"$limit":5}]))




    #Some of queries were executed in MongoDB shell itself. Refer Project summary document for codes and observations                           
