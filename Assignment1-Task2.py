# Problem Statement: Write a Python program that:
#1.  Takes a user's first name and last name as input.
#2.  Concatenates the first name and last name into a full name.
#3.  Prints a personalized greeting message using the full name.


# Taking input from the user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenating first name and last name
full_name = first_name + " " + last_name

# Displaying the greeting message
print(f"\nHello, {full_name}! Welcome to the Python program.")
