import random as rand
import main
from main import *
from characters import *



#För alla inventory system inklusive 
MAX_INV_CAP = 5
class InventorySys():
    """The inventory system"""
    def __init__(self, inv_max_space):
        self.inv = list()
        self.inv_cap = inv_max_space

    def inv_max_space_upgrade(self, upgrade_range):
        """Upgrade the inventory max space"""
        if self.inv_cap == MAX_INV_CAP:
            print("Error, already at max capacity")
        else:
            self.inv_cap += upgrade_range

    def item(self, item_name, item_strength_bonus):
        """The item class"""
        self.name = item_name
        self.strength_bonus = item_strength_bonus
        item = {'name': self.name, 'strength_bonus': self.strength_bonus}
        return item

    def drop(self):
        """Drop an item"""
        if self.inv == []:
            print("Thou doth not have any items")
        else:
            print("Which item would you like to drop?")
            for a in range(self.inv):
                print(f"Example. {self.inv[a]} is number {a}")

    def pickup_item(self, item_name, item_strength_bonus):
        """Pickup an item"""
        if len(self.inv) >= self.inv_cap:
            try:
                the_item_dilemma = str(input("You do not have enough space to pickup an item, would you like to swap and discard? \n Y/n -->"))
            except TypeError:
                print("Please provide a Y/n answer")
            except:
                print("Unknown error has occured")
            if the_item_dilemma.lower == "y" or the_item_dilemma == "yes":
                inv_show()
                print("Which item would thau most prefferably switch?")

                for item_numbah in range(self.inv):
                    print(f"{item_numbah + 1}, self.inv{item_numbah}")

                the_item_dilemma_final_choice = int(input("Choose numbah----->"))
                self.inv.pop(the_item_dilemma_final_choice-1)
                self.inv.append(self.item(item_name, item_strength_bonus))
                # Not working fully yet dingus

            elif the_item_dilemma.lower == "n" or the_item_dilemma == "no":
                print("As thau wish good sir")
            else:
                print("Please provide a Y/n answer")
        else: 
            self.inv.append(self.item(item_name, item_strength_bonus))
            print(f"{item_name} successfully picked up")

MAX_HP_BONUS = 0
HP_BONUS = MAX_HP_BONUS
DAMAGE = 0
SPEED_BONUS = 0
NAME = ""
TYPE = ""
COST = 0

ITEM_LIST = {
    "Weapons": {"Kaspers Roasts", "sword", "NUKE_MUSIC", "aliexpress shipping time", "dabbington", "DragonSlayer Greatsword", "Greatsword"},
    "Armor": {"Cargo Pants", "stripper boots", "eldorados nudlar", "simpa_wardrobe", "mega_condom", "Steel Breastplate"},
    }
item_rarity =  [range(0,30), range(30,60), range(60,90), range(90,120), range(120,150)]

class Item_Creator_3000_V2():
    def __init__(self, MAX_HP_BONUS, HP_BONUS, DAMAGE, SPD_BONUS, NAME, TYPE, COST):
        max_hp_bonus = MAX_HP_BONUS
        hp_bonus = HP_BONUS
        spd_bonus = SPD_BONUS

        dmg = DAMAGE
        
        name = NAME
        type = TYPE
        cost = COST

    def starter_weapon():
        #starter weapon
        return Item_Creator_3000_V2(0, 0, 0, 0, "Fists", "weapon", 0)
    def create_item_random(self):
        rand_item_choice = ITEM_LIST.get(rand.choice("Weapons", "Armor"))

        if rand_item_choice == "Weapon":
            item_iteration_weapon_list = list(ITEM_LIST.get("Weapons"))
            item = item_iteration_weapon_list[rand.randint(0, len(item_iteration_weapon_list)-1)]
            item = Item_Creator_3000_V2()
            item.type = "weapon"
            item.name = item_iteration_weapon_list
            item.dmg = rand.randint(3, 5)
            item.spd_bonus = rand.randint(5, 6)
            item.cost = rand.randint(50,66)
            return item
        if rand_item_choice == "Armor":
            item_iteration_armor_list = list(ITEM_LIST.get("Armor"))
            item = item_iteration_armor_list[rand.randint(0, len(item_iteration_armor_list)-1)]
            item = Item_Creator_3000_V2()
            item.type = "armor"
            item.name = item_iteration_armor_list
            item.max_hp_bonus = rand.randint(50,70)
            item.cost = rand.randint(70, 80)
            return item
    def create_purchasable_item(self, choice):
            if choice == item_iteration_weapon:
                item_iteration_weapon = list(ITEM_LIST.get("Weapons"))
                item = item_iteration_weapon[rand.randint(0, len(item_iteration_weapon)-1)]
                item = Item_Creator_3000_V2()
                item.type = "weapon"
                item.name = item_iteration_weapon
                item.dmg = rand.randint(3, 5)
                item.spd_bonus = rand.randint(5, 6)
                item.cost = rand.randint(50,66)
                return item
            if choice == item_iteration_armor:
                item_iteration_armor = Item_Creator_3000_V2()
                item_iteration_armor.type = "armor"
                item_iteration_armor.name = item_iteration_armor
                item_iteration_armor.max_hp_bonus = rand.randint(50,70)
                item_iteration_armor.cost = rand.randint(70, 80)
                return item
    def pull_item_rarity(item, item_rarity):
        # rarity = item_rarity[item_list_weapons.index(item)]
        # if rand.randint(1, rarity) == 1:
        #     return "rare"
        # else:
        #     return "common"

    
    def get_item_name(item):
        return item.name
    def get_item_type(item):
        return item.type
    def get_item_damage(item):
        return item.dmg
    def get_item_spd_bonus(item):
        return item.spd_bonus
    def get_item_max_hp_bonus(item):
        return item.max_hp_bonus
    def get_item_cost(item):
        return item.cost

#Chest system

class ChestSys():
    """The chest system"""
    def __init__(self):
        self.chest = list()
    def chest_generate(self):
        """Generate a chest"""
        chest_item = Item_Creator_3000_V2.create_item_random()
        self.chest.append(chest_item)

chestRicketyBridge = ChestSys()
chest2 = chestRicketyBridge.chest_generate()
print(f"A chest has been generated with {chest2} inside")

# class Armour( ):
#     def __init__(self, armour_name, armour_defence):
#         self.name = armour_name
#         self.defence = armour_defence

# class Weapon( ):
#     """The weapon class"""
#     def __init__(self, weapon_name, weapon_dmg):
#         self.name = weapon_name
#         self.damage = weapon_dmg

class Heals( ):
    """The healing class"""
    def __init__(self, heal_name, health_restored, heal_rarity):
        self.name = heal_name
        self.healstat = health_restored
        self.rarity = heal_rarity
meth = Heals("Crystal Meth", 40, 30)
heroin = Heals("Heroin", 50, 30)
cocaine = Heals("Crack Cocaine", 30, 50)
            