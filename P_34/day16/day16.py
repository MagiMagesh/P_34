url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'

# request - HTTPS - Hypter Text Transfer Protocol Secure

# types of http requests
# GET - to read the data

import requests,json

sample1 = 'https://api.github.com/repos/pandas-dev/pandas/issues'

req = requests.get(sample1) # response res[200]

response = req.json()
# print(req.json()) #  json format

with open('file.json',mode='w') as file:
    json.dump(response,file)
    # json.dump(json_data,file_name_to_create)