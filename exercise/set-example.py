games = {"Monopoly", "Chess", "Cluedo"}
print(games)

games.add("Dominion")
print(games)

games.remove("Chess")
print(games)

games.add("Cluedo")
print(games)

#creates a cleaner look
for g in games:
    print(g)

#empty set is created with empty set = set()