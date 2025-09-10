import math
#receives two parameters
def calculate_unit_price(diameter_cm, price_eur):
    #The function calculates and returns the unit price of the pizza per square meter
    diameter_m = diameter_cm / 100
    radius_m = diameter_m / 2
    area_sqm = math.pi * (radius_m ** 2)
    unit_price_sqm = price_eur / area_sqm
    return unit_price_sqm

diameter1_cm = float(input("Enter the diameter of the first pizza (cm): "))
price1_eur = float(input("Enter the price of the first pizza (euros): "))

diameter2_cm = float(input("Enter the diameter of the second pizza (cm): "))
price2_eur = float(input("Enter the price of the second pizza (euros): "))

unit_price1 = calculate_unit_price(diameter1_cm, price1_eur)
unit_price2 = calculate_unit_price(diameter2_cm, price2_eur)

if unit_price1 < unit_price2:
    print(f"Unit price of the first pizza: {unit_price1:.2f} euros/m²")
    print(f"Unit price of the second pizza: {unit_price2:.2f} euros/m²")
    print("The first pizza provides better value for money.")

elif unit_price2 < unit_price1:
    print(f"Unit price of the first pizza: {unit_price1:.2f} euros/m²")
    print(f"Unit price of the second pizza: {unit_price2:.2f} euros/m²")
    print("The second pizza provides better value for money.")

else:
    print("Both pizzas offer the same value for money.")



    
