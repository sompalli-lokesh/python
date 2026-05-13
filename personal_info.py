# Personal Information

print("=" * 50)
print("        PERSONAL INFORMATION ")
print("=" * 50)

print("\nPlease tell me about yourself:")
print("-" * 40)

# Static information
name = "Sompalli Lokesh"      # user's name
age = 24                   # user's age in years
city = "Puttur"     # user's city
hobby = "Reading"   # user's hobby

# Get user input
favorite_food = input("What's your favorite food? ").strip()
favorite_color = input("What's your favorite color? ").strip()

# Basic validation
if favorite_food == "":
    favorite_food = "Not provided"

if favorite_color == "":
    favorite_color = "Not provided"

# Enhancement - calculate age in months
age_in_months = age * 12

#  Display information
print("\n" + "=" * 50)
print("             YOUR INFORMATION")
print("=" * 50)

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")

print(f"\nFavorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")

print("\n" + "=" * 50)
print("Goodbye          ")
print("=" * 50)