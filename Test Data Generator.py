import os
import datetime
import random
from pymongo import MongoClient


#connect to database and verify connection
connection_string = "mongodb://localhost:27017/" #replace with "mongodb://ip_of_database:27017" if database is not on local machine
client = MongoClient(connection_string)
current_db = client.SensorData
collection = current_db.test
meta = current_db.Metadata

def create_index():
    collection.create_index([('Date Recorded', -1)])


def generate_data():

    x = int(input("what type of data would you like to generate: \n 1. Random Data \n 2. Completly Normal Data \n 3. Data With Abnormal ADC \n 4. Data With Abnormal Voltage \n 5. Data With Abnormal Temp \n :"))
    y = int(input("How many records would you like to generate?"))

    for i in range(y):

        day = datetime.datetime(2024, random.randint(1,12), random.randint(1,28))
        module = random.randint(1,50)
        moring = random.randint(1,5)
    
        if (x == 1):
            insert_test_doc(day, module, moring)
        elif x == 2:
            insert_good_doc(day, module, moring)
        elif x == 3:
            bad_adc(day, module, moring)
        elif x == 4:
            bad_voltage(day, module, moring)
        elif x == 5:
            bad_temp(day, module, moring)

def generate_same_day_data():

    day = datetime.datetime(2024, random.randint(1,12), random.randint(1,28))
    module = random.randint(1,50)
    moring = random.randint(1,5)

  
    x = int(input("what type of data would you like to generate: \n 1. Random Data \n 2. Completly Normal Data \n 3. Data With Abnormal ADC \n 4. Data With Abnormal Voltage \n 5. Data With Abnormal Temp \n :"))
    y = int(input("How many records would you like to generate?"))

    for i in range(y):

        if (x == 1):
            insert_test_doc(day, module, moring)
        elif x == 2:
            insert_good_doc(day, module, moring)
        elif x == 3:
            bad_adc(day, module, moring)
        elif x == 4:
            bad_voltage(day, module, moring)
        elif x == 5:
            bad_temp(day, module, moring)


#Generate Completly Random Test Data 
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

#Generate Test Data That Is Not Misbehaving 
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


#Generate Test Document With Abnormal ADC
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

#Generate Test Document With Abnormal Voltage
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

#Generate Test Document With Abnormal Temp
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
       

def main():
     create_index()
     x = int(input("Enter 1 if you would like to generate data for one day, enter 2 if you would like to generate data for many random days: "))
     if x == 1:
         generate_same_day_data()
     elif x == 2:
         generate_data()

if __name__ == "__main__":
    main()






