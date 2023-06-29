import random
from colorama import Fore, Back, Style
from loot import Loot
import sys

loot = Loot()
class Combat:
    """combat"""

    def __init__(self, mob_name="", health_mob=0):
        """combat"""
        #self.damage = [1, 1, 1]
        self.player_health_pool = 20
        #self.health = self.health_max
        #self.attack = random.randint(damage, weights = [])
        #self.mob = mob
        self.mob_name = mob_name
        self.m_health_pool = health_mob


    def player_h(self):
        """returns current player health???"""
        current_health = self.player_health_pool
        return current_health

    def mob_h(self):
        """returns current mob health???"""
        current_heal = self.m_health_pool
        return current_heal


    def recover_health(self):
        heal = random.randint(5,6)
        player_health = self.player_health_pool + heal
        if player_health >= 20:
            player_health = 20
        self.player_health_pool = player_health
        return heal, player_health

    def damage_to_char(self):
        """picks from list of numbers to do random damage to player
        from the mob, returns damage to player and player health"""
        list3 = [2, 2, 3, 3, 4, 5, 6]
        damages = random.choice(list3)
        player_health = self.player_health_pool - damages
        if player_health <= 0:
            player_health = 0
        self.player_health_pool = player_health
        return damages, player_health

    def attack(self):
        """in this function the player attacks the mob, hits are taken from a random number list, and  then returns
         the attacks as damage to mob and returns the mob health after taking damage"""
        #hits = [1, 2, 3, 4, 5, 1, 0]
        #damages = random.choice(hits)
        damages = random.randint(3,6)
        c_mob_health = self.m_health_pool - damages
        if c_mob_health <= 0:
            c_mob_health = 0
        self.m_health_pool =  c_mob_health
        #if self.m_health_pool <= 0:
            #return (print("the troll is dead"))
        #else:
        print(f"{damages, c_mob_health, self.m_health_pool}, damage dealt by player, mob health after damage, current mob health")
        return damages, c_mob_health


    def m_take_damage(self):
        c_mob_health = self.m_health_pool - self.attack
        return c_mob_health

    def fighting_c(self, char_name, mob_name, health_mob):



        while self.m_health_pool >= 1 and self.player_health_pool >= 1:

            select = input(f"{Fore.RED}Press '1' to swing your sword at the {mob_name}, press '2' to use a health potion\n")
            if select == '1':
                print(f"{Fore.BLUE}{char_name} swings their sword at the {mob_name} and hits it for {Fore.RED}{self.attack()[0]} damage.")
                print(f"{Fore.BLUE}The {mob_name} hits back at you with and hits you for {Fore.RED}{self.damage_to_char()[0]} damage")
                print(f"{Fore.BLUE}Your health is now {Fore.GREEN}{self.player_h()}.")
                print(f"{Fore.BLUE}The {mob_name} health is now {Fore.RED}{self.mob_h()}")
            if select == '2':
                print(f"{Fore.BLUE}{char_name} uses a health potion and heals for {Fore.GREEN}{self.recover_health()[0]}.")
                print(f"{Fore.BLUE}{char_name} health is now at {Fore.GREEN}{self.player_h()}.")
                print(f"{Fore.BLUE}The {mob_name} hits back at you for {self.damage_to_char()[0]}")
        if self.player_health_pool >= 1:
            print(f"You have slain {mob_name}!")
            print(f"You loot {loot.loot_mob_name(mob_name)} gold!")

        else:
            print(f"You died!")





