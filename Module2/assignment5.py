#Requirements:
#The program should prompt the user with "Enter talents:"
#The program should prompt the user with "Enter pounds:"
#The program should prompt the user with "Enter lots:"
#The program should calculate the weight in grams from the given values
#The program should convert the grams to kilograms and grams
#The program should output "The weight in modern units:"
#The program should output the kilograms and grams in the form "[kilograms] kilograms and [grams] grams."
#Store the talents in a variable called 'talents'
#Store the pounds in a variable called 'pounds'
#Store the lots in a variable called 'lots'
#Store the total weight in grams in a variable called 'total_grams'
#Store the kilograms in a variable called 'kilograms'
#Store the remaining grams in a variable called 'remaining_grams'

talents_str = input("Enter talents: ")
pounds_str = input("Enter pounds: ")
lots_str = input("Enter lots: ")

talents = int(talents_str)
pounds = int(pounds_str)
lots = int(lots_str)

#Convert talents -> pounds -> lots -> grams

total_grams = (talents*20*32*13.3)+(pounds*32*13.3)+(lots*13.3)

kilograms = int(total_grams // 1000)
remaining_grams = int(total_grams % 1000)

print("The weight in modern units:")
print(kilograms, "kilograms and", remaining_grams, "grams.")