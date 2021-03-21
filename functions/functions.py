def hello():
    print("Hello!")

hello()

def user_age_in_second():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")

print("Welcome to the age in second program!")
user_age_in_second()

print("Goobye!")

friends = ["Rolf", "Bob"] 

def add_friend():
    friend_name = input("Enter your friend name: ")
    #friends.append(friend_name)
    new_friends = friends + [friend_name]
    print(new_friends)

add_friend()
