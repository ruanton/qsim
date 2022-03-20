import numpy as np
from qsim import OperationIdentity, Circuit


def test_operation_identity():
    c = Circuit(qubit_count=1)
    o = OperationIdentity(c)
    assert o.qubits_count == 1
    assert np.array_equal(o.op_matrix, [[1, 0], [0, 1]])
