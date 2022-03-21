import numpy as np
from qsim import OperationCNOT, Circuit


def test_operation_cnot():
    c = Circuit(qubit_count=2)
    o = OperationCNOT(c)
    assert o.qubits_count == 2
    op_matrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]])
    assert np.array_equal(o.op_matrix, op_matrix)


def test_operation_cnot_not_adjacent():
    c = Circuit(qubit_count=3)
    c.initialize([1, 0, 0])
    c.cnot.on(0, 2)
    state = c.execute()
    assert np.array_equal(state, [0, 0, 0, 0, 0, 1, 0, 0])

    c = Circuit(qubit_count=3)
    c.initialize([0, 0, 1])
    c.h.on(2)
    c.cnot.on(2, 0)
    state = c.execute()
    diff_state = state - [0.5**0.5, 0, 0, 0, 0, -0.5**0.5, 0, 0]
    assert abs(max(diff_state.max(), diff_state.min(), key=abs)) < 0.000001
