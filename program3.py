# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Password Protection
# Date:        9/28/2020

# Creates dictionary
user_pass = {}
amount = 0

# Requests user input
amount = int(input("Enter the amount of user:pass combinations you wish to enter: "))
for i in range(amount):
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    user_pass[username] = password

# Asks the user for the username and password they want to access
entered_user = input("Enter the username you wish to access: ")
entered_password = input("Enter the password of {}: ".format(entered_user))

# If the username exists, accesses the dictionary
if entered_user in user_pass:
    returned_password = user_pass[entered_user]
# If it doesn't, keeps asking the user for a username that exists
while entered_user not in user_pass:
    print("That username does not exist!")
    entered_user = input("Enter the username you wish to access: ")
    entered_password = input("Enter the password of {}: ".format(entered_user))
# When the user enters one, does the same as above
returned_password = user_pass[entered_user]

# As long as the user keeps entering the wrong password, starts from the top
while entered_password != returned_password:
    print("Error! Please try again: ")
    entered_user = input("Enter the username you wish to access: ")
    entered_password = input("Enter the password of {}: ".format(entered_user))
    returned_password = user_pass[entered_user]
# Once the user enters a correct username and password combination, user eats the red pill
print("Success! Welcome to the Matrix...")