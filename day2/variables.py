# Day 2: 30 Days of python programming

# Level 1 Exercises:

 
first_name = 'Nicolas'

last_name = 'Zavala'


full_name = first_name + ' ' + last_name


country = 'Mexico'


city = 'Aguascalientes'


age = 18


year = 2025


is_married = True


is_true = True


is_light_on = False


street, postal_code, is_student = 'Katu 1', '00100', False

print("--- Level 1 Variables ---")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Full Name: {full_name}")
print(f"Country: {country}")
print(f"City: {city}")
print(f"Age: {age}")
print(f"Year: {year}")
print(f"Is Married: {is_married}")
print(f"Is True: {is_true}")
print(f"Is Light On: {is_light_on}")
print(f"Street: {street}, Postal Code: {postal_code}, Is Student: {is_student}")


# Level 2 Exercises:

print("\n--- Level 2 Checks and Operations ---")


print(f"\nData type of first_name: {type(first_name)}")
print(f"Data type of last_name: {type(last_name)}")
print(f"Data type of full_name: {type(full_name)}")
print(f"Data type of country: {type(country)}")
print(f"Data type of city: {type(city)}")
print(f"Data type of age: {type(age)}")
print(f"Data type of year: {type(year)}")
print(f"Data type of is_married: {type(is_married)}")
print(f"Data type of is_true: {type(is_true)}")
print(f"Data type of is_light_on: {type(is_light_on)}")
print(f"Data type of street: {type(street)}")
print(f"Data type of postal_code: {type(postal_code)}")
print(f"Data type of is_student: {type(is_student)}")


first_name_length = len(first_name)
print(f"\nLength of first name '{first_name}': {first_name_length}")


last_name_length = len(last_name)
print(f"Length of last name '{last_name}': {last_name_length}")
if first_name_length > last_name_length:
    print("First name is longer than last name.")
elif first_name_length < last_name_length:
    print("Last name is longer than first name.")
else:
    print("First name and last name have the same length.")


num_one = 5
num_two = 4


total = num_one + num_two
print(f"\n{num_one} + {num_two} = {total}")


diff = num_one - num_two
print(f"{num_one} - {num_two} = {diff}")


product = num_one * num_two
print(f"{num_one} * {num_two} = {product}")


division = num_one / num_two
print(f"{num_one} / {num_two} = {division}")


remainder = num_two % num_one
print(f"{num_two} % {num_one} = {remainder}")


exp = num_one ** num_two
print(f"{num_one} ** {num_two} = {exp}")


floor_division = num_one // num_two
print(f"{num_one} // {num_two} = {floor_division}")


radius = 30
import math 
area_of_circle = math.pi * (radius ** 2)
print(f"\nWith radius = {radius}m:")
print(f"Area of circle: {area_of_circle:.2f} square meters") 


circum_of_circle = 2 * math.pi * radius
print(f"Circumference of circle: {circum_of_circle:.2f} meters") # Formatted to 2 decimal places

print("\n--- Circle Area from User Input ---")
try:
    user_radius_str = input("Enter the radius of a circle (in meters): ")
    user_radius = float(user_radius_str)
    user_area_of_circle = math.pi * (user_radius ** 2)
    print(f"Area of circle with user-defined radius {user_radius}m: {user_area_of_circle:.2f} square meters")
except ValueError:
    print("Invalid input for radius. Please enter a number.")



print("\n--- Personal Information from User Input ---")
user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_country = input("Enter your country: ")
try:
    user_age_str = input("Enter your age: ")
    user_age = int(user_age_str)
    print("\n--- User Details ---")
    print(f"Your Name: {user_first_name} {user_last_name}")
    print(f"From: {user_country}")
    print(f"Age: {user_age}")
except ValueError:
    print("Invalid input for age. Please enter a whole number.")




