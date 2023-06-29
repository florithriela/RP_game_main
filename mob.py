import random

class Mob:
    """Models each Menu Item."""
    def __init__(self, name_mob="", health_mob=0):
        self.name_mob = name_mob
        self.health_mob = health_mob
        #self.hit = random.randint(1, 3)
        #self.create_ch() #if you want to initialize one of the functions when the class is called, such as creating an object on screen

    def spider_type(self):

        spider = Mob("spider", 7)
        #self.name_mob = "spider"
        #self.health_mob = 5
        #self.hit = random.randint(1, 2)
        return spider

    def troll_type(self):
        #golds = random.randint(1, 3)
        troll = Mob("troll", 15)
        #self.health_mob = 5
        #self.hit = random.randint(1, 2)
        return troll



    def goblin_type(self):
        goblin = Mob("goblin", 11)
        #self.health = 8
        #self.hit = random.randint(1, 3)
        return goblin

    def bear_type(self):
        bear = Mob("bear", 10)
        return bear

    def dragon_type(self):
        dragon = Mob("dragon", 11)
        return dragon

    def bird_type(self):
        birds = Mob("flock of birds", 12)
        return birds


    def orc_type(self):
        orc = Mob("Orc", 14)
        return orc

    def boss_dragon_type(self):
        boss_dragon = Mob("Large Dragon", 24)
        return boss_dragon

    def boss_orc_type(self):
        boss_orc = Mob("Orc Leader", 20)
        return boss_orc

    def boss_spider_type(self):

        boss_spider = Mob("Gigantic spider", 20)

        return boss_spider

    def boss_goblin_type(self):
        boss_goblin = Mob("Goblin leader", 20)
        return boss_goblin

    def boss_loot_gold(self):
        golds = random.randint(4, 8)
        #self.inventory.append(golds)
        return (golds)