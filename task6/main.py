import game

krakivska = game.Street("Krakivska")
krakivska.set_description("A street with a lot of shops, located in the center of Lviv")

stryyska = game.Street("Stryyska")
stryyska.set_description("A large and long street with a lot of modern buildings")

kozelnytska = game.Street("Kozelnytska")
kozelnytska.set_description("A street where the best university is located")

franka = game.Street("Franka")
franka.set_description("A street named after famous Ukrainian poet Ivan Franko")

rynok_square = game.Street("Rynok Square")
rynok_square.set_description("A central square of Lviv")
kozelnytska.link_street(stryyska, "west")
stryyska.link_street(kozelnytska, "east")
kozelnytska.link_street(franka, "north")
franka.link_street(kozelnytska, "south")
franka.link_street(rynok_square, "north")
rynok_square.link_street(franka, "south")
rynok_square.link_street(krakivska, "north")
krakivska.link_street(rynok_square, "south")

lotr = game.Enemy("Lotr", "Bad guy who wants to rob you")
lotr.set_conversation("Give me your money!")
lotr.set_weakness("pistol")
franka.set_character(lotr)

pistol = game.Item("pistol")
pistol.set_description("A really great vintage pistol")
kozelnytska.set_item(pistol)

batyar = game.Friend("Batyar", "A good but slightly drunk guy who can talk but won't fight")
batyar.set_conversation("My friend! You got something to drink?")
franka.set_character(batyar)

zbuy = game.Enemy("Zbuy", "A mafiozo who will try to kill you")
zbuy.set_conversation("Nothing in this world worths more than la familia")
zbuy.set_weakness('pistol')
stryyska.set_character(zbuy)

kavaler = game.Enemy("Kavaler", "A Kazanova guy who will steal your girlfriend")
kavaler.set_conversation("Give me your girlfriend and your wallet!")
kavaler.set_weakness("rum")
rum = game.Item('rum')
rum.set_description('bottle of rum')
rynok_square.set_item(rum)

laydak = game.Boss("Laydak",
                    "Boss of this game, if you want to fight him you gonna need a special weapon")
laydak.set_weakness("coin")
krakivska.set_character(laydak)
coin = game.Item("coin")
coin.set_description("Desire of laidak, \
if you use it against him he will surrender and set you free!")
rynok_square.set_item(coin)


current_street = kozelnytska
backpack = []


dead = False
# print(kitchen.linked_rooms)

while dead == False:

    print("\n")
    current_street.get_details()

    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_street.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_street = current_street.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:
                if inhabitant.fight(fight_with):
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_street.character = None
                    if laydak.get_defeated():
                        print("Congratulations, you have vanquished the enemy!!!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_street.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)
