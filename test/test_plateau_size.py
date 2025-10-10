from input.plateau_size import PlateauSize

def test_plateau():
    ps = PlateauSize(1, 2)
    assert ps.width == 1
    assert ps.height == 2