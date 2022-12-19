import sys
import time
import random
import subprocess as sp
import os
from platform import system
import pkg_resources



# Check if the user has the required packages installed
if system() == "Windows":
    required = {'progressbar', 'emoji', 'pydub'}
else:
    required = {'progressbar', 'emoji', 'pydub', 'getch'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

# for clearing console (windows and unix systems)
CLEAR = "cls"
if os.name == "posix":
    CLEAR = "clear"
def clear_screen():
    """Clears the screen"""
    sp.call(CLEAR, shell=True)

# If the user is missing any of the required packages, install them
if missing:
    print("Installing dependencies... \nThis may take a while")
    sp.check_call([sys.executable, '-m', 'pip', 'install', *missing], stdout=sp.DEVNULL)
    clear_screen()
    print("Dependencies installed")
    time.sleep(0.5)
    clear_screen()

from pydub import AudioSegment
from pydub.playback import play
import ui_elements as ui
import characters as ch

if system() == "Windows":
    from msvcrt import getch as getkey
else:
    from getch import getch as getkey_linux # For linux systems, getch is not included in the standard library on windows.

def animate_text(text, sleep_time):
    '''
    Makes text appear one letter at a time at a given speed
    fast, slow, or default
    '''
    FAST = 0.03
    SLOW = 0.1
    DEFAULT = 0.05
    if sleep_time == "fast":
        sleep_time = FAST
    elif sleep_time == "slow":
        sleep_time = SLOW
    else:
        sleep_time = DEFAULT
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(sleep_time)
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




FIGHT = 1
RUN = 2

def fight_start():
    print("Do thau wish to fight, or wish to run? 1 = FIHT, 2 = RUN")
    fight_or_flight = int(input("Yeh m8"))
    if fight_or_flight == FIGHT:
        fight_loop_tm()
    
    if fight_or_flight == RUN:
        running_coward_tm()

CLASS_CHOICE_1 = 1
CLASS_CHOICE_2 = 2
CLASS_CHOICE_3 = 3
def fight_loop_tm():
    print("Kasper jag är oskyldig")

def running_coward_tm():
    print("You've successfully escaped!")
    print("Though it came with an item loss")




animate_text("Hello world", "fast")
clear_screen()
print(ui.ui_inventory)

#def ending1
    
#def ending2:
#def death:
#-------------------------------------------------------------------------Selection System-----------------------------------------------------------------
class DefaultActionMenu():
    """
    Default action menu that is used in the game.
    """
    def default_action_menu(self, action_1, action_2, action_3):
        """
        This is the default action menu that is used in the game.
        It is used in the main game loop and in the menu system.
        """
        while True:
            print(ui.ui_actionmenu)
            selection = int(input("Your command -->"))
            try:
                if selection == 1:
                    print(f"{action_1} selected")
                    return 1
                if selection == 2:
                    print(f"{action_2} selected")
                    return 2
                if selection == 3:
                    print(f"{action_3} selected")
                    return 3
            except ValueError:
                print("Please enter a valid number")
                continue
            except:
                print("Unknown error has occured")
                continue
    def subclass_selection(self, subclass_1, subclass_2):
        """
        The menu of the choices of the subclasses (Human or Beast) of the player and the name of the player.
        """
        clear_screen()
        print(ui.characterselect)
        HUMAN = "1"
        BEAST = "2"
        MORE_INFO = "i"
        player = None
        choice = input("What is your choice? --> ")
        try:
            if choice == HUMAN:
                print(f"{subclass_1} selected")
                player = ch.Human()
            elif choice == BEAST:
                print(f"{subclass_2} selected")
                player = ch.Beast()
            elif choice == MORE_INFO:
                print(f"{ui.class_info}")
                user_choice = input("Please type b to go back (or y?)--> ")
                if user_choice == "b" or user_choice == "B":
                    PlayerAndNameSelect()
                elif user_choice == "y" or user_choice == "Y":
                    print("Hidden user aquired! (not really) \nYou are the god now.")
                    player = ch.More_Info_Player()
            else:
                print("Please enter a valid input...")
                time.sleep(1)
                input("Press enter to continue...")
                return
            return player
        except ValueError:
            print("Please enter a valid number.")
            return
        except:
            print("Unknown error has occured")
            time.sleep(1)
            clear_screen()
            animate_text("Retrying...", "default")
            return

class PlayerAndNameSelect(DefaultActionMenu):
    """for selecting the player and the name of the player"""
    def __init__(self):
        clear_screen()
        self.player = None
        self.name = None
        while True:
            if self.player is None:
                self.player_select()
            else:
                break
        self.name_select()
    def player_select(self):
        """
        player selection menu
        """
        self.player = self.subclass_selection("Human", "Beast")
    def name_select(self):
        """
        name selection menu
        """
        self.name = input("What is your name? --> ")
        print(f"Welcome {self.name} the {self.player.SUBCLASS}")

def menu():
    """
    The menu system of the game that is used to navigate, save, and exit the game.
    """
    GOTO_TUTORIAL = "1"
    SAVE_AND_EXIT = "2"
    INVENTORY = "3"
    CONTINUE = ""
    clear_screen()
    print(ui.ui_textbox)
    menu_choice = input("What do thau wish to do? ");
    if menu_choice == GOTO_TUTORIAL:
        #tutorial()
        print("tutoral")
    if menu_choice == SAVE_AND_EXIT:
        print("Save + Exit")
    if menu_choice == INVENTORY:
        print("inv")
    if menu_choice == CONTINUE:
        animate_text("Continuing with story...", "default")

def tutorial():
    # This is the tutorial to make sure the player knows how to play the game
    pass

def level_choice():
    # Choose level and "difficulty"
    pass

def fleeflight():
    # Probability of success or failure
    pass

def fight():
    # If boss fight, then fight_loop_tm(), else fight_loop()
    # If player dies, then death()
    # If boss fight, make choice to save available at the end of the fight (if player dies, then death())
    pass

def death():
    # Shows the death screen and the ending of the game
    # Shows the player their total score and items/triumphs
    pass

def ending1():
    pass

def ending2():
    pass

def ending3():
    pass

#-------------------------------------------------------------------------Game Functions-----------------------------------------------------------------

def main():
    intro()
    PlayerAndNameSelect()
    menu()
    tutorial()
    level_choice()
    fleeflight()
    fight()
    death()
    

    
if __name__ == "__main__":
    main()