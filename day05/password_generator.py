import random

final_password = []

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
for i in range(nr_letters):
    final_password += random.choice(letters)

nr_symbols = int(input(f"How many symbols would you like?\n"))
for i in range(nr_symbols):
    final_password += random.choice(symbols)

nr_numbers = int(input(f"How many numbers would you like?\n"))
for i in range(nr_numbers):
    final_password += random.choice(numbers)

random.shuffle(final_password)
password = "".join(final_password)
print(f"your password is: {password}")
























#The Gauss Challenge (Add all numbers from 1 to 100)
# sum_of_numbers = 0

# for number in range(1, 101):
#     sum_of_numbers += number
# print(sum_of_numbers)
    


# student_scores = [150, 200, 250, 300, 350, 400, 450, 500]

# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score 
# #Removing indent from print statement lets the loop run fully before printing
# print(max_score)




# fruits = ["Apple", "Banana", "Cherry"] 
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
# print(fruits)



