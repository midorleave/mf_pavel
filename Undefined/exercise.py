# finds slovo vo vete
text = input("Veta: ")
word = input("Slovo: ")

def search(text, word):

   if word in text:
      return "Word found"
   else:
      return "Word not found"


print(search(text, word))


#dýškomat
bill = int(input("Suma účtu: "))

dysko = bill*0.2
print(dysko)


#BMI
user_weight = int(input("Tvoja váha: "))
user_height = float(input("Tvoja výška: "))
w_h = user_weight / (user_height**2)

if w_h < 18.5:
    print("Podváha")
elif 18.5<=w_h<25:
    print("Ideál")
elif 25<=w_h<30:
    print("Nadváha")
else:
    print("Obezita")


#
nums = [1,2,3]
print(nums + [4,5,6])
print(nums*3)


# T/F
words = ["spam", "dogs", "food", "why"]
print("dogs" in words)
print("why" in words)
print("nope" in words)
print(not "spam" in words)
print(not "eggs" in words)


# + !
words = ["hello", "hi", "bye", "good morning"]

for word in words:
    print(word + "!")



#samohlásky check
str = input("Veta: ")
count = 0
sam = "a", "e", "i", "o", "u", "y"
for x in str:
    if x in sam:
        count += 1

print(count)


#
cisla = [2, 3, 4, 5, 6, 7]

for x in cisla:
    if(x%2==1 and x>4):     #delene 2 so zvyskom 1
        print(x)
        #break



import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("Original dicstionary: ", d)

sorted_d = sorted(d.items(), key=operator.itemgetter(1))                   # key:VALUE ig(value index)
print("Dictionary in ascending order by value: ", sorted_d)

sorted_d = sorted(d.items(), key=operator.itemgetter(1),reverse=True)      #T = od najvyssieho, default F
print("Dictionary in descending order by value: ", sorted_d)



from collections import defaultdict

test_points1 = {1: 96, 2: 80, 3: 100}
test_points2 = {3: 55, 5: 40, 6: 66}
test_points3 = {5: 100}
test_points4 = {9: 99, 7: 60, 6: 100}
test_points5 = {7: 27, 8: 80, 3: 100}

dd = defaultdict(list)

for d in (test_points1,test_points2,test_points3,test_points4,test_points5):
    for key, value in d.items():
        dd[key].append(value)                                  # k:v  (key ostava, value scituje)

print(dd)

sorted_points = sorted(test_points1.items(), key=operator.itemgetter(1))        # line 87
print("Points in ascending order: ", sorted_points)

sorted_points = dict(sorted(test_points1.items(), key=operator.itemgetter(1), reverse=True))    # line 90
print("Points in descending order: ", sorted_points)
print(f"{sorted_points}")

for test, points in sorted_points.items():
    print(f"Test: {test} Points: {points}")

test_points0 = {}

for d in (test_points1,test_points2,test_points3,test_points4,test_points5): test_points0.update(d)
print(test_points0)



# bunda zips
keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]

both = dict(zip(keys, values))

for keys, values in both.items():
    print(f"{keys} : {values}")



#merging lists
names = ["john", "paul", "george", "ringo"]
job = ["guitar", "bass", "guitar", "drums"]
status = ["dead", "alive", "dead", "alive"]
grammy = ["one", "two", "three", "four"]
age = [ 73, 63, 63, 85]
persons = []


for n, j, s, g, a in zip(names, job, status, grammy, age):
    person = {"name" : n, "job": j, "status": s, "grammy": g, "age": a}
    persons.append(person)

print(persons)



#merging dictionaries
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


dict3 = {**dict1, **dict2}
print(dict3)


sampleDict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}

print(sampleDict["class"]["student"]["marks"]["history"])       # znamka(body) z history


employees = ['Kelly', 'Emma', 'John', "Alice"]
defaults = {"designation": 'Application Developer', "salary": 8000}

added = dict.fromkeys(employees, defaults)
print(added)
