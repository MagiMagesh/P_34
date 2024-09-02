import requests

sample1 = 'https://api.github.com/repos/pandas-dev/pandas/issues'

req = requests.get(sample1)

print(req) 