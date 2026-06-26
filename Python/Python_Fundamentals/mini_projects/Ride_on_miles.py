# Project 1

user_input = int(input("How far would you like to travell in miles? "))

if user_input < 3:
    print("I suggest Bicycle to your destination")
elif user_input >= 3 and user_input < 300:
    print("I suggest Motor-Cycle to your destination")
else:
    print("I suggest Super-Car to your destination")


# Project 2

print("It cost", 0.51 * 24, "to operate one srever per day")
print("It cost", 0.51 * 24 * 7, "to operate one srever per week")
print("It cost", 0.51 * 24 * 30, "to operate one srever per month")
print(918/(0.51*24), "days I can operate one server with $918")
