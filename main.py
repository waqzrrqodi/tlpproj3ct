import sys
import time
import subprocess as sp
import pkg_resources
import os
from platform import system
import random



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
    print("Installing dependencies... \nThis may take a while")
    sp.check_call([sys.executable, '-m', 'pip', 'install', *missing], stdout=sp.DEVNULL)
    clear_screen()
    print("Dependencies installed")
    time.sleep(0.5)
    clear_screen()

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

CLASS_CHOICE_1 = 1
CLASS_CHOICE_2 = 2
CLASS_CHOICE_3 = 3
def fight_loop_tm():
    print("")

def running_coward_tm():
    print("You've successfully escaped!")
    print("Though it came with an item loss")


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
    def subclass_selection(self, subclass_1, subclass_2, more_info):
        HUMAN = "1"
        BEAST = "2"
        MORE_INFO = "i"
        self.choice = input("What is your choice? --> ")
        try:
            if self.choice == HUMAN:
                print(f"{subclass_1} selected")
                player = ch.Human()
            elif self.choice == BEAST:
                print(f"{subclass_2} selected")
                player = ch.Beast()
            elif self.choice == MORE_INFO:
                print(f"{ui.class_info}")
                user_choice = input("Please type b to go back (or y?)--> ")
                if user_choice == "b" or user_choice == "B":
                    Player_And_Name_Select()
                elif user_choice == "y" or user_choice == "Y":
                    print("Hidden user aquired! (not really) \nYou are the god now.")
                    player = ch.More_Info_Player()
            return player
        except ValueError:
            print("Please enter a valid number.")
            return
        
        except:
            print("Unknown error has occured")
            return

class Player_And_Name_Select(Default_action_menu):
    def __init__(self):
        clear_screen()
        self.player = None
        self.name = None
        self.player_select()
        self.name_select()
    def player_select(self):
        print(ui.characterselect)
        self.player = self.subclass_selection("Human", "Beast", "More info")
    def name_select(self):
        self.name = input("What is your name? --> ")
        print(f"Welcome {self.name} the {self.player.SUBCLASS}")


Player_And_Name_Select()