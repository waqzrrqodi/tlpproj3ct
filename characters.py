#för spelaren
from item_management import *
from main import *

class Player( ):
    """The player class"""
    def __init__(self, chosen_strength, chosen_health, chosen_name, chosen_subclass, chosen_speed):
        #subclass kan antingen vara human eller beast
        self.strength = chosen_strength
        HP  = chosen_health
        self.name = chosen_name
        self.subclass = chosen_subclass
        self.speed = chosen_speed
        self.inventory = InventorySys(3)
        self.gold = 0
        self.armour = None
        self.weapon = Item_Creator_3000_V2(0, 0, 0, "Fists", "weapon", 0, 0)
        self.level = 1  
        self.xp = 0
        self.level_max_xp = 100
    
    def attack(self, enemy):
        """Attack an enemy"""
        if self.weapon == None:
            enemy.health -= self.strength
        else:
            enemy.health -= self.strength + self.weapon.damage
    
    def defend(self):
        pass

class Human( ):
    """The human subclass"""
    def __init__(self) -> None:
        self.HP = 100
        self.SPEED = 5
        self.STRENGHT = 100
        self.SUBCLASS = "Human"

class Beast( ):
    """The beast subclass"""
    def __init__(self) -> None:
        self.HP = 200
        self.SPEED = 10
        self.STRENGHT = 50
        self.SUBCLASS = "Beast"
class More_Info_Player( ):
    """The player class with more info aka the god class"""
    def __init__(self) -> None:
        self.HP = 999999
        self.SPEED = 999999
        self.STRENGHT = 999999
        self.SUBCLASS = "God"

#för alla fiender
class Enemy():
    """The enemy class"""
    def __init__(self, enemy_name, enemy_damage, enemy_health, enemy_type):
        self.name = enemy_name
        self.damage = enemy_damage
        self.health = enemy_health
        self.type = enemy_type