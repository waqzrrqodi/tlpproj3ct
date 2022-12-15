import sys
import time
import subprocess as sp
import pkg_resources
import os
from platform import system



# Check if the user has the required packages installed
if system() == "Windows":
    required = {'progressbar', 'emoji', 'pydub'}
else:
    required = {'progressbar', 'emoji', 'pydub', 'getch'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

# for clearing console (windows and unix systems)
clear = "cls"
if os.name == "posix":
    clear = "clear"
def clear_screen():
    sp.call(clear, shell=True)

# If the user is missing any of the required packages, install them
if missing:
    sp.check_call([sys.executable, '-m', 'pip', 'install', *missing], stdout=sp.DEVNULL)
    clear_screen()
    print("Dependencies installed")

import ui_elements as ui
import characters as ch
from pydub import AudioSegment
from pydub.playback import play

if system() == "Windows":
    from msvcrt import getch as getkey
else:
    import getch as getkey_linux # For linux systems, getch is not included in the standard library on windows.

def animate_text(text):
    '''Makes text appear one letter at a time'''
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)

def wait_for_keypress():
    if system() == "Windows":
        getkey()
    else:
        getkey_linux()

def intro():
    clear_screen() # Clears the screen
    print("nah no way")
    print(ui.intro_name)
    wait_for_keypress()

def main():
    intro()
    
if __name__ == "__main__":
    main()

FIGHT = 1
RUN = 2

def fight_start():
    print("Do thau wish to fight, or wish to run? 1 = FIHT, 2 = RUN")
    fight_or_flight = int(input("Yeh m8"))
    if fight_or_flight == FIGHT:
        fight_loop_tm()
    
    if fight_or_flight == RUN:
        running_coward_tm()

def fight_loop_tm():
    """
    Fight loop with the tutorial monster (tm) and the player.
    A fight loop is a loop that runs until one of the two characters die.
    The fight loop will also call the menu function when the player presses the menu button.
    The menu function will then return the player to the fight loop.
    The fight loop will also call the default_action_menu function when the player presses the action button.
    The default_action_menu function will then return the player to the fight loop.
    """
    print("")
    
def running_coward_tm():
    print("")


def menu():
    GOTO_TUTORIAL = 1
    SAVE_AND_EXIT = 2
    INVENTORY = 3
    menu_choice = int(input("What do thau wish to do?"));
    if menu_choice == GOTO_TUTORIAL:
        #tutorial()
        print("tutoral")
    if menu_choice == SAVE_AND_EXIT:
        print("Save + Exit")
    if menu_choice == INVENTORY:
        print("inv")

animate_text("Hello world")
clear_screen()
print(ui.ui_inventory)

#def ending1
    
#def ending2:
#def death:
#-------------------------------------------------------------------------Selection System-----------------------------------------------------------------
class Default_action_menu():
    def default_action_menu(self, action_1, action_2, action_3):
        while True:
            print(ui.ui_actionmenu)
            self.selection = int(input("Your command -->"))
            try:
                if self.selection == 1:
                    print(f"{action_1} selected")
                    return 1
                if self.selection == 2:
                    print(f"{action_2} selected")
                    return 2
                if self.selection == 3:
                    print(f"{action_3} selected")
                    return 3
            except ValueError:
                print("Please enter a valid number")
                continue
            except:
                print("Unknown error has occured")
                continue


def player_select():
    HUMAN = "1"
    BEAST = "2"
    MORE_INFO = "i"
    print(ui.characterselect)
    player_choice = input("What doth thou choose? --> ")
    if player_choice == HUMAN:
        print("Human selected")
        return "Human"
    elif player_choice == BEAST:
        print("Beast selected")
        return "Beast"
    elif player_choice == MORE_INFO:
        print("More info") # TODO: Skriv mer info
        input("Press enter to go back...")
        player_select()
    else:
        print("Please enter a valid choice")
        player_select()


def player_and_name_select():
    name = input(ui.name_select)
    selected_player = player_select()
    if selected_player == "Human":
        player = ch.Player(100, 100, name, "Human", 5)
    elif selected_player == "Beast":
        player = ch.Player(200, 50, name, "Beast", 10)
    print(f"Welcome {name} the {ch.Player}")
    print (f"Your health is {player.health}")

player_and_name_select()