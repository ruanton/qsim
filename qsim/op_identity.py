import numpy as np
from qsim import Operation, Circuit


class OperationIdentity(Operation):
    """
    Identity quantum operation
    """
    def __init__(self, circuit: Circuit):
        op_matrix = np.array([
            [1, 0],
            [0, 1]])
        super().__init__(circuit, op_matrix)
