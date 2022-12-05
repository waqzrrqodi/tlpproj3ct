import sys
import time
import subprocess as sp
import pkg_resources

# Check if the user has the required packages installed
required = {'progressbar', 'playsound', 'emoji'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

# If the user is missing any of the required packages, install them
if missing:
    sp.check_call([sys.executable, '-m', 'pip', 'install', *missing], stdout=sp.DEVNULL)
    sp.call("cls", shell=True)
    print("Dependencies installed")

import ui_elements
from emoji import emojize

# Makes text appear one letter at a time
def animate_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)


def intro():
    sp.call("cls", shell=True)
    print("nah no way")
    print(ui_elements.intro_name)

def main():
    intro()
    
if __name__ == "__main__":
    main()

def fight():
    print("Do thau wish to fight")

def menu():
    menu_choice = int(input("What do thau wish to do?"));
    if menu_choice == 1:
        #tutorial()
        print("tutoral")
    if menu_choice == 2:
        print("Save + Exit")
    if menu_choice == 3:
        print("inv")
animate_text("Hello world")
sp.call("cls", shell=True)
print(ui_elements.ui_inventory)

#def ending1
    
#def ending2:
#def death:
#-------------------------------------------------------------------------Selection System-----------------------------------------------------------------

class default_action_menu():
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
