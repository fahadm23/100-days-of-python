# Treasure Island Game
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

crossroads = input("You are at a crossroads, which direction do you want to go?\nLeft or Right?\n").lower()
# swim_or_wait = input("You have reached a lake but there is no boat. Do you want to wait for a boat or swim?\nSwim or Wait\n")
# which_door = input("Three magical doors have appeared while you were waiting. You must choose between the Red, Blue, or Yellow Doors to find the treasure.\nChoose Red, Blue, or Yellow\n")

if crossroads == "Right":
    print("You fell into a hole. Game Over!")
elif crossroads == "Left": 
    swim_or_wait = input("You have reached a lake but there is no boat. Do you want to wait for a boat or swim?\nSwim or Wait\n").lower()
    if swim_or_wait == "Swim":
        print("You were eaten alive by a Trout while swimming. Game Over!")
    elif swim_or_wait == "Wait":
        which_door = input("Three magical doors have appeared while you were waiting. You must choose between the Red, Blue, or Yellow Doors to find the treasure.\nChoose Red, Blue, or Yellow\n").lower()
        if which_door == "Red":
            print("You entered a door full of fire. You were burned. Game over!")
        elif which_door == "Blue":
            print("You were eaten alive by beasts. Game over!")
        elif which_door == "Yellow":
            print("You found the Treasure!⭐️👑🏆🥇🔑 You Win!")






# PIZZA DELIVERY EXERCISE 🍕

# print("Welcome to my pizza store!")
# size = input("What size pizza do you want? S, M, or L?")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N")
# extra_cheese = input("Do you want extra cheese on your pizza? Y or N")

# bill = 0

# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# elif size == "L":
#     bill = 25

# if pepperoni == "Y" and size == "S":
#         bill += 2
# else:
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1

# print(f"your total bill is {bill}")


# ROLLER COASTER EXERCISE 🎢

# print("Welcome to the rollercoaster!")
# height = (int(input("What is your height in cm? ")))

# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?"))
#     if age >= 45 and age <= 55:
#         bill = 0
#         print("Free ride")
#     elif age > 18:
#         bill = 12
#         print("Adult tickets are $12")
#     elif age > 12:
#         bill = 7
#         print("Youth tickets are $7")
#     else:
#         bill = 5
#         print("Child tickets are $5")
#     photo = input("Do you want a photo taken? type y for yes and n for no.")
#     if photo == "y":
#         bill += 3
#     print(f"your final bill is ${bill}")

# else :
#     print("Sorry you are too short")


