# This file will contain the nfl stats
import http.client
from dotenv import load_dotenv
import os
import json
from .League import League
from .Team import Team
from .Player import Player

# Hide my api key from github
load_dotenv()
api_key = os.getenv("API_KEY")

# connect to the api
conn = http.client.HTTPSConnection("v1.american-football.api-sports.io")

headers = {
    'x-rapidapi-host': "v1.american-football.api-sports.io",
    'x-rapidapi-key': api_key
    }

# in certain api calls I feel like there is some information that is not needed so I am omitting the information such as height and weight, team code and player numbers

def get_leagues():
    """This is a method that will get all leagues of the sport and return the leagues"""

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

def get_teams(league_id: int, season: int):
    """This is a method to return the teams of a given league for a given season"""
    
    # make the api call
    conn.request("GET", f"/teams?league={league_id}&season={season}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    json_str = data.decode('utf-8')

    json_data = json.loads(json_str)

    print(json_data)

    # make a list of teams
    teams = []
    # for each response gotten we will create a Team object
    for r in json_data['response']:
        # parse info from the api call
        id = r['id']
        name = r['name']
        seasons = r['city']
        # create a league based on the parsed info and append it to the leagues list
        teams.append(Team(id, name, seasons))
    return teams

def get_team_players(team_id: int, season: int):
    """This is a method to return the players of a given team for a given season"""
    
    # make the api call
    conn.request("GET", f"/players?team={team_id}&season={season}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    json_str = data.decode('utf-8')

    json_data = json.loads(json_str)

    # list of players
    players = []
    # get responses from the api call
    for r in json_data['response']:
        # make player objects based on the info given from the api call
        id = r['id']
        name = r['name']
        # call a helper function to get the player stats
        #stats = get_player_stats(id, season)
        players.append(Player(id, name, None))
    return players

def get_player_stats(player_id: int, season: int):
    """Gives stats of a player for a given season"""
    # make the api call
    conn.request("GET", f"/players/statistics?id={player_id}&season={season}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    json_str = data.decode('utf-8')

    json_data = json.loads(json_str)

    for stat in json_data['response']:
        print(stat)