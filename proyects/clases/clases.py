"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    health = 3
    total_aliens_created = 0

    def __init__(self,coordinatex,coordinatey) :
        self.x_coordinate = coordinatex
        self.y_coordinate = coordinatey
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -=1

    def is_alive(self):
        return self.health > 0
    
    def teleport(self,new_coordx,new_coordy):
        self.x_coordinate = new_coordx
        self.y_coordinate = new_coordy

    def collision_detection(self,other_object):
        pass

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(coordinates):
    collect = [Alien(*Ali) for Ali in coordinates]
    return (collect)

a = new_aliens_collection([(4, 7), (-1, 0), (-1, 0)])
print(a)
for aa in a:
    print(aa.x_coordinate, aa.y_coordinate)
