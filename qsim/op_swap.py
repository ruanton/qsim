import numpy as np
from qsim import Operation, Circuit


class OperationSWAP(Operation):
    """
    Quantum SWAP operation
    """
    def __init__(self, circuit: Circuit):
        op_matrix = OperationSWAP.get_swap_matrix()
        super().__init__(circuit, op_matrix)

    @classmethod
    def get_swap_matrix(cls):
        return np.array([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]])
