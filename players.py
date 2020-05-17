players = ['charles', 'martina', 'michael', 'florence', 'eli']
print (players)
print ("\n\tWE ARE SLICING INDEXES MY FRIENDS AND TAKING OUT OF THE LIST ABOVE")
print(players[0:3])
print(players[1:4])
print("\n Omitting the first = starting at the begining of the list.")
print(players[:4])
print("\n Omitting the second = going to the end from the desired start point ie: print(players)[2:]")
print(players[2:])
print("\nhere we are going to do some looping through a slice")

print("here are the first three players in a loop:")
for player in players[:3]:
    print (player.title())
print("\n\tCOPYING lists in multiple variables")
my_foods = ['pizza', 'tofu', 'indian', 'vietnames', 'carrot cake']
friends_foods = my_foods[:]
print ("My favorite foods are:")
my_foods.append('cannoli')
friends_foods.append('ice cream')
print (my_foods)


print("\nMy friend's favorite foods are:")
print(friends_foods)
