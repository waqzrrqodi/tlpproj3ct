import random as rand

# För alla inventory system inklusive
MAX_INV_CAP = 5


class InventorySys():
    """The inventory system"""

    def __init__(self, inv_starter_space):
        self.inv = list()
        self.inv_cap = inv_starter_space

    def inv_max_space_upgrade(self, upgrade_range):
        """Upgrade the inventory max space"""
        if self.inv_cap == MAX_INV_CAP:
            print("Error, already at max capacity")
        else:
            self.inv_cap += upgrade_range
            print(f"Inventory max space upgraded to {self.inv_cap}")

    def pickup_item(self, item):
        """Pickup an item"""
        if len(self.inv) >= self.inv_cap:
            try:
                the_item_dilemma = str(input(
                    "You do not have enough space to pickup an item, would you like to swap and discard? \n Y/n -->"))
            except TypeError:
                print("Please provide a Y/n answer")
            except:
                print("Unknown error has occured")
            if the_item_dilemma.lower == "y" or the_item_dilemma == "yes":
                inv_show()
                print("Which item would thau most prefferably switch?")

                for item_numbah in range(self.inv):
                    print(f"{item_numbah + 1}, self.inv{item_numbah}")

                the_item_dilemma_final_choice = int(
                    input("Choose numbah----->"))
                self.inv.pop(the_item_dilemma_final_choice-1)
                self.inv.append(self.item(item))
                print(f'''
                ----------==================----------
                    You picked up ___{item}!___
                ----------==================----------
                ''')
                # Not working fully yet dingus

            elif the_item_dilemma.lower == "n" or the_item_dilemma == "no":
                print("As thau wish good sir")
            else:
                print("Please provide a Y/n answer")
        else:
            self.inv.append(self.item(item))
            print(f'''
                ----------==================----------
                    You picked up ___{item}!___
                ----------==================----------''')
    

ITEM_LIST = {
    "Weapons": {"Kaspers Roasts", "sword", "NUKE_MUSIC", "aliexpress shipping time", "dabbington", "DragonSlayer Greatsword", "Greatsword", "Big Wheel", "rolling pin"},
    "Armor": {"Cargo Pants", "stripper boots", "eldorados nudlar", "simpa_wardrobe", "mega_condom", "Steel Breastplate", "OsKars Jawline"},
    "Heals": {"Crystal Meth", "Heroin", "Crack Cocaine", "Penjamin", "Ketamine", "LSD", "MDMA", "Rohypnol", "Täby AK steroider", "horse meat"},
}

class Item_Creator_3000_V2():
    def __init__(self):
        self.hp_bonus = None
        self.healing = None
        self.damage = None
        self.armor = None

        self.name = None
        self.type = None
        self.cost = None
        self.worth = None
        self.rarity = None
        self.equipped_check = False

    def create_item_DIY(self, name, rarity, type):
        """When in development you want to create an item on the fly"""
        type = type.lower()
        DIY_item = self.create_item_random()
        DIY_item["Rarity"] = rarity
        if name == None or name == "":
            DIY_item["Name"] = DIY_item["Name"]
        else:
            DIY_item["Name"] = name

        if type == "Weapon":
            DIY_item["Type"] = "Weapon"
            DIY_item["HP_Bonus"] = 0
            DIY_item["Healing Capability"] = 0
        if type == "Armor" or type == "Armour":
            DIY_item["Type"] = "Armor"
            DIY_item["Damage"] = 0
            DIY_item["Healing Capability"] = 0
        if type == "Heals":
            DIY_item["Type"] = "Heals"
            DIY_item["HP_Bonus"] = 0
            DIY_item["Damage"] = 0
        else:
            DIY_item["Type"] = type
        return DIY_item
            
    def create_item_random(self):
        """Function to create a random item"""
        self.__init__()
        WEAPON = 1
        ARMOR = 2
        HEALS = 3
        rand_item_choice = rand.randint(1,3)
        if rand_item_choice == WEAPON:
            item_iteration_weapon_list = list(ITEM_LIST.get("Weapons"))
            self.type = "Weapon"
            self.name = item_iteration_weapon_list[rand.randint(0, len(item_iteration_weapon_list)-1)]
            self.damage = rand.randint(3, 5)
        if rand_item_choice == ARMOR:
            item_iteration_armor_list = list(ITEM_LIST.get("Armor"))
            self.type = "Armor"
            self.name = item_iteration_armor_list[rand.randint(0, len(item_iteration_armor_list)-1)]
            self.armor = rand.randint(60, 90)
        if rand_item_choice == HEALS:
            item_iteration_heals_list = list(ITEM_LIST.get("Heals"))
            self.type = "Heals"
            self.name = item_iteration_heals_list[rand.randint(0, len(item_iteration_heals_list)-1)]
            self.healing = rand.randint(30, 50)
        self.cost = rand.randint(30, 400)
        self.worth = round(self.cost*0.9)
        self.rarity = self.item_rarity(self.cost)
        finished_item = {"Name": self.name, "Type": self.type, "Cost": self.cost, "Worth": self.worth, "Rarity": self.rarity, "HP_Bonus": self.armor, "Healing Capability": self.healing, "Damage": self.damage, "Equip": self.equipped_check}
        return finished_item

    # Item rarity system based on cost
    def item_rarity(self, item):
        """Function to determine the rarity of an item based on cost"""
        if item < 30:
            rarity = "Poop"
        if item >= 30:
            rarity = "Common"
        if item >= 110:
            rarity = "Rare"
        if item >= 190:
            rarity = "Epic"
        if item >= 250:
            rarity = "Legendary"
        if item >= 350:
            rarity = "Mythic"
        return rarity

#Creates an item that is purchasable
def item_shop(player):
    """Function to create a shop where the player can buy and sell items"""
    item_shop_list = []
    for i in range(5):
        item_shop_list.append(Item_Creator_3000_V2.create_item_random())

    print("Would you like to buy or sell an item?")
    buy_sell_item = input("buy/sell/quit--> ").lower()
    
    
    if buy_sell_item == "buy" or buy_sell_item == "b" or buy_sell_item == "":
        print("List of purchasable items:")
        for i in range(len(item_shop_list)):
            print(f"{i+1}. {item_shop_list[i].get('Name')} - {item_shop_list[i].get('Cost')} gold")
    
        print("Which item would you like to buy?")
        item_choice = int(input("--> ")) - 1
        if item_choice <= len(item_shop_list):
            if item_shop_list[item_choice].get("Cost") <= player.gold:
                player.gold = player.gold - item_shop_list[item_choice].get("Cost")
                player.inventory.inv.append(item_shop_list[item_choice])
                print(f"You bought {item_shop_list[item_choice].get('Name')} for {item_shop_list[item_choice].get('Cost')} gold")
            else:
                print("You do not have enough gold")
        else:
            print("Please provide a valid item number")

    elif buy_sell_item == "sell":
        print("Which item would you like to sell?")
        inv_show()
        item_choice = int(input("--> ")) - 1
        if item_choice <= len(player.inventory.inv):
            player.gold = player.gold + player.inventory.inv[item_choice].get("Worth")
            player.inventory.inv.pop(item_choice)
            print(f"You sold an item for {player.inventory.inv[item_choice].get('Worth')} gold")
        else:
            print("Please provide a valid item number")

    elif buy_sell_item == "quit" or buy_sell_item == "q" or buy_sell_item == "exit" or buy_sell_item == "e" or buy_sell_item == "leave":
        print("You quit the shop")
        return
        
    else:
        print("Please provide a valid input")


# Chest system

SCRAP_LIST = ["Rock", "Trash", "Dirty Socks", "Dr Pepper", "Macbook", "Estet Linjen"]

class ChestSys():
    """The chest system"""

    def __init__(self):
        self.chest = []

    #Generates the chest
    def chest_generate(self):
        """Generate a chest"""
        rand_item = Item_Creator_3000_V2()
        rand_item = rand_item.create_item_random()
        self.chest.append(rand_item)

        for i in range(0, 1):
            trash = Item_Creator_3000_V2()
            trash_created = trash.create_item_DIY(rand.choice(SCRAP_LIST), "Poop", "Trash")
            self.chest.append(trash_created)
        return self.chest

    #Request chest content
    def print_chest(self, chest):
        """Show the item in the chest"""
        if (chest[0])["Type"] == "Weapon":
            print(f"""\n You find a chest with a {(chest[0])["Name"]} inside it. \n
            Type: {(chest[0])["Type"]}
            Damage: {(chest[0])["Damage"]}
            Worth: {(chest[0])["Worth"]}
            Rarity: {(chest[0])["Rarity"]}
            """)
        if (chest[0])["Type"] == "Armor":
            print(f""" 
            Name: {(chest[0])["Name"]}
            Type: {(chest[0])["Type"]}
            Max HP Bonus: {(chest[0])["HP_Bonus"]}
            Worth: {(chest[0])["Worth"]}
            Rarity: {(chest[0])["Rarity"]}
            """)
        if (chest[0])["Type"] == "Heals":
            print(f""" 
            Name: {(chest[0])["Name"]}
            Type: {(chest[0])["Type"]}
            Health Restored: {(chest[0])["Healing Capability"]}
            Worth: {(chest[0])["Worth"]}
            Rarity: {(chest[0])["Rarity"]}
            """)
        print(f"And...")
        print(f""" some scrap at the bottom of the chest. \n
        Name: {(chest[1])["Name"]}
        Type: {(chest[1])["Type"]}
        Worth: {(chest[1])["Worth"]}
        Rarity: {(chest[1])["Rarity"]}
        """)
'''
Chest = ChestSys()  # Create chest
chest1 = Chest.chest_generate() # Generate a chest
Chest.print_chest(chest1) # Print the chest
'''