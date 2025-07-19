import random
import ClassCharechter
import FunctionMoveControllers
import colorama
import math
colorama.init(autoreset=True)

savedcharecter = ClassCharechter.saved_chatacters

def create_custom_character(player_name):
    total_sp = 100
    print("\n--- Create Your Custom Character ---")
    print("You have 100 Skill Points (SP) to distribute.")
    print("Costs:")
    print(" - 4 HP = 1 SP")
    print(" - 2 PP = 1 SP")
    print(" - 1 Attack Power = 1 SP")
    print(" - 1 Charge Use = 2 SP")

    while True:
        try:
            print(colorama.Fore.YELLOW+f"\nSP Remaining: {total_sp}")
            hp = int(input("Enter HP (multiple of 4): "))
            hp_sp = math.floor(hp // 4)

            print(colorama.Fore.YELLOW+f"SP Remaining: {total_sp - hp_sp}")
            pp = int(input("Enter PP (multiple of 2): "))
            pp_sp = math.floor(pp // 2)

            print(colorama.Fore.YELLOW+f"SP Remaining: {total_sp - hp_sp - pp_sp}")
            attack = int(input("Enter Attack Power: "))
            attack_sp = math.floor(attack)

            print(colorama.Fore.YELLOW+"SP Remaining: {total_sp - hp_sp - pp_sp - attack_sp}")
            charge_uses = int(input("Enter Charge Amount (Uses): "))
            charge_sp = math.floor(charge_uses * 2)

            total_used = hp_sp + pp_sp + attack_sp + charge_sp
            if total_used > total_sp:
                print(colorama.Fore.RED + f"\n Too many points used! You used {total_used} SP, but only have {total_sp}.")
            else:
                print(colorama.Fore.GREEN +f"\nCustom character created with {total_used} SP used and {total_sp - total_used} SP remaining.")
                break
        except ValueError:
            print(" Invalid input! Please enter integers only.")

    max_health = hp
    charge_pp_power = 5  # Default fixed charge power for custom characters
    return ClassCharechter.Character(player_name, hp, max_health, attack, pp, charge_pp_power, charge_uses, 0, "custom")

def main():
    player_name = input("Enter your character's name: ")

    player = None
    char_type = None

    while True:
        try:
            print("Choose your class:")
            for idx, cls in enumerate(savedcharecter, 1):
                print(f"{idx}. {cls}")
            print(f"{len(savedcharecter) + 1}. Create Custom Character")

            char_choice = int(input("Enter your choice (number): "))

            if 1 <= char_choice <= len(savedcharecter):
                char_type = savedcharecter[char_choice - 1]
                player = ClassCharechter.Character(player_name, 1, 100, 20, 75, 5, 1, 0, char_type)
                break
            elif char_choice == len(savedcharecter) + 1:
                player = create_custom_character(player_name)
                char_type = "custom"
                break
            else:
                print("Invalid choice! Please try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    print(f"Unknown: {player.name}, you are here at WGUOABATGOAT's HQ to prove yourself to the elite Villains of the Council of Villainy.")
    input(colorama.Fore.GREEN+"Press ENTER to continue")

    print("\nUnknown: You must defeat Asher 'Awesomeness', Biochemist, and the leader of GHA, Anaconda!")
    input(colorama.Fore.GREEN+"Press ENTER to deploy")

    heros = [
        ClassCharechter.Character("Asher", 100, 1, 20, 75, 5, 1,0,"asher_hero"),
        ClassCharechter.Character("Biochemist", 120, 1, 25, 80, 6, 1,0,"biochemistry_hero"),
        ClassCharechter.Character("Anaminion", 100, 1, 22, 75, 5, 1,0,"anaminion"),
        ClassCharechter.Character("Anaconda", 100, 1, 22, 75, 5, 1,0,"anaconda"),
        ClassCharechter.Character("Sane Scientist", 120, 1, 25, 80, 6, 1,0,"biochemistry_hero"),
        ClassCharechter.Character("Anaminion 2", 100, 1, 22, 75, 5, 1,0,"anaminion"),
        ClassCharechter.Character("Anaconda", 100, 1, 22, 75, 5, 1,0,"anaconda2"),
    ]

    potions = ["HP Potion", "PP Potion", "Attack Potion", "Shield Potion"]
    for hero in heros:
        player.potions = (random.choice(potions))
        print(f"\nYou received a {player.potions[0]}!")

    for hero in heros:
        while player.is_alive() and hero.is_alive():
            print("\n\n" + colorama.Back.RED + colorama.Fore.BLACK + f"{hero.name}'s Health: {hero.health}, Shield: {hero.shield_points}, PP: {hero.pp}, Charge Uses: {hero.charge_uses}")
            print(colorama.Back.BLUE + colorama.Fore.BLACK + f"{player.name}'s Health: {player.health}, Shield: {player.shield_points}, PP: {player.pp}, Charge Uses: {player.charge_uses}")

            FunctionMoveControllers.action_controller_main(player, hero)
            if hero.is_alive():
                hero.ai_action(player)

            if hero.health <= 0:
                print("\n\n\n\nYou have Defeated " + str(hero.name))
                print("You have regained your strength")

                player.pp += 50 + player.attack_power
                player.health += 50
                player.charge_uses += 5
                if player.health > player.max_health:
                    player.health = player.max_health

                if hero.name == "Biochemist":
                    print("Anaconda: This will be fast, surrender now or DIE.")
                    print("Unknown gives you an Ultimate Shield with 60 Shield Points!")
                    player.shield_points += 60
                    input(colorama.Fore.GREEN + "Press ENTER to start")
                    player.pp += 50 + player.attack_power * 3
                elif hero.name == "Anaminion 2":
                    print("Anaconda: Ha! You thought you had defeated me!")

    if player.is_alive():
        print("You have proved yourself to the Council of Villainy. You are now truly a villain.")
    else:
        print("You have been defeated.")

if __name__ == "__main__":
    main()
