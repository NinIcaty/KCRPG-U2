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

    def attack(self, other, attack_type):
        damage = 0
        if attack_type == "basic":
            if self.pp >= 0:
                damage = 3
                if other.shield_points > damage:
                    other.shield_points -= damage
                    damage = 0

                else:
                    damage -= other.shield_points
                    other.shield_points = 0
                other.health -= damage
                print(colorama.Back.YELLOW+colorama.Fore.BLACK+f"{self.name} uses Basic Attack on {other.name} for {damage} damage! (Cost: 0 PP)")
        elif attack_type == "power":
            if self.pp >= 10:
                damage = random.randint(10, self.attack_power)
                if other.shield_points > damage:
                    other.shield_points -= damage
                    damage = 0
                else:
                    damage -= other.shield_points
                    other.shield_points = 0
                other.health -= damage
                self.pp -= 10
                print(colorama.Back.YELLOW+colorama.Fore.BLACK+f"{self.name} uses Power Attack on {other.name} for {damage} damage! (Cost: 10 PP)")
        elif attack_type == "super":
            if self.pp >= 20:
                damage = random.randint(15, self.attack_power + 10)
                if other.shield_points > damage:
                    other.shield_points -= damage
                    damage = 0
                else:
                    damage -= other.shield_points
                    other.shield_points = 0
                other.health -= damage
                self.pp -= 20
                print(colorama.Back.YELLOW+colorama.Fore.BLACK+f"{self.name} uses Super Attack on {other.name} for {damage} damage! (Cost: 20 PP)")
        elif attack_type == "special":
            if self.pp >= 25:
                damage = random.randint(15, self.attack_power + 15)
                #Remember to add Special pierces/Neglects Shield
                other.health -= damage
                self.pp -= 25
                print(colorama.Back.YELLOW+colorama.Fore.BLACK+f"{self.name} uses Special Attack on {other.name} for {damage} damage! (Cost: 25 PP)")
        elif attack_type == "explosive":
            if self.pp >= 30:
                damage = random.randint(20, self.attack_power + 20)
                if other.shield_points > damage:
                    other.shield_points -= damage
                    damage = 0

                else:
                    damage -= other.shield_points
                    other.shield_points = 0
                other.health -= damage
                self.pp -= 30
                print(colorama.Back.YELLOW+colorama.Fore.BLACK+f"{self.name} uses Explosive Attack on {other.name} for {damage} damage! (Cost: 30 PP)")
        elif attack_type == "frenzy":
            if self.pp >= 40:

                damage = random.randint(40, self.attack_power * 2 + 15)
                if other.shield_points > damage:
                    other.shield_points -= damage
                    damage = 0

                else:
                    damage -= other.shield_points
                    other.shield_points = 0
                other.health -= damage
                self.pp -= 40
                print(colorama.Back.YELLOW+colorama.Fore.BLACK+f"{self.name} uses Frenzy Attack on {other.name} for {damage} damage! (Cost: 40 PP)")
    def charge_pp(self):
        if self.charge_uses > 0:
            gained_pp = 25 + self.charge_pp_power
            self.pp += gained_pp
            self.charge_uses -= 1
            print(colorama.Fore.BLACK+colorama.Back.YELLOW+f"{self.name} charges up for {gained_pp} PP! Uses left: {self.charge_uses}")
        else:
            print(f"{self.name} has no charge uses left!")

    def heal(self, heal_type):
        if heal_type == "light":
            if self.pp >= 5:
                heal_amount = random.randint(5, 10)
                self.health += heal_amount
                if self.health > self.max_health:self.health = self.max_health
                self.pp -= 5
                print(colorama.Fore.BLACK+colorama.Back.YELLOW+f"{self.name} performs a Light Heal for {heal_amount} HP! (Cost: 5 PP)")
        elif heal_type == "medium":
            if self.pp >= 10:
                heal_amount = random.randint(10, 20)
                self.health += heal_amount
                if self.health > self.max_health:self.health = self.max_health

                self.pp -= 10
                print(colorama.Fore.BLACK+colorama.Back.YELLOW+f"{self.name} performs a Medium Heal for {heal_amount} HP! (Cost: 10 PP)")
        elif heal_type == "heavy":
            if self.pp >= 15:
                heal_amount = random.randint(20, 30)
                self.health += heal_amount
                if self.health > self.max_health:self.health = self.max_health
                self.pp -= 15
                print(colorama.Back.YELLOW+colorama.Fore.BLACK+f"{self.name} performs a Heavy Heal for {heal_amount} HP! (Cost: 15 PP)")
        elif heal_type == "rejuvenate":
            if self.pp >= 25:
                heal_amount = random.randint(30, 50)
                self.health += heal_amount
                if self.health > self.max_health:self.health = self.max_health
                self.pp -= 25
                print(colorama.Back.YELLOW+colorama.Fore.BLACK+f"{self.name} performs a Rejuvenate Heal for {heal_amount} HP! (Cost: 25 PP)")
        elif heal_type == "ultimate_heal":
            if self.pp >= 40:
                heal_amount = random.randint(40, 60)
                self.health += heal_amount
                if self.health > self.max_health:self.health = self.max_health
                self.pp -= 40
                print(colorama.Back.YELLOW+colorama.Fore.BLACK+f"{self.name} performs an Ultimate Heal for {heal_amount} HP! (Cost: 40 PP)")

    def shield(self, shield_type):
        shield_costs = {"light": 20, "medium": 30, "heavy": 50, "reflective": 40}
        shield_values = {"light": 10, "medium": 20, "heavy": 40, "reflective": 30}

        if shield_type in shield_costs:
            cost = shield_costs[shield_type]
            if self.pp >= cost:
                self.pp -= cost
                self.shield_points += shield_values[shield_type]
                print(colorama.Fore.BLACK+f"{self.name} activates a {shield_type.capitalize()} Gaining {shield_values[shield_type]} Shield Points! (Cost: {cost} PP)")
            else:
                print(f"{self.name} doesn't have enough PP for {shield_type.capitalize()} Shield!")


    def is_alive(self):
        return self.health > 0

    def ai_action(self, opponent):

        if self.charge_uses == 0 and self.pp == 0:

            self.attack(opponent, "basic")
        if self.name != "Anaconda":

            if self.health < 30 and self.pp >= 10:
                if self.pp <= 10:
                    heal_type = "light"
                    self.heal(heal_type)
                elif self.pp <= 35:
                    heal_type = "medium"
                    self.heal(heal_type)

                elif self.pp <= 40:
                    heal_type = "heavy"
                    self.heal(heal_type)


            elif self.pp >= 25 and random.random() < 0.5:
                self.attack(opponent, "special")
            elif self.pp >= 20 and random.random() < 0.4:
                self.attack(opponent, "super")
            elif self.pp >= 10 and random.random() < 0.7:
                self.attack(opponent, "power")
            elif self.pp >= 60 and random.random() < 0.6:
                self.attack(opponent, "frenzy")
            elif self.charge_uses > 0:
                self.charge_pp()
            else:
                self.pp += 5
                print (f"{self.name} rested and got 5 PP")
        elif self.name == "Anaconda":
            if self.health < 100 and self.pp >= 10:
                if self.pp <= 10:
                    heal_type = "light"
                    self.heal(heal_type)
                elif self.pp <= 35:
                    heal_type = "medium"
                    self.heal(heal_type)

                elif self.pp <= 40:
                    heal_type = "heavy"
                    self.heal(heal_type)


            elif self.pp >= 25 and random.random() < 0.5:
                self.attack(opponent, "special")
            elif self.pp >= 20 and random.random() < 0.4:
                self.attack(opponent, "super")
            elif self.pp >= 10 and random.random() < 0.7:
                self.attack(opponent, "power")
            elif self.pp >= 60 and random.random() < 0.6:
                self.attack(opponent, "frenzy")
            elif self.charge_uses > 0 and self.pp <= 10:
                self.charge_pp()
            else:
                self.pp += 5
                print (f"{self.name} rested and got 5 PP")

    '''def use_potion(self, potion):
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
