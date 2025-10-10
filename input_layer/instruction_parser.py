from input_layer.instruction import Instruction

class InstructionParser:
    def __init__(self, instruction_input):
        self.instruction_input = instruction_input
        self.instructions = []

        for char in instruction_input:
            try:
                self.instructions.append(Instruction(char))

            except ValueError:
                pass


# takes instruction input and changes into list of instructions 
# ignore invalid instruction characters 

