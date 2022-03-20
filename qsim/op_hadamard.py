import numpy as np
from qsim import Operation, Circuit


class OperationHadamard(Operation):
    """
    Hadamard quantum operation
    """
    def __init__(self, circuit: Circuit):
        op_matrix = 0.5**0.5*np.array([
            [1, 1],
            [1, -1]])
        super().__init__(circuit, op_matrix)
