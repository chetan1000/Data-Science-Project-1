#!pip install requests --upgrade
import requests
# from requests import post

url = 'http://localhost:5000/results'       # http://192.168.38.110:5000/results
r = requests.post(url, json={'key':'value'})      # ,json={'Key':'value'}
# r.status_code
print(r)

print(r.json())