# This file will contain the nfl stats
import http.client
from dotenv import load_dotenv
import os
import json

# Hide my api key from github
load_dotenv()
api_key = os.getenv("API_KEY")

# connect to the api
conn = http.client.HTTPSConnection("v1.american-football.api-sports.io")

headers = {
    'x-rapidapi-host': "v1.american-football.api-sports.io",
    'x-rapidapi-key': api_key
    }

# get all leagues
conn.request("GET", "/leagues", headers=headers)

res = conn.getresponse()
data = res.read()

# makes data into a string so i can make it a python dictionary
json_str = data.decode('utf-8')

json_data = json.loads(json_str)

# for each result parse the league
# make a dictionary that stores the id of the league named
leagues = []
for r in json_data['response']:
    league = {"Name": r['league']['name'],
              "ID": r['league']['id']
            }
    leagues.append(league)

print(leagues)