# Saving system for the game
import pickle
import characters


class Status():
    """The status of the game"""
    def __init__(self, param):
        self.param = param


def save_game(obj):
    """Save the game to the savegame.dat file"""
    try:
        savefile_name = input("What is the name of the save file? (default: savegame.dat)")
        if savefile_name == "":
            savefile_name = "savegame.dat"
        with open(savefile_name, 'wb') as file:
            pickle.dump(obj, file)
    except Exception as ex:
        print("Error during picling object: " + str(ex))

saved_items = Status(characters)
print(saved_items.param)
save_game(saved_items)


def load_game():
    """Load the game from the savegame.dat file"""
    try:
        savefile_name = input("What is the name of the save file? (default: savegame.dat)")
        if savefile_name == "":
            savefile_name = "savegame.dat"
        with open(savefile_name, 'rb') as file:
            saved_items = pickle.load(file)
            return saved_items
    except Exception as ex:
        print("Error during picling object: " + str(ex))