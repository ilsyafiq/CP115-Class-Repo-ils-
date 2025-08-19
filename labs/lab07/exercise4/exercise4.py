# Imports menu_data.py and displays the information using f-strings

import menu_data

# Welcome message with restaurant name
print(f"Welcome to {menu_data.restaurant_name}!")

# Customer number
print(f"Your customer number is {menu_data.customer_number}.")

# Complete menu with all items
print("=== Menu ===")
print(f" - {menu_data.menu_items[0]}")
print(f" - {menu_data.menu_items[1]}")
print(f" - {menu_data.menu_items[2]}")

# Today's special (based on the random number)
print(f"Today's special is: {menu_data.menu_items[menu_data.daily_special]}")