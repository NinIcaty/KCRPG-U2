import random
import colorama
import ClassCharechter
import FunctionMoveControllers
colorama.init(autoreset=True)


def main():
    player1_name = input("Enter Player 1's name: ")
    print("Classes are:")
    print("1. Mage")
    print("2. Warrior")
    print("3. Rogue")

    while True:
        try:
            char_choice = int(input("Choose a class (use  numbers) (1-3): "))
            # test/god mode
            # if char_choice == 789123 :char_type = "god"
            # Remember to remove test/god mode
            if 1 <= char_choice <= 5:
                char_types = ["Mage", "Warrior", "Rogue", "god"]
                player1_type = char_types[char_choice - 1]
                break
            else:
                print("Invalid choice! Please choose a valid number.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    player1      = ClassCharechter.Character(player1_name, 1, 100, 20, 75, 5, 1,0,player1_type)


    player2_name = input("Enter Player 2's name: ")
    print("Classes are:")
    print("1. Mage")
    print("2. Warrior")
    print("3. Rogue")
    while True:
        try:
            char_choice = int(input("Choose a class (use  numbers) (1-3): "))
            # test/god mode
            # if char_choice == 789123 :char_type = "god"
            # Remember to remove test/god mode
            if 1 <= char_choice <= 5:
                char_types = ["Mage", "Warrior", "Rogue", "god"]
                player2_type  = char_types[char_choice - 1]
                break
            else:
                print("Invalid choice! Please choose a valid number.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    player2 =  ClassCharechter.Character(player2_name, 1, 100, 20, 75, 5, 1,0,player2_type)

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
