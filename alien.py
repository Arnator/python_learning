alien_0 = {'color': 'green', 'points':5}
print('alien_0')

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

print (alien_0['color'])
print (alien_0['points'])

new_points = alien_0['points']
print("You've just earned " +str(new_points) + " points!")

print ("\nTHIS IS ALIEN_1")

alien_1 = {'color':'green'}
print("The alien is " + alien_1['color'] + ".")

alien_1['color'] = 'yellow'
print("The alien is now " + alien_1['color'] + ".")
