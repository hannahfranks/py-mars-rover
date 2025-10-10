from input_layer.compass_direction import CompassDirection

class RoverPosition:
     
     def __init__(self, x, y, direction: CompassDirection):
          self.x = x
          self.y = y
          self.direction = direction

    