#för spelaren
from item_management import *
import random
class Player( ):
    """The player class"""
    def __init__(self, chosen_strength, chosen_health, chosen_name, chosen_subclass, chosen_speed):
        #subclass kan antingen vara human eller beast (eller secret gnoblin som jag precis hittade på)
        self.strength = chosen_strength
        self.MAX_HP = chosen_health
        self.hp = self.MAX_HP
        self.name = chosen_name
        self.subclass = chosen_subclass
        self.speed = chosen_speed
        self.inventory = InventorySys(3)
        self.gold = 122
        self.level = 1
        self.xp = 0

        item = Item_Creator_3000_V2()
        armour = item.create_item_DIY("Skin", "Poop", "Armor")
        weapon = item.create_item_DIY("Fist", "Poop", "Weapon")
        self.armour = armour
        self.weapon = weapon

    #equip the item from inventory
    def player_equip_item(self):
            """Equip an item"""
            #print inventory
            print("What item do you want to equip?")
            print("Inventory: ")
            if self.inventory.inv == []:
                print("Inventory is empty")
                input ("Press enter to continue")
                return
            else:
                for item in enumerate(self.inventory.inv):
                    print(f"""{item[0] + 1}. {item[1]["Name"]} """)

            try:
                item_choice = int(input("Item number: \n --> "))
            except ValueError:
                print("Input must be a number")
                input ("Press enter to continue")
                return
            item_choice -= 1

            if item_choice <= len(self.inventory.inv):
                item = self.inventory.inv[item_choice]
                if item.get("Type") == "Armor":
                    self.armour = self.inventory.equip_item(item, self.armour)
                    print(f"""Armor: {self.armour["Name"]} equipped""")
                    input("Press enter to continue")
                    return
                elif item.get("Type") == "Weapon":
                    self.weapon = self.inventory.equip_item(item, self.weapon)
                    print(f"""Weapon: {self.weapon["Name"]} equipped""")
                    input("Press enter to continue")
                    return
            else:
                print("Item not found")
                input ("Press enter to continue")

    #unequip the item
    def player_unequip_item(self):
        """Unequip an item"""
        print ("What item do you want to unequip?")
        print ("equipped items: ")
        print (f"""Armour: {self.armour["Name"]}""")
        print (f"""Weapon: {self.weapon["Name"]}""")
        item_name = input("Item name: \n --> ")
        if item_name == self.armour["Name"]:
            #replace armer item with an empty one
            self.armour = self.inventory.unequip_item(self.armour)
            print("Armour unequipped")
            input ("Press enter to continue")
            return
        elif item_name == self.weapon["Name"]:
            self.weapon = self.inventory.unequip_item(self.weapon)
            print("Weapon unequipped")
            input ("Press enter to continue")
            return
        else:
            print("Item not found")
            input ("Press enter to continue")
            return
        
class Human( ):
    """The human subclass"""
    def __init__(self) -> None:
        self.HP = 100
        self.SPEED = 10
        self.STRENGTH = 5
        self.SUBCLASS = "Human"

class Gnoblin( ):
    """The secret gnoblin subclass, AKA ultra nightmare mode"""
    def __init__(self) -> None:
        self.HP = 1
        self.SPEED = 1
        self.STRENGTH = 1
        self.SUBCLASS = "Gnoblin"

class Beast( ):
    """The beast subclass"""
    def __init__(self) -> None:
        self.HP = 200
        self.SPEED = 2
        self.STRENGTH = 10
        self.SUBCLASS = "Beast"
class More_Info_Player( ):
    """The player class with more info aka the god class"""
    def __init__(self) -> None:
        self.HP = 999999
        self.SPEED = 999999
        self.STRENGTH = 999999
        self.SUBCLASS = "God"

#för alla fiender
class Enemy():
    """The enemy class"""
    def __init__(self, enemy_name, enemy_damage, enemy_health, enemy_type, enemy_speed):
        self.alive = True
        self.name = enemy_name
        self.damage = enemy_damage
        self.health = enemy_health
        self.type = enemy_type
        self.speed = enemy_speed
        self.gold = random.randint(1, 3) * self.health * 0.1
    def enemy_stats(self):
        """Print the enemy stats"""
        print("Name: " + self.name)
        print("Damage: " + str(self.damage))
        print("Health: " + str(self.health))
        print("Type: " + self.type)
