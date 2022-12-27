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


animate_text("Hello world", "fast")
clear_screen()
print(ui.ui_inventory)


#-------------------------------------------------------------------------Selection System-----------------------------------------------------------------
class DefaultActionMenu():
    """
    Default player_action menu that is used in the game.
    """
    def default_action_menu(self, action_1, action_2, action_3):
        """
        This is the default player_action menu that is used in the game.
        It is used in the main game loop and in the menu system.
        """
        while True:
            # Prompt the player to attack or defend
            player_action = input("What do you want to do? (A)ttack, (D)efend?")

            # Handle the player's player_action
            try:
                if player_action.lower() == "a":
                    print("Select Attack")
                    if selection == 1:
                        print(f"{action_1} selected")
                        return 1
                    if selection == 2:
                        print(f"{action_2} selected")
                        return 2
                    if selection == 3:
                        print(f"{action_3} selected")
                        return 3
                    # Calculate the damage dealt by the player
                    print(f"You attack the enemy and deal {damage} points of damage!")
                elif player_action.lower() == "d":
                    # Reduce the damage taken by the player by 50%
                    print(f"You defend against the enemy's attack and take {damage * 0.5} points of damage.")

            except(IndexError,ValueError):
                print("Invalid player_action. Please try again.")
                continue

            except:
                print("Unknown error has occured")
                print(ui.ui_actionmenu)
                selection = int(input("Your command -->"))
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

#-----------------------------------------------------------------------FIGHTING-----------------------------------------------------------------------#

FIGHT = 1
RUN = 2
def fight_start():
    print("Do thau wish to fight, or wish to run? 1 = FIHT, 2 = RUN")
    fight_or_flight = int(input("Yeh m8"))
    if fight_or_flight == FIGHT:
        fight_loop_tm()
    
    if fight_or_flight == RUN:
        running_coward_tm()


def running_coward_tm():
    if random.randint(1, 100) <= 20:
        print("You try to run, but the enemy blocks thau escape!")
        fight_loop_tm()
    elif random.randint(1, 100) <= 5:
        print("You try to run, but thau trips and falls, shattering every bone in your body.")
        death()
    else:
        print("Thau successfully run away from the fight!")
        print("Though it came with an item loss")






# Start the fight loop
def fight_loop_tm():
    while True:
        # Display the current health of the player and the enemy
        print(f"Player health: {player_health}")
        print(f"Enemy health: {enemy_health}")

        DefaultActionMenu().action_menu()

        # Check if the enemy has been defeated
        if enemy_health <= 0:
            print("You have defeated the enemy!")
            break

        # Enemy attacks the player
        print(f"The enemy attacks you and deals {damage} points of damage.")

        # Check if the player has been a "has been"
        if player_health <= 0: death()

#--------------------------------------------------------------Death and Endings-----------------------------------------------------------------------#




def death():
    print("You have died")
    print("Game over")
    wait_for_keypress()
    time.sleep(2)
    quit()

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