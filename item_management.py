import random as rand
from main import *

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


HP_BONUS = 0
DAMAGE = 0
HEALTH_RESTORED = 0

NAME = ""
TYPE = ""
COST = 0
WORTH = 0
RARITY = ""

ITEM_LIST = {
    "Weapons": {"Kaspers Roasts", "sword", "NUKE_MUSIC", "aliexpress shipping time", "dabbington", "DragonSlayer Greatsword", "Greatsword"},
    "Armor": {"Cargo Pants", "stripper boots", "eldorados nudlar", "simpa_wardrobe", "mega_condom", "Steel Breastplate"},
    "Heals": {"Crystal Meth", "Heroin", "Crack Cocaine", "Penjamin"},
    }

class Item_Creator_3000_V2():
    def __init__(self, HP_BONUS, HEALTH_RESTORED, DAMAGE, NAME, TYPE, COST, WORTH, RARITY ):
        self.hp_bonus = HP_BONUS
        self.health_restored = HEALTH_RESTORED
        self.damage = DAMAGE

        self.name = NAME
        self.item_type = TYPE
        self.cost = COST
        self.worth = WORTH
        self.rarity = RARITY

    def create_item_random(self):
        #rand_item_choice = ITEM_LIST.get(rand.choice("Weapons", "Armor"))
        rand_item_choice = "Weapon"
        if rand_item_choice == "Weapon":
            item_iteration_weapon_list = list(ITEM_LIST.get("Weapons"))
            item = Item_Creator_3000_V2(0, 0, 0, 0, 0, 0, 0, 0)
            item.type = "Weapon"
            item.name = item_iteration_weapon_list[rand.randint(0, len(item_iteration_weapon_list)-1)]
            item.damage = rand.randint(3, 5)
            item.cost = rand.randint(50,66)
            item.worth = item.cost/2
        if rand_item_choice == "Armor":
            item_iteration_armor_list = list(ITEM_LIST.get("Armor"))
            item = Item_Creator_3000_V2(0, 0, 0, 0, 0, 0, 0, 0)
            item.type = "Armor"
            item.name = item_iteration_armor_list[rand.randint(0, len(item_iteration_armor_list)-1)]
            item.max_hp_bonus = rand.randint(50,70)
            item.cost = rand.randint(70, 80)
            item.worth = item.cost/2
        if rand_item_choice == "Heals":
            item_iteration_heals_list = list(ITEM_LIST.get("Heals"))
            item = Item_Creator_3000_V2(0, 0, 0, 0, 0, 0, 0, 0)
            item.type = "Heals"
            item.name = item_iteration_heals_list[rand.randint(0, len(item_iteration_heals_list)-1)]
            item.health_restored = rand.randint(30, 50)
            item.cost = rand.randint(10, 20)
            item.worth = item.cost/2
        return item

    def create_purchasable_item(self, choice):
            if choice in ITEM_LIST.get("Weapons") == True:
                item_iteration_weapon_list = list(ITEM_LIST.get("Weapons"))
                item = Item_Creator_3000_V2(0, 0, 0, 0, 0, 0, 0, 0)
                item.type = "Weapon"
                item.name = item_iteration_weapon_list[rand.randint(0, len(item_iteration_weapon_list)-1)]
                item.damage = rand.randint(3, 5)
                item.cost = rand.randint(50,66)
                item.worth = item.cost/2
                
            if choice in ITEM_LIST.get("Armor") == True:
                item_iteration_armor_list = list(ITEM_LIST.get("Armor"))
                item = Item_Creator_3000_V2(0, 0, 0, 0, 0, 0, 0, 0)
                item.type = "Armor"
                item.name = item_iteration_armor_list[rand.randint(0, len(item_iteration_armor_list)-1)]
                item.max_hp_bonus = rand.randint(50,70)
                item.cost = rand.randint(70, 80)
                item.worth = item.cost/2
            if choice in ITEM_LIST.get("Heals") == True:
                item_iteration_heals_list = list(ITEM_LIST.get("Heals"))
                item = Item_Creator_3000_V2(0, 0, 0, 0, 0, 0, 0, 0)
                item.type = "Geals"
                item.name = item_iteration_heals_list[rand.randint(0, len(item_iteration_heals_list)-1)]
                item.health_restored = rand.randint(30, 50)
                item.cost = rand.randint(70, 80)
                item.worth = item.cost/2
            item.rarity = item_rarity(item)
            return item

    
    def get_item_name(item):
        return item.name
    def get_item_type(item):
        return item.type
    def get_item_damage(item):
        return item.damage
    def get_item_max_hp_bonus(item):
        return item.max_hp_bonus
    def get_item_cost(item):
        return item.cost
    def get_item_health_restored(item):
        return item.health_restored
    
def item_rarity(item):
        if item.cost >= 50 and item.cost <= 66:
            rarity = "Common"
        if item.cost >= 67 and item.cost <= 80:
            rarity = "Rare"
        if item.cost >= 81 and item.cost <= 100:
            rarity = "Epic"
        if item.cost >= 101 and item.cost <= 150:
            rarity = "Legendary"
        if item.cost >= 151 and item.cost <= 200:
            rarity = "Mythic"
        return rarity

#Chest system, verkligen inte klart
class ChestSys():
    """The chest system"""
    def __init__(self):
        self.chest = None
    def chest_generate(self):
        """Generate a chest"""
        rand_item = Item_Creator_3000_V2(0, 0, 0, 0, 0, 0, 0, 0)
        rand_item = rand_item.create_item_random()
        self.chest = (rand_item)
        return self.chest

    def print_chest(self, chest):
        print(f"""
        This is in the chest: 
        {chest.type}:
        {chest.name}
        """ )
