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
