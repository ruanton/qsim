import numpy as np
from qsim import Operation, Circuit


def test_operation_one_dimension_matrix():
    c = Circuit(qubit_count=1)
    try:
        Operation(c, np.array([0, 1]))
    except ValueError:
        pass
    else:
        assert False


def test_operation_three_dimension_matrix():
    c = Circuit(qubit_count=3)
    try:
        Operation(c, np.array([
            [[1, 0, 0], [1, 0, 0], [1, 0, 0]],
            [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
            [[0, 0, 1], [0, 0, 1], [0, 0, 1]]]))
    except ValueError:
        pass
    else:
        assert False


def test_operation_matrix_size_not_power_of_two():
    c = Circuit(qubit_count=3)
    try:
        Operation(c, np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]]))
    except ValueError:
        pass
    else:
        assert False


def test_operation_qubits_count1():
    c = Circuit(qubit_count=1)
    o = Operation(c, np.array([
        [0, 1],
        [1, 0]]))
    assert o.qubits_count == 1


def test_operation_qubits_count2():
    c = Circuit(qubit_count=2)
    o = Operation(c, np.array([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]]))
    assert o.qubits_count == 2


def test_on():
    c = Circuit(3)
    o = Operation(c, np.array([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]]))
    o.on(1, 2)
    assert len(c.operations) == 1
    assert c.operations[0].circuit == c
    assert c.operations[0].qubit_positions == (1, 2)


def test_on_several():
    c = Circuit(3)
    o = Operation(c, np.array([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]]))
    o.on(1, 2)
    o = Operation(c, np.array([
        [1, 0],
        [0, 1]]))
    o.on(0)
    assert len(c.operations) == 2
    assert c.operations[0].circuit == c
    assert c.operations[0].qubit_positions == (1, 2)
    assert c.operations[1].qubit_positions == (0,)


def test_on_positions_out_of_range1():
    c = Circuit(3)
    o = Operation(c, np.array([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]]))
    try:
        o.on(0, 3)
    except ValueError:
        pass
    else:
        assert False


def test_on_positions_out_of_range2():
    c = Circuit(3)
    o = Operation(c, np.array([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]]))
    try:
        o.on(-1, 1)
    except ValueError:
        pass
    else:
        assert False
