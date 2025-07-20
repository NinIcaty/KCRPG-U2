import random
import colorama
import ClassCharechter
import FunctionMoveControllers
colorama.init(autoreset=True)
savedcharecter = ClassCharechter.saved_chatacters
import math
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

    max_health = hp * 1.5
    charge_pp_power = charge_uses/2  # Default fixed charge power for custom characters
    return ClassCharechter.Character(player_name, hp, max_health, attack, pp, charge_pp_power, charge_uses, 0, "custom")


def main():
    player1_name = input("Enter Player 1's name: ")
    print("Classes are:")
    print("1. Mage")
    print("2. Warrior")
    print("3. Rogue")
    print("4. Custom Charachter")
    while True:
        try:
            char_choice = int(input("Choose a class (use  numbers) (1-4): "))
            # test/god mode
            # if char_choice == 789123 :char_type = "god"
            # Remember to remove test/god mode
            if 1 <= char_choice <= len(savedcharecter):
                player1_type = savedcharecter[char_choice - 1]
                player1 = ClassCharechter.Character(player1_name, 1, 100, 20, 75, 5, 1, 0, player1_type)
                break
            elif char_choice == len(savedcharecter) + 1:
                player1 = create_custom_character(player1_name)
                player1_type = "custom"
                break
            else:
                print("Invalid choice! Please choose a valid number.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    #player1      = ClassCharechter.Character(player1_name, 1, 100, 20, 75, 5, 1,0,player1_type)


    player2_name = input("Enter Player 2's name: ")
    print("Classes are:")
    print("1. Mage")
    print("2. Warrior")
    print("3. Rogue")
    print("4. Custom Charachter")
    while True:
        try:
            char_choice = int(input("Choose a class (use  numbers) (1-3): "))
            # test/god mode
            # if char_choice == 789123 :char_type = "god"
            # Remember to remove test/god mode
            if 1 <= char_choice <= len(savedcharecter):
                char_type = savedcharecter[char_choice - 1]
                player2 = ClassCharechter.Character(player2_name, 1, 100, 20, 75, 5, 1, 0, char_type)
                break
            elif char_choice == len(savedcharecter) + 1:
                player2 = create_custom_character(player2_name)
                player2_type = "custom"
                break
            else:
                print("Invalid choice! Please choose a valid number.")
        except ValueError:
            print("Invalid input! Please enter a number.")

#    player2 =  ClassCharechter.Character(player2_name, 1, 100, 20, 75, 5, 1,0,player2_type)

    print(f"\nWelcome to the RPG: {player1.name} ({player1.char_type}) vs {player2.name} ({player2.char_type})!")

    while True:
        # Player 1's turn
        if player1.is_alive and player2.is_alive == False:
            print(f"{player1.name} Won the game!")
            break
        elif player2.is_alive and player1.is_alive == False:
            print(f"{player2.name} Won the game!")
            break
        else:
            print(f'{player1.name}\'s turn')
            print(
                "\n\n" + colorama.Back.RED + colorama.Fore.BLACK + f"{player1.name}'s Health: {player1.health},Shield Points: {player1.shield_points}, PP: {player1.pp}, Charge Uses: {player1.charge_uses}")
            print(
                colorama.Back.BLUE + colorama.Fore.BLACK + f"{player2.name}'s Health: {player2.health},Shield Points: {player2.shield_points} PP: {player2.pp}, Charge Uses: {player2.charge_uses}")
            FunctionMoveControllers.action_controller_main(player1,player2)
            #player 2 turn
            print(
                "\n\n" + colorama.Back.RED + colorama.Fore.BLACK + f"{player1.name}'s Health: {player1.health},Shield Points: {player1.shield_points}, PP: {player1.pp}, Charge Uses: {player1.charge_uses}")
            print(
                colorama.Back.BLUE + colorama.Fore.BLACK + f"{player2.name}'s Health: {player2.health},Shield Points: {player2.shield_points} PP: {player2.pp}, Charge Uses: {player2.charge_uses}")
            print(f"{player2.name}\'s turn")
            FunctionMoveControllers.action_controller_main(player2,player1)
        # Determine winner
        if player1.is_alive() and player2.is_alive() ==False:
            print(f"{player1.name} has defeated {player2.name}!")
            break
        elif player1.is_alive()== False:
            print(f"{player2.name} has defeated {player1.name}!")
            break
if __name__ == "__main__":
    main()
