from input_layer.rover_position import RoverPosition
from input_layer.position_parser import PositionParser
from input_layer.compass_direction import CompassDirection
import pytest

# test returns two integers and compass direction
# test raise error with invalid input 

def test_pos_parser_works():
    parser = PositionParser("1 2 W")
    rp = parser.position
    assert isinstance(parser.position, RoverPosition)
    assert rp.x == 1
    assert rp.y == 2
    assert rp.direction == CompassDirection.WEST

def test_with_invalid_position_raise_error():
    with pytest.raises(ValueError) as e:
        parser = PositionParser("1 N N")
        assert str(e.value) == "Invalid position"

def test_with_invalid_direction():
    with pytest.raises(ValueError) as e:
        parser = PositionParser("1 2 F")
        assert str(e.value) == "Invalid direction"

