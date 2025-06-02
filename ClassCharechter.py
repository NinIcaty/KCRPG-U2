import FunctionAction
import colorama
import random

class Character:
    def __init__(self, name, health,max_health, attack_power, pp,charge_pp_power, charge_uses,shield_points, char_type):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack_power = attack_power
        self.pp = pp
        self.charge_pp_power = charge_pp_power
        self.charge_uses = charge_uses
        self.shield_points = 0
        self.char_type = char_type
        self.potions = ""  # Hold potions
        self.adjust_attributes()

    def adjust_attributes(self):
        if self.char_type == "Mage":
            self.pp = 110
            self.attack_power = 20
            self.health = 50
            self.charge_pp_power = 25
            self.charge_uses = 5
            self.max_health  = 75
        elif self.char_type == "Warrior":
            self.charge_pp_power = 0
            self.charge_uses = 10
            self.health = 150
            self.attack_power = 30
            self.pp = 30
            self.max_health = 225
        elif self.char_type == "Rogue":
            self.charge_pp_power = 10
            self.health = 100
            self.pp = 70
            self.attack_power = 25
            self.charge_uses = 20
            self.max_health = 150
        elif self.char_type == "asher_hero":
            self.charge_pp_power = 10
            self.health = 90
            self.attack_power = 20
            self.pp = 70
            self.max_health = 135
            self.charge_uses = 6
        elif self.char_type == "biochemistry_hero":
            self.health = 150
            self.charge_pp_power = 5
            self.attack_power = 20
            self.pp = 100
            self.charge_uses = 7
            self.max_health = 225
        elif self.char_type == "anaconda":
            self.charge_pp_power = 0
            self.health = 250
            self.attack_power = 40
            self.pp = 150
            self.charge_uses = 10
            self.max_health = 375
        #Test Mode/God
        if self.char_type == "god":
            self.pp = 1000000
            self.health = 5000
            self.charge_uses = 500
            self.max_health = 132893479247827492749
        if self.char_type == "anaminion":
            self.pp = 100
            self.attack_power = 25
            self.health = 150
            self.charge_pp_power = 25
            self.charge_uses = 20
            self.max_health  = 225
        elif self.char_type == "anaconda2":
            self.charge_pp_power = 35
            self.health = 750
            self.attack_power = 50
            self.pp = 500
            self.charge_uses = 20
            self.max_health = 1125
    def is_alive(self):
        return self.health > 0
    def ai_action(self, opponent):

        if self.charge_uses == 0 and self.pp == 0:
            print(f"{self.name} has no charge uses and PP! It uses Basic Attack.")
            FunctionAction.attack(opponent, "basic")
        elif self.health < 30 and self.pp >= 10:
            heal_type = random.choice(["light", "medium", "heavy"])
            FunctionAction.heal(self,heal_type)
        elif self.pp >= 25 and random.random() < 0.2:
            FunctionAction.attack(self,opponent, "special")
        elif self.pp >= 20 and random.random() < 0.4:
            FunctionAction.attack(self,opponent, "super")
        elif self.pp >= 10 and random.random() < 0.6:
            FunctionAction.attack(self,opponent, "power")
        elif self.pp >= 10 and random.random() < 0.3:
            FunctionAction.attack(self,opponent, "frenzy")

        else:
            FunctionAction.charge_pp(self)
    '''def use_potion(self, potion)
        if potion == "HP Potion":
            self.health += 50
            print(colorama.Fore.BLACK+colorama.Back.YELLOW+f"{self.name} uses an HP Potion and restores 50 HP!")
        elif potion == "PP Potion":
            self.pp += 75
            print(colorama.Fore.BLACK+colorama.Back.YELLOW+f"{self.name} uses a PP Potion and restores 75 PP!")
        elif potion == "Attack Potion":
            self.attack_power += 10
            print(colorama.Fore.BLACK+colorama.Back.YELLOW+f"{self.name} uses an Attack Potion and increases attack power by 10!")
        elif potion == "Shield Potion":
            self.shield_strength += 10
            print(colorama.Fore.BLACK+colorama.Back.YELLOW+f"{self.name} uses a Shield Potion and gains 10 shield strength!")
'''
