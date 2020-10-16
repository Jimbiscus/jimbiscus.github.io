import sys
import time
from random import choice, randint
from bcolors import *
from helpers import *
from characters import *


def intro():
    print("""                                                                           
     /\                            | |                                      
    /  \    __   __   ___   _ __   | |_   _   _   _ __    ___    ___   _ __ 
   / /\ \   \ \ / /  / _ \ | '_ \  | __| | | | | | '__|  / _ \  / _ \ | '__|
  / ____ \   \ V /  |  __/ | | | | | |_  | |_| | | |    |  __/ |  __/ | |   
 /_/    \_\   \_/    \___| |_| |_|  \__|  \__,_| |_|     \___|  \___| |_|   
                                                       'Soon on PS5 !'                                         
                                                                            """)
def show_characters(characters_list):
    print(":-=-=-=-=-:".center(75))
    for character in characters_list:
        print(f"  {character.name}.".center(75))
    print(":-=-=-=-=-:".center(75))

def choose_character(characters_list):
    hero = input("Choose your Hero : ")
    for character in characters_list:
        if character.name == hero:
            return character

def choose_ennemy():
    heel = input("Choose your Nemesis : ")
    for character in characters:
        if character.name == heel:
            return character



def initGame(hero, heel):
    hero.show_stats()
    
    input(f"Ready to go on an adventure ? Press [ENTER]".center(75))
    
    hero.attack(heel)
    
    if hero.is_dead == True:
        dprintf(f"Vous êtes mort !")
        hero.is_dead == False
        hero.heal()
    
    if heel.is_dead == True:
        dprintf(f"{heel.name} est mort")
        hero.level_up(1)
        heel.heal()
        heel = set_ennemy()
        heel.is_dead = False
        initGame(hero, heel)
    else:
        dprintf("Ok")
        heel.level_up(1)
        hero.show_stats()
        hero.attack(heel)
        initGame(hero, heel)

def set_ennemy():
    new_ennemy = choice(characters)
    if new_ennemy == hero:
        set_ennemy()
    else:
        return new_ennemy
characters = [
    # (self, name, job, hp, defaultHp, atk, res, gold, luck,is_dead):
    Aventureer("Jolan", "Necromancer", 25, 25, 11, 2, 100, 2, False),
    Aventureer("Allan", "Rogue", 28, 28, 12, 1, 100, 1, False),
    Aventureer("Marcus", "Barbarian", 30, 30, 9, 3, 100, 1, False),
    Aventureer("Arnaud", "Bard", 15, 15, 18, 3, 100, 7, False),
    Aventureer("Stalin", "Unbending", 25, 25, 15, 3, 100, 5, False),
    Aventureer("Bastien", "Magicien", 25, 25, 20, 3, 100, 6, False),
]

intro()

show_characters(characters)

hero = choose_character(characters)
heel = choose_ennemy()

initGame(hero, heel)