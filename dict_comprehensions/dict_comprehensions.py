users = [
    (0, "Bob", "password"),
    (1, "Rolf", "blabla"),
    (2, "Jose", "1234"),
    (3, "username", "fantastic"),

]

user_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = user_mapping[username_input]

if password_input == password:
    print("Your details are correct.")
else: 
    print("Your details are incorrect.")