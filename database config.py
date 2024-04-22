import os
import datetime
import pprint
import random
import pprint
from pymongo import MongoClient

printer = pprint.PrettyPrinter()

#connect to database and verify connection
connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)
current_db = client.SensorData
collection = current_db.SensorInfo
meta = current_db.Metadata

def create_index():
    collection.create_index([('Date Recorded', -1)])


def generate_data():
    #day = datetime.datetime(2024, random.randint(1,12), random.randint(1,28))
    module = random.randint(1,50)
    moring = random.randint(1,5)
    for i in range(1400):
        day = datetime.datetime(2024, random.randint(1,12), random.randint(1,28))
        insert_test_doc(day, module, moring)
        #insert_good_doc(day, module, moring)
        #bad_adc(day, module, moring)
        #bad_voltage(day, module, moring)
        #bad_temp(day, module, moring)


#Generate Sample Data
def insert_test_doc(day, module, moring):
    specific_date = day.replace(hour=random.randint(1,23), minute = random.randint(1,59), second=random.randint(1,59), microsecond=random.randint(1,999999)) # Year, Month, Day, Hour, Minute, Second
    sample_document = {
        "Date Recorded" : specific_date,
        "Moring Line #" : moring,
        "Module #" : module,
        "Photo Multiplier # " : random.randint(1,1000),
        "Voltage" : random.randint(900,1500),
        "Temperature" : random.randint(15,30),
        "ADC" : random.randint(1100,1300)
    }
    collection.insert_one(sample_document)
    check_date(specific_date)

def insert_good_doc(day, module, moring):
    specific_date = day.replace(hour=random.randint(1,23), minute = random.randint(1,59), second=random.randint(1,59), microsecond=random.randint(1,999999)) # Year, Month, Day, Hour, Minute, Second
    sample_document = {
        "Date Recorded" : specific_date,
        "Moring Line #" : moring,
        "Module #" : module,
        "Photo Multiplier # " : random.randint(1,1000),
        "Voltage" : random.uniform(1000,1400),
        "Temperature" : random.randint(18,28),
        "ADC" : random.randint(1200,1250)
    }
    collection.insert_one(sample_document)
    check_date(specific_date)


def bad_adc(day, module, moring):
    specific_date = day.replace(hour=random.randint(1,23), minute = random.randint(1,59), second=random.randint(1,59), microsecond=random.randint(1,999999)) # Year, Month, Day, Hour, Minute, Second
    sample_document = {
        "Date Recorded" : specific_date,
        "Moring Line #" : moring,
        "Module #" : module,
        "Photo Multiplier # " : random.randint(1,1000),
        "Voltage" : random.uniform(1000,1400),
        "Temperature" : random.randint(18,28),
        "ADC" : random.randint(1000,1100)
    }
    collection.insert_one(sample_document)
    check_date(specific_date)

def bad_voltage(day, module, moring):
    specific_date = day.replace(hour=random.randint(1,23), minute = random.randint(1,59), second=random.randint(1,59), microsecond=random.randint(1,999999)) # Year, Month, Day, Hour, Minute, Second
    sample_document = {
        "Date Recorded" : specific_date,
        "Moring Line #" : moring,
        "Module #" : module,
        "Photo Multiplier # " : random.randint(1,1000),
        "Voltage" : random.uniform(1500,1600),
        "Temperature" : random.randint(18,28),
        "ADC" : random.randint(1200,1250)
    }
    collection.insert_one(sample_document)
    check_date(specific_date)

def bad_temp(day, module, moring):
    specific_date = day.replace(hour=random.randint(1,23), minute = random.randint(1,59), second=random.randint(1,59), microsecond=random.randint(1,999999)) # Year, Month, Day, Hour, Minute, Second
    sample_document = {
        "Date Recorded" : specific_date,
        "Moring Line #" : moring,
        "Module #" : module,
        "Photo Multiplier # " : random.randint(1,1000),
        "Voltage" : random.uniform(1000,1400),
        "Temperature" : random.randint(10,15),
        "ADC" : random.randint(1200,1250)
    }
    collection.insert_one(sample_document)
    check_date(specific_date)

def check_date(newdate):
    metacollec = meta.find()
    for m in metacollec:
        mostrecent = m["Most Recent"]

    if (newdate > mostrecent) :
        filter = {"Most Recent": mostrecent}
        update = {'$set': {'Most Recent': newdate}}
        meta.update_one(filter,update)


 
create_index()
generate_data()






