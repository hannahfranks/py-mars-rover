from input_layer.rover_position import RoverPosition
from input_layer.compass_direction import CompassDirection

def test_class():
    rp = RoverPosition(1, 2, CompassDirection.EAST)
    assert rp.x_position == 1
    assert rp.y_position == 2
    assert rp.direction == CompassDirection.EAST