from main import *
from itertools import chain


def story(player_choice_route):
    # Intro text for level
    # Choose path and stick with it
    # Enemy encounter, fight, loot, etc., trap encounter, or chest encounter.
    global level
    global story_progress
    PATH = [narr.INTRO_TXT1, narr.INTRO_TXT2, narr.ROUTE1, player_choice_route, narr.ROUTE2, player_choice_route,
                narr.ROUTE3, player_choice_route, narr.ROUTE4, player_choice_route, narr.ROUTE5, player_choice_route,
                narr.ROUTE6, player_choice_route, ending]

    for text in chain(story_progress):
        print(text + "\n")
        clear_screen()
        ending = None
        #try: Test if there is a another text box to display
            #print(PATH[level])
            #input("Press enter to continue...")
            #clear_screen()
        #except:

    level += 1