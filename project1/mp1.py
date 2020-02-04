import random

print("-----First Hero-----")
first_hero = input("Enter your hero name: ")

print("-----Second Hero-----")
second_hero = input("Enter your hero name: ")

while second_hero==first_hero:
    print("Hero name has to be different one!")
    second_hero = input("Enter your hero name: ")


players = [first_hero, second_hero]

starter_player = random.choice(players)


players.remove(starter_player)
other_player = players[0]

print("Coin toss result: ", starter_player, " starts first!")

starter_hero_health = 100
other_hero_health = 100

print("------{} attacks first!------".format(starter_player))

while True:

    starter_hero_health_str = str("|" * starter_hero_health)
    other_hero_health_str = str("|" * other_hero_health)

    status = "{} \n  HP[ {} ] {} \n {} \n HP[ {} ] {}".format(starter_player, starter_hero_health,
                                                              starter_hero_health_str, other_player,
                                                              other_hero_health, other_hero_health_str)

    print(status)

    attack_magnitude = int(input("Choose your attack magnitude between 1 and 50: "))
    chance = random.randrange(100)

    while attack_magnitude>50 or attack_magnitude<=0:
        print("attack magnitude must be between 1 and 50!")
        attack_magnitude = int(input("Choose your attack magnitude between 1 and 50: "))

    if chance in range(1, 100-attack_magnitude):
        other_hero_health -= attack_magnitude
        print("attack success")
        print(starter_player, ":", starter_hero_health)
        print(other_player, ":", other_hero_health)
        if other_hero_health<=1:
            break
        print(other_player, " attacks!")

    else:
        print("attack miss!")
        print(starter_player, ":", starter_hero_health)
        print(other_player, ":", other_hero_health)
        print(other_player, " attacks!")

    attack_magnitude = int(input("Choose your attack magnitude between 1 and 50: "))
    chance = random.randrange(100)
    while attack_magnitude>50 or attack_magnitude<=0:
        print("attack magnitude must be between 1 and 50!")
        attack_magnitude = int(input("Choose your attack magnitude between 1 and 50: "))

    if chance in range(1, 100-attack_magnitude):
        starter_hero_health -= attack_magnitude
        print("attack success")
        print(starter_player, ":", starter_hero_health)
        print(other_player, ":", other_hero_health)
        if starter_hero_health<=1:
            break
        print(starter_player, " attacks!")

    else:
        print("attack miss!")
        if starter_hero_health<=1:
            break
        print(starter_player, " attacks!")


if starter_hero_health > 1:
    print("winner is: ", starter_player)
    print("{} \n HP[ {} ] {}".format(other_player, other_hero_health, 0))
    print("{} \n HP[ {} ] {}".format(starter_player, starter_hero_health, starter_hero_health * "|"))
else:
    print("winner is: ", other_player)
    print("{} \n HP[ {} ] {}".format(starter_player, starter_hero_health, 0))
    print("{} \n HP[ {} ] {}".format(other_player, other_hero_health, other_hero_health * "|"))
