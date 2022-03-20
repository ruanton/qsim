import numpy as np
from qsim import OperationY, Circuit


def test_operation_y():
    c = Circuit(qubit_count=1)
    o = OperationY(c)
    assert o.qubits_count == 1
    assert np.array_equal(o.op_matrix, [[0, -1j], [1j, 0]])
