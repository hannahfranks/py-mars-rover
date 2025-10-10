from input.rover_position import RoverPosition
from input.instruction import Instruction
from input.compass_direction import CompassDirection

class Rover:
    def __init__(self, position: RoverPosition):
        self.position = position
        