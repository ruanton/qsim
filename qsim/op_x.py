import numpy as np
from qsim import Operation, Circuit


class OperationX(Operation):
    """
    Quantum X operation
    """
    def __init__(self, circuit: Circuit):
        op_matrix = np.array([
            [0, 1],
            [1, 0]])
        super().__init__(circuit, op_matrix)
