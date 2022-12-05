# Saving system for the game

import pickle
import main
import characters
import ui_elements


class Status():
    def __init__(self, param):
        self.param = param


def save_game():
    try:
        with open('savegame.dat', 'wb') as file:
            pickle.dump(Status('test'), file)
    except Exception as ex:
        print("Error during picling object: " + str(ex))

obj = Status(characters.bilo)
print(obj.param)
save_game(obj)