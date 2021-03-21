#add / change the key  
friend_ages = {"Rolf": 20, "Adam": 30, "Anne": 27}

friend_ages["Rolf"] = 24
friend_ages["Elvis"] = 1

print(friend_ages)


friends = [
    {"name": "Rolf", "age": 24, "pet": "dog"},
    {"name": "Adam", "age": 36, "pet": "dog"},
    {"name": "Anne", "age": 27, "pet": "cat"},
    {"name": "Elvis", "age": 1, "pet": "dog"},
] 

print(friends[3]["name"])

for friend in friends:
    age = friend["age"]
    pet = friend["pet"]
    #print("{} - {}".format(age, pet))
    print(f"{age} - {pet}")
 

student_attendance = {"Rofl": 96, "Bob": 80, "Anne": 100}

for student, attandace in student_attendance.items():
    print(f"{student} : {attandace} %")


if "Bob" in student_attendance:
    print(f"Bob : {student_attendance['Bob']}")
else:
    print(f"Bob is not a student in this class.")

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(student_attendance))
