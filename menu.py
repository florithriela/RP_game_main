import sys
import colorama
from colorama import Fore
class Menu:
    """menu"""
    def __init__(self, rpg):
        """menu options"""


    def run_menu(self):
        print(f"{Fore.BLUE}Welcome to text world\n")
        print(f"C{Fore.BLUE}hoose from the following options\n")
        print(f"""{Fore.BLUE}Menu:\n
        {Fore.CYAN}1: Start a new game\n
        {Fore.CYAN}2: Quit\n
        """)

        opt = input(f"{Fore.BLUE}what would you like to do? -->\n")

        if opt == "1":
            print(f"{Fore.BLUE}ok starting game")
            print(f"{Fore.YELLOW} :) :) :)")
            starting_game
        if opt == "2":
            sys.exit()
