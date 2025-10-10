from input_layer.rover_position import RoverPosition

class Plateau:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def check_position_is_in_plateau(self, position: RoverPosition):
        if 0 <= position.x <= self.width and 0 <= position.y <= self.height:
            return True
        else:
            return False
        
    def is_position_empty(self, position: RoverPosition):
        return True


# holds size - check if position is within plateau
# can check if a position is empty