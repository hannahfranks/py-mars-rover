from input_layer.instruction import Instruction

def test_instruction():
    assert Instruction.LEFT.value == 'L'
    assert Instruction.RIGHT.value == 'R'
    assert Instruction.MOVE.value == 'M'
