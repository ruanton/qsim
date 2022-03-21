import numpy as np
from qsim import OperationSWAP, Circuit


def test_operation_swap():
    c = Circuit(qubit_count=2)
    o = OperationSWAP(c)
    assert o.qubits_count == 2
    op_matrix = np.array([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]])
    assert np.array_equal(o.op_matrix, op_matrix)
    c.initialize([1, 0])
    c.swap.on(0, 1)
    state = c.execute()
    assert np.array_equal(state, [0, 0, 1, 0])

    c = Circuit(qubit_count=2)
    c.initialize([1, 0])
    c.swap.on(1, 0)
    state = c.execute()
    assert np.array_equal(state, [0, 0, 1, 0])


def test_operation_swap_not_adjacent():
    c = Circuit(qubit_count=3)
    c.initialize([1, 0, 0])
    c.swap.on(0, 2)
    state = c.execute()
    assert np.array_equal(state, [0, 0, 0, 0, 1, 0, 0, 0])
