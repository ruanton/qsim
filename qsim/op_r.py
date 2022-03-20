import numpy as np
from qsim import Operation, Circuit


class OperationR(Operation):
    """
    Quantum R operation
    """
    def __init__(self, circuit: Circuit):
        op_matrix = np.array([
            [1, 0],
            [0, 1]])
        super().__init__(circuit, op_matrix)

    def on(self, qubit_position: int, angle: float):
        """
        Applies R quantum operation.
        :param angle: angle of rotation
        :param qubit_position: qubit position in the circuit apply to
        """
        self.op_matrix = np.array([
            [1, 0],
            [0, np.exp(angle*1j)]])
        super().on(qubit_position)
