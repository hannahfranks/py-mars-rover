from input_layer.compass_direction import CompassDirection

class RoverPosition:
     
     def __init__(self, x_position, y_position, direction: CompassDirection):
          self.x_position = x_position
          self.y_position = y_position
          self.direction = direction

    