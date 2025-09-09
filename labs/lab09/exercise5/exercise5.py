main_course = input()
drink = input()
dessert = input()
customer_age = int(input())

# TODO: Your code here

# Chicken
if main_course == "Chicken":
    total_food_cost = 10.00

    if drink == "Soft Drink":
        total_food_cost += 2.00

        if dessert == "Ice Cream":
            total_food_cost += 4.00

        elif dessert == "Cake":
            total_food_cost += 5.00



    elif drink == "Coffee":
        total_food_cost += 3.00

        if dessert == "Ice Cream":
            total_food_cost += 4.00
        
        elif dessert == "Cake":
            total_food_cost += 5.00


# Beef
elif main_course == "Beef":
    total_food_cost = 12.00

    if drink == "Soft Drink":
        total_food_cost += 2.00

        if dessert == "Ice Cream":
            total_food_cost += 4.00

        elif dessert == "Cake":
            total_food_cost += 5.00

    elif drink == "Coffee":
        total_food_cost += 3.00

        if dessert == "Ice Cream":
            total_food_cost += 4.00

        elif dessert == "Cake":
            total_food_cost += 5.00


# Fish
elif main_course == "Fish":
    total_food_cost = 11.00

    if drink == "Soft Drink":
        total_food_cost += 2.00

        if dessert == "Ice Cream":
            total_food_cost += 4.00

        elif dessert == "Cake":
            total_food_cost += 5.00

    elif drink == "Coffee":
        total_food_cost += 3.00

        if dessert == "Ice Cream":
            total_food_cost += 4.00

        elif dessert == "Cake":
            total_food_cost += 5.00


if customer_age < 18:
    final_bill = total_food_cost * 1.1 * 0.9  # 10% service charge and 10% discount

elif customer_age > 60:
    final_bill = total_food_cost * 1.1 * 0.85 # 10% service charge and 15% discount

else:
    final_bill = total_food_cost * 1.1        # 10% service charge

print(f"{final_bill:.2f}")