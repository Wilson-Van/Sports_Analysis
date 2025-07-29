# This file will contain the nfl stats
import http.client
from dotenv import load_dotenv
import os
import json
from .League import League

# Hide my api key from github
load_dotenv()
api_key = os.getenv("API_KEY")

# connect to the api
conn = http.client.HTTPSConnection("v1.american-football.api-sports.io")

headers = {
    'x-rapidapi-host': "v1.american-football.api-sports.io",
    'x-rapidapi-key': api_key
    }

def get_leagues():
    # This is a method that will get all leagues of in the sport and return the leagues

    # api call to get the leagues
    conn.request("GET", "/leagues", headers=headers)

    res = conn.getresponse()
    data = res.read()

    # makes data into a string so i can make it a python dictionary
    json_str = data.decode('utf-8')

    json_data = json.loads(json_str)

    # make a list of leagues
    leagues = []
    # for each response gotten we will create a League object
    for r in json_data['response']:
        # parse info from the api call
        id = r['league']['id']
        name = r['league']['name']
        seasons = [s['year'] for s in r['seasons']]
        # create a league based on the parsed info and append it to the leagues list
        leagues.append(League(id, name, seasons))
    return leagues
