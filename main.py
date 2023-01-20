import sys
import time
import random
import subprocess as sp
import os
from platform import system
import pkg_resources
from itertools import chain
import narration as narr
# from AI import *

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
    '''
    Waits for a keypress on the keyboard
    '''
    if system() == "Windows":
        getkey()
    else:
        getkey_linux()

def intro():
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
    background_theme("./SoundEngine5000/Theme_Song.wav")
    time.sleep(1)

    wait_for_keypress()
    
    intro_menu()

def intro_splash_only():
    clear_screen()
    wait_for_keypress()
    intro_menu()

#----------------------------------------------------------------------Player, Enemy and Objects----------------------------------------------------------#
valma = ch.Enemy("Waldy", 200, 1000, "God")
simon = ch.Enemy("Simpa", 50, 100, "Human")
goblin = ch.Enemy("Lwittle Gwoblin", 50, 100, "Monster")
bilo = ch.Enemy("Bilo, the Town Rapist", 100, 50, "Human")
qlex = ch.Enemy("Steroid Beast", 25, 400, "Monster")
pangloss = ch.Enemy("Pangloss", 200, 50, "Human")
bandits = ch.Enemy("Bandits", 100, 100, "Human")
neo = ch.Enemy("Neo Järnmalm", 200, 200, "Human")
fulcrum = ch.Enemy("Fulcrum", 250, 100, "Yodie Gang")
bill = ch.Enemy("Retired Orthodox Rabbi Bill Clinton", 300, 40, "Human")
antivirgin = ch.Enemy("The Anti-Virgin", 100, 150, "Human")
homeless = ch.Enemy("Hobo", 120, 120, "Human")
guard = ch.Enemy("Guards", 150, 120, "Human")
rapgod = ch.Enemy("The Rap God", 90, 120, "Human")
ladythatstolemylypsyl = ch.Enemy("Strange Lady", 90, 90, "Human")
skeletons = ch.Enemy("Skeletons", 180, 120, "Monster")
ghosts = ch.Enemy("Ghosts", 50, 150, "Monster")
witch = ch.Enemy("Witch", 150, 150, "Monster")
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
    def action_menu(self, action_1, action_2, action_3):
        """
        This is the default player_action menu that is used in the game.
        It is used in the main game loop and in the menu system.
        """
        while True:
            # Prompt the player to attack or defend
            # print(ui_actionmenu)
            GOTO_MENU = "4"
            
            print (f"Action Menu: \n 1. {action_1} \n 2. {action_2} \n 3. {action_3} \n 4. Go to menu") # For testing purposes
            selection = int(input("Your command -->"))

            # Handle the player's player_action
            try:
                if selection == "1":
                    print(f"Going to {action_1} selected")
                    return action_1
                if selection == "2":
                    print(f"{action_2} selected")
                    return action_2
                if selection == "3":
                    print(f"{action_3} selected")
                    return action_3
                elif selection == GOTO_MENU:
                    print("Going to menu")
                    return 4

            except(IndexError,ValueError):
                print("Invalid player_action. Please try again.")
                return "error"

            except:
                print("Unknown error hath occured")
                return "error"


    def fight_menu(self):
        """
        The menu of the choices of the player's attacks.
        """
        # action_menu = ui_actionmenu
        # action_1 = "Attack"
        # action_2 = "Defend"
        # action_3 = "Heal"
        clear_screen()
        # print(ui_actionmenu)
        print("Action Menu: \n 1. Attack \n 2. Defend \n 3. Heal") # For testing purposes
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
                # print(f"{<}")
                user_choice = input("Please type b to go back (or y?)--> ")
                if user_choice.lower() == "b":
                    PlayerAndNameSelect()
                elif user_choice == "y" or user_choice == "Y":
                    print("Hidden user aquired! (not really) \nYou are the god now.")
                    player_subclass = ch.More_Info_Player()
            else:
                print("Please enter a valid input...")
                time.sleep(1)
                input("Press enter to continue...")
                return
            return player_subclass
        except ValueError:
            print("Please enter a valid number.")
            return

def inv_show():
    """
    Shows the player's inventory
    """
    
    clear_screen()
    #small splash
    print(f"Player Health: {player.hp}")
    print(f"Player Strenght: {player.strength}")
    print(f"Player Armour: {player.armour}")
    print(f"Player Awesome level: {player.level}")

    
    while True:
        inv_expasion = input("------------------------------- \n Do you wish to expand to full overview? (Y/n) \n------------------------------- \n-->")
        if inv_expasion.lower() == "y" or inv_expasion.lower() == "yes" or inv_expasion.lower() == "":
            clear_screen()
            
            print(f"HP: {player.hp} stronks:{player.strength} armor:{player.armour} lvl{player.level}")
            print("---------------------------------------------")
            #expand to full inventory view
            if len(player.inventory.inv) == 0:
                print("Inventory is empty")
                input("Press enter to continue...")
                break
            else:
                print("Inventory: ")
                for item in enumerate(player.inventory.inv):
                    print(f"---------\nItem Name: {item[1]['name']} \nStrenght Bonus: {item[1]['strength_bonus']}\n---------")
                input("Press enter to continue...")
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
    "Arne", "Birger","Bjorn","Bjornulf","Bo", "Frode", "Knud", "Odger", "Trygve", "Troels" #Man
    
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
        print(f"{user_name_input} is a good name, though I think {self.name} is a stronger and a more viking name.")
        time.sleep(1)

        input(f"Confirm {self.name}? yes/absolutly --> ")
        print("Are you sure? You won't be able to change it later (yes/perhaps)")
        input("Confirm --> ")
        print(f"{self.name} accepted")

        time.sleep(1)
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
                time.sleep(1)
                clear_screen()
                load_game()
            elif choice == NEW_GAME:
                PlayerAndNameSelect()
                menu()
                play()
        except ValueError:
            print("Invalid input")
            intro_menu()
        clear_screen()
        animate_text("Loading...", "fast")
    elif menu_choice == OPTIONS:
        animate_text("\nSummoning options menu...\n", "fast")
        options_menu()
    elif menu_choice == TUTORIAL:
        tutorial()
        intro_menu()
    elif menu_choice == CREDITS:
        animate_text("\ninitiating credits sequence\n", "fast")
        credits()
        intro_menu()
    elif menu_choice == EXIT:
        exit()
    else:
        print("Invalid input")
        time.sleep(1)
        intro_menu()

def menu():
    """
    The menu system of the game that is used to navigate, save, and exit the game.
    """
    GOTO_TUTORIAL = "1"
    SAVE_AND_EXIT = "2"
    INVENTORY = "3"
    CONTINUE = "4"
    # name = "Navigation Menu"
    # action_1 = "Tutorial"
    # action_2 = "Save and Exit"
    # action_3 = "Inventory"
    # action_4 = "Continue"
    clear_screen()
    # print(ui_textbox)
    print("Navigation Menu: \n1. Tutorial \n2. Save and Exit \n3. Inventory \n4. Continue") # For testing purposes
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

def tutorial():
    '''
    This is the tutorial to make sure the player knows how to play the game
    '''
    user_input = input("Wouldst thou like to see the tutorial, or art thou bold enough to continue without it? (y/N) --> ")
    try:
        if user_input.lower() == "y":
            animate_text("Loading tutorial...", "fast")
            print("Haha Silly, you thought there was a tutorial, but there is not.")
            time.sleep(1)
        elif user_input.lower() == "n" or user_input.lower() == "":
            animate_text("Continuing without tutorial...", "fast")
        else:
            print("Invalid input")
            tutorial()
        input("Press enter to go back to the main menu...")
    except:
        print("Unknown error hath occured")
        tutorial()

def options_menu():
    '''
    So you can change text speed, mute music, etc
    (not even remotely close to being finished)
    '''
    user_input = input("\nOptions:\n1. Text Speed\n2. Mute Sound\n3. Font Colour\n")
    try:
        if user_input.lower() == "1":
            clear_screen()
            print("\nHow fast do you want the text to move?\n1. Fast\n 2. Medium\n 3. Slow\n")
        elif user_input.lower() == "2":
            clear_screen()
            print("\nAre you absolutely certain?(y/n)\n")
        elif user_input.lower() == "3":
            clear_screen()
            print("\nSelect a colour:\n1. Crimson Red\n2. Goblin Green\n3. Blueballs Blue\n")
        else:
            print("Invalid Input")
        input("Press enter to return to the main menu")
    except:
        print("Unknown error")
        options_menu() 




#-----------------------------------------------------------------------------------Sounds and whatnot------------------------------------------------------------------------#
def background_theme(music):
    if pygame.mixer.get_busy() == False:
        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.fadeout(3)
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()



def sound_engine(sound):
    pygame.mixer.init()
    pygame.mixer.Sound(sound)
    return pygame.mixer.Sound(sound)

chest_sound = sound_engine("./SoundEngine5000/Chest_sound.wav")
item_sound = sound_engine("./SoundEngine5000/Item_Pickup.wav")
enemy_grunt = sound_engine("./SoundEngine5000/Enemy_Grunt.wav")
enemy_grunt2 = sound_engine("./SoundEngine5000/Enemy_Grunt2.wav")

# chest_sound.play()

#-----------------------------------------------------------------------FIGHTING-----------------------------------------------------------------------#
class FightLoopTM(DefaultActionMenu):
    def __init__(self, enemy):
        background_theme("./SoundEngine5000/battle_theme.wav")
        self.player_health = player.health
        self.player_max_health = player.max_health
        self.player_weapon = player.weapon
        self.armour = player.armour
        self.enemy_health = enemy.health
        self.damage = enemy.damage
        self.fight_loop()

    def attack(self):
        self.enemy_health -= self.player_weapon.damage
        print(f"Thou attacketh the foe and dealeth {self.player_weapon.damage} points of damage!")

    def run(self):
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
        if self.armour != None:
            print(f"You defend against the enemy's attack and take {damage * self.armour.defense} points of damage.")
        else:
            # Reduce the damage taken by the player by 50% or maybe probability of taking damage?
            print(f"You defend against the enemy's attack and take {damage * 0.5} points of damage.")

    def heal(self):
        if self.player_health != self.player_max_health:
            print("Thou art not at full health!")
            inv_show()
            
            # Show the player it's inventory and ask them to select an item to use to heal
            # Calculate the amount of health restored by the player and add it to the player's health
            # If the player's health is greater than the player's maximum health, set the player's health to the player's maximum health
        elif self.player_health == self.player_max_health:
            print("Thou art already at full health!")

    
    def enemy_attack(self, damage, type):
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

    def fight_loop(self):
        '''
        The proprieatary fighting loop of the game (no copying pls) which is used to fight enemies and makes the shots about what happens next
        '''
        while self.player_health > 0 or self.enemy_health > 0:
            # Display the current health of the player and the enemy
            print(f"Player health: {self.player_health}")
            print(f"Enemy health: {self.enemy_health}")

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
            if self.enemy_health <= 0:
                print("Thou hast defeated the enemy!")
                break

            # Enemy attacks the player
            self.enemy_attack(self.damage)

            # Check if the player has been a "has been"
            if self.player_health <= 0: death()

#--------------------------------------------------------------Death and Endings-----------------------------------------------------------------------#




def death():
    print("YOU DIED")
    # if player does something stupid and dies play ending 1
    # if player dies fighting Valma the Soulbroken play ending 2
    # if player dies in a normal fight play ending 3
    print(game_over)
    animate_text(credits_text, "fast")
    # Prints the ending and stats of the player and their achievements.
    wait_for_keypress()
    time.sleep(2)
    quit()

def ending1():
    print(narr.COWARD_END)

def ending2():
    print(narr.TRUE_END_DEATH)

def ending3():
    print(narr.NORMAL_DEATH)
    
#-------------------------------------------------------------------------Game Functions----------------------------------------------------------------#

def game_loop():
    '''
    The main game loop of the game which is used to run the main mechanics of the game
    '''
    
    while True:
        story()
    # level_choice() with narration and the story
    # default action menu
    # If not find shop increase chance of finding shop
    # if there is enemy spawn enemy and enter fight loop
    # if there is chest spawn chest and enter chest loop and inventory loop
    # if there is trap spawn trap and enter trap loop
    # Continue story with different parts of the story depending on the level obsticles
    # Go back to top of loop
    # Give player option to go back to menu
    # If player goes back to menu give them option to save and exit or continue

saveFileNumberTracker = 0 #for all the lazy mfs
def save_game():
    """
    Save the game to the savegame.dat file
    """
    save_game = input("Would you like to save your game? (Y/n): ")
    
    if save_game.lower() == "y" or save_game == "":
        savefile_name = input("What is the name of the save file? (default: savegame {+ number})")
        saveFileNumberTracker += 1
        if savefile_name == "":
            savefile_name = f"savegame_save_{saveFileNumberTracker}"
    
        user_data = [player, story_progress, tutorial_done]
        
        with open(savefile_name + ".dat", 'wb') as file:
            pickle.dump(user_data, file)

    if save_game.lower() == "n":
        return
    else:
        print("Not a valid choice")

def load_game():
    """
    Load the game from the savegame.dat file or a file specified by the user
    """
    
    global player
    global story_progress
    global tutorial_done
    savefile_name = input("What is the name of the save file? (default: savegame)")
    if savefile_name == "":
        savefile_name = f"savegame_save_{saveFileNumberTracker}"
    try:
        testInfile = open(savefile_name + ".dat", 'rb')
        testInfile.close()
        doesSaveExist = True
    except FileNotFoundError:
        print("That save file does not exist")
        choice = input("Would you like to try again? (Y/n): ")
        if choice.lower() == "y" and choice == "":
            load_game()
        else:
            doesSaveExist = False

    if doesSaveExist == True:
        with open(savefile_name, 'rb') as file:
            user_data = pickle.load(file)

        player = user_data[0] # Not implemented yet
        story_progress = user_data[1] # Not implemented yet
        tutorial_done = user_data[2] # Not implemented yet
    elif doesSaveExist == False:
        intro_menu()

def story():
    # Intro text for level
    # Choose path and stick with it
    # Enemy encounter, fight, loot, etc., trap encounter, or chest encounter.
    global level
    global story_progress
    global used_routes
    possible_routes = [narr.ROUTE]
    PATH = [narr.PLACE_NAMES]
    
    if story_progress == 0:
        print(narr.INTRO_TXT)
        user_input = input("Press enter to continue")
        clear_screen()
        # randomize number between 0 and lenght of path
        random_path = random.randint(0, len(PATH) - 1)
        # add the random number to the used routes list
        used_routes.append(random_path)
        # print the text of the path
        print(possible_routes[random_path] + "\n")
        user_input = input("Press enter to continue")
        clear_screen()
        # add 1 to the story progress
        story_progress += 1
        
        
    if story_progress != 0:
        random_path1 = random.choice(PATH)
        random_path2 = random.choice(PATH)
        random_path3 = random.choice(PATH)
        choice = DefaultActionMenu.action_menu(random_path1, random_path2, random_path3)
        used_routes.append(choice)
        for text in chain(PATH[story_progress]):
            print(text + "\n")
            user_input = input("Press enter to continue")
            clear_screen()
            story_progress += 1
            
    if story_progress == len(PATH):
        ending = narr.TRUE_END_WIN
        print(ending)
        user_input = input("Press enter to continue")
        clear_screen()
        credits()
        quit()
    
    # Not properly implemented yet
    # if val == ROUTE17:
    #     player.inventory.pickup_item("Placeholder Item", 1)
    # elif val == ROUTE13:
    #     player.inventory.pickup_item("Rollin pin", 1)
    # elif val == ROUTE9:
    #     player.inventory.pickup_item("Bag of cocaine", 1)
    # elif val == ROUTE8:
    #     player.inventory.pickup_item("Fjord", 1, "rare")
    # elif val == ROUTE7:
    #     open_shop()
    # else:
    #   pass


    level += 1
    return level

def credits():
    animate_text(credits_text, "fast")
    user_input = input("Press enter to return to the main menu")
    return

#-------------------------------------------------------------------------Main-------------------------------------------------------------------------#
def play():
    
    '''
    The main function of the game which is used to run the main functions of the game
    '''
    #player.inventory.pickup_item("fjord", 1) # For testing purposes
    game_loop()

pygame.init()
intro()
play()