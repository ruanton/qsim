import numpy as np
from qsim import Operation, Circuit


class OperationY(Operation):
    """
    Quantum Y operation
    """
    def __init__(self, circuit: Circuit):
        op_matrix = np.array([
            [0, -1j],
            [1j, 0]])
        super().__init__(circuit, op_matrix)
