import sys
import time
import subprocess as sp
import pkg_resources
import msvcrt as m

# Check if the user has the required packages installed
required = {'progressbar', 'emoji', 'pydub'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

# If the user is missing any of the required packages, install them
if missing:
    sp.check_call([sys.executable, '-m', 'pip', 'install', *missing], stdout=sp.DEVNULL)
    sp.call("cls", shell=True)
    print("Dependencies installed")

import ui_elements
import characters
from pydub import AudioSegment
from pydub.playback import play

def animate_text(text):
    '''Makes text appear one letter at a time'''
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

def wait_for_keypress():
        m.getch()

def intro():
    sp.call("cls", shell=True) # Clears the screen
    print("nah no way")
    print(ui_elements.intro_name)
    wait_for_keypress()

def main():
    intro()
    
if __name__ == "__main__":
    main()

def fight():
    print("Do thau wish to fight")

def menu():
    Goto_tutorial = 1
    Save_and_exit = 2
    inventory = 3
    menu_choice = int(input("What do thau wish to do?"));
    if menu_choice == Goto_tutorial:
        #tutorial()
        print("tutoral")
    if menu_choice == Save_and_exit:
        print("Save + Exit")
    if menu_choice == inventory:
        print("inv")

animate_text("Hello world")
sp.call("cls", shell=True)
print(ui_elements.ui_inventory)

#def ending1
    
#def ending2:
#def death:
#-------------------------------------------------------------------------Selection System-----------------------------------------------------------------

class Default_action_menu():
    def default_action_menu(self, action_1, action_2, action_3):
        while True:
            print(ui_elements)
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

def player_and_name_select():
    name = input("What is thy name? -->")
    HUMAN = 1
    BEAST = 2
    # Lista av spelbara karaktärer
    player_human = characters.Player(100, 100, name)
    player_beast = characters.Player(200, 50, name)
    more_info = "i"
    print(ui_elements.characterselect)
    player_choice = int(input("What doth thou choose? -->"))
    if player_choice == HUMAN:
        print("Human selected")
        return player_human
    elif player_choice == BEAST:
        print("Beast selected")
        return player_beast
    elif player_choice == more_info:
        print("More info")
        player_and_name_select()
    else:
        print("Please enter a valid choice")
        player_and_name_select()
    

player_and_name_select()