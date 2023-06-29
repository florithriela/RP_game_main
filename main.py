import random
import pickle
import json
import sys
from colorama import Fore, Back, Style
from charcter import Character
from mob import Mob
from combat import Combat
#from story import Story
from loot import Loot
import os
from dics_lists import *





def death(self):
     print(f"{Fore.RED}You died!")
     sel = input(f"{Fore.BLUE}type 1 to return to the menu,  2 exit.\n")
     if sel == "1":
         run_menu()
     if sel == "2":
         sys.exit()


def fight_combat():
        while combat.m_health_pool >= 1 and combat.player_health_pool >= 1:

            select = input(f"{Fore.RED}Press '1' to swing your sword at the troll, press '2' to use a health potion\n")
            if select == '1':
                print(
                    f"{Fore.BLUE}{char_name} swings their sword at the troll and hits it for {Fore.RED}{combat.attack()[0]} damage.")
                print(
                    f"{Fore.BLUE}The troll swings back at you with its mighty fists and hits you for {Fore.RED}{combat.damage_to_char()[0]} damage")
                print(f"{Fore.BLUE}Your health is now {Fore.GREEN}{combat.player_h()}.")
                print(f"{Fore.BLUE}The trolls health is now {Fore.RED}{combat.mob_h()}")
            if select == '2':
                print(
                     f"{Fore.BLUE}{char_name} uses a health potion and heals for {Fore.GREEN}{combat.recover_health()[0]}.")
                print(f"{Fore.BLUE}{char_name} health is now at {Fore.GREEN}{combat.player_h()}.")
                print(f"{Fore.BLUE}The troll swings back at you with its mighty fists and hits you for {combat.damage_to_char()[0]}")

        return combat.m_health_pool, combat.player_health_pool

def quest_town(npc, items):

    print(f"{npc} says 'adventurer, will you assist me? I need some {items}")
    assist = input(f"y for yes, n for no")
    if assist == "y":
        print(f"You agree to assist {npc} with their request. You head to the plains surrouding the town to collect {items}")
    if assist == "n":
        print(f"You continue on your journey")
    print(f"You go to collect the items for the quest")
    print(f"You go to collect the items for the quest")


def game_start(player):

    dessert_one = daily_desserts
    #create new char or use old one
    #player_class = create_new_char()

    #return player_one.name, player_one.cla
    #char_name = player_class[0]
    #print(player_class[0])

    loot = Loot()
    mob = Mob()

    #Establish instances of mob types
    troll = mob.troll_type()
    spider = mob.spider_type()
    goblin = mob.goblin_type()
    birds = mob.bird_type()
    boss_spider = mob.boss_spider_type()
    print(spider.name_mob)
    print(spider.health_mob)


    #Establish combat instances for each mob type
    spider_combat = Combat(spider.name_mob, spider.health_mob)
    #spider_combat.fighting_c(char_name, spider.name_mob, spider.health_mob)

    troll_combat = Combat(troll.name_mob, troll.health_mob)
    #troll_combat.fighting_c(char_name, troll.name_mob, troll.health_mob)

    birds_combat = Combat(birds.name_mob, birds.health_mob)
    # birds_combat.fighting_c(char_name, birds.name_mob, birds.health_mob)

    goblin_combat = Combat(goblin.name_mob, goblin.health_mob)
    # goblin_combat.fighting_c(char_name, goblin.name_mob, goblin.health_mob)

    boss_spider_combat = Combat(boss_spider.name_mob, boss_spider.health_mob)
    # boss_spider_combat.fighting_c(char_name, boss_spider.name_mob, boss_spider.health_mob)

    print(f"You have made a {player.cla} named {player.name}, and you are level {player.level}")
    print(f"{Fore.BLUE}The hero {player.name} sets off on a journey to find fame and adventure.")
    #print(Style.RESET_ALL)
    print(f"{Fore.BLUE}{player.name} sets off on a path towards the dark forest.")
    print(f"{Fore.BLUE}{player.name} finds a troll blocking the path.")
    #player_class.special_skills.append('ithild')
    op = input(f"{Fore.BLUE}type 1 to fight the troll, 2 to sneak around it.\n")

    if op == "1":
        troll_combat.fighting_c(player.name, troll.name_mob, troll.health_mob)
        #calls function to start combat, pass char name to function, later add mob name from class of mob and type of loot
        #mob_name_one = troll

        #troll_combat.fighting_c(char_name, troll[0], troll[1])
        # while combat.m_health_pool >= 1 and combat.player_health_pool >= 1:
        #
        #     select = input(f"{Fore.RED}Press '1' to swing your sword at the troll, press '2' to use a health potion\n")
        #     if select == '1':
        #         print(
        #             f"{Fore.BLUE}{char_name} swings their sword at the troll and hits it for {Fore.RED}{combat.attack()[0]} damage.")
        #         print(
        #             f"{Fore.BLUE}The troll swings back at you with its mighty fists and hits you for {Fore.RED}{combat.damage_to_char()[0]} damage")
        #         print(f"{Fore.BLUE}Your health is now {Fore.GREEN}{combat.player_h()}.")
        #         print(f"{Fore.BLUE}The trolls health is now {Fore.RED}{combat.mob_h()}")
        #     if select == '2':
        #         print(
        #              f"{Fore.BLUE}{char_name} uses a health potion and heals for {Fore.GREEN}{combat.recover_health()[0]}.")
        #         print(f"{Fore.BLUE}{char_name} health is now at {Fore.GREEN}{combat.player_h()}.")
        #         print(f"{Fore.BLUE}The troll swings back at you with its mighty fists and hits you for {combat.damage_to_char()[0]}")
        #
        #     # print(f"The troll is now at {self.combat.attack()[1]} health.")
        #     # print(f"Your health is now {self.combat.damage_to_char()[1]}.")

        if troll_combat.player_health_pool <= 1:

            print(f"{Fore.RED}You died!")
            sel = input(f"{Fore.BLUE}type 1 to return to the menu,  2 exit.\n")
            if sel == "1":
                run_menu()
            if sel == "2":
                sys.exit()
        elif troll_combat.m_health_pool <= 1:

            print(f"{Fore.RED}You have slain the troll!")

            print(f"{Fore.BLUE}You search the dead troll and find {loot.gold()} gold, {loot.loot_dic()} from loot dic")
            print(f"Here is your inventory {loot.list_inventory_dic()} {loot.inventory_gold} from gold purse ")



    elif op == "2":
        print(f"{Fore.BLUE}You attempt to sneak past the troll but you are not stealthy enough")
        print(f"{Fore.BLUE}He sees you and hits you with his might fists for {troll_combat.damage_to_char()[0]}")
        troll_combat.fighting_c(player.name, troll.name_mob, troll.health_mob)


    else:
        print(f"{Fore.BLUE} Please make a valid selection")
        op = input(f"{Fore.BLUE}type 1 to fight the troll, 2 to sneak around it.\n")

    print(f"You continue and enter the dark forest. It becomes darker and darker. The path splits into two")
    next = input("One path apppears to lead deeper into the darkness of the forst, the other follows a small stream, type '1' to take the first path, '2' to take the second")
    if next == "1":


        print(
            f"{Fore.BLUE}The path grows darker and darker. Just when you think it can't get any darker you hear sound")
        print(
            f"{Fore.BLUE}Then you see things moving, all around you. You are surrounded by large spiders. You run as fast as you can")
        print(f"{Fore.BLUE}Now you are completely lost and can't find the path. You enter a cave")
        print(f"{Fore.BLUE}Suddenly you see a huge spider, it comes at you quickly")
        print(f"{Fore.BLUE}It jabs at you for {spider_combat.damage_to_char()[0]} and you strike back")
        spider_combat.fighting_c(player.name, spider.name_mob, spider.health_mob)

        loot.boss_loot_items()
        print(f"{Fore.BLUE}The spider dies and you find on it {loot.boss_loot_items(), loot.boss_loot_gold()} ")

        print(f"{Fore.BLUE}You see a light outside of the cave, you go towards it and see a glowing, sparkeling ball of light ")
        print(f"{Fore.BLUE}It is still very dark around you, but and the light begins to move, you follow it")
        print(f"{Fore.BLUE}After some time it leads you to a glade in the forest, where you find some wood elves guarding an outpost")
        print(f"{Fore.BLUE}The light belongs to an elven mage named Gladhwyn, she and the other elves welcome you to the safety of their outpost")
        print(f"{Fore.BLUE}While there, the mage offers to teach you a spell in exchange for swearing an oath to assist her at some future time")
        accept_offer = input(f"{Fore.BLUE} do you accept her offer?")
        if accept_offer == "y":
            print(f"{Fore.BLUE}You swear an oath to assist the mage when she requests ")
            print(f"{Fore.BLUE}The mage is able to teach you the secret magic of the ithild, a guiding light in the dark")
            print(f"{Fore.BLUE}'This will guide you in times of darkness and also serve to rescue others' she states")
            player.special_skills.append('ithild')

        if accept_offer == "n":
            print(f"{Fore.BLUE} the elven mage seems slightly annoyed, stating /'You will not find such a great offer of knowledge elsewhere/'")
            print(f"{Fore.BLUE}however, you still part on peaceful terms, and the elves direct you towards the path that goes northward, to the town of Altwyn")


    elif next == "2":
        print(f"{Fore.BLUE} You head towards the sound of a waterfall")
        print(f"{Fore.BLUE} You stop at the a stream near the waterfall to take a drink of water")
        print(f"{Fore.BLUE} A hear a faint sound and turn around, a goblin is trying to sneak up on you and steal your pack")

        goblin_combat.fighting_c(player.name, goblin.name_mob, goblin.health_mob)
        print(f"{Fore.BLUE}You {loot.gold()} gold")
        print(f"{Fore.BLUE}You follow the stream south, you come to a grassy open area, filled with sunlight. You sit down to rest")
        print(f"{Fore.BLUE}You notice something sparkly nearby inside a tree")
        print(f"{Fore.BLUE} You go over to investigate")
        print(f"{Fore.BLUE} You find a glowing treasure chest, you open it to find {loot.treasure()} gold {loot.special_item_treasure()}")

    else:
        print(f"Please enter a valid number")
        next = input("One to head to the forest, two for the stream")

    print(f"Here is your inventory {loot.inventory}, {loot.list_inventory_dic()} {loot.inventory_gold} from gold purse ")

    print(f"You head north, and come to the town of Valden")
    print(f"The main street of the town is busy and filled with shops, people, and children playing on the street ")
    print(f"On the main street is an Inn, a armour shop, a curiosity shop and pastry store.")
    town = input(f"type 'I' for the Inn, 'A' for the armour shop, 'C' for the curiosity shop, 'P' for the pasty store.")
    print(f"You go to collect the items for the quest")
    if town == 'p':
        print(f"You enter the pastry shop, a variety of delicous pastries are avaialbe,")
        des = input(f"Type d for a list of todays desserts, type q to find out if the shopkeeper has a quest for you, type s to ask the shopkeeper about the town")
        if des == "d":
            print(f"Here is a list of todays desserts {dessert_one}, {dessert_two}, {dessert_three}. Type 1, 2 or 3 for your desired dessert, n to cancel")
        if des == "s":
                  print(f"You ask the shopkeeper "
    if town == 'i':
        tow = input(f"q for a quest from the innkeeper, b to get a bed for the night, s to have a friendly chat with the innkeeper")



def create_new_char():
    import os
    import pickle

    def create_new_char():
        # function to create a new character
        print("Welcome to RPG world")

        if os.path.isfile('player_file.pickle'):
            with open('player_file.pickle', 'rb') as f:
                player = pickle.load(f)
                print(f"Your saved character is a {player.cla} named {player.name}, and you are level {player.level}")
        else:
            print(f"You do not have any saved characters, please make one")
            name = input("Enter name: ")
            cla = input("Enter class: ")
            player = Character(name, cla)
            with open('player_file.pickle', 'wb') as f:
                pickle.dump(player, f)

        return player




    #return Character(name, cla)










def create_new_char_two():
    print("Welcome to RPG world")
    try:
        un_pickled_player = pickle.load(open('player_file.pickle', 'rb'))
        player_class = un_pickled_player

        print(f"Your saved character is a {player_class.cla} named {player_class.name}, and you are level{player_class.level}")

        if player_class:
            print(f"Your saved character is a {player_class.cla} named {player_class.name}, and you are level {player_class.level}")
            new_or_no = input(f"Would you like to use this character? y to use this character or n to make a new one")
            if new_or_no == "n":
                class_name = input(f"Enter your class, choose mage or warrior")
                char_name = input(f"Enter your name")
                player_class = Character(char_name, class_name)

            if new_or_no == "y":
                print("Starting game with current character")

    except FileNotFoundError:
        print(f"You do not have any saved characters, please make one")
        class_name = input(f"Enter your class, choose mage or warrior")
        char_name = input(f"Enter your name")
        player_class = Character(char_name, class_name)


        # if player_class:
        #     print(f"Your saved character is a {player_class.cla} named {player_class.name} and you are level {player_class.level}")
        #     new_or_no = input(f"Would you like to use this character? y to use this character or n to make a new one")
        #     if new_or_no == "n":
        #         class_name = input(f"Enter your class, choose mage or warrior")
        #         char_name = input(f"Enter your name")

        #    if new_or_no == "y":
        #        print("Starting game with current character")


    #player_class = Character(char_name, class_name)
    player_info = {'Name: "f{player_one.name}", Class:"f{player_one.cla}"'}
    print(f"Your have made a {player_class.cla} named {player_class.name} and are level {player_class.level}")
    pickled_player = pickle.dump(player_class, open('player_file.pickle', 'wb'))
    print("why is this looping")
    #un_pickled_player = pickle.load(open('player_file.pickle', 'rb'))
    #player_one = un_pickled_player
    #print(f"This is the unpickled player {player_one}")


    return player_class.name, player_class.cla, player_class.level



def run_menu_two():
    print(f"{Fore.BLUE}Welcome to text world\n")
    print(f"{Fore.BLUE}choose from the following options\n")
    print(f"""{Fore.BLUE}Menu:\n
    {Fore.CYAN}1: Start a new game\n
    {Fore.CYAN}2: Quit\n
    {Fore.CYAN}3: Load game\n
    """)

    opt = input(f"{Fore.BLUE}what would you like to do? -->\n")

    if opt == "1":
        print(f"{Fore.BLUE}ok starting game")
        print(f"{Fore.YELLOW} :) :) :)")
        game_start()
        #create_new_char()
    if opt == "2":
        sys.exit()

    if opt == "3":
        un_pickled_player = pickle.load(open('player_file.pickle', 'rb'))
        player_class = un_pickled_player
        #with open('player_info.txt', 'r') as f:
            # player_data = f.read()
            # char_name = player_data[0]
            # class_name = player_data[1]
            # player_one = Character(char_name, class_name)



        print(f"Your saved character is a {player_one.cla} named {player_one.name}")
        game_start(player_class)
        return player_one.name, player_one.cla


def run_menu():
    print(f"{Fore.GREEN}\nWelcome to RPG world\n")
    print(f"{Fore.BLUE}type 1 to create a new character")
    print(f"type 2 to load your character")

    while True:
        choice = input(f"{Fore.GREEN}Enter your choice: ")
        if choice == "1":
            name = input(f"{Fore.BLUE}What is the name of your character?\n")
            class_name = input(f"Enter your class, choose mage or warrior")

            player = Character(name, class_name)
            with open("savefile.txt", "wb") as file:
                pickle.dump(player, file)

            break
        elif choice == "2":
            if os.path.exists("savefile.txt"):
                with open("savefile.txt", "rb") as file:
                    player = pickle.load(file)
                    print(f"You have loaded your character {player.name}")
                    cho = input(f"Do you want to use this character?")
                    if cho.lower() == "y":
                        break
                    if cho.lower() == "n":
                        choice = "1"
            else:
                print(f"{Fore.RED}No saved file found\n")
        else:
            print(f"{Fore.RED}Invalid option, please try again")

    # start the game
    game_start(player)


#player = create_new_char()

#game_start(player)

run_menu()




