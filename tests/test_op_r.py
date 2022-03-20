import numpy as np
from qsim import OperationR, Circuit


def test_operation_r():
    c = Circuit(qubit_count=1)
    o = OperationR(c)
    assert o.qubits_count == 1
    o.on(0, angle=np.pi)
    diff_matrix = o.op_matrix - [[1, 0], [0, -1]]
    assert abs(max(diff_matrix.max(), diff_matrix.min(), key=abs)) < 0.000001
    o.on(0, angle=np.pi/2)
    diff_matrix = o.op_matrix - [[1, 0], [0, 1j]]
    assert abs(max(diff_matrix.max(), diff_matrix.min(), key=abs)) < 0.000001
