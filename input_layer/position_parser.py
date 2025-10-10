from input_layer.rover_position import RoverPosition
from input_layer.compass_direction import CompassDirection

class PositionParser:
    def __init__(self, position_input):
        self.position_input = position_input
        
        try:
            x_in, y_in, dir = position_input.split()
            x = int(x_in)
            y = int(y_in)
            direction = CompassDirection(dir)
        
        except ValueError:
            raise ValueError("Invalid position")
        
        except KeyError:
            raise ValueError("Invalid direction")
        
        self.position = RoverPosition(x, y, direction)

# takes initial position input and changes format to (x_position, y_position, direction) 

