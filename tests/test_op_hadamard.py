import numpy as np
from qsim import OperationHadamard, Circuit


def test_operation_hadamard():
    c = Circuit(qubit_count=1)
    o = OperationHadamard(c)
    assert o.qubits_count == 1
    assert np.array_equal(o.op_matrix, np.array([[1, 1], [1, -1]])*0.5**0.5)
