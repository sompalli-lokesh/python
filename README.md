Personal Information Program

This project is a simple Python program that stores personal details, takes user input, validates it, and displays the information in a readable format. The assignment instructions visible in the attached screenshot specify creating a personal_info.py file, defining variables for name, age, city, and hobby, accepting favorite food and favorite color as input, checking for empty input, and displaying the result with f-strings .

 Features:

Stores static information such as name, age, city, and hobby
Accepts user input for favorite food and favorite color.
Validates input to make sure values are not empty.
Displays all information in a clean formatted output using f-strings.
  
File Structure:

personal_info.py — main Python program.
README.md — project description and usage guide.

Requirements

Python 3.x
How to Run
Create a file named personal_info.py.
Copy the Python code into the file.
Open a terminal in the project folder.

Run the program using: python personal_info.py

Example Code:
# Name: Your Name
# Project: Personal Information Program

name = "Your Name"
age = 24
city = "puttur"
hobby = "Reading"

favorite_food = input("Enter your favorite food: ").strip()
favorite_color = input("Enter your favorite color: ").strip()

if not favorite_food:
    favorite_food = "Not provided"

if not favorite_color:
    favorite_color = "Not provided"

print("--- Personal Information ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")

Sample Output:

===================================
     PERSONAL INFORMATION
===================================

Enter your favorite food: Pizza
Enter your favorite color: Blue

====================================
         YOUR INFORMATION
====================================
Name: Your Name
Age: 24
City: Puttur
Hobby: Reading
Favorite Food: Pizza
Favorite Color: Blue
