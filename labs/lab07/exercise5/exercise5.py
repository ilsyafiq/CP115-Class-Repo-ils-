# Imports personal_data.py and displays the information using f-strings

import personal_data

print("=== Personal Data ===")
print(f"Student Name: {personal_data.full_name}")
print(f"Age: {personal_data.age}")
print(f"Height: {personal_data.height_cm} cm")
print(f"Weight: {personal_data.weight_kg} kg")
print(f"Phone Number: {personal_data.phone_number}")
print(f"Email: {personal_data.email}")

# String operations
print("\nString Operations:")
print(f"Full Name (Upper): {personal_data.full_name_upper}")
print(f"Full Name Length: {personal_data.full_name_length}")
print(f"City (Upper): {personal_data.city_upper}")

# Address information section
print("\nAddress Information:")
print(f"Full Address: {personal_data.full_address}")