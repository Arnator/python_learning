for value in range(1,21):
    print (value)
numbers = list(range(1,1000001))
print ("\n\tThat was a printed list of a range using the 'for' loop. Next I gather the sum, min and max values of that given looped range")
print (sum(numbers))
print (min(numbers))
print (max(numbers))
print("Looping for even numbers requires the first 'int' even, if odd it will loop for odd numbers.")
even_numbers = list(range(2,21,2))
print ("\nEven number:")
for even_number in even_numbers:
    print (even_number)
print ("\nTrying to go for multiples of 3 here. not working out so far!")
for value in range(3,31,3):
    print (value)
print ("\ntyring to go for third to the power of numbers in 1-10")

thirds = []
for value in range(1,11):
    thirds.append(value**3)
print (thirds)
print ("\n\tDONE! must define list as [] before using for value in range command, then an .append for the desired value must be applied after the loop")

thirds = [value**3 for value in range(1,20)]
print (thirds)
