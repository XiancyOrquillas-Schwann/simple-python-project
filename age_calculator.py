# Age Calculator
# This program calculates the user's age

# Ask the user for their name
name = input("Enter your name: ")

# Ask the user for birth year
birth_year = int(input("Enter your birth year: "))

# Ask the user for the current year
current_year = int(input("Enter the current year: "))

# Calculate the age
age = current_year - birth_year

# Display the result
print("\nHello,", name)
print("Your age is:", age, "years old.")
