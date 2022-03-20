import numpy as np
from qsim import OperationX, Circuit


def test_operation_x():
    c = Circuit(qubit_count=1)
    o = OperationX(c)
    assert o.qubits_count == 1
    assert np.array_equal(o.op_matrix, [[0, 1], [1, 0]])
