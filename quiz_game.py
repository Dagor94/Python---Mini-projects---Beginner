
#* Idea behind this "game" is that we ask the user a bunch of questions - everytime they answer correctly we'll add +1 to their score.
#* Then at the end of the program we'll count up their score and and print it out.

print("Welcome to my computer Quiz!")

playing = input("Do you want want to play? [y/n]  ")

if playing.lower() != "y":
    print("Alright, have a nice day!")
    quit()
else:
    print("Okay! Let's play!")
score = 0
questions = 0

answer = input("What does CPU stand for? ")
questions += 1
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
questions += 1
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
questions += 1
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
questions += 1
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You're answered " + str(score) + " out of " + str(questions) + " correctly!")
print("You're answered " + str(score/questions*100) + "% correct")