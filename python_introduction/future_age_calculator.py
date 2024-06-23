#Python script that asks the user for their current age and then calculates how old they will be in a specific future year.

current_age = int(input("How old are you? "))

#Let's assume the user will input a valid integer value and Calculate how old the user will be in the year 2050
#We'd also assume the current year is 2023
years_to_add = 2050 - 2023
future_age = current_age + years_to_add
#Printing the user’s age in 2050
print(f"In 2050, you will be {future_age} years old.")
