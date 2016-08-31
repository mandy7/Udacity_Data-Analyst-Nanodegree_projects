import json
import pymongo


if __name__ == "__main__":
    
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.cities

    with open('newdelhi.osm.json') as f:
        for line in f:
            db.newdelhi.insert(json.loads(line))
            
