url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'

# request - HTTPS - Hypter Text Transfer Protocol Secure

# types of http requests
# GET - to read the data

import requests,json

sample1 = 'https://api.github.com/repos/pandas-dev/pandas/issues'

req = requests.get(sample1) # response res[200]

response = req.json()
# print(req.json()) #  json format

data = response

with open('file.json',mode='w') as file:
    json.dump(response,file)
    # json.dump(json_data,file_name_to_create)




import requests,json

data = [
    {
       "url":"https://api.github.com/repos/pandas-dev/pandas/issues/59686",
       "repository_url":"https://api.github.com/repos/pandas-dev/pandas",
       "labels_url":"https://api.github.com/repos/pandas-dev/pandas/issues/59686/labels{/name}",
       "comments_url":"https://api.github.com/repos/pandas-dev/pandas/issues/59686/comments",
       "events_url":"https://api.github.com/repos/pandas-dev/pandas/issues/59686/events",
       "html_url":"https://github.com/pandas-dev/pandas/pull/59686",
       "id":2500915021,
       "node_id":"PR_kwDOAA0YD856KQwr",
       "number":59686,
       "title":"TST (string dtype): resolve all infer_string TODO/xfails in pandas/tests/arrays",
       "user":{
          "login":"jorisvandenbossche",
          "id":1020496,
          "node_id":"MDQ6VXNlcjEwMjA0OTY=",
          "avatar_url":"https://avatars.githubusercontent.com/u/1020496?v=4",
          "gravatar_id":"",
          "url":"https://api.github.com/users/jorisvandenbossche",
          "html_url":"https://github.com/jorisvandenbossche",
          "followers_url":"https://api.github.com/users/jorisvandenbossche/followers",
          "following_url":"https://api.github.com/users/jorisvandenbossche/following{/other_user}",
          "gists_url":"https://api.github.com/users/jorisvandenbossche/gists{/gist_id}",
          "starred_url":"https://api.github.com/users/jorisvandenbossche/starred{/owner}{/repo}",
          "subscriptions_url":"https://api.github.com/users/jorisvandenbossche/subscriptions",
          "organizations_url":"https://api.github.com/users/jorisvandenbossche/orgs",
          "repos_url":"https://api.github.com/users/jorisvandenbossche/repos",
          "events_url":"https://api.github.com/users/jorisvandenbossche/events{/privacy}",
          "received_events_url":"https://api.github.com/users/jorisvandenbossche/received_events",
          "type":"User",
          "site_admin":False
        }
    }
]

print(data[0]['user']['url'])
# response
# to fetch the html_url from the line 59 response

req2 = requests.get(data[10]['user']['url'])
res2 = req2.json()
print(res2['html_url'])

# PROJECT Q1:
# 1. to take the html_url for all the data present in the https://api.github.com/repos/pandas-dev/pandas/issues