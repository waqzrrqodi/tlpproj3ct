#för spelaren
class Player( ):
    def __init__(self, chosen_strength, chosen_health, chosen_name, chosen_subclass, chosen_speed):
        #subclass kan antingen vara human eller beast
        self.strength = chosen_strength
        HP  = chosen_health
        self.name = chosen_name
        self.subclass = chosen_subclass
        self.speed = chosen_speed
        self.inventory = Inventory_Sys(5)
        self.gold = 0
        self.armour = None
        self.weapon = None
        self.level = 1
        self.xp = 0
        self.level_max_xp = 100
    
    def attack(self, enemy):
        if self.weapon == None:
            enemy.health -= self.strength
        else:
            enemy.health -= self.strength + self.weapon.damage
    
    def defend(self):
        pass

class Human( ):
    def __init__(self) -> None:
        self.HP = 100
        self.SPEED = 5
        self.STRENGHT = 100
        self.SUBCLASS = "Human"

class Beast( ):
    def __init__(self) -> None:
        self.HP = 200
        self.SPEED = 10
        self.STRENGHT = 50
        self.SUBCLASS = "Beast"

class More_Info_Player( ):
    def __init__(self) -> None:
        self.HP = 999999
        self.SPEED = 999999
        self.STRENGHT = 999999
        self.SUBCLASS = "God"
class Armour( ):
    def __init__(self, armour_name, armour_defence):
        self.name = armour_name
        self.defence = armour_defence

wardrobe = Armour("simpa_wardrobe", 100)
condom = Armour("mega_condom", 70)
steelplate = Armour("Steel Breastplate", 50)

class Weapon( ):
    def __init__(self, weapon_name, weapon_dmg):
        self.name = weapon_name
        self.damage = weapon_dmg
sword = Weapon("Sword", 100)
greatsword = Weapon("Greatsword", 200)
dragonslayer = Weapon("DragonSlayer Greatsword", 250)

class Heals( ):
    def __init__(self, heal_name, health_restored, heal_rarity):
        self.name = heal_name
        self.healstat = health_restored
        self.rarity = heal_rarity
meth = Heals("Crystal Meth", 40, 30)
heroin = Heals("Heroin", 50, 30)
cocaine = Heals("Crack Cocaine", 30, 50)


#för alla fiender
class Enemy():
    def __init__(self, enemy_name, enemy_damage, enemy_health, enemy_type):
        self.name = enemy_name
        self.damage = enemy_damage
        self.health = enemy_health
        self.type = enemy_type

#Lista av alla fiender
valma = Enemy("Waldy", 200, 1000, "God")
simon = Enemy("Simpa", 50, 100, "Human")
goblin = Enemy("Lwittle Gwoblin", 50, 100, "Monster")
bilo = Enemy("Bilo, the Town Rapist", 100, 50, "Human")
qlex = Enemy("Steroid Beast", 25, 400, "Monster")
pangloss = Enemy("Pangloss", 200, 50, "Human")
bandits = Enemy("Bandits", 100, 100, "Human")
neo = Enemy("Neo Järnmalm", 200, 200, "Human")
fulcrum = Enemy("Fulcrum", 250, 100, "Yodie Gang")
bill = Enemy("Retired Orthodox Rabbi Bill Clinton", 300, 40, "Human")

#För alla inventory system inklusive 
MAX_INV_CAP = 5
class Inventory_Sys():
    def __init__(self, inv_max_space, ):
        self.inv = list()
        self.inv_cap = inv_max_space

    def inv_max_space_upgrade(self, upgrade_range):
        if self.inv_cap == MAX_INV_CAP:
            print("Error, already at max capacity")
        else:
            self.inv_cap += upgrade_range

    def drop(self):
        if self.inv == []:
            print("Thou doth not have any items")
        else:
            print("Which item would you like to drop?")
            for a in range(self.inv):
                print(f"Example. {self.inv[a]} is number {a}")

    def pickup_item(self, item):
        if self.inv_cap >= self.inv_cap:
            try:
                the_item_dilemma = str(input("You do not have enough space to pickup an item, would you like to swap and discard? \n Y/n -->"))
            except TypeError:
                print("Please provide a Y/n answer")
            except:
                print("Unknown error has occured")
            if the_item_dilemma.lower == "y" or the_item_dilemma == "yes":
                print("item menu")
                print("Which item would thau most prefferably switch?")

                for item_numbah in range(self.inv):
                    print(f"{item_numbah + 1}, self.inv{item_numbah}")

                the_item_dilemma_final_choice = int(input("Choose numbah----->"))
                self.inv.pop(the_item_dilemma_final_choice-1)
                self.inv.append(item)

            elif the_item_dilemma.lower == "n" or the_item_dilemma == "no":
                print("As thau wish good sir")
            else:
                print("Please provide a Y/n answer")
        else: 
            self.inv.append(item)
            print(f"{item} successfully picked up")

#Chest system
class Chest_sys():
    def __init__(self):
        self.chest = list()
    def chest_add(self, item):
        self.chest.append(item)