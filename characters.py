#för spelaren
class Main_Char( ):
    def __init__(self, chosen_subclass, chosen_name, chosen_strength, chosen_health):
        self.subclass = chosen_subclass
        #subclass kan antingen vara human eller beast
        self.name = chosen_name
        self.strength = chosen_strength
        HP  = chosen_health


#för alla fiender
class enemy():
    def __init__(self, enemy_name, enemy_damage, enemy_health):
        self.name = enemy_name
        self.damage = enemy_damage
        self.health = enemy_health

#Lista av alla fiender
valma = enemy("Waldy", 100, 100)
simon = enemy("Simpa", 50, 200)
goblin = enemy("Lwittle Gwoblin", 50, 50)
bilo = enemy("Bilo, the Town Rapist", 100, 50)
qlex = enemy("Qlex", 25, 400)
candide = enemy("Candide", 200, 50)


#För alla inventory system inklusive 
class Inventory_Sys():
    def __init__(self, inv_max_space, ):
        self.inv = list()
        self.inv_cap = inv_max_space
    def drop(self):
        if self.inv == []:
            print("Thou doth not have any items")
        else:
            print("Which item would you like to drop?")
            for a in range(self.inv):
                print(f"Example. {self.inv[a]} is number {a}")
    def pickup_item(self, item):
        if self.inv_cap >= 3:
            input("You do not have enough space to pickup an item, would you like to swap or discard? \n -->")
        else: 
            self.inv.append(item)
            print(f"{item} successfully picked up")



#Chest system
class chest_sys():
    def __init__(self):
        self.chest = list()
    def chest_add(self, item):
        self.chest.append(item)
    def chest_item_swap() -> None:
        pass