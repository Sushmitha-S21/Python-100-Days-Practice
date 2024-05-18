# easy level
import random
print("Welcome to my Password Generator!")

user_letters = int(input("How many letters of password do you want? \n"))
user_symbols = int(input("How many symbols do you want? \n"))
user_numbers = int(input("How many numbers do you want? \n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# password = "" #when we have it as a string it comes in the order we have specified

# for char in range(1, user_letters + 1):
#     # !used to find random item from the list provided in the list mention in the ()
#     password += random.choice(letters)

# for char in range(1, user_symbols + 1):
#     # !used to find random item from the list provided in the list mention in the ()
#     password += random.choice(symbols)

# for char in range(1, user_numbers + 1):
#     # !used to find random item from the list provided in the list mention in the ()
#     password += random.choice(numbers)

# print(password)

# *hard level

password_list = []  # if we give it as a list, we can shuffle the list to generate random password

for char in range(1, user_letters + 1):
    # !used to find random item from the list provided in the list mention in the ()
    password_list.append(random.choice(letters))

for char in range(1, user_symbols + 1):
    # !used to find random item from the list provided in the list mention in the ()
    password_list.append(random.choice(symbols))
    

for char in range(1, user_numbers + 1):
    # !used to find random item from the list provided in the list mention in the ()
    password_list.append(random.choice(numbers))

print(random.shuffle(password_list))

password = ""
for char in password_list:
    password += char
    
print(f"Your password is: {password}")
