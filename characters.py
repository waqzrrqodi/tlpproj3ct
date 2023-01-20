#för spelaren
from item_management import *
import random as rand
# INTE LAGLIGT ATT IMPORTERA MAIN I EN ANNAN FIL AJABAJA
class Player( ):
    """The player class"""
    def __init__(self, chosen_strength, chosen_health, chosen_name, chosen_subclass, chosen_speed):
        #subclass kan antingen vara human eller beast (eller secret gnoblin som jag precis hittade på)
        self.strength = chosen_strength
        self.hp= chosen_health
        self.name = chosen_name
        self.subclass = chosen_subclass
        self.speed = chosen_speed
        self.inventory = InventorySys(3)
        self.gold = 0
        self.armour = None
        self.weapon = None
        self.level = 1  
        self.xp = 0
        self.level_max_xp = 100

    #equip weapon from inventory
    def player_equip_item(self, item):
        print("What item do you want to equip?")
        item_name = input("-->")
        if item_name["Type"] == "Armour":
            self.armour = self.inventory.equip_item(item_name)
        if item_name["Type"] == "Weapon":
            self.weapon = self.inventory.equip_item(item_name)
    
    def player_attack(self, enemy):
        """Attack an enemy"""
        if self.weapon == None:
            enemy.health -= self.strength
        else:
            enemy.health -= self.strength + self.weapon.damage
    
    def enemy_attack(self, enemy):
        """Attack the player"""
        if self.armour == None or self.armour <= 0:
            self.hp -= enemy.damage
        if self.armour != None or self.armour > 0:
            for i in range(enemy.damage-1):
                if self.armour <= 0:
                    self.hp -= 1
                else:
                    self.armour -= 1
    
    def defend(self, enemy):
        """Defend"""
        damage_decrease = rand.randint(0, 10)
        if self.armour == None or self.armour <= 0:
            self.hp -= (enemy.damage-damage_decrease)
        if self.armour != None or self.armour > 0:
            for i in range(enemy.damage-damage_decrease-1):
                if self.armour <= 0:
                    self.hp -= 1
                else:
                    self.armour -= 1
        

class Human( ):
    """The human subclass"""
    def __init__(self) -> None:
        self.HP = 100
        self.SPEED = 5
        self.STRENGTH = 100
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
        self.SPEED = 10
        self.STRENGTH = 50
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
        self.name = enemy_name
        self.damage = enemy_damage
        self.health = enemy_health
        self.type = enemy_type
        self.speed = enemy_speed
    def enemy_stats(self):
        """Print the enemy stats"""
        print("Name: " + self.name)
        print("Damage: " + str(self.damage))
        print("Health: " + str(self.health))
        print("Type: " + self.type)
