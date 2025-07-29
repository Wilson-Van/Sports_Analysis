from . import american_football




def main():
    # call method to get all american football leagues
    af_leagues = american_football.get_leagues()
    # this is just a place holder for now to work on getting other methods working
    id = int(input(f"Which league NFL (1), NCAA(2))?"))
    print(af_leagues)



if __name__ == '__main__':
    main()