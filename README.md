# Test Data Generator Documentation

This Python script is designed to generate test data for a MongoDB database, specifically for a collection named `SensorData`. It can generate normal data and data with abnormal ADC, voltage, or temperature values.


## Setup

    Ensure that your MongoDB instance is running. The default connection string assumes a local MongoDB instance:
    ```python
    connection_string = "mongodb://localhost:27017/"
    ```

    If your MongoDB instance is running on a different machine, replace the connection string accordingly.
    
## External Tools Used

- **Pymongo**:
  - Pymongo is the Object-Document Mapping Library used to access the database. Its documentation can be found [here](https://pymongo.readthedocs.io/en/stable/).

## Script Description

### Functions

- `create_index()`: Creates an index on the `Date Recorded` field in descending order.
- `generate_data()`: Prompts the user to select the type of data to generate and the number of records, then generates data for different random days.
- `generate_same_day_data()`: Similar to `generate_data()`, but generates all records for the same randomly chosen day.
- `insert_test_doc(day, module, moring)`: Inserts a document with random test data.
- `insert_good_doc(day, module, moring)`: Inserts a document with normal data.
- `bad_adc(day, module, moring)`: Inserts a document with abnormal ADC values.
- `bad_voltage(day, module, moring)`: Inserts a document with abnormal voltage values.
- `bad_temp(day, module, moring)`: Inserts a document with abnormal temperature values.
- `check_date(newdate)`: Updates the metadata collection with the most recent date if the new date is more recent.

### Main Function

The main function prompts the user to choose whether to generate data for one day or multiple random days and calls the appropriate function to generate the data.

## Usage

1. Run the script:
    ```bash
    python Test\ Data\ Generator.py
    ```

2. Follow the prompts to select the type of data and the number of records to generate.

### Example

When prompted, you can choose:
- `1`: Random Data
- `2`: Completely Normal Data
- `3`: Data With Abnormal ADC
- `4`: Data With Abnormal Voltage
- `5`: Data With Abnormal Temperature

Then, specify the number of records you want to generate.


# Import Script Documentation

This Python script is designed to import data from a JSON file into a MongoDB database. It performs the following main tasks:
1. Connects to a MongoDB database.
2. Reads data from a JSON file.
3. Inserts the data into a specified MongoDB collection.
4. Updates metadata to keep track of the most recent document.


## External Tools Used

- **Pymongo**:
  - Pymongo is the Object-Document Mapping Library used to access the database. Its documentation can be found [here](https://pymongo.readthedocs.io/en/stable/).


## Configuration

Before running the script, ensure you have the MongoDB server running and accessible. Update the following configurations in the script:

1. **MongoDB Connection String:**
   Update the `connection_string` variable with your MongoDB connection details.

   ```python
   connection_string = "mongodb://localhost:27017/"
   ```

2. **JSON File Path:**
   Update the `file_path` variable with the location of your JSON file.

   ```python
   file_path = "json/file/location"
   ```

## Script Overview

### Libraries Imported

```python
import json
from pymongo import MongoClient
from datetime import datetime
```

### MongoDB Connection

```python
connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)
current_db = client.SensorData
collection = current_db.SensorInfo
meta = current_db.Metadata
```

### Function: `insert()`

This function reads data from the specified JSON file, converts the date format, and inserts the data into the `SensorInfo` collection. It also calls `check_date()` to update the metadata.


### Function: `check_date(newdate)`

This function checks if the newly inserted date is the most recent and updates the `Metadata` collection accordingly.


### Main Execution

The `insert()` function is called when the script is run directly.


## Running the Script

Ensure that the JSON file path is correct and the MongoDB server is running. The script will read the data from the JSON file, insert it into the database, and update the metadata with the most recent date.


