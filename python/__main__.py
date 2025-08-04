from . import american_football as af




def main():
    # call method to get all american football leagues
    #af_leagues = af.get_leagues()
    #print(af_leagues)
    #af_teams = af.get_teams(1, 2021)
    #for team in af_teams:
        #print(team)
    players = af.get_player_stats(842, 2022)



if __name__ == '__main__':
    main()