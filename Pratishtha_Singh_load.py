import pandas as pd
import requests
import json
import numpy as np
import re
import sys

f=sys.argv[1]
df=pd.read_csv(f, usecols=["serial_number","facility_name", "score"], index_col=["serial_number"])
df.head()

url="https://inf551-48566.firebaseio.com/loaded_data.json"
data=df.to_json(orient="index")
response=requests.put(url,data)
response.json()

# to_json reference from https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html

dataf=pd.read_csv(f, usecols=["serial_number","facility_name", "score"])
dataf.head()

inverted_index={}

for k, l in zip(dataf["facility_name"], dataf["serial_number"]):  
        k=re.sub('[\W_]+',' ',k)
        for val in k.lower().split():
            if inverted_index.get(val):
                if k not in inverted_index[val]:
                    inverted_index[val].append(l)
            else:
                inverted_index[val] = [l]

# inverted index reference from https://stackoverflow.com/questions/28019543/inverted-index-given-a-list-of-document-tokens-using-python

url1="https://inf551-48566.firebaseio.com/invert_index.json"
j_index=json.dumps(inverted_index)
response=requests.put(url1,j_index)
response.json()
print(inverted_index)


