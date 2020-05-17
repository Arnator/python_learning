motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)
#append will add at the end of the list
motorcycles.append('ducati')
print (motorcycles)
#insert allows for specific placement within the list
motorcycles.insert(1, 'ninja')
print (motorcycles)
#removing objects from lists at certain positions
del motorcycles[2]
print (motorcycles)
#poping removes items from lists but stores them in variables. Can use specific positions
popped_motorcycle = motorcycles.pop(1)
print (motorcycles)
print (popped_motorcycle)
last_owned = motorcycles.pop(0)
print("The last motorcycle i owned was a " + last_owned.title() + ".")
#All values that have been popped are no longer within the list of motorcycles, and are now stored in variables
print (motorcycles)

cars = ['Mercedes', 'Ford', 'GMC', 'Subaru', 'Dodge', 'Mercedes']
print (cars)
#Example of the remove function, must specify string value
spendy = 'Mercedes'
cars.remove(spendy)
print (cars)
print ("\nA " + spendy.title() + " is too expensive for me.")
