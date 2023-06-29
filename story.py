import random
#from mob import Mob

mob = Mob()

class Story:
    """Models each Menu Item."""
    def __init__(self):
        self.scene = []
        #self.name = name
        #self.cla = cla


    def scene_one(self):
        print(f"You set out on an adventure. As you walk down the road you meet a {mob.name}")
        print(f"The {mob.name} attacks! It hits you for {mob.hit}")