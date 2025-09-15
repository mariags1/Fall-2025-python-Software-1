#function called get_season
def get_season(month):
    #month number as a parameter and returns the season
    if month in (12, 1, 2):
        return "Winter"
    elif month in (3, 4, 5):
        return "Spring"
    elif month in (6, 7, 8):
        return "Summer"
    elif month in (9, 10, 11):
        return "Autumn"
    else:
        return None

month = int(input("Enter a month number (1-12): "))
season = get_season(month)

if season:
    print(f"You entered: {month}\nThe season is {season}.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")