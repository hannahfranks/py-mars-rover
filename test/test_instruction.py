from input_layer.instruction import Instruction

def test_instruction():
    assert Instruction.LEFT.value == 'L'
    assert Instruction.RIGHT.value == 'R'
    assert Instruction.MOVE.value == 'M'

# def test_turn_instruction_into_list():
#     i = Instruction('LRLM')
#     assert i.turn_instruction_into_list() == ['L', 'R', 'L', 'M']

# def test_validate_instruction_list():
#     i = Instruction("LRMB")
#     assert i.filter_instruction_list() == ['L', 'R', 'M']