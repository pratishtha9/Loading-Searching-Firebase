import sys
import requests
import pandas as pd
import json

url1="https://inf551-48566.firebaseio.com/invert_index.json"
url2="https://inf551-48566.firebaseio.com/loaded_data.json"
inverted_index={}
response=requests.get(url1)
response2 = requests.get(url2)
original_database = response2.json()
inverted_index = response.json()

serial_numbers = set()
serial_numbers=[]
for i in sys.argv[1].split(" "):
    for key in inverted_index[i]:
        serial_numbers.append(key)

for serial_number in serial_numbers:
    print(original_database[serial_number]["facility_name"], original_database[serial_number]["score"])