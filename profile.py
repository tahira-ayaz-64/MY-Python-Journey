
# Get user information
name = input("Enter your name: ")
age = int(input("Enter your age: "))
favourite_number = int(input("Enter your favourite number: "))

# Calculate birth year and double number
birth_year = 2026 - age
double_number = favourite_number * 2

# Display friendly messages using f-strings
print(f"Hello {name}! Welcome to Python.")
print(f"You are {age} years old.")
print(f"Your approximate birth year is {birth_year}.")
print(f"Your favourite number is {favourite_number}.")
print(f"Double your favourite number is {double_number}.")
print("Keep learning and enjoy coding!")
