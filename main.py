from classes.game import Person, bcolors
import random

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 12, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 60},
         {"name": "Cure", "cost": 5, "dmg": 145}]


player = Person(460, 65, 60, 34, magic)
enemy = Person(850, 65, 38, 25, magic)

battle = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while battle:
    print("===========================================\n")
    player.choose_action()
    choice = input("Choose Action: ")
    index = int(choice) - 1
    print("\n")

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(bcolors.OKBLUE + "Attack deals", dmg, "points of damage" + bcolors.ENDC)
    elif index == 1:
        player.choose_magic()
        mchoice = input("Choose Magic: ")
        magic_choice = int(mchoice) - 1
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)
        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + bcolors.BOLD + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        magic_damage = player.generate_spell_damage(magic_choice)

        if spell == "Cure":
            player.heal(magic_damage)
            print(bcolors.OKBLUE + "\n" + spell + " heals for", str(magic_damage), "HP" + bcolors.ENDC)
        else:
            enemy.take_damage(magic_damage)
            print(bcolors.OKBLUE + "\n" + spell + " deals", str(magic_damage), "points of damage" + bcolors.ENDC)

    if enemy.get_mp() >= 12:
        enemy_choice = random.randrange(1, 100)
    else:
        enemy_choice = 1

    if enemy_choice <= 30:
        edmg = enemy.generate_damage()
        player.take_damage(edmg)
        print(bcolors.FAIL + "Enemy strikes for", edmg, "points of damage\n" + bcolors.ENDC)
    else:
        emagic_choice = random.randrange(0, 3)
        espell = enemy.get_spell_name(emagic_choice)
        ecost = enemy.get_spell_mp_cost(emagic_choice)
        ecurrent_mp = enemy.get_mp()

        enemy.reduce_mp(ecost)
        emagic_damage = enemy.generate_spell_damage(emagic_choice)

        if espell == "Cure":
            enemy.heal(emagic_damage)
            print(bcolors.FAIL + "\nEnemy " + spell + " heals for", str(magic_damage), "HP" + bcolors.ENDC)
        else:
            player.take_damage(emagic_damage)
            print(bcolors.FAIL + "\nEnemy " + spell + " deals", str(magic_damage), "points of damage" + bcolors.ENDC)

    print("------------------------------------")

    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC, "\n")
    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC, "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        battle = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        battle = False






