from input_layer.compass_direction import CompassDirection

def test_compass_direction_enum():
    assert CompassDirection.NORTH.value == 'N'
    assert CompassDirection.SOUTH.value == 'S'
    assert CompassDirection.EAST.value == 'E'
    assert CompassDirection.WEST.value == 'W'