alien_2 = {'color': 'green', 'points' : 5}
print alien_2

alien_2['x_position'] = 0
alien_2['y_position'] = 25
print(alien_2)

print("\n\tDIFFERENT ALIEN")
alien_3 = {}

alien_3['color'] = 'black'
alien_3['points'] = 25

print(alien_3)

alien_3 = {'color': 'green'}
print ("the alien is " + alien_3['color'] + ".")

alien_3['color'] = 'yellow'
print("the alien is " +alien_3['color'] + ".")

alien_3 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print ("Original x-position: " + str (alien_3['x_position']))

#Move the alien to the right
#determine how far to move the alien based on its current speed

if alien_3['speed'] == 'slow':
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3
# the new position is the old position plus the x_increment
alien_3['x_position'] = alien_3['x_position'] + x_increment

print "Now x-position: " + str(alien_3['x_position'])

alien_3['speed'] == 'fast' 
