import random

class Loot:
    """loot table"""
    def __init__(self):
        """loot"""
        drop_list = ["sword", "coat", "shoes", "hat", "cape", "ring",
                     "coat", "junk", "earring"]

        golds = ["1 gold", "1 gold", "1 gold", "1 gold", "2 gold", "2 gold",
                 "3 gold"]
        self.inventory = []
        self.inventory_dic = {}
        self.inventory_gold = 0

    def list_inventory_dic(self):
        invent =[]
        for item_invent in self.inventory_dic:
            invent.append(item_invent)

        return invent

    def loot_drops(self):
        drop_list = ["sword", "coat", "shoes", "hat", "cape", "ring",
                     "coat", "junk", "earring"]
        drops = (random.choices(drop_list, weights=[8, 8, 8, 3, 3, 3, 1, 1, 1], k=2))
        return (drops)

    def gold_drops(self):
        golds = ["1 gold", "1 gold", "1 gold", "1 gold", "2 gold", "2 gold",
                     "3 gold"]
        drops = (random.choices(drop_list, weights=[3, 3, 1, 1, 1, 1, 1], k=1))
        return (drops)

    def loot_dic(self):
        inventory = {'sword': 5, 'ring level one': 2, 'magic gloves': 4}

        # get a random key from the dictionary
        random_key = random.choice(list(inventory.keys()))

        # get the value for the random key
        random_value = inventory[random_key]
        self.inventory_dic[random_key] = random_value
        # print the random key-value pair
        print(f"from loot one Random key-value pair: key: {random_key} value: {random_value}")
        return (random_key, random_value)

    def loot_dic_two(self):
        inventory = {'sword': 1, 'ring level one': 2, 'magic gloves': 4}

        looted, numeric_val = random.choice(list(inventory.items()))
        self.inventory_dic[looted] = numeric_val
        print(f"from loot two Looted {looted} with a numeric value of {numeric_val}")
        return (looted, numeric_val)

    def gold(self):
        golds = random.randint(1,4)
        self.inventory.append(golds)
        self.inventory_gold += (golds)
        return (golds)
    #print(f"you walk further and find a chest, you open and inside you find {loot()}")

    def boss_loot_gold(self):
        golds = random.randint(4, 8)
        self.inventory.append(golds)
        return (golds)

    def boss_loot_items(self):
        drops_boss = ("level 1 ring", "staff", "sword", "bracelet")
        items = random.choices(drops_boss)

        return (items)

    def list_inventory(self):
        for item in self.inventory:
            return(item)

    def treasure(self):
        golds = random.randint(6,11)
        self.inventory.append(golds)
        return (golds)

    def special_item_treasure(self):
        drops_boss = ("magic ring", "magic ball", "magic ring", "magic ring")
        items = random.choices(drops_boss)
        self.inventory.append(items)
        return (items)

    def loot_mob_name(self, mob_name):
        if mob_name == "troll" or "spider" or "goblin":
            return self.gold()
        if mob_name == "Orc Leader" or "Gigantic spider" or "Goblin leader":
            self.boss_loot_gold()
            self.boss_loot_items()

