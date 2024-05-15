# Globals for the directions
# Change the values as you see fit
EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"

class Robot:
    
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos

    @property #si requiero que un metodo se comporte como una propiedad uso el decorador 
    def coordinates(self):
        return (self.x_pos,self.y_pos)
    
    def move(self,new_direction):
        rose = ["NORTH","EAST","SOUTH","WEST"]
        self.new_direction = new_direction
        dir = rose.index(self.direction)
        for letter in self.new_direction:
            if letter == "R":
                if dir == 3:
                    dir = 0
                else: dir += 1
            if letter == "L":
                if dir == 0:
                    dir = 3
                else: dir -= 1
            self.direction = rose[dir]
            if letter == "A":
                if self.direction == "NORTH":
                    self.y_pos += 1
                if self.direction == "SOUTH":
                    self.y_pos -= 1
                if self.direction == "EAST":
                    self.x_pos += 1
                if self.direction == "WEST":
                    self.x_pos -= 1


# robot = Robot(NORTH, 0, 0)
# print(robot.direction)
# print(robot.move("R"))
# print(robot.direction)
# print(robot.move("R"))
# print(robot.direction)
# print(robot.move("R"))
# print(robot.direction)
# print(robot.move("R"))
# print(robot.direction)