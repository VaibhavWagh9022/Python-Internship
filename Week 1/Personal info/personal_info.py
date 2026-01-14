# Name - Vaibhav Kushaba Wagh
# project : Personal information manager
print("=" * 40)
print("     Personal information manager")
print("=" * 40)

# static information

# to store name
Name = "Vaibhav Wagh"
# to store age
age_years = 20
# Claculate age in months
age_in_months = age_years * 12

# to store city
city = "Nashik"
# to store hobby
hobby = "Play Games"

# get user input
Favourite_food = ""
while True:
    Favourite_food = input("What is your favourite food : ").strip()
    if not Favourite_food:
        print("please enter your favourite food ")
    else:
        break

print()

Favourite_color = ""

while True:
    Favourite_color = input("What is your favourite color : ").strip()
    if not Favourite_color:
        print("please enter your favourite color ")
    elif not Favourite_color.isalpha():
        print("please enter valid data (no numbers or spaces) ")
    else:
        break

# Display information
print(f"""
================================     
    Here is your information
================================
    Name :{Name}
    Age :{age_years} years ({age_in_months} months)
    City :{city}
    Hobby :{hobby}

    Favourite Food :{Favourite_food}
    Favourite Color :{Favourite_color}
      """)


# Goodbye message
print("-"*40)
print("    😊😊😊😊Thanks you😊😊😊😊")
print("-"*40)
