from input_layer.plateau_size import PlateauSize

class PlateauParser:
    def __init__(self, size_input):
        self.size_input = size_input
        try:
            width, height = map(int, size_input.split())
        except ValueError:
            raise ValueError (f"Invalid Plateau size")
        self.plateau = PlateauSize(width, height)




# takes imput (num 1 num2) and changes format plateau(width, height)