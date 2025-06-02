import random
import ClassCharechter
import FunctionMoveControllers
import colorama
colorama.init(autoreset=True)

'''
def get_potion_choice(character):

    print("\nAvailable potions:")
    for i, potion in enumerate(character.potions, 1):
        print(f"{i}: {potion}")

    while True:
        try:
            potion_choice = int(input("Choose your potion (1-{}): ".format(len(character.potions))).strip())
            if 1 <= potion_choice <= len(character.potions):
                return character.potions[potion_choice - 1]
            else:
                print("Invalid choice! Please choose a valid number.")
        except ValueError:
            print("Invalid input! Please enter a number.")

'''
def main():
    player_name = input("Enter your character's name: ")

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
                char_type = char_types[char_choice - 1]
                break
            else:
                print("Invalid choice! Please choose a valid number.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    # player = ClassCharechter.Character(player_name, 100, 20, 75, 5, char_type)
    # hero = ClassCharechter.Character("Asher", 100, 20, 75, 5, "none")
    # hero2 = ClassCharechter.Character("Biochemistry123",100 , 22 ,75,5,"none")
    # hero_boss1 = ClassCharechter.Character("Anaconda",100 , 22 ,75,5,"anaconda_hero")

    # potions = ["HP Potion", "PP Potion", "Attack Potion", "Shield Potion"]
    # hero.potions.append(random.choice(potions))
    # print(f"\nYou received a {hero.potions[0]}!")

    player = ClassCharechter.Character(player_name, 1, 100, 20, 75, 5, 1,0,char_type)
    print(f"Unknown:{player.name} you are here at WGUOABATGOAT(We Gave Up On Acronyms Because All the Good Ones Are Taken)\'s HeadQuarters to prove yourself to the elite Villans of the council of Villany.You must defeat the \"great\" heros of WGUOABATGOAT .")
    input(colorama.Fore.GREEN+"Press ENTER to continue")
    print("\nUnknown:You must defeat Asher \'Awesomeness\' their latest recruite (according to our intel) , The Biochemist(A scientest who messes with life ) and the leader of GHA(Global Hero Organisation) Anaconda a weekling who you can easily defeat")
    print("Remember DO NOT get captured and bad luck to you!")
    jk=input(colorama.Fore.GREEN+"Press ENTER to deploy")
    if jk == "no": print("You pressed enter and thus you shall get deployed")
    heros = [
        ClassCharechter.Character("Asher", 100, 1, 20, 75, 5, 1,0,"asher_hero"),
        ClassCharechter.Character("Biochemist", 120, 1, 25, 80, 6, 1,0,"biochemistry_hero"),
        ClassCharechter.Character("Anaminion", 100, 1, 22, 75, 5, 1,0,"anaminion"),
        ClassCharechter.Character("Anaconda", 100, 1, 22, 75, 5, 1,0,"anaconda"),
       ClassCharechter.Character("Sane Scientist", 120, 1, 25, 80, 6, 1,0,"biochemistry_hero"),
        ClassCharechter.Character("Anaminion 2", 100, 1, 22, 75, 5, 1,0,"anaminion"),
        ClassCharechter.Character("Anaconda", 100, 1, 22, 75, 5, 1,0,"anaconda2"),


    ]
    # Randomly assign a potion at the start
    potions = ["HP Potion", "PP Potion", "Attack Potion", "Shield Potion"]
    # for hero in heros:
    for hero in heros:
        player.potions = (random.choice(potions))
        print(f"\nYou received a {player.potions[0]}!")

    for hero in heros:
        while player.is_alive() and hero.is_alive():

            print("\n\n"+colorama.Back.RED+colorama.Fore.BLACK+f"{hero.name}'s Health: {hero.health},Shield Points: {hero.shield_points}, PP: {hero.pp}, Charge Uses: {hero.charge_uses}")
            print(colorama.Back.BLUE+colorama.Fore.BLACK+f"{player.name}'s Health: {player.health},Shield Points: {player.shield_points} PP: {player.pp}, Charge Uses: {player.charge_uses}")

            FunctionMoveControllers.action_controller_main(player, hero)
            if hero.is_alive():
                hero.ai_action(player)
            if hero.health <= 0:
                print("\n\n\n\nYou have Defeated " + str(hero.name))
                print("You have regained your stregnth")


                player.pp += 50 + player.attack_power
                player.health += 50
                player.charge_uses += 5
                if player.health > player.max_health:player.health = player.max_health
                if hero.name == "Biochemist":
                    print("Anaconda:This will be fast , surrender now and get a shorter sentance if you do not you shall DIE.")
                    print("You burn with rage.")
                    print(f"Unknown:You better defeat her else you shall fail.\n Unknown gives {player.name} an Ultimate Shield with 60 Shield Points")
                    player.shield_points += 60
                    input(colorama.Fore.GREEN+"Press ENTER to start")
                    player.pp += 50 + player.attack_power * 3
                elif hero.char_type == "a   naconda":
                    print("Anaconda:You have NOT killed me !\n  I shall defeat you and the council of Villany!")

                elif hero.name == "Anaminion 2":
                                    print("Anaconda:Ha you thought you had defeated me!\n How foolish of you. ")

    if player.is_alive():
        print("You Have proved yourself to the council of Villany now you truly are a Villan.")
        ClassCharechter.Character
    else:
        print("You have been defeated.")
        return


if __name__ == "__main__":
    main()
