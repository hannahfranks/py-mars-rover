from input_layer.rover_position import RoverPosition
from logic_layer.plateau import Plateau

def test_within_plateau_inside():
    plateau = Plateau(3, 3)
    pos = RoverPosition(1, 2, None)
    assert plateau.check_position_is_in_plateau(pos) is True

def test_within_plateau_edge():
    plateau = Plateau(3, 3)
    pos = RoverPosition(3, 3, None)
    assert plateau.check_position_is_in_plateau(pos) is True

def test_within_plateau_outside():
    plateau = Plateau(3, 3)
    pos = RoverPosition(6, 6, None)
    assert plateau.check_position_is_in_plateau(pos) == False

def test_position_empty_default_true():
    plateau = Plateau(3, 3)
    pos = RoverPosition(3, 3, None)
    assert plateau.is_position_empty(pos) == True
