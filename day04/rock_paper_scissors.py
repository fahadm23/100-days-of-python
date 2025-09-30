import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

Computer = random.randint(0, 2)

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors?\n"))

print(f"Computer chose {Computer}")

if choice == Computer:
    print("It's a tie")
if choice == 0 and Computer == 1:
    print("You lose, Paper beats Rock")
if choice == 0 and Computer == 2:
    print("You win, Rock beats Scissors")
if choice == 1 and Computer == 0:
    print("You win, Paper beats Rock")
if choice == 1 and Computer == 2:
    print("You lose, Scissors beats Paper")
if choice == 2 and Computer == 0:
    print("You lose, Scissors beats Rock")
if choice == 2 and Computer == 1:
    print("You win, Scissors beats Paper")















# NESTED LISTS

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen[1][2])



#HEADS or TAILS

# random_number = random.randint(1, 2)

# print(random_number)
# if random_number <= 1:
#     print("Heads")
# elif random_number > 1:
#     print("Tails")
