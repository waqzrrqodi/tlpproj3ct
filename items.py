import random as rand
import main
from main import *

MAX_HP_BONUS = 0
HP_BONUS = MAX_HP_BONUS
STR_BONUS = 0
SPD_BONUS = 0
NAME = ""
TYPE = ""
COST = 0

item_list_weapons=["Kaspers Roasts", "sword", "NUKE_MUSIC", "aliexpress shipping time", "dabbington"]
item_list_armor=["Cargo Pants", "stripper boots", "eldorados nudlar"]
item_rarity =  [range(0,30), range(30,60), range(60,90), range(90,120), range(120,150)]

class Item_Creator_3000_V2():
    def __init__(self, MAX_HP_BONUS, HP_BONUS, STR_BONUS, SPD_BONUS, NAME, TYPE, COST):
        max_hp_bonus = MAX_HP_BONUS
        hp_bonus = HP_BONUS
        str_bonus = STR_BONUS
        spd_bonus = SPD_BONUS
        name = NAME
        type = TYPE
        cost = COST
        starter_weapon=Item_Creator_3000_V2(0, 0, 0, 0, "Fists", "weapon", 0)
    def create_item(choice):
        for item_iteration_weapon in item_list_weapons:
            if choice == item_iteration_weapon:
                item_iteration_weapon = Item_Creator_3000_V2()
                item_iteration_weapon.type = "weapon"
                item_iteration_weapon.name = item_iteration_weapon
                item_iteration_weapon.str_bonus = rand.randint(3, 5)
                item_iteration_weapon.spd_bonus = rand.randint(5, 6)
                item_iteration_weapon.cost = rand.randint(50,66)
                rarity = item_rarity[item_list_weapons.index(choice)]
                if rand.randint(1, rarity) == 1:
                    return "rare", item_iteration_weapon
                else:
                    return "common", item_iteration_weapon
        for item_iteration_armor in item_list_armor:
            if choice == item_iteration_armor:
                item_iteration_armor = Item_Creator_3000_V2()
                item_iteration_armor.type = "armor"
                item_iteration_armor.name = "Small dagger"
                item_iteration_armor.max_hp_bonus = rand.randint(50,70)
                item_iteration_armor.cost = rand.randint(70, 80)
                rarity = item_rarity[item_list_armor.index(choice)]
                if rand.randint(1, rarity) == 1:
                    return "rare", item_iteration_armor
                else:
                    return "common", item_iteration_armor
    def get_item_name(item):
        return item.name
    def get_item_type(item):
        return item.type
    def get_item_str_bonus(item):
        return item.str_bonus
    def get_item_spd_bonus(item):
        return item.spd_bonus
    def get_item_max_hp_bonus(item):
        return item.max_hp_bonus
    def get_item_cost(item):
        return item.cost


            