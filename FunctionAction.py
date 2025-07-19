import colorama
import random
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
            print(
                colorama.Back.YELLOW + colorama.Fore.BLACK + f"{self.name} uses Basic Attack on {other.name} for {damage} damage! (Cost: 0 PP)")
    elif attack_type == "power":
        if self.pp >= 10:
            damage = random.randint(10, self.attack_power)

            other.health -= damage
            self.pp -= 10
            print(
                colorama.Back.YELLOW + colorama.Fore.BLACK + f"{self.name} uses Power Attack on {other.name} for {damage} damage! (Cost: 10 PP)")
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
            print(
                colorama.Back.YELLOW + colorama.Fore.BLACK + f"{self.name} uses Super Attack on {other.name} for {damage} damage! (Cost: 20 PP)")
    elif attack_type == "special":
        if self.pp >= 25:
            if self.char_type == "Mage":
                damage = random.randint(20, self.attack_power + 15)
                self.health += 10
            elif self.char_type == "Warrior":
                damage = random.randint(30, self.attack_power * 1.5)
                self.shield_points += 5
            elif self.char_type == "Rouge":
                damage = random.randint(30, self.attack_power * 1.5)
                self.health += 5
                self.shield_points += 5
            else:damage = random.randint(15, self.attack_power + 15)
            if other.shield_points > damage:
                other.shield_points -= damage
                damage = 0
            else:
                damage -= other.shield_points
                other.shield_points = 0
            other.health -= damage
            self.pp -= 25
            print(
                colorama.Back.YELLOW + colorama.Fore.BLACK + f"{self.name} used their Special Move on {other.name} for {damage} damage! (Cost: 25 PP)")
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
            print(
                colorama.Back.YELLOW + colorama.Fore.BLACK + f"{self.name} uses Explosive Attack on {other.name} for {damage} damage! (Cost: 30 PP)")
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
            print(
                colorama.Back.YELLOW + colorama.Fore.BLACK + f"{self.name} uses Frenzy Attack on {other.name} for {damage} damage! (Cost: 40 PP)")


def charge_pp(self):
    if self.charge_uses > 0:
        gained_pp = 25 + self.charge_pp_power
        self.pp += gained_pp
        self.charge_uses -= 1
        print(
            colorama.Fore.BLACK + colorama.Back.YELLOW + f"{self.name} charges up for {gained_pp} PP! Uses left: {self.charge_uses}")
    else:
        print(f"{self.name} has no charge uses left!")


def heal(self, heal_type):
    if heal_type == "light":
        if self.pp >= 5:
            heal_amount = random.randint(5, 10)
            self.health += heal_amount
            if self.health > self.max_health: self.health = self.max_health
            self.pp -= 5
            print(
                colorama.Fore.BLACK + colorama.Back.YELLOW + f"{self.name} performs a Light Heal for {heal_amount} HP! (Cost: 5 PP)")
    elif heal_type == "medium":
        if self.pp >= 10:
            heal_amount = random.randint(10, 20)
            self.health += heal_amount
            if self.health > self.max_health: self.health = self.max_health

            self.pp -= 10
            print(
                colorama.Fore.BLACK + colorama.Back.YELLOW + f"{self.name} performs a Medium Heal for {heal_amount} HP! (Cost: 10 PP)")
    elif heal_type == "heavy":
        if self.pp >= 15:
            heal_amount = random.randint(20, 30)
            self.health += heal_amount
            if self.health > self.max_health: self.health = self.max_health
            self.pp -= 15
            print(
                colorama.Back.YELLOW + colorama.Fore.BLACK + f"{self.name} performs a Heavy Heal for {heal_amount} HP! (Cost: 15 PP)")
    elif heal_type == "rejuvenate":
        if self.pp >= 25:
            heal_amount = random.randint(30, 50)
            self.health += heal_amount
            if self.health > self.max_health: self.health = self.max_health
            self.pp -= 25
            print(
                colorama.Back.YELLOW + colorama.Fore.BLACK + f"{self.name} performs a Rejuvenate Heal for {heal_amount} HP! (Cost: 25 PP)")
    elif heal_type == "ultimate_heal":
        if self.pp >= 40:
            heal_amount = random.randint(40, 60)
            self.health += heal_amount
            if self.health > self.max_health: self.health = self.max_health
            self.pp -= 40
            print(
                colorama.Back.YELLOW + colorama.Fore.BLACK + f"{self.name} performs an Ultimate Heal for {heal_amount} HP! (Cost: 40 PP)")

#Copy For others in next Update
def shield(self, shield_type):
    shield_costs = {"light": 20, "medium": 30, "heavy": 50, "reflective": 40}
    shield_values = {"light": 10, "medium": 20, "heavy": 40, "reflective": 30}

    if shield_type in shield_costs:
        cost = shield_costs[shield_type]
        if self.pp >= cost:
            self.pp -= cost
            self.shield_points += shield_values[shield_type]
            print(
                colorama.Fore.BLACK + f"{colorama.Back.YELLOW+self.name} activates a {shield_type.capitalize()} Gaining {shield_values[shield_type]} Shield Points! (Cost: {cost} PP)")
        else:
            print(f"{self.name} doesn't have enough PP for {shield_type.capitalize()} Shield!")
