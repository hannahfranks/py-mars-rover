from input_layer.plateau_parser import PlateauParser
from input_layer.plateau_size import PlateauSize
import pytest

# test returns width and height 
# test raise error with invalid input 

def test_parser_works():
    parser = PlateauParser("5 5")
    assert isinstance(parser.plateau, PlateauSize)
    assert parser.plateau.width == 5
    assert parser.plateau.height == 5

def test_with_invalid_raises_error():
    with pytest.raises(ValueError) as e:
        parser = PlateauParser("3 E")
        assert str(e.value) == "Invalid Plateau size"