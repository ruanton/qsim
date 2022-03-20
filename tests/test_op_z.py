import numpy as np
from qsim import OperationZ, Circuit


def test_operation_z():
    c = Circuit(qubit_count=1)
    o = OperationZ(c)
    assert o.qubits_count == 1
    assert np.array_equal(o.op_matrix, [[1, 0], [0, -1]])
