# Choose your own adventure game - you pick where you wanna go - point of this project is for the user to pick a bunch of different choices which will create a story for them.

name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirtroad, it has come to an end and you can go left or right. Which way would like to go? (left / right) ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it  or swin across. Type WALK to walk around it and SWIM to swim across: ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator")
    
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost your game.")

    else:
        print("Not a vaild option - you lose!")


elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross / back) ").lower()

    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (yes / no) ").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold and food enough to continue your journey without trouble! - YOU WIN!")
        elif answer == "no":
            print("You ignore the stranger and continue your travels... you fall ill quickly after passing the stranger and die - you lose the game.")
        else:
            print("Not a vaild option - you lose!")

    elif answer == "back":
        print("You go back to the main road and are killed by bandits, you lose the game.")
    else:
        print("Not a vaild option - you lose!")

else:
    print("Not a vaild option - you lose!")

print("Thanks for playing", name)