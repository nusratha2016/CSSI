class Spaceship:
    def __init__ (self, spaceship_name, spaceship_color,spaceship_speed ):
        self.name = spaceship_name
        self.color = spaceship_color
        self.speed = spaceship_speed
    def description(self):
        print "Hey, my spaceship name is %s and color is %s and speed is %s spaceship." % (self.name, self.color,self.speed)
# Creating two Spaceship objects, using the Spaceship template.
nightingale = Spaceship ('Nightingale', 'Red', 360)
battleship = Spaceship ('Battleship', 'Original', 520)
# Printing the properties of the Spaceship objects we've created.
print(nightingale.name + ': ' + nightingale.color)
print(battleship.name + ': ' + str(battleship.speed))
# Calling the description method.
battleship.description()
