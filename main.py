import sys
import time
import random
import subprocess as sp
import os
from platform import system
import pkg_resources
from itertools import chain
import narration as narr
from item_management import *
from ad_screen import *

# Check if the user has the required packages installed
if system() == "Windows":
    required = {'progressbar', 'pygame', 'wit', 'webp'}
else:
    required = {'progressbar', 'pygame', 'getch', 'wit', 'webp'}
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

import pygame
from pygame.locals import *
from pygame import mixer
import pickle
from ui_elements import * # production materials
import characters as ch

if system() == "Windows":
    from msvcrt import getch as getkey
else:
    from getch import getch as getkey_linux # For linux systems, getch is not included in the standard library on windows.
SETTING1 = ""
SETTING2 = ""
SETTING3 = ""
def animate_text(text, sleep_time):
    '''
    Makes text appear one letter at a time at a given speed
    fast, slow, or default
    '''
    
    SUPERSPEED = 0.004
    FAST = 0.01
    SLOW = 0.1
    DEFAULT = 0.05
    
    if SETTINGS["text_speed_choice"]["SETTING"] == "fast":
        sleep_time = FAST
    elif SETTINGS["text_speed_choice"]["SETTING"] == "slow":
        sleep_time = SLOW
    elif SETTINGS["text_speed_choice"]["SETTING"] == "superspeed":
        sleep_time = SUPERSPEED
    elif SETTINGS["text_speed_choice"]["SETTING"] == "med":
        sleep_time = DEFAULT
    else: 
        if sleep_time == "fast":
            sleep_time = FAST
        elif sleep_time == "slow":
            sleep_time = SLOW
        elif sleep_time == "superspeed":
            sleep_time = SUPERSPEED
        else:
            sleep_time = DEFAULT
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(sleep_time)
    time.sleep(1)

def wait_for_keypress():
    '''
    Waits for a keypress on the keyboard
    '''
    if system() == "Windows":
        getkey()
    else:
        getkey_linux()

def intro():
    """
    Runs the intro sequence and the disclaimer, as well as starts the intro music.
    """
    
    clear_screen() # Clears the screen
    print(disclaimer)
    time.sleep(3)
    clear_screen()

    print(thx_disclaimer)
    time.sleep(1)
    clear_screen()

    print(ilovetaxfraud)
    time.sleep(1)
    clear_screen()

    print(intro_name)
    background_theme("./SoundEngine5000/theme_song.wav")
    time.sleep(1)

    wait_for_keypress()
    
    intro_menu()

def intro_splash_only():
    clear_screen()
    print(ilovetaxfraud)
    time.sleep(1)
    clear_screen()

    print(intro_name)
    background_theme("./SoundEngine5000/theme_song.wav")
    time.sleep(1)
    wait_for_keypress()
    intro_menu()

#----------------------------------------------------------------------Player, Enemy and Objects----------------------------------------------------------#

# Initialize all the enemies and add stats for story progression, level, and tutorial etc.
valma = ch.Enemy("Valma the Soulbroken", 200, 1000, "God", 3)
simpa = ch.Enemy("Simpa", 50, 100, "Human", 2)
goblin = ch.Enemy("Lwittle Gwoblin", 50, 100, "Monster", 1)
bilo = ch.Enemy("Bilo, the Town Rapist", 100, 50, "Human", 4)
qlex = ch.Enemy("Steroid Beast", 25, 400, "Monster", 1)
pangloss = ch.Enemy("Pangloss", 200, 50, "Human", 3)
bandits = ch.Enemy("Bandits", 100, 100, "Human", 2)
neo = ch.Enemy("Neo Järnmalm", 200, 200, "Human", 3)
fulcrum = ch.Enemy("Fulcrum", 250, 100, "Yodie Gang", 3)
bill = ch.Enemy("Retired Orthodox Rabbi Bill Clinton", 300, 40, "Human", 4)
steroid_beast = ch.Enemy("Steroid Beast", 25, 400, "Monster", 1)
anti_virgin = ch.Enemy("The Anti-Virgin", 100, 150, "Human", 2)
homeless_man = ch.Enemy("Hobo", 120, 120, "Human", 3)
guards = ch.Enemy("Guards", 150, 120, "Human", 2)
rap_god = ch.Enemy("The Rap God", 90, 120, "Human", 4)
ladythatstolemylypsyl = ch.Enemy("Strange Lady", 90, 90, "Human", 3)
skeletons = ch.Enemy("Skeletons", 180, 120, "Monster", 1)
ghosts = ch.Enemy("Ghosts", 50, 150, "Monster", 1)
witch = ch.Enemy("Witch", 150, 150, "Monster", 1)
strongman = ch.Enemy("Russian Muscle Man", 200, 200, "Human", 5)
player = None
level = 0
story_progress = 0
tutorial_done = bool
used_routes = []


#-------------------------------------------------------------------------Selection System----------------------------------------------------------------#
class DefaultActionMenu():
    """
    Default player_action menu that is used in the game.
    """
    def action_menu(action_1, action_2, action_3):
        """
        This is the default player_action menu that is used in the game.
        It is used in the main game loop and in the menu system.
        """
        GOTO_MENU = "4"
        
        print (f"Action Menu: \n 1. Head North \n 2. Head West \n 3. Head East \n 4. Go to menu") # For testing purposes
        selection = input("Your command --> ")
        
        # Handle the player's player_action
        try:
            if selection == "1":
                animate_text(f"\nYou choose to head north and you stumble upon the {action_1}!", "fast")
                return action_1
            if selection == "2":
                animate_text(f"\nYou choose to head west and in your path stands the {action_2}!", "fast")
                return action_2
            if selection == "3":
                animate_text(f"\nYou choose to head east, and after some walking you find the {action_3}!", "fast")
                return action_3
            if selection == GOTO_MENU or selection == "menu":
                animate_text("\nGoing to menu", "fast")
                menu()

        except(IndexError,ValueError):
            print("Invalid player_action. Please try again.")
            return

        except:
            print("Unknown error hath occured")
            return


    def fight_menu(self):
        """
        The menu of the choices of the player's attacks.
        """
        ATTACK = "a"
        DEFEND = "d"
        HEAL = "h"
        MORE_INFO = "i"
        player_action = None
        selection = input(fight_menu_choices)
        try:
            if selection.lower() == ATTACK:
                print(f"Attack Selected")
                return "attack"

            elif selection == DEFEND:
                print(f"Defend selected")
                return "defend"

            elif selection == HEAL:
                print(f"Heal selected")
                return "heal"

            elif selection == MORE_INFO:
                print("Prints more info about the player's attacks and info about the enemy")
                user_choice = input("Please type b to go back --> ")
                if user_choice.lower() == "b":
                    self.fight_menu()
                else:
                    print("Invalid input")
                    self.fight_menu()
            else:
                print("Invalid input")
                self.fight_menu()
        except(IndexError,ValueError):
            print("Invalid input")
            self.fight_menu()
        except:
            print("Unknown error hath occured")
            self.fight_menu()
        return player_action


    def subclass_selection(self, subclass_1, subclass_2, subclass_3):
        """
        The menu of the choices of the subclasses (Human or Beast (or gnoblin)) of the player and the name of the player.
        """
        clear_screen()
        print(characterselect)
        HUMAN = "1"
        BEAST = "2"
        GNOBLIN = "g"
        MORE_INFO = "i"
        player_subclass = None
        choice = input("What is your choice? --> ")
        try:
            if choice == HUMAN:
                print(f"{subclass_1} selected")
                player_subclass = ch.Human()
            elif choice == BEAST:
                print(f"{subclass_2} selected")
                player_subclass = ch.Beast()
            elif choice == GNOBLIN:
                print(f"{subclass_3} selected")
                player_subclass = ch.Gnoblin() 
            elif choice == MORE_INFO:
                clear_screen()
                print(class_info)
                user_choice = input("Please type b to go back (or y?)--> ")
                if user_choice.lower() == "b":
                    PlayerAndNameSelect()
                elif user_choice == "y" or user_choice == "Y":
                    print("Hidden user aquired! (not really) \nYou are the god now.")
                    player_subclass = ch.More_Info_Player()
            else:
                print("Please enter a valid input...")
                time.sleep(1)
                input("\nPress enter to continue...")
                return
            return player_subclass
        except ValueError:
            print("Please enter a valid number.")
            return

def inv_show():
    """
    Shows the player's inventory, in a small and a full view.
    """
    
    clear_screen()
    #small splash
    print(f"\nYour name: {player.name}")
    print(f"\nPlayer Health: {player.hp}")
    print(f"\nPlayer Strenght: {player.strength}")
    print(f"\nPlayer Armour: {player.armour}")
    print(f"\nPlayer Awesomeness level: {player.level}")

    
    while True:
        inv_expasion = input("------------------------------- \n Do you wish to expand to full overview? (Y/n) \n------------------------------- \n-->")
        if inv_expasion.lower() == "y" or inv_expasion.lower() == "yes" or inv_expasion.lower() == "":
            clear_screen()
            
            print(f"Name: {player.name}")
            print(f"HP: {player.hp}, stronks: {player.strength}, armor: {player.armour}, lvl: {player.level}")
            print("---------------------------------------------")
            #expand to full inventory view
            if len(player.inventory.inv) == 0:
                print("Inventory is empty")
                input("\nPress enter to continue...")
                break
            else:
                print("Inventory: ")
                for item in enumerate(player.inventory.inv):
                    print('Name: {}\nType: {}\nCost: {}\nWorth: {}\nRarity: {}\nBonus: {} HP\nHealing: {}\nDamage: {}'.format(item.get("Name"), item.get("Type"), item.get("Cost"), item.get("Worth"), item.get("Rarity"), item.get("HP_Bonus"), item.get("Healing Capability"), item.get("Damage")))
                input("\nPress enter to continue...")
                break
        elif inv_expasion.lower() == "n" or inv_expasion.lower() == "no" or inv_expasion.lower() == "q":
            break
        else:
            input("Please provid valid input")
            continue
    return

#-------------------------------------------------------------------------Player and Name Selection----------------------------------------------------------------#
VIKING_NAMES=[
    #Viking names
    "Arne", "Birger","Bjorn","Bjornulf","Bo", "Frode", "Knud", "Odger", "Trygve", "Troels", #Man
    
    "Astrid","Bodil","Frida","Gertrud", "Gudrun","Gunnhild","Gunnvor","Halla","Hedvig","Helga", #Kvinna
    ]
class PlayerAndNameSelect(DefaultActionMenu):
    """for selecting the player and the name of the player"""
    def __init__(self):
        clear_screen()
        self.player_subclass = None
        self.name = None
        while True:
            if self.player_subclass is None:
                self.player_select()
            else:
                break
        self.name_select()
        global player
        player = self.create_player()
    def player_select(self):
        """
        player selection menu
        """
        self.player_subclass = self.subclass_selection("Human", "Beast", "Gnoblin")
    def name_select(self):
        """
        name selection menu
        """
        user_name_input = input("What is your name? --> ")
        self.name = random.choice(VIKING_NAMES)
        clear_screen()
        if user_name_input.lower == "Martin" or user_name_input.lower == "Oskis" or user_name_input.lower == "Sebbis" or user_name_input.lower == "Kaspis":
            print("That is an absolutely beautiful name mate")
            self.name = user_name_input
        else:
            print(f"{user_name_input} is a good name, though I think {self.name} is a stronger and a more viking name.")
            input(f"Confirm {self.name}? yes/absolutly --> ")
            print("Are you sure? You won't be able to change it later (yes/perhaps)")
            input("Confirm --> ")
            print(f"{self.name} accepted")
        time.sleep(0.3)

        time.sleep(0.3)
        clear_screen()

        animate_text(f"Welcome {self.name} the {self.player_subclass.SUBCLASS}", "fast")
    def create_player(self):
        """
        creates the player
        """
        player = ch.Player(100, self.player_subclass.HP, self.name, self.player_subclass.SUBCLASS, self.player_subclass.SPEED)
        return player

#-----------------------------------------------------------------------------------Menus------------------------------------------------------------------------#
def intro_menu():
    """
    The menu that is used to start the game.
    """
    PLAY = "1"
    OPTIONS = "2"
    TUTORIAL = "3"
    CREDITS = "4"
    EXIT = "5"
    clear_screen()
    print(intro_menu_choices)
    menu_choice = input("What doth thou wish to do? --> ")
    if menu_choice == PLAY:
        LOAD = "1"
        NEW_GAME = "2"
        try:
            clear_screen()
            choice = input("Do you wish to load a save file or start a new game? (1)Load or (2)New Game --> ")
            # Check if the player has a save file
            # If the player has a save file, ask if the player wants to load the save file
            # If the player does not have a save file, start the game
            if choice == LOAD: # Not implemented yet
                animate_text("Loading...", "fast")
                time.sleep(0.3)
                clear_screen()
                load_game()
            elif choice == NEW_GAME:
                PlayerAndNameSelect()
                game_loop()
        except ValueError:
            print("Invalid input")
            intro_menu()
        clear_screen()
        animate_text("Loading...", "fast")
    elif menu_choice == OPTIONS:
        animate_text("\nSummoning options menu...\n", "fast")
        clear_screen()
        options_menu()
        intro_menu()
    elif menu_choice == TUTORIAL:
        tutorial()
        intro_menu()
    elif menu_choice == CREDITS:
        clear_screen()
        animate_text("\ninitiating credits sequence...\n", "fast")
        credits()
        intro_menu()
    elif menu_choice == EXIT:
        exit()
    else:
        print("Invalid input")
        time.sleep(0.3)
        intro_menu()

def menu():
    """
    The menu system of the game that is used to navigate, save, and exit the game.
    """
    GOTO_TUTORIAL = "1"
    SAVE_AND_EXIT = "2"
    INVENTORY = "3"
    OPTIONS = "4"
    CONTINUE = "continue"
    # name = "Navigation Menu"
    # action_1 = "Tutorial"
    # action_2 = "Save and Exit"
    # action_3 = "Inventory"
    # action_4 = "Continue"
    # action_5 = "Options"
    clear_screen()
    # print(ui_textbox)
    print("Navigation Menu: \n1. Tutorial \n2. Save and Exit \n3. Inventory or stats \n4. Options \n\nTo continue with story, press [Enter]\n") # For testing purposes
    menu_choice = input("What do thau wish to do? ");
    if menu_choice == GOTO_TUTORIAL:
        print("tutorial")
        tutorial()
    if menu_choice == SAVE_AND_EXIT:
        print("Save + Exit")
        save_game()
        exit()
    if menu_choice == INVENTORY:
        print("inv")
        player.inventory.inv.append(player.inventory.item("Test Item", 10)) # For testing purposes
        player.inventory.inv.append(player.inventory.item("Test Item 2", 5)) # For testing purposes
        inv_show()
        menu()
    if menu_choice == CONTINUE or menu_choice == "":
        animate_text("Continuing with story...", "default")
        clear_screen()
        return
    if menu_choice == OPTIONS:
        clear_screen()
        options_menu()

def tutorial():
    '''
    This is the tutorial to make sure the player knows how to play the game
    '''
    user_input = input("Wouldst thou like to see the tutorial, or art thou bold enough to continue without it? (y/N) --> ")
    try:
        if user_input.lower() == "y":
            animate_text("Loading tutorial...", "fast")
            print("Haha Silly, you thought there was a tutorial, but there is not.")
            time.sleep(0.3)
        elif user_input.lower() == "n" or user_input.lower() == "":
            animate_text("Continuing without tutorial...", "fast")
        else:
            print("Invalid input")
            tutorial()
        input("Press enter to go back to the main menu...")
    except:
        print("Unknown error hath occured")
        tutorial()


#-----------------------------------------------------------------------------Options---------------------------------------------------------------


def options_menu():
    '''
    So you can change text speed, mute music and alter font colour
    '''
    global SETTING1
    global SETTING2
    global SETTING3
    print("\nOptions:\n1. Text Speed\n2. Sound\n3. Font Colour\n4. Go back\n")
    user_input = input("-->")
    try:
        if user_input == "1":
            clear_screen()
            print("\nHow fast do you want the text to move?\n1. Martin Mode (TURBO FAST)\n2. Fast\n3. Medium\n4. Slow\n5. Go back\n")
            text_speed_input = input("--> ")
            if text_speed_input == "1" and SETTINGS["text_speed_choice"]["SETTING"] == "superspeed":
                animate_text("The text speed is already set to turbo you absolute buffoon", "fast")
                clear_screen()
            elif text_speed_input == "2" and SETTINGS["text_speed_choice"]["SETTING"] == "fast":
                animate_text("The text is already set to fast, you lowly peasant", "fast")
                clear_screen()
            elif text_speed_input == "3" and SETTINGS["text_speed_choice"]["SETTING"] == "medium":
                animate_text("The text is already set to medium, cockhead", "fast")
                clear_screen()
            elif text_speed_input == "4" and SETTINGS["text_speed_choice"]["SETTING"] == "slow":
                animate_text("Text speed is already set to slow you nonce", "fast")
                clear_screen()
            elif text_speed_input == "1":
                SETTINGS["text_speed_choice"]["SETTING"] = "superspeed"
                animate_text("Changed text speed to turbo", "fast")
                clear_screen()
            elif text_speed_input == "2":
                SETTINGS["text_speed_choice"]["SETTING"] = "fast"
                animate_text("Changed text speed to fast", "fast")
                clear_screen()
            elif text_speed_input == "3":
                SETTINGS["text_speed_choice"]["SETTING"] = "medium"
                animate_text("Changed text speed to medium", "fast")
                clear_screen()
            elif text_speed_input == "4":
                SETTINGS["text_speed_choice"]["SETTING"] = "slow"
                animate_text("Changed text speed to slow", "fast")
                clear_screen()
            elif text_speed_input == "5":
                clear_screen()
                return
            else:
                print("Invalid Input")
                clear_screen()
                return
        elif user_input.lower() == "2":
            clear_screen()
            print("\nSound:\n1. On\n2. Off\n")
            sound_input = input("--> ")
            if sound_input == "1" and SETTING2 == "on":
                animate_text("Sound is already turned on, you lowborn craven.", "fast")
                clear_screen()
            elif sound_input == "2" and SETTING2 == "off":
                animate_text("The game is already muted, fuckface", "fast")
                clear_screen()
            elif sound_input == "1":
                pygame.mixer.music.set_volume(0.5)
                animate_text("Volume On", "fast")
                SETTING2 = "on"
                clear_screen()
            elif sound_input == "2":
                pygame.mixer.music.set_volume(0.0)
                animate_text("Game Muted", "fast")
                SETTING2 = "off"
                clear_screen()
            else:
                print("Invalid Input")
                clear_screen()
                return
        elif user_input == "3":
            clear_screen()
            print("\nSelect a colour:\n1. Crimson Red\n2. Goblin Green\n3. Blueballs Blue\n4. Severe Lack of Sunlight White\n5. Go back\n")
            colour_input = input("--> ")
            if colour_input == "1" and SETTING3 == "red":
                animate_text("Text is already set to red you fucking incompetent moron", "fast")
                clear_screen()
            elif colour_input == "2" and SETTING3 == "green":
                animate_text("The text is already green you little prick", "fast")
                clear_screen()
            elif colour_input == "3" and SETTING3 == "blue":
                animate_text("The text is already set to blue you fucking twat", "fast")
                clear_screen()
            elif colour_input == "4" and SETTING3 == "white":
                animate_text("Are you daft?! The text is already white", "fast")
                clear_screen()
            elif colour_input == "1":
                os.system('color 4')
                SETTING3 = "red"
                animate_text("Colour changed to red", "fast")
                clear_screen()
            elif colour_input == "2":
                os.system('color 2')
                SETTING3 = "green"
                animate_text("Colour changed to green", "fast")
                clear_screen()
            elif colour_input == "3":
                os.system('color 1')
                SETTING3 = "blue"
                animate_text("Colour changed to blue", "fast")
                clear_screen()
            elif colour_input == "4":
                os.system('color 7')
                SETTING3 = "white"
                animate_text("Colour changed to white", "fast")
                clear_screen()
            elif colour_input == "5":
                clear_screen()
                return
            else:
                print("Invalid Input")
        elif user_input.lower() == "4":
            clear_screen()
            return
        else:
            print("Invalid Input")
            clear_screen()
        options_menu()
    except:
        print("Unknown Error")
        options_menu() 


SETTINGS = {
    "text_speed_choice": {"input_choice": "", "SETTING": SETTING1},
    "mute_choice": {"input_choice": "", "SETTING": SETTING2},
    "colour_choice": {"input_choice": "", "SETTING": SETTING3},
}

SETTINGS["text_speed_choice"]["SETTING"] = SETTING1
SETTINGS["mute_choice"]["SETTING"] = SETTING2
SETTINGS["colour_choice"]["SETTING"] = SETTING3


#-----------------------------------------------------------------------------------Sounds and whatnot------------------------------------------------------------------------#
def background_theme(music):
    """
    Plays background music
    """
    if pygame.mixer.get_busy() == False:
        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.fadeout(3)
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()



def sound_engine(sound):
    """
    Plays sound effects
    """
    pygame.mixer.init()
    pygame.mixer.Sound(sound)
    return pygame.mixer.Sound(sound)

chest_sound = sound_engine("./SoundEngine5000/Chest_sound.wav")
item_sound = sound_engine("./SoundEngine5000/Item_Pickup.wav")
enemy_grunt = sound_engine("./SoundEngine5000/Enemy_Grunt.wav")
enemy_grunt2 = sound_engine("./SoundEngine5000/Enemy_Grunt2.wav")
# level_up = sound_engine("./SoundEngine5000/Level_Up.wav")

# chest_sound.play()

#-----------------------------------------------------------------------FIGHTING-----------------------------------------------------------------------#
class FightLoopTM(DefaultActionMenu):
    """
    The actual fight loop with all of the other fighting classes and loops
    """
    def __init__(self, enemy_name):
        background_theme("./SoundEngine5000/battle_theme.wav")
        self.instant_win = False
        self.player_health = player.hp
        self.player_weapon = player.weapon
        self.armour = player.armour
        self.speed = player.speed
        if enemy_name == "Goblins":
            self.enemy_health = goblin.health
            self.enemy_damage = goblin.damage
            self.enemy_speed = goblin.speed
        elif enemy_name == "Skeletons":
            self.enemy_health = skeletons.health
            self.enemy_damage = skeletons.damage
            self.enemy_speed = skeletons.speed
        elif enemy_name == "Simpa":
            self.enemy_health = simpa.health
            self.enemy_damage = simpa.damage
            self.enemy_speed = simpa.speed
        elif enemy_name == "Pangloss":
            self.enemy_health = pangloss.health
            self.enemy_damage = pangloss.damage
            self.enemy_speed = pangloss.speed
        elif enemy_name == "Bilo":
            self.enemy_health = bilo.health
            self.enemy_damage = bilo.damage
            self.enemy_speed = bilo.speed
        elif enemy_name == "Steroid Beast":
            self.enemy_health = steroid_beast.health
            self.enemy_damage = steroid_beast.damage
            self.enemy_speed = steroid_beast.speed
        elif enemy_name == "Homeless man":
            self.enemy_health = homeless_man.health
            self.enemy_damage = homeless_man.damage
            self.enemy_speed = homeless_man.speed
        elif enemy_name == "The Anti-Virgin":
            self.enemy_health = anti_virgin.health
            self.enemy_damage = anti_virgin.damage
            self.enemy_speed = anti_virgin.speed
        elif enemy_name == "Guards":
            self.enemy_health = guards.health
            self.enemy_damage = guards.damage
            self.enemy_speed = guards.speed
        elif enemy_name == "Rap God":
            self.enemy_health = rap_god.health
            self.enemy_damage = rap_god.damage
            self.enemy_speed = rap_god.speed
        elif enemy_name == "Strange Lady":
            self.enemy_health = ladythatstolemylypsyl.health
            self.enemy_damage = ladythatstolemylypsyl.damage
            self.enemy_speed = ladythatstolemylypsyl.speed
        elif enemy_name == "Ghosts":
            self.enemy_health = ghosts.health
            self.enemy_damage = ghosts.damage
            self.enemy_speed = ghosts.speed
        elif enemy_name == "Witch":
            self.enemy_health = witch.health
            self.enemy_damage = witch.damage
            self.enemy_speed = witch.speed
        elif enemy_name == "Russian Muscle Man":
            self.enemy_health = strongman.health
            self.enemy_damage = strongman.damage
            self.enemy_speed = strongman.speed
        elif enemy_name == "Valma the Soulbroken":
            self.enemy_health = valma.health
            self.enemy_damage = valma.damage
            self.enemy_speed = valma.speed
            self.enemy_name = valma.name
        elif enemy_name == "Shop":
            self.instant_win = True
        elif enemy_name == "Instant win":
            self.instant_win = True
        else:
            print("Unknown enemy")
            death()
            return
        if self.instant_win == False:
            print(f"Thou hast encountered {enemy_name}!")
            print(f"The {enemy_name} hath {self.enemy_health} health")
            print(f"Thou hast {self.player_health} health")
            # print(f"Thou hast {self.player_weapon.name} which deals {self.player_weapon.damage} damage")
            # print(f"Thou hast {self.armour.name} which reduces damage by 'placeholder' damage")
            self.fight_loop(enemy_name)

        self.fight_loop(enemy_name)

    def attack(self):
        """When the player selects the attack option in a fight"""
        self.enemy_health -= self.player_weapon.damage
        print(f"Thou attacketh the foe and dealeth {self.player_weapon.damage} points of damage!")

    def run(self):
        """When the player selects the run option in a fight"""
        if random.randint(1, 100) >= 50:
            print("You try to run, but the enemy blocks thau escape!")
            background_theme("./SoundEngine5000/battle_theme.wav")
            self.fight_loop()
        elif random.randint(1, 100) >= 10:
            print("Thau successfully run away from the fight!")
            print("Though it came with an item loss")
        elif random.randint(1, 100) >= 1:
            print("You try to run, but thau trips and falls, shattering every bone in your body.")
            death()

        else:
            ending1()

    def defend(self, damage):
        """When the player selects the defend option in a fight"""
        if self.armour != None:
            print(f"You defend against the enemy's attack and take {damage * self.armour.defense} points of damage.")
        else:
            # Reduce the damage taken by the player by 50% or maybe probability of taking damage?
            print(f"You defend against the enemy's attack and take {damage * 0.5} points of damage.")

    def heal(self):
        """When the player selects the heal option in a fight"""
        if self.player_health != self.player_max_health:
            print("Thou art not at full health!")
            inv_show()
            
            # Show the player it's inventory and ask them to select an item to use to heal
            # Calculate the amount of health restored by the player and add it to the player's health
            # If the player's health is greater than the player's maximum health, set the player's health to the player's maximum health
        elif self.player_health == self.player_max_health:
            print("Thou art already at full health!")

    
    def enemy_attack(self, damage, type):
        """When the enemy attacks the player in a fight and all the moves the enemy can do"""
        HUMAN_ATTACK_LIST = {
            "Punch": {"type": "Physical", "damage": 10},
            "Kick": {"type": "Physical", "damage": 15},
            "Block": {"type": "Physical", "damage": 5},
            "Dodge": {"type": "Physical", "damage": 0},
            "Sweep": {"type": "Physical", "damage": 12},
            "Jab": {"type": "Physical", "damage": 8},
            "Uppercut": {"type": "Physical", "damage": 20},
            "Haymaker": {"type": "Physical", "damage": 25},
            "Elbow Strike": {"type": "Physical", "damage": 15},
            "Headbutt": {"type": "Physical", "damage": 18},
        }

        MONSTER_ATTACK_LIST = {
            "Bite": {"type": "Physical", "damage": 20},
            "Claw": {"type": "Physical", "damage": 15},
            "Tail Whip": {"type": "Physical", "damage": 10},
            "Roar": {"type": "Physical", "damage": 0},
            "Pounce": {"type": "Physical", "damage": 25},
            "Charge": {"type": "Physical", "damage": 20},
            "Slam": {"type": "Physical", "damage": 30},
            "Poison Spit": {"type": "Magical", "damage": 15},
            "Acid Spray": {"type": "Magical", "damage": 20},
            "Fire Breath": {"type": "Magical", "damage": 25},
        }

        GOD_ATTACK_LIST = {
            "Divine Strike": {"type": "Magical", "damage": 30},
            "Holy Smite": {"type": "Magical", "damage": 25},
            "Celestial Blast": {"type": "Magical", "damage": 35},
            "Divine Shield": {"type": "Magical", "damage": 0},
            "Divine Healing": {"type": "Magical", "damage": -20},
            "Divine Summoning": {"type": "Magical", "damage": 20},
            "Divine Retribution": {"type": "Magical", "damage": 40},
            "Divine Judgement": {"type": "Magical", "damage": 50},
            "Divine Intervention": {"type": "Magical", "damage": 0},
            "Divine Wrath": {"type": "Magical", "damage": 60},
        }

        YODIE_GANG_ATTACK_LIST = {
            "Yodie Blast": {"type": "Magical", "damage": 25},
            "Yodie Strike": {"type": "Magical", "damage": 20},
            "Yodie Flail": {"type": "Magical", "damage": 15},
            "Yodie Swing": {"type": "Magical", "damage": 30},
            "Yodie Rush": {"type": "Magical", "damage": 25},
            "Yodie Shout": {"type": "Magical", "damage": 10},
            "Yodie Scream": {"type": "Magical", "damage": 15},
            "Yodie Smack": {"type": "Magical", "damage": 20},
        }
        if type == "Human":
            attack = random.choice(HUMAN_ATTACK_LIST)
        elif type == "God":
            attack = random.choice(GOD_ATTACK_LIST)
        elif type == "Monster":
            attack = random.choice(MONSTER_ATTACK_LIST)
        elif type == "Yodie Gang":
            attack = random.choice(YODIE_GANG_ATTACK_LIST)
            

        # "Oh no, the enemy hath practiced the sacred art of sparring and maketh double damage."
        # damage = damage * 2
        # "Oh no, the enemy hath drunken a kong strong and maketh triple damage."
        # damage = damage * 3
        attack_probability = random.randint(1, 100)
        if attack_probability <= 20:
            print(f"The enemy attacks you with {attack}and deals {damage} points of damage.")
        elif attack_probability <= 5:
            print(f"Oh no, The enemy is listening to some banger tunes and attacks you with double ({damage * 2}) points of damage.")

    def fight_loop(self, enemy_name):
        '''
        The proprieatary fighting loop of the game (no copying pls) which is used to fight enemies and makes the shots about what happens next
        '''
        if self.instant_win == True:
            print("Thou hast leveled up!")
            # sound
            # self.level_up()
            self.instant_win = False
            background_theme("./SoundEngine5000/theme_song.wav")
            return
        while self.player_health > 0 or self.enemy_health > 0:
            # Display the current health of the player and the enemy
            
            if enemy_name == "Valma the Soulbroken":
                # background_theme("./SoundEngine5000/valma_theme.wav")
                pass
            # Display the fight menu and get the user's selection
            user_selection = self.fight_menu()
            if user_selection == "attack":
                self.attack()
            elif user_selection == "run":
                self.run()
            elif user_selection == "defend":
                self.defend(self.damage)
            elif user_selection == "heal":
                self.heal()

            # Check if the enemy has been defeated
            if self.enemy_health <= 0 and self.enemy_name != "Valma the Soulbroken":
                print("\nThou hast defeated the enemy!")
                print("\nThou hast leveled up!")
                print(f"Player health: {self.player_health}")
                player.gold += self.enemy_gold
                print(random.choice(narr.COIN_COLLECT_LIST) + f" You have gained {self.enemy_gold} gold.")
                # sound_engine("level_up")
                player.level += 1
                break
            elif self.enemy_health <= 0 and self.enemy_name == "Valma the Soulbroken":
                print("\nThou hast defeated Valma the soulbroken!")
                print(f"\nPlayer health: {self.player_health}")
                player.gold += 99998888
                print(random.choice(narr.COIN_COLLECT_LIST) + f"\n\nYou have gained infinite gold.")
                break

            # Enemy attacks the player
            self.enemy_attack(self.enemy_damage)

            # Check if the player has been a "has been"
            if self.player_health <= 0: death()
        background_theme("./SoundEngine5000/theme_song.wav")

#--------------------------------------------------------------Death and Endings-----------------------------------------------------------------------#




def death():
    print("YOU DIED")
    # if player does something stupid and dies play ending 1
    # if player dies fighting valma the Soulbroken play ending 2
    # if player dies in a normal fight play ending 3
    print(game_over)
    animate_text(credits_text, "slow")
    # Prints the ending and stats of the player and their achievements.
    print(f"Your level was {player.level}")
    print(f"You had {player.gold} gold")
    print(f"You killed player.kills enemies")
    print("Thanks for playing!")
    print("\nPress any key to continue")
    
    wait_for_keypress()
    time.sleep(0.3)
    print("Quick ad break, please wait...")
    screen_engine()
    return

def ending1():
    print(narr.COWARD_END)
    screen_engine()

def ending2():
    print(narr.TRUE_END_DEATH)
    screen_engine()

def ending3():
    print(narr.NORMAL_DEATH)
    screen_engine()
    
#-------------------------------------------------------------------------Game Functions----------------------------------------------------------------#

def game_loop():
    '''
    The main game loop of the game which is used to run the main mechanics of the game
    '''
    
    while True:
        story()
        # if story_progress == len(possible_routes) - 3: # -3 because the we dont want to give the player less than 3 routes
        if story_progress == 3:
            # Boss fight
            route = route = narr.PLACE_NAMES["End game boss"]["ROUTE"]
            if len(route) == 1:
                animate_text(route, "fast")
                input("\nPress enter to continue")
                clear_screen()
            else:
                for text in range(len(route) -1):
                    animate_text(route[text], "fast")
                input("\nPress enter to continue")
        # start the fight loop
        FightLoopTM(narr.PLACE_NAMES["End game boss"]["ENEMY"])
        # Prints the win text after the fight loop
        if len(route) != 1:
            print(route[-1] + "\n")
            clear_screen()
            print(narr.TRUE_END_WIN)
            credits()
            break
    intro_splash_only()


saveFileNumberTracker = 0 #for all the lazy mfs
def save_game():
    """
    Save the game to the savegame.dat file
    """
    global saveFileNumberTracker
    save_game = input("Would you like to save your game? (Y/n): ")
    
    if save_game.lower() == "y" or save_game == "":
        savefile_name = input("What is the name of the save file? (default: savegame {+ number})")
        saveFileNumberTracker += 1
        if savefile_name == "":
            savefile_name = (f"savegame.dat")
    
        user_data = [player, story_progress, tutorial_done, used_routes, SETTINGS]
        
        with open(savefile_name, 'wb') as file:
            pickle.dump(user_data, file)

    if save_game.lower() == "n":
        return
    else:
        print("Not a valid route")

def load_game():
    """
    Load the game from the savegame.dat file or a file specified by the user
    """
    
    global player
    global story_progress
    global tutorial_done
    global SETTINGS
    savefile_name = input("What is the name of the save file? (default: savegame)")
    if savefile_name == "":
        savefile_name = (f"savegame.dat")
    try:
        testInfile = open(savefile_name, 'rb')
        testInfile.close()
        doesSaveExist = True
    except FileNotFoundError:
        print("That save file does not exist")
        choice = input("Would you like to try again? (Y/n): ")
        if choice.lower() == "n":
            doesSaveExist = False
        else:
            load_game()

    if doesSaveExist == True:
        with open(savefile_name, 'rb') as file:
            user_data = pickle.load(file)

        player = user_data[0] # Not implemented yet
        story_progress = user_data[1] # Not implemented yet
        tutorial_done = user_data[2] # Not implemented yet
        SETTINGS = user_data[3] # Not implemented yet
    elif doesSaveExist == False:
        intro_menu()

def story():
    """All the story of the game and the narration of the game, as well as when to play each story part. Also initiates the fight loop and the chest loop with the right enemies and items."""
    global level
    global story_progress
    global used_routes
    possible_routes = narr.ROUTE
    
    menu()

    if story_progress == 0:
        clear_screen()
        animate_text(narr.INTRO_TXT[0], "fast")
        input("\nPress enter to continue")
        clear_screen()
        # randomize number between 0 and lenght of path
        place = random.choice(list(narr.PLACE_NAMES.keys()))
        route = narr.PLACE_NAMES[place]["ROUTE"]
        while place == 'Shop':
            place = random.choice(list(narr.PLACE_NAMES.keys()))
            route = narr.PLACE_NAMES[place]["ROUTE"]
        used_routes.append(place)
        # print the text of the path
        print(place + ":")
        if len(route) == 1:
            animate_text(route, "fast")
            input("\nPress enter to continue")
            clear_screen()
        else:
            for text in range(len(route) -1):
                animate_text(route[text], "fast")
                input("\nPress enter to continue")
        # start the fight loop
        FightLoopTM(narr.PLACE_NAMES[place]["ENEMY"])
        # Prints the win text after the fight loop
        if len(route) != 1:
            print(route[-1] + "\n")
            input("\nPress enter to continue")
            clear_screen()
        # add 1 to the story progress
        story_progress += 1
        
        
    if story_progress != 0:
        def get_random_places(used_routes):
            places = list(narr.PLACE_NAMES.keys())
            place1, place2, place3 = None, None, None
            while place1 == place2 or place1 == place3 or place2 == place3 or (place1 in used_routes) or (place2 in used_routes) or (place3 in used_routes):
                place1 = random.choice(places)
                place2 = random.choice(places)
                place3 = random.choice(places)
            return place1, place2, place3

        place1, place2, place3 = get_random_places(used_routes)

        choice = None
        while choice == None:
            choice = DefaultActionMenu.action_menu(place1, place2, place3)
            if choice == None:
                print("Please choose a valid route")
        route = narr.PLACE_NAMES[choice]["ROUTE"]
        random_trap_chest = random.choice(["trap", "chest", "nothing"])
        if random_trap_chest == "trap":
            trap()
        elif random_trap_chest == "chest":
            chest()

        used_routes.append(choice)
        
        if len(route) == 1:
            animate_text(route, "fast")
            input("\nPress enter to continue")
            clear_screen()
        else:
            for text in range(len(route) -1):
                animate_text(route[text], "fast")
                input("\nPress enter to continue")
        
        if route == narr.ROUTE17:
            player.inventory.pickup_item(Item_Creator_3000_V2.create_item_DIY(None, "Rare"))
        elif route == narr.ROUTE6:
            player.inventory.pickup_item(Item_Creator_3000_V2.create_item_DIY("Used Rollin pin", "Legendary"))
        elif route == narr.ROUTE9:
            player.inventory.pickup_item(Item_Creator_3000_V2.create_item_DIY("Bag of cocaine", "Mythic"))
        elif route == narr.ROUTE8:
            player.inventory.pickup_item(Item_Creator_3000_V2.create_item_DIY(None, "Poop"))
        elif route == narr.ROUTE7:
            item_shop(player)
        else:
            FightLoopTM(narr.PLACE_NAMES[choice]["ENEMY"])
        
        if len(route) != 1:
            print(route[-1] + "\n")
            input("\nPress enter to continue")
            clear_screen()
        story_progress += 1
    """       
     """


    level += 1
    return level
"""Speed trap that damages the player if they are too slow"""
def trap():
    """A trap that damages the player"""
    if player.speed >= 10:
        player.hp -= range(1, 5)
        print("You managed to avoid the trap")
        input("\nPress enter to continue")

    if player.speed <= 5:
        player.hp -= range(1, 10)
        print("You got caught in the trap")
        input("\nPress enter to continue")
        
    elif player.speed < 10:
        player.hp -= range(1, 10)
        print("You got caught in the trap")
        input("\nPress enter to continue")

def chest():
    chest = ChestSys()
    chest.chest_generate()
    chest.print_chest()

def credits():
    """Play the credits of the game"""
    animate_text(credits_text, "fast")
    input("\nPress enter to return to the main menu")
    return

#-------------------------------------------------------------------------Main-------------------------------------------------------------------------#

pygame.init()
dev = input("Do you want to skip setup and go directly to story? (y/N): ")
if dev.lower() == "y":
    dev = True
else:
    dev = False
if dev == True:
    player = ch.Player(100, 100, "Bon", "Beast", 10)
    game_loop()
else:
    intro()
    game_loop()
