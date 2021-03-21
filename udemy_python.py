# art = {"Bob", "Jen", "Rolf", "Charlie"}
# science = {"Bob", "Jen", "Adam", "Anne"}
# both = art.intersection(science)
# print(both) """

#print( 5 == 5)
#print( 5 > 5)
#print (5 < 6)


import datetime

x = datetime.datetime.today().weekday()

if x == 0:
    print("Monday")
elif x == 1:
    print("Tuesday")
elif x == 2:
    print("Wednesday")
elif x == 6:
    print("Sunday")
else:
    print("Other day")

day_of_week = input("What day of the week is it today? ").lower()

if day_of_week == "monday":
    print("Have a great start of the week!")
elif day_of_week == "tuesday":
    print("Happy Tuesday!")
elif day_of_week == "friday":
    print("Happy Friyay!")
else:
    print("Almost Friday!")



series_watched = {"Lupin", "Alice in Borderland", "Sweet Home" }
user_serie = input("Enter something you've seen recently: ")

print(user_serie in series_watched)



series_watched = {"Lupin", "Alice in Borderland", "Sweet Home"}
user_serie = input("Enter something you've seen recently: ")

if user_serie in series_watched:
    print(f"I have watched {user_serie} too!")
else:
    print("I haven't watched it yet.")



number = 2 

while True:
    user_input = input("Would you like to play? (Y/n) ")

    if user_input == "n":
        break

    user_number = int(input("Guess my number: "))
    if user_number == number:
        print ("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You missed by one.")
    else:
        print("Sorry, wrong guess.")



grades = [35, 67, 98, 100, 100]
total = sum(grades)
amount = len(grades)

print(total / amount)


friends = ["John", "Sabine", "Patrick", "Sam", "Kate"]
starts_s = [friend for friend in friends if friend.startswith("S")] 

print(friends)
print(starts_s)
print(friends is starts_s)
print("friends: ", id(friends), "starts_s: ", id(starts_s))




 
 