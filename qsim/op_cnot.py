import numpy as np
from qsim import Operation, Circuit


class OperationCNOT(Operation):
    """
    Quantum CNOT operation
    """
    def __init__(self, circuit: Circuit):
        op_matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]])
        super().__init__(circuit, op_matrix)
