# WAP to find a user age is greater than 18 or not?
# New born -> 0, 3 -> age > 0 and age < 4
# kinder - 4, 12 -> (age >= 4) and (age <= 12)
# Teenage -  13 - 17 -> (age >= 13) and (age <= 17)
# Adult - 18 to 60 -> (age >= 18 and age <= 60)
# Old age - 61 to __ -> (age > 60)

# if (age >= 18):
#     print("Age is Greater")
# else:
#     print("Age is smaller")
age = 2
if (age > 0 and age < 4):
    print("New born")
elif ((age >= 4) and (age <= 12)):
    print("Kinder")
elif((age >= 13) and (age <= 17)):
    print("teenage")
elif((age >= 18 and age <= 60)):
    print("adult")
elif((age > 60)):
    print("senior")
else:
    print("Invalid age")
