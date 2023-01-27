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
import pickle
from ui_elements import * # production materials
import characters as ch

if system() == "Windows":
    from msvcrt import getch as getkey
else:
    from getch import getch as getkey_linux # For linux systems, getch is not included in the standard library on windows.
SETTING1 = ""
SETTING2 = "on"
SETTING3 = "white"
item_creator = Item_Creator_3000_V2()
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

# Initialize all the enemies and add stats for story progression, level etc.
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
        RUN = "r"
        HEAL = "h"
        INFO = "i"
        player_action = None
        
        while True:
            print(fight_menu_choices)
            selection = input("-->").lower()
            try:
                if selection == ATTACK or selection == "attack" or selection == "1":
                    print(f"Attack Selected")
                    time.sleep(0.5)
                    return "attack"

                elif selection == RUN or selection == "run" or selection == "3":
                    print(f"Run selected")
                    time.sleep(0.5)
                    return "run"
                elif selection == HEAL or selection == "heal" or selection == "4":
                    print(f"Heal selected")
                    time.sleep(0.5)
                    return "heal"

                elif selection == INFO or selection == "info" or selection == "5":
                    """Prints more info about the player's attacks and info about the enemy"""
                    print(f"Info selected")
                    print(f"Enemy info: \n Enemy health: {self.enemy_health} \n Enemy damage: {self.enemy_damage}")
                    print(f"""Player info: \n Player health:{player.hp} \n Player Strength: {player.strength} \n Player weapon damage: {player.weapon["Damage"]} \n Player Armor: {player.armour["HP_Bonus"]}""")
                    
                    print("Would you like to enter inv? (y/n)")
                    selection = input("-->").lower()
                    if selection == "y" or selection == "yes":
                        inv_show()
                    else:
                        pass
                    input("Press enter to continue")
                    continue
                else:
                    print("Invalid input")
                    input("Press enter to continue")
                    continue
            except(IndexError,ValueError):
                print("Invalid input")
                input("Press enter to continue")
                continue
            # except:
            #     print("Unknown error hath occured")
            #     input("Press enter to continue")
            #     continue


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
    EQUIP = 1
    UNEQUIP = 2
    PURCHASE = 3
    """
    Shows the player's inventory, in a small and a full view.
    """
    clear_screen()
    #small splash screen
    print(f"\nYour name: {player.name}")
    print(f"\nPlayer Health: {player.hp}")
    print(f"\nPlayer Strength: {player.strength}")
    print(f"\nPlayer Awesomeness level: {player.level}")
    print(f"\nPlayer shillings: {player.gold}")
    print(f"""\nPlayer Armour: {player.armour["Name"]}""")
    print(f"""\nPlayer Weapon: {player.weapon["Name"]}""")
    
   
    
    while True:
        inv_expasion = input("------------------------------- \n Do you wish to expand to full overview? (Y/n) \n------------------------------- \n-->")
        if inv_expasion.lower() == "y" or inv_expasion.lower() == "yes" or inv_expasion.lower() == "":
            clear_screen()
            
            print(f"Name: {player.name}")
            print(f"""HP: {player.hp}, stronks: {player.strength} lvl: {player.level}""")
            print(f"""
            Armour: {player.armour["Name"]} 
            Armour type: {player.armour["Type"]}
            Armour worth: {player.armour["Worth"]} Shillings
            Armour rarity: {player.armour["Rarity"]}
            """)
            print(f"""
            Weapon: {player.weapon["Name"]}
            Weapon type: {player.weapon["Type"]}
            Weapon worth: {player.weapon["Worth"]} Shillings
            Weapon rarity: {player.weapon["Rarity"]}
            """)
            print("---------------------------------------------")
            #expand to full inventory view
            if len(player.inventory.inv) == 0:
                print("Inventory is empty")
                input("\nPress enter to continue...")
                clear_screen()
            else:
                #prints the inventory
                print("Inventory: ")
                for item in enumerate(player.inventory.inv):
                    print(f""" {item[0] + 1}. {item[1]["Name"]}""")
                input("\nPress enter to continue...")
                clear_screen()
                
            print("Would you like to equip, unequip or purchase an item?")
            equip_choice = int(input("1. Equip \n2. Unequip \n3. Purchase \n--> "))
            if equip_choice == EQUIP:
                clear_screen()
                player.player_equip_item()
                    
            elif equip_choice == UNEQUIP:
                clear_screen()
                player.player_unequip_item()

            elif equip_choice == PURCHASE:
                clear_screen()
                item_shop(player)

            else:
                print("Invalid input")
            continue
                    
        elif inv_expasion.lower() == "n" or inv_expasion.lower() == "no" or inv_expasion.lower() == "q":
            break
        else:
            input("Please provid valid input")
            continue
        
    print("Quick ad break, please wait...")
    screen_engine()
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
        if user_name_input == "Martin" or user_name_input == "Oskis" or user_name_input == "Sebbis" or user_name_input == "Kaspis" or user_name_input == "Booster shillings":
            print("That is an absolutely beautiful name mate.")
            self.name = user_name_input
        else:
            print(f"{user_name_input} is a good name, though I think {self.name} is a stronger and a more viking name.")
            input(f"Confirm {self.name}? yes/absolutly --> ")
            print("Are you sure? You won't be able to change it later (yes/perhaps)")
            input("Confirm --> ")
            print(f"{self.name} accepted")
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
    CREDITS = "3"
    EXIT = "4"
    main_menu = True
    while main_menu:
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
                continue
            clear_screen()
            animate_text("Loading...", "fast")
        elif menu_choice == OPTIONS:
            animate_text("\nSummoning options menu...\n", "fast")
            clear_screen()
            options_menu()
            continue
        elif menu_choice == CREDITS:
            clear_screen()
            animate_text("\ninitiating credits sequence...\n", "fast")
            credits()
            continue
        elif menu_choice == EXIT:
            screen_engine()
            exit()
        else:
            print("Invalid input")
            time.sleep(0.3)
            continue

def menu():
    """
    The menu system of the game that is used to navigate, save, and exit the game.
    """
    SAVE_AND_EXIT = "1"
    INVENTORY = "2"
    OPTIONS = "3"
    CONTINUE = "continue"
    while True:
        clear_screen()
        # print(ui_textbox)
        print("Navigation Menu: \n1. Save and Exit \n2. Inventory or stats \n3. Options \n\nTo continue with story, press [Enter]\n") # For testing purposes
        menu_choice = input("What do thau wish to do? ");
        if menu_choice == SAVE_AND_EXIT:
            print("Save + Exit")
            save_game()
            screen_engine()
            exit()
        if menu_choice == INVENTORY:
            print("inv")
            inv_show()
            continue
        if menu_choice == CONTINUE or menu_choice == "":
            animate_text("Continuing with story...", "fast")
            clear_screen()
            return
        if menu_choice == OPTIONS:
            clear_screen()
            options_menu()

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

def random_fight_sound(list):
    #Randomize item from list
    random_sound = random.choice(list)
    #Play random item from list
    random_sound.play()
    

chest_sound = sound_engine("./SoundEngine5000/Chest_sound.wav")
item_sound = sound_engine("./SoundEngine5000/Item_Pickup.wav")
enemy_grunt = sound_engine("./SoundEngine5000/Enemy_Grunt.wav")
enemy_grunt2 = sound_engine("./SoundEngine5000/Enemy_Grunt2.wav")
level_up = sound_engine("./SoundEngine5000/levelup.wav")
# level_up = sound_engine("./SoundEngine5000/Level_Up.wav")

# chest_sound.play()

#Legalize fighting sounds
Dab_Holics = sound_engine("./SoundEngine5000/Nukes/Dab_Holics.wav")
Legalize = sound_engine("./SoundEngine5000/Nukes/Legalize.wav")
Nuke_Music = sound_engine("./SoundEngine5000/Nukes/Nuke_Music.wav")
War_Crime = sound_engine("./SoundEngine5000/Nukes/War_Crime.wav")
WTF_He = sound_engine("./SoundEngine5000/Nukes/WTF_He.wav")

fighting_sounds = [Dab_Holics, Legalize, Nuke_Music, War_Crime, WTF_He]

#-----------------------------------------------------------------------FIGHTING-----------------------------------------------------------------------#
class FightLoopTM(DefaultActionMenu):
    """
    The actual fight loop with all of the other fighting classes and loops
    """
    def __init__(self, enemy_name):
        background_theme("./SoundEngine5000/battle_theme.wav")
        self.instant_win = False
        if enemy_name == "Goblins":
            self.enemy_health = goblin.health
            self.enemy_damage = goblin.damage
            self.enemy_speed = goblin.speed
            self.enemy_type = goblin.type
            self.enemy_gold = goblin.gold
        elif enemy_name == "Skeletons":
            self.enemy_health = skeletons.health
            self.enemy_damage = skeletons.damage
            self.enemy_speed = skeletons.speed
            self.enemy_type = skeletons.type
            self.enemy_gold = skeletons.gold
        elif enemy_name == "Simpa":
            self.enemy_health = simpa.health
            self.enemy_damage = simpa.damage
            self.enemy_speed = simpa.speed
            self.enemy_type = simpa.type
            self.enemy_gold = simpa.gold
        elif enemy_name == "Pangloss":
            self.enemy_health = pangloss.health
            self.enemy_damage = pangloss.damage
            self.enemy_speed = pangloss.speed
            self.enemy_type = pangloss.type
            self.enemy_gold = pangloss.gold
        elif enemy_name == "Bilo":
            self.enemy_health = bilo.health
            self.enemy_damage = bilo.damage
            self.enemy_speed = bilo.speed
            self.enemy_type = bilo.type
            self.enemy_gold = bilo.gold
        elif enemy_name == "Steroid Beast":
            self.enemy_health = steroid_beast.health
            self.enemy_damage = steroid_beast.damage
            self.enemy_speed = steroid_beast.speed
            self.enemy_type = steroid_beast.type
            self.enemy_gold = steroid_beast.gold
        elif enemy_name == "Homeless man":
            self.enemy_health = homeless_man.health
            self.enemy_damage = homeless_man.damage
            self.enemy_speed = homeless_man.speed
            self.enemy_type = homeless_man.type
            self.enemy_gold = homeless_man.gold
        elif enemy_name == "The Anti-Virgin":
            self.enemy_health = anti_virgin.health
            self.enemy_damage = anti_virgin.damage
            self.enemy_speed = anti_virgin.speed
            self.enemy_type = anti_virgin.type
            self.enemy_gold = anti_virgin.gold
        elif enemy_name == "Guards":
            self.enemy_health = guards.health
            self.enemy_damage = guards.damage
            self.enemy_speed = guards.speed
            self.enemy_type = guards.type
            self.enemy_gold = guards.gold
        elif enemy_name == "Rap God":
            self.enemy_health = rap_god.health
            self.enemy_damage = rap_god.damage
            self.enemy_speed = rap_god.speed
            self.enemy_type = rap_god.type
            self.enemy_gold = rap_god.gold
        elif enemy_name == "Strange Lady":
            self.enemy_health = ladythatstolemylypsyl.health
            self.enemy_damage = ladythatstolemylypsyl.damage
            self.enemy_speed = ladythatstolemylypsyl.speed
            self.enemy_type = ladythatstolemylypsyl.type
            self.enemy_gold = ladythatstolemylypsyl.gold
        elif enemy_name == "Ghosts":
            self.enemy_health = ghosts.health
            self.enemy_damage = ghosts.damage
            self.enemy_speed = ghosts.speed
            self.enemy_type = ghosts.type
            self.enemy_gold = ghosts.gold
        elif enemy_name == "Witch":
            self.enemy_health = witch.health
            self.enemy_damage = witch.damage
            self.enemy_speed = witch.speed
            self.enemy_type = witch.type
            self.enemy_gold = witch.gold
        elif enemy_name == "Russian Muscle Man":
            self.enemy_health = strongman.health
            self.enemy_damage = strongman.damage
            self.enemy_speed = strongman.speed
            self.enemy_type = strongman.type
            self.enemy_gold = strongman.gold
        elif enemy_name == "Valma the Soulbroken":
            self.enemy_health = valma.health
            self.enemy_damage = valma.damage
            self.enemy_speed = valma.speed
            self.enemy_name = valma.name
            self.enemy_type = valma.type
            self.enemy_gold = valma.gold
        elif enemy_name == "Shop":
            self.instant_win = True
        elif enemy_name == "Instant win":
            self.instant_win = True
        else:
            print("Unknown enemy")
            death()
        if self.instant_win == False:
            print(f"\nThou hast encountered {enemy_name}!")
            print(f"The {enemy_name} hath {self.enemy_health} health")
            print(f"\nThou hast {player.hp} health")
            print(f"""Thou hast {player.weapon["Name"]} which deals {player.weapon["Damage"]} damage""")
            print(f"""Thou hast {player.armour["Name"]} which protects with {player.armour["HP_Bonus"] } armor""")
            self.fight_loop(enemy_name)
        else:
            self.fight_loop(enemy_name)

    def attack(self):
        """When the player selects the attack option in a fight"""
        random_fight_sound(fighting_sounds)
        strength_bonus = player.strength * 0.1
        if player.weapon["Name"] == "Empty":
            health_lost = strength_bonus + random.randint(1, 5)
            if random.randint(1, 100) <= 5:
                health_lost *= 2
                print("Critical hit!")
            self.enemy_health -= health_lost
            print(f"""Thou attacketh the foe and dealeth {health_lost} points of damage!""")
            print(f"""The foe hast {self.enemy_health} health left""")
            print("You have {} HP left.".format(player.hp))
        else:
            health_lost = strength_bonus + player.weapon["Damage"] + random.randint(1, 5)
            if random.randint(1, 100) <= int(player.weapon["Damage"]):
                health_lost *= 2
                print("Critical hit!")
            self.enemy_health -= health_lost
            print(f"""Thou attacketh the foe and dealeth {health_lost} points of damage!""")
            print(f"""The foe hast {self.enemy_health} health left""")
            print("You have {} HP left.".format(player.hp))

    def run(self):
        """When the player selects the run option in a fight"""
        global player
        random_fight_sound(fighting_sounds)
        if random.randint(1, 100) >= 50:
            print("You try to run, but the enemy blocks thau escape!")
            background_theme("./SoundEngine5000/battle_theme.wav")
        elif random.randint(1, 100) >= 10:
            print("Thau successfully run away from the fight!")
            if len(player.inventory.inv) > 0:
                print("Though it came with an item loss")
                player.inventory.inv.remove(random.choice(list(player.inventory.inv)))
            else:
                print("Since you had no items, you lost nothing peasants.")
            return True
        elif random.randint(1, 100) >= 1:
            print("You try to run, but thau trips and falls, shattering every bone in your body.")
            death()

    def heal(self):
        """When the player selects the heal option in a fight"""
        random_fight_sound(fighting_sounds)
        if player.inventory.inv == []:
            print("You have no items to heal with!")
        else:
            for item in enumerate(player.inventory.inv):
                print(f"""{item[0] + 1}. {item[1]["Name"]} """)
            print("Which item would you like to use to heal?")
            item_choice = int(input("--> "))
            item_choice -= 1
            if item_choice <= len(player.inventory.inv):
                if player.inventory.inv[item_choice].get("Type") == "Healing":
                    print(f"""You used {player.inventory.inv[item_choice].get("Name")} to heal for {player.inventory.inv[item_choice].get("Healing")} health""")
                    player.hp += player.inventory.inv[item_choice].get("Healing")
                    player.inventory.inv.pop(item_choice)
                    print(f"Your current health is {player.hp}")
                    input("Press enter to continue \n -->")
                    return
                else:
                    print("That item is not a healing item!")
                    self.heal()

            # Show the player it's inventory and ask them to select an item to use to heal
            # Calculate the amount of health restored by the player and add it to the player's health
            # If the player's health is greater than the player's maximum health, set the player's health to the player's maximum health
    
    def enemy_attack(self, enemy_name, type):
        """When the enemy attacks the player in a fight and all the moves the enemy can do"""
        HUMAN_ATTACK_LIST = {
            "Punch": {"name": "Punch","type": "Physical", "damage": 2},
            "Kick": {"name": "Kick","type": "Physical", "damage": 5},
            "Block": {"name": "Block","type": "Physical", "damage": 1},
            "Dodge": {"name": "Dodge","type": "Physical", "damage": 0},
            "Sweep": {"name": "Sweep","type": "Physical", "damage": 6},
            "Jab": {"name": "Jab","type": "Physical", "damage": 7},
            "Uppercut": {"name": "Uppercut","type": "Physical", "damage": 10},
            "Haymaker": {"name": "Haymaker","type": "Physical", "damage": 11},
            "Elbow Strike": {"name": "Elbow Strike","type": "Physical", "damage": 4},
            "Headbutt": {"name": "Headbutt","type": "Physical", "damage": 8},
            "Power Slam": {"name": "Power Slam", "type": "Physical", "damage": 8},
            "Elegant Ejaculation": {"name": "Elegant Ejaculation","type": "Physical", "damage": 7},
        }


        MONSTER_ATTACK_LIST = {
            "Bite": {"name": "Bite","type": "Physical", "damage": 13},
            "Claw": {"name": "Claw","type": "Physical", "damage": 11},
            "Tail Whip": {"name": "Tail Whip","type": "Physical", "damage": 8},
            "Roar": {"name": "Roar","type": "Physical", "damage": 0},
            "Pounce": {"name": "Pounce","type": "Physical", "damage": 7},
            "Charge": {"name": "Charge","type": "Physical", "damage": 10},
            "Slam": {"name": "Slam","type": "Physical", "damage": 9},
            "Poison Spit": {"name": "Poison Spit","type": "Magical", "damage": 11},
            "Acid Spray": {"name": "Acid Spray", "type": "Magical", "damage": 10},
            "Fire Breath": {"name": "Fire Breath","type": "Magical", "damage": 12},
        }

        GOD_ATTACK_LIST = {
            "Divine Strike": {"name": "Divine Strike","type": "Magical", "damage": 13},
            "Holy Smite": {"name": "Holy Smite","type": "Magical", "damage": 13},
            "Celestial Blast": {"name": "Celestial Blast","type": "Magical", "damage": 13},
            "Divine Shield": {"name": "Divine Shield","type": "Magical", "damage": 0},
            "Divine Healing": {"name": "Divine Healing","type": "Magical", "damage": -20},
            "Divine Summoning": {"name": "Divine Summoning","type": "Magical", "damage": 13},
            "Divine Retribution": {"name": "Divine Retribution","type": "Magical", "damage": 14},
            "Divine Judgement": {"name": "Divine Judgement","type": "Magical", "damage": 15},
            "Divine Intervention": {"name": "Divine Intervention","type": "Magical", "damage": 0},
            "Divine Wrath": {"name": "Divine Wrath","type": "Magical", "damage": 16},
        }

        YODIE_GANG_ATTACK_LIST = {
            "Yodie Blast": {"name": "Yodie Blast","type": "Magical", "damage": 8},
            "Yodie Strike": {"name": "Yodie Strike","type": "Magical", "damage": 4},
            "Yodie Flail": {"name": "Yodie Flail","type": "Magical", "damage": 2},
            "Yodie Swing": {"name": "Yodie Swing","type": "Magical", "damage": 6},
            "Yodie Rush": {"name": "Yodie Rush","type": "Magical", "damage": 2},
            "Yodie Shout": {"name": "Yodie Shout","type": "Magical", "damage": 1},
            "Yodie Scream": {"name": "Yodie Scream","type": "Magical", "damage": 1},
            "Yodie Smack": {"name": "Yodie Smack","type": "Magical", "damage": 3},
        }
        if type == "Human":
            attack_name = random.choice(list(HUMAN_ATTACK_LIST.keys()))
            attack = HUMAN_ATTACK_LIST[attack_name]
        if type == "God":
            attack_name = random.choice(list(GOD_ATTACK_LIST.keys()))
            attack = GOD_ATTACK_LIST[attack_name]
        if type == "Monster":
            attack_name = random.choice(list(MONSTER_ATTACK_LIST.keys()))
            attack = MONSTER_ATTACK_LIST[attack_name]
        if type == "Yodie Gang":
            attack_name = random.choice(list(YODIE_GANG_ATTACK_LIST.keys()))
            attack = YODIE_GANG_ATTACK_LIST[attack_name]
            

        """Attack the player"""
        damage_level_reduction = round(int(attack["damage"] + player.level*2))
        attack_probability = random.randint(1, 100)
        if attack_probability >= 60:
            print("The enemy attacks you with {} and misses.".format(attack["name"]))
            print("You have {} HP left.".format(player.hp))
        elif attack_probability <= 20 and attack_probability >= 6:
            player.hp -= damage_level_reduction
            print("The enemy attacks you with {} and deals {} points of damage.".format(attack["name"], damage_level_reduction))
            print("You have {} HP left.".format(player.hp))
        elif attack_probability <= 5:
            health_loss = damage_level_reduction * 2
            player.hp -= health_loss
            print("Oh no, The enemy is listening to some banger tunes and attacks you with {} with double power and deals({}) points of damage.".format(attack["name"], health_loss))
            print("You have {} HP left.".format(player.hp))

    def fight_loop(self, enemy_name):
        '''
        The proprieatary fighting loop of the game (no copying pls) which is used to fight enemies and makes the shots about what happens next
        '''
        global player
        if self.instant_win == True:
            print("Thou hast leveled up!")
            sound_engine("./SoundEngine5000/levelup.wav")
            # self.level_up()
            self.instant_win = False
            background_theme("./SoundEngine5000/theme_song.wav")
            return
        while player.hp > 0 or self.enemy_health > 0:
            # Display the current health of the player and the enemy
            
            if enemy_name == "Valma the Soulbroken":
                # background_theme("./SoundEngine5000/valma_theme.wav")
                pass
            # Display the fight menu and get the user's selection
            user_selection = self.fight_menu()
            if user_selection == "attack":
                self.attack()
            elif user_selection == "run":
                escape_rate = self.run()
                if escape_rate == True:
                    self.instant_win = True
                    break
                else:
                    continue
            elif user_selection == "heal":
                self.heal()
            else:
                return False

            # Check if the enemy has been defeated
        if self.enemy_health <= 0 and enemy_name != "Valma the Soulbroken":
            print("\nThou hast defeated the enemy!")
            print("\nThou hast leveled up!")
            if player.hp < player.MAX_HP:
                player.hp = player.MAX_HP
            else:
                player.hp = player.hp
            print(f"You heal up to default health: {player.hp}")
            player.gold += self.enemy_gold
            print(random.choice(narr.COIN_COLLECT_LIST) + f" You have gained {self.enemy_gold} shillings.")
            sound_engine("./SoundEngine5000/levelup.wav")
            player.level += 1
            return False
        elif self.instant_win == True:
            print("\nThou hast leveled up!")
            if player.hp < player.MAX_HP:
                player.hp = player.MAX_HP
            else:
                player.hp = player.hp
            print(f"You heal up to default health: {player.hp}")
            print(f"Player health: {player.hp}")
            sound_engine("./SoundEngine5000/levelup.wav")
            player.level += 1
            return True
        elif self.enemy_health <= 0 and self.enemy_name == "Valma the Soulbroken":
            print("\nThou hast defeated Valma the soulbroken!")
            print(f"\nPlayer health: {player.hp}")
            player.gold += 99998888
            print(random.choice(narr.COIN_COLLECT_LIST) + f"\n\nYou have gained infinite shillings.")
            return False

        # Enemy attacks the player
        self.enemy_attack(enemy_name, self.enemy_type)

        # Check if the player has been a "has been"
        if player.hp <= 0: death()
        background_theme("./SoundEngine5000/theme_song.wav")

#--------------------------------------------------------------Death and Endings-----------------------------------------------------------------------#

def death():
    print("YOU DIED")
    # if player does something stupid and dies play ending 1
    # if player dies fighting valma the Soulbroken play ending 2
    # if player dies in a normal fight play ending 3
    print(game_over)
    # Prints the ending and stats of the player and their achievements.
    print(f"Your level was {player.level}")
    print(f"You had {player.gold} shillings")
    print(f"You killed player.kills enemies")
    print("Thanks for playing!")
    animate_text(credits_text, "default")
    print("\nPress any key to continue")
    
    wait_for_keypress()
    time.sleep(0.3)
    print("Quick ad break, please wait...")
    screen_engine()
    quit()

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
        possible_routes = narr.ROUTE
        if story_progress == len(possible_routes) - 3: # -3 because the we dont want to give the player less than 3 routes
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
    
        user_data = [player, story_progress, used_routes, SETTINGS]
        
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
        SETTINGS = user_data[2] # Not implemented yet
    elif doesSaveExist == False:
        intro_menu()

def story():
    """All the story of the game and the narration of the game, as well as when to play each story part. 
    Also initiates the fight loop and the chest loop with the right enemies and items."""
    global level
    global story_progress
    global used_routes
    
    menu()

    if story_progress == 0:
        clear_screen()
        animate_text(narr.INTRO_TXT[0], "fast")
        input("\nPress enter to continue")
        clear_screen()
        # randomize number between 0 and lenght of path
        place = random.choice(list(narr.PLACE_NAMES.keys()))
        route = narr.PLACE_NAMES[place]["ROUTE"]
        while place == 'Shop' or place == 'End game boss' or place == 'Landfill' or place == 'Used Condom':
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
        is_coward = FightLoopTM(narr.PLACE_NAMES[place]["ENEMY"])
        # Prints the win text after the fight loop
        if is_coward == False:
            if len(route) != 1:
                print(route[-1] + "\n")
                input("\nPress enter to continue")
                clear_screen()
            # add 1 to the story progress
            story_progress += 1
        elif is_coward == True:
            is_coward = False
        
        
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
        random_trap_chest = random.choice(["chest", "trap", "nothing", "nothing"])
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
            player.inventory.pickup_item(item_creator.create_item_DIY("", "Rare", "Weapon"))
        elif route == narr.ROUTE6:
            player.inventory.pickup_item(item_creator.create_item_DIY("Used Rollin pin", "Legendary", "Weapon"))
        elif route == narr.ROUTE9:
            player.inventory.pickup_item(item_creator.create_item_DIY("Bag of cocaine", "Mythic", "Heals"))
        elif route == narr.ROUTE8:
            player.inventory.pickup_item(item_creator.create_item_DIY("", "Poop", "Armor"))
        elif route == narr.ROUTE7:
            item_shop(player)
        else:
            is_coward = FightLoopTM(narr.PLACE_NAMES[choice]["ENEMY"])
        
        if is_coward == False:
            if len(route) != 1:
                print(route[-1] + "\n")
                input("\nPress enter to continue")
                clear_screen()
            story_progress += 1
        elif is_coward == True:
            is_coward = False


    level += 1
    return level
"""Speed trap that damages the player if they are too slow"""
def trap():
    """A trap that damages the player"""
    if player.speed >= 10:
        player.hp -= 5
        print("\n\nYou managed to avoid the trap but you lost 5 health")
        input("\nPress enter to continue")

    if player.speed <= 5:
        player.hp -= 10
        print("\n\nYou got caught in the trap and lost 10 health")
        input("\nPress enter to continue")
        
    elif player.speed < 10:
        player.hp -= 20
        print("\n\nYou got caught in the trap and lost 20 health")
        input("\nPress enter to continue")
    return

def chest():
    chest = ChestSys()
    chest1 = chest.chest_generate()
    print("On your way to the destination you found a chest which contains:")
    chest.print_chest(chest1)
    print("Do you want to take the item? (Y/n)")
    print("If you don't take the item, it will be destroyed")
    choice = input("--> ")
    if choice.lower() != "n":
        player.inventory.pickup_item(chest1[0])
        print("You took the item")

        print("Would you like to equip the item? (Y/n)")
        choice = input("--> ")
        if choice.lower() != "n":
            player.inventory.equip_item(chest1[0])
            print("You equipped the item")
            inv_show()
        else:
            print("You didn't equip the item")
        
        input("\nPress enter to continue")
        clear_screen()
    else:
        print("You didn't take the item")
        input("\nPress enter to continue")
        clear_screen()

def credits():
    """Play the credits of the game"""
    background_theme("./SoundEngine5000/Weight of the World.wav")
    animate_text(credits_text, "default")
    animate_text(simpa_pic, "fast")
    input("\nPress enter to return to the main menu")
    background_theme("./SoundEngine5000/theme_song.wav")
    return

#-------------------------------------------------------------------------Main-------------------------------------------------------------------------#
pygame.init()
dev = input("Do you want to skip setup and go directly to story? (y/N): ")
if dev.lower() == "y":
    dev = True
else:
    dev = False
if dev == True:
    player = ch.Player(10, 100, "Bing Chillin' ", "Beast", 10)
    game_loop()
else:
    intro()
    game_loop()
