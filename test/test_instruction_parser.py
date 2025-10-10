from input_layer.instruction_parser import InstructionParser
from input_layer.instruction import Instruction

# test returns a list of valid instructions 
# test with all valid 
# test ignores invalid char 
# test for empty list

def test_parser_returns_list():
    parser = InstructionParser("LRML")
    assert parser.instructions == [
        Instruction.LEFT,
        Instruction.RIGHT,
        Instruction.MOVE,
        Instruction.LEFT
    ]

def test_parser_ignores_invalid_characters():
    parser = InstructionParser("LRMFL")
    assert parser.instructions == [
        Instruction.LEFT,
        Instruction.RIGHT,
        Instruction.MOVE,
        Instruction.LEFT
    ]

def test_empty_imput_return_empty_list():
    parser = InstructionParser('')
    assert parser.instructions == []


