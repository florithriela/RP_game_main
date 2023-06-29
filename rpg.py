from charcter import Character



print("Welcome to RPG world")
class_one = input(f"Enter your class, choose mage or warrior")
name_one = input(f"Enter your name")

player_one = Character(name_one, class_one)
print(f"Your have made a {player_one.cla} named {player_one.name}")
