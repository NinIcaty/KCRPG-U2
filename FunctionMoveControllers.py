import FunctionAction
import colorama
def attack_moves_controller(character,other):
    print("\nAvailable attack moves:")
    move_num = 1
    if character.pp >= 0:
        print(colorama.Fore.RED+f"{move_num}. Basic Attack (Cost: 0 PP)")
        move_num += 1
    if character.pp >= 10:
        print(colorama.Fore.RED+f"{move_num}. Power Attack (Cost: 10 PP)")
        move_num += 1
    if character.pp >= 20:
        print(colorama.Fore.RED+f"{move_num}. Super Attack (Cost: 20 PP)")
        move_num += 1
    if character.pp >= 25:
        print(colorama.Fore.RED+f"{move_num}. Special Attack (Cost: 25 PP)")
        move_num += 1
    if character.pp >= 30:
        print(colorama.Fore.RED+f"{move_num}. Explosive Attack (Cost: 30 PP)")
        move_num += 1
    if character.pp >= 40:
        print(colorama.Fore.RED+f"{move_num}. Frenzy Attack (Cost: 40 PP)")
        move_num += 1
    attack_choice = input("Choose your attack move:(\"exit\" to Exit the menu) ")
    if attack_choice == "1":
        FunctionAction.attack(character,other, "basic")
    elif attack_choice == "2":
        FunctionAction.attack(character,other, "power")
    elif attack_choice == "3":
        FunctionAction.attack(character,other, "super")
    elif attack_choice == "4":
        FunctionAction.attack(character, other, "special")
    elif attack_choice == "5":
        FunctionAction.attack(character,other, "explosive")
    elif attack_choice == "6":
        FunctionAction.attack(character,other, "frenzy")
    elif attack_choice == "exit":
        action_controller_main(character,other)
    else:
        print("Invalid attack choice!")
        attack_moves_controller(character,other)

def heal_moves_controller(character):
    print("\nAvailable heal moves:")
    move_num = 1
    if character.pp >= 5:
        print(colorama.Fore.MAGENTA+f"{move_num}. Light Heal (Cost: 5 PP)")
        move_num += 1
    if character.pp >= 10:
        print(colorama.Fore.MAGENTA+f"{move_num}. Medium Heal (Cost: 10 PP)")
        move_num += 1
    if character.pp >= 15:
        print(colorama.Fore.MAGENTA+f"{move_num}. Heavy Heal (Cost: 15 PP)")
        move_num += 1
    if character.pp >= 25:
        print(colorama.Fore.MAGENTA+f"{move_num}. Rejuvenate Heal (Cost: 25 PP)")
        move_num += 1
    if character.pp >= 40:
        print(colorama.Fore.MAGENTA+f"{move_num}. Ultimate Heal (Cost: 40 PP)")
        move_num += 1
    heal_choice = input("Choose your heal move:(\"exit\" to Exit the menu) ")
    if heal_choice == "1":
        FunctionAction.heal(character,"light")
    elif heal_choice == "2":
        FunctionAction.heal(character,"medium")
    elif heal_choice == "3":
        FunctionAction.heal(character,"heavy")
    elif heal_choice == "4":
        FunctionAction.heal(character,"rejuvenate")
    elif heal_choice == "5":
        FunctionAction.heal(character,"ultimate_heal")
    elif heal_choice == "exit":
        action_controller_main(character,other)
    else:
        print("Invalid heal choice!")
        heal_moves_controller(character)

def shield_moves_controller(character):

    print("\nAvailable shield moves:")
    if character.pp >= 20:
        print(colorama.Fore.CYAN+"1. Light Shield (Cost: 20 PP) Giving 10 Shield Points")
    if character.pp >= 30:
        print(colorama.Fore.CYAN+"2. Medium Shield (Cost: 30 PP) Giving 20 Shield Points")
    if character.pp >= 40:
        print(colorama.Fore.CYAN+"3. Reflective Shield (Cost: 40 PP) Giving 30 Shield Points")
    if character.pp >= 50:
        print(colorama.Fore.CYAN+"4. Heavy Shield (Cost: 50 PP) Giving 40 Shield Points")
    shield_choice = input("Choose your shield move:(\"exit\" to Exit the menu) ")
    if shield_choice == "1":
        FunctionAction.shield(character,"light")
    elif shield_choice == "2":
        FunctionAction.shield(character,"medium")
    elif shield_choice == "3":
        FunctionAction.shield(character,"reflective")
    elif shield_choice == "4":
        FunctionAction.shield(character,"heavy")
    elif shield_choice == "exit":
        action_controller_main(character,other)
    else:
        print("Invalid shield choice!")
        shield_moves_controller(character)
def charge_pp(character):
    if character.charge_uses > 0:
        gained_pp = 25 + character.charge_pp_power
        character.pp += gained_pp
        character.charge_uses -= 1
        print(colorama.Back.YELLOW+ colorama.Fore.BLACK+f"{character.name} charges up for {gained_pp} PP! Uses left: {character.charge_uses}")
def action_controller_main(player,hero):
    print("\nChoose your action:")
    print("1. Attack")
    print("2. Heal")
    print("3. Charge PP")
    print("4. Shield")
    # print("5. Use Potion")

    action = input("Choose an action (1-4): ").strip()

    if action == "1":
        attack_moves_controller(player, hero)
    elif action == "2":
        heal_moves_controller(player)
    elif action == "3":
        charge_pp(player)
    elif action == "4":
        shield_moves_controller(player)
    else:
        print("Invalid action!\nYou Gain 5 PP by resting")
        player.pp += 5