import sys
import time
from random import choice, randint
from bcolors import *
from helpers import *
crit = False 
class Character:
    def __init__(self,name, hp, defaultHp, atk, res):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.res = res
        self.defaultHp = defaultHp

    def is_dead(self):
        if self.hp <= 0:
            print(f"{self.name} is dead")
            self.hp = self.defaultHp
class Aventureer(Character):
    # TODO : IMPLEMENT MAX XP VALUES PER LEVEL 
    def __init__(self, name, job, hp, defaultHp, atk, res, gold, luck,is_dead):
        self.name = name
        self.job  = job
        self.hp   = hp
        self.defaultHp = defaultHp
        self.atk  = atk
        self.defaultAtk = hp
        self.res  = res
        self.defaultRes = res
        self.gold = gold
        self.luck = luck
        self.is_dead = is_dead
        # Would make sense to keep track of the level
        # Since every Aventureer starts at level 1, we can assign it by default without
        # passing it as parameter to the constructor
        self.level = 1


    def full_name(self):
        return f"{self.name} the {self.job}"

    def level_up(self, levelAmount):
        self.hp = int(self.hp) + 5
        self.atk  = int(self.atk) + 3
        self.res  = int(self.res) + 1
        self.gold = int(self.gold + 100)
        # Now here we can increment his level
        self.level += levelAmount
    def heal(self):
        self.hp = self.defaultHp
    def show_stats(self):
        dprintf(":-=-=-=-=-=-=-=-=-=-=-=-=-=-:".center(75))
        dprintf(f"Stats of {self.full_name()}".center(75))
        dprintf(":-=-=-=-=-=-=-=-=-=-=-=-=-=-:".center(75))
        dprintf(f"LEVEL :  {self.level}".center(75))
        dprintf(f"HP    : {self.hp} / {self.defaultHp} ".center(75))
        dprintf(f"STR   :  {self.atk}".center(75))
        dprintf(f"DEF   :  {self.res} ".center(75))
        dprintf(f"Gold  : {self.gold} ".center(75))
        dprintf(f"Luck  : {self.luck} ".center(75))

        dprintf(":-=-=-=-=-=-=-=-=-=-=-=-=-=-:".center(75))

    def calculate_critical(self):
        random_chance = randint(1, 10)
        if self.luck >= random_chance:
            self.atk *= 1.5
            round(self.atk, 1)
            print(f"⚡ Critique pour {self.name}")
            return True
        else:
            return False
        

    def attack(self, opponent):
            print(f"{bcolors.WARNING}       You are attacking {opponent.full_name()}{bcolors.ENDC}".center(75))

            while self.hp > 0 and opponent.hp > 0:
                input(f"- - - - - - -".center(75))
                # WHERE THE FIGHT TAKES PLACE
                dprintf(f"{self.name} 🗡️ {opponent.name} ☠️")
                
                # Calculate if the next hit will be critical, since calculate_critical modify the self.atk itself
                self.calculate_critical()
                
                hero_attack_dmg = self.atk - opponent.res
                if self.calculate_critical == True:
                    self.atk /= 0.75
                    self.calculate_critical == False
                if hero_attack_dmg < 0:
                    hero_attack_dmg = 0

                opponent.calculate_critical()

                opponent.hp -= hero_attack_dmg
                if opponent.calculate_critical == True:
                    self.atk /= 0.75
                    opponent.calculate_critical = False
                dprintf(f"{opponent.name} takes {hero_attack_dmg} DMG from {self.name} !")
                dprintf(f"☠️  {opponent.name} : {opponent.hp} / {opponent.defaultHp} HP")
                if opponent.hp > 0:
                        dprintf(f"{bcolors.FAIL}☠️  {opponent.name} 🗡️ {self.name}{bcolors.ENDC}")             
                        opponent.calculate_critical()
                        heel_attack_dmg = opponent.atk - self.res
                        if heel_attack_dmg < 0:
                            heel_attack_dmg = 0
                        self.hp -= heel_attack_dmg
                    # What is shown during combat
                
                        dprintf(f"{self.name} takes {heel_attack_dmg} DMG from {opponent.name} !")
                        dprintf(f"❤️  {self.name} : {self.hp} / {self.defaultHp} HP")
                        

                if self.hp <= 0:
                    dprint("You lose !")
                    dprint(f"{self.name} : 0 HP")
                    self.is_dead = True
                    
                    
                if opponent.hp <= 0:
                        opponent.is_dead = True
                        dprint("You won !")
                        dprint(f"{opponent.name} : 0 HP")
                        
                        
                        


class Ennemy(Character):
    def __init__(self, name, hp, atk, res):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.res = res