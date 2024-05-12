import json
from pymongo import MongoClient
from datetime import datetime

connection_string = "mongodb://localhost:27017/" #replace with "mongodb://ip_of_database:27017" if database is not on local machine
client = MongoClient(connection_string)
current_db = client.SensorData
collection = current_db.SensorInfo
meta = current_db.Metadata

def insert():
    #Open Json File 
    file_path = "json/file/location" #change
    with open(file_path, 'r') as file:
        #create list of dictionaries from the file 
        data = json.load(file)

        #add those dictionaries to the database
    for x in data:
        newdatestr = x["Date Recorded"]
        newdate = datetime.strptime(newdatestr, '%m/%d/%Y %I:%M:%S.%f %p' )
        x["Date Recorded"] = newdate #make sure date is in the proper format
        collection.insert_one(x)
        check_date(newdate)

#Keep track of most recent document
def check_date(newdate):
    
    metacollec = meta.find()
    for m in metacollec:
        mostrecent = m["Most Recent"]

    if (newdate > mostrecent) :
        filter = {"Most Recent": mostrecent}
        update = {'$set': {'Most Recent': newdate}}
        meta.update_one(filter,update)


if __name__ == "__main__":
    insert()