shop_name = "coffee shop"
drinks_sold_number = 120
price_per_drink = 3
pastries_sold_number = 80
price_per_pastry = 4
drink_revenue = drinks_sold_number * price_per_drink
pastry_revenue = pastries_sold_number * price_per_pastry
total_revenue = drink_revenue + pastry_revenue
with open("result.txt", "w") as f:
    f.write(shop_name + " sales\n")
    f.write("Total revenue: $" + str(total_revenue) + "\n")
with open("result.txt", "r") as f:
    print(f.read())
if total_revenue<500:
    print("Revenue did not meet the target")
else:
    print("Revenue target achieved")
print("Drink revenue: $" + str(drink_revenue))
print("Pastry revenue: $" + str(pastry_revenue))
if drink_revenue> pastry_revenue:
    print("Drinks contribute more than pastries")
elif drink_revenue==pastry_revenue:
    print("The contributions of beverages and pastries are the same.")
else:
    print("Pastries contribute more than drinks")

