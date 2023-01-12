import random as rand
class Item:
    max_hp_bonus = 0
    hp_bonus = max_hp_bonus #KAN ÄNDRAS INDIVIDUELLT, DEFAULT ÄR ATT DE ÄR SAMMA
    str_bonus = 0
    spd_bonus = 0
    name = ""
    type = ""
    cost = 0
fists = Item()
fists.type = "weapon"
fists.name = "Fists"
empty_armor = Item()
empty_armor.type = "armor"
empty_armor.name = "None"
empty_accessory = Item()
empty_accessory.type = "accessory"
empty_accessory.name = "None"
item_list=          ["dagger", "sword", "explosive", "ultra_greatsword", "springfield rifle", "rocket launcher", "crusader helm", "leather boots", "philosophy book", "voltaire's pencil"]
item_rarity_list =  [100,       100,     60,          20,                 60,                  1099999999,       100,             100,             100,               100]
def create_item(choice):
    if choice == "dagger":
        dagger = Item()
        dagger.type = "weapon"
        dagger.name = "Small dagger"
        dagger.str_bonus = rand.randint(3, 5)
        dagger.spd_bonus = rand.randint(5, 6)
        dagger.cost = rand.randint(50,66)
        return dagger
    elif choice == "crusader helm":
        crusader_helm = Item()
        crusader_helm.type = "armor"
        crusader_helm.name = "Crusader helm"
        crusader_helm.max_hp_bonus = rand.randint(50,70)
        crusader_helm.cost = rand.randint(70, 80)
        return crusader_helm
    elif choice == "philosophy book":
        philosophy_book = Item()
        philosophy_book.type = "accessory"
        philosophy_book.name = '''Pangloss`s "Metaphysiology collection" book'''
        philosophy_book.max_hp_bonus = rand.randint(30, 40)
        philosophy_book.str_bonus = rand.randint(-8, -2)
        philosophy_book.spd_bonus = rand.randint(5, 8)
        philosophy_book.cost = rand.randint(1, 5)
        return philosophy_book