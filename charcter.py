import random
HEALTH = 20 #this is where constants go

class Character:
    """Models each Menu Item."""
    def __init__(self, name, cla):
        self.name = name
        self.cla = cla
        self.health = 20
        self.hit = random.randint(4, 6)
        self.level = 1
        self.special_skills = []

        #self.hp = 10 + self.level * 5

        #hit_amount = level +=1
        #self.create_ch() if you want to initialize one of the functions when the class is called, such as creating an object on screen

    def display(self):
        print(f"Name: {self.name}, Level: {self.level}, Class: {self.cla}")

    def get_player_info(self):
        pass

    #def create_ch(self):




class Menu:
    """Models the Menu."""
    def __init__(self):
        pass