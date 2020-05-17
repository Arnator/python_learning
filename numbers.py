print (2 * 4)
print (64 / 8)
print (4 + 4)
print (20 - 12)
#loops within numbers using the RANGE function within the 'for' loop.
for value in range(1,51):
    print (value)

numbers = list(range(1,11))
print (numbers)
even_numbers = list(range(2,11,2))
print (even_numbers)
#Creating a list and assigning value in a range for the lists
squares = []
for value in range(1,11):
    squares.append(value**2)

print (squares)
print(sum(squares))
print(max(squares))
#boutta get into list compressions
squares = [value**2 for value in range(1,11)]
print (squares)
