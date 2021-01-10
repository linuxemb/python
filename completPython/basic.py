## List
# Imagine you've got all your friends in a list, and you want to print it out.
friends = ["Rolf", "Anne", "Charlie"]
print(f"My friends are {friends}.")

# Not the prettiest, so instead you can join your friends using a ",":
friends = ["Rolf", "Anne", "Charlie"]
comma_separated = ", ".join(friends)
print(f"My friends are {comma_separated}.")

grades = [80, 75, 90, 100]
grades = (80, 75, 90, 100)
grades = {80, 75, 90, 100}  # This one, because of no duplicates


total = sum(grades)
length = len(grades)

average = total / length
print(f"average {average}")
##################### Directory
friend_ages = {"rolf": 24, "Adm": 30}
print("=============dirc====")
print(f"Rolf 's age is :{friend_ages['rolf']}")


# -- Lists of dictionaries --
# Imagine you have a program that stores information about your friends.
# This is the perfect place to use a list of dictionaries.
# That way you can store multiple pieces of data about each friend, all in a single variable.

friends = [("Rolf", 24) , ("Adam", 30)]
friend_ages = dict(friends)
print("+++++ dict frineds")
print(friend_ages)



###### zip   #########################

# While that is extremely useful when we have conditionals, sometimes we
# just want to create a dictionary out of two lists or tuples.
# That's when `zip` comes in handy!


# Remember how we can turn a list of lists or tuples into a dictionary?
# `zip(friends, time_since_seen)` returns something like [("Rolf", 3), ("Bob", 7)...]
# We then use `dict()` on that to get a dictionary.
friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]
friends_last_seen = dict(zip(friends, time_since_seen))
print("ZIP++++++")
print(friends_last_seen)




####################### set ##################3
#definng sets
art_fridends1 = {"Rold","Anne"}

## add to set
art_fridends1.add("Jen")
art_fridends1.remove("Anne")

print(f"art_frindes1: {art_fridends1}")
##################### Advabced Set #########33

art_friends = {"Rolf", "Anne", "Jen"}   ## define set
science_friends = {"Jen", "Charlie"}
# -- Difference --
# Gives you members that are in one set but not the other.
art_but_not_science = art_friends.difference(science_friends)
science_but_not_art = science_friends.difference(art_friends)
print(f"art_butnotsicec , {art_but_not_science}")
print(f"science_butnotare, {science_but_not_art}")



# -- Symmetric difference --
# Gives you those members that aren't in both sets
# Order doesn't matter with symmetric_difference

not_in_both = art_friends.symmetric_difference(science_friends)

print(not_in_both)

# -- Intersection --
# Gives you members of both sets

art_and_science = art_friends.intersection(science_friends)
print(art_and_science)

# -- Union --
# Gives you all members of all sets, but of course without duplicates

all_friends = art_friends.union(science_friends)
print(all_friends)

#####################  tuples ####################

short_tuple ="Rolf", "Bob"

## add to tuple
friends =("Rolf", "BoB")
#friends.append("Jen")  ## Wrong it is not changable
print(friends)


######## List #######################
friend1="Rolf"
friends = ["Rolf", "Bob", "Anne"]
print(friends[0])  ## subscript

## len of list
print(len(friends))

## List inside lists---
friends = [["Rolf",24], ["Bob",30], ["Anne",27]]
print(friends[0][1])
print(friends[1][0])
## pime nmumber
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:  # if n is divisible by x, it means it's not a prime number.
            print(f"{n} equals {x} * {n//x}")
            break
    else:  # if n was not divisible by any x, it means it is a prime number.
        print(f"{n} is a prime number.")

#### if else

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break

    print(f"This car is {status}.")
else:
    print("All cars built successfully. No faulty cars!")

######## break and continue ######################3

###Terminates the current iteration and moves onto the next one.

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("======sFound faulty car, skipping...")
        continue

    print(f"=====This car is {status}.")
    print("=====Shipping new car to customer!")




####### iterration over dict

their_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

for name in their_ages:    ### key
    print(name)

for age in their_ages.values():   ## val
    print(age)

### list of list
# -- Destructuring in a loop --
# If you've got a list of lists, such as friend names and ages, you can destructure
# in a loop like this:

friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob", 22)]
for name, age in friends:  # for friend in friends first
    print(f"{name} is {age} years old.")

################################# lambda #####################
print("++++++++++++++++=lambda++++++++++++++++++++")
result=(lambda x,y: x+y)(15,3)
print(result)

#######
def average(sequence):
    return sum(sequence)/ len(sequence)
students =[ {"name": "Rolf", "grades" : (67,89,55,100)},
            {"name": "Bob", "grades": (45,60,44,20)}
            ]
for student in students:
    print("+++++++  Average +++++++++++++++++")
    print(average(student["grades"]))
##### using lambda######
print("+++++++  Lamda Average +++++++++++++++++")
average = lambda  sequence: sum(sequence)/len(sequence)

for student in students:
    print(average(student["grades"]))



    #####===========================
    #
    # avg = lambda seq: sum(seq) / len(seq)
    # total = lambda seq: sum(seq)  # could just be `sum`
    # top = lambda seq: max(seq)  # could just be `max`
    #
    # students = [
    #     {"name": "Rolf", "grades": (67, 90, 95, 100)},
    #     {"name": "Bob", "grades": (56, 78, 80, 90)},
    #     {"name": "Jen", "grades": (98, 90, 95, 99)},
    #     {"name": "Anne", "grades": (100, 100, 95, 100)},
    # ]
    #
    # for student in students:
    #     name = student["name"]
    #     grades = student["grades"]
    #
    #     print(f"Student: {name}")
    #     operation = input("Enter 'average', 'total', or 'top': ")
    #
    #     if operation == "average":   #top
    #         print(avg(grades))
    #     elif operation == "total":
    #         print(total(grades))
    #     elif operation == "top":
    #         print(top(grades))

   ####################### re write using store functin s inside a dictorar just as we do with numbrers
   ## creating a dictinaory of what would be user inpur to the function that we want to run in each case

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

# operations = {
#        "average" : avg,
#        "total"   : total,  #couldb ejust sum
#        "top" :      top,  #coud be just max
#    }

### define opeartoin dic inline


operations = {
    "average": lambda  seq: sum(seq)/len(seq),
    "total": lambda seq: sum(seq),
    "top":   lambda seq: max(seq),    # couldb ejust sum

}
### use 'operation ' dict
for  student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("enter 'average' 'total' or 'top'")

    operation_function = operations[operation]

    print(operation_function(grades))





# class SimpleList:
#     def __init__(self, items):
#         self._items = list(items)
#
#     def add(self, item):
#         self._items.append(item)
#
#     def __getitem__(self, index):
#         return self._items[index]


