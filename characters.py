#för spelaren
from item_management import *
import random
# INTE LAGLIGT ATT IMPORTERA MAIN I EN ANNAN FIL AJABAJA
class Player( ):
    """The player class"""
    def __init__(self, chosen_strength, chosen_health, chosen_name, chosen_subclass, chosen_speed):
        #subclass kan antingen vara human eller beast (eller secret gnoblin som jag precis hittade på)
        self.strength = chosen_strength
        self.hp = chosen_health
        self.name = chosen_name
        self.subclass = chosen_subclass
        self.speed = chosen_speed
        self.inventory = InventorySys(3)
        self.gold = 22
        self.armour = None
        self.weapon = None
        self.level = 1  
        self.xp = 0
        self.level_max_xp = 100
        self.auto_equip()
    
    def auto_equip(self):
        """Auto equip items"""
        item = Item_Creator_3000_V2()
        armour = item.create_item_DIY("Skin", "Poop", "Armor")
        weapon = item.create_item_DIY("Fist", "Poop", "Weapon")
        self.inventory.inv.append(armour)
        self.inventory.inv.append(weapon)
        self.armour = self.inventory.equip_item("Skin")
        self.weapon = self.inventory.equip_item("Fist")

    #equip weapon from inventory
    def player_equip_item(self):
        """Equip an item"""
        clear_screen()
        #print inventory
        inv_show()
        print("What item do you want to equip?")
        item_name = input("-->")
        if item_name in self.inventory.inv:
            if item_name["Type"] == "Armour":
                self.armour = self.inventory.equip_item(item_name)
            if item_name["Type"] == "Weapon":
                self.weapon = self.inventory.equip_item(item_name) 

class Human( ):
    """The human subclass"""
    def __init__(self) -> None:
        self.HP = 100
        self.SPEED = 10
        self.STRENGTH = 10
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
        self.STRENGTH = 15
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
