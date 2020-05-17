friends = ['Caleb', 'Matt', 'Brian', 'Sam', 'Luke']
print ("This is the original list:")
print (friends)
#TEMPORARY SORTING function
print ("\nHere is the sorted list")
print (sorted(friends))
print ("\nthe 'sorted' function retains the original list format as seen below")
print (friends)
#REVERSE function
print ("\nThe reverse function reversed the order and only the order, not alphabetically like the sort function [not to be confused with SORTED]")
friends.reverse()
print (friends)
print ("\nReverse is a permanent change however, when used again on another line it will return to the original order")
friends.reverse()
print (friends)
#LENGTH will tally the entire remainders of the lists
print (len(friends))
#LOOPING using the "for" function
print ("\n\tHERE GOES SOME LOOPS! using the 'for' function. Use plurals when naming lists and this function seems to work. Otherwise wtf how does it know.")
for friend in friends:
    print(friend)
#plural list names will help with the for function
for friend in friends:
    print(friend.title() + ", that was super gay")
    print("get her next time bud, go and give ur balls a tug " + friend.title() + ".\n")

print("Thank you for your names, for they have served their purpose")
