import numpy as np
from qsim import Operation


class Executor:
    """
    Quantum operation executor
    """
    def __init__(self, initial_state: np.ndarray):
        """
        Initializes executor with initial one-hot vector
        :param initial_state: initial one-hot vector
        """
        # save initial one-hot state vector
        self.state = initial_state

        # calculate qubits count of the circuit
        self.qubits_count = int(np.log2(len(self.state)))

        # verifies the length of the one-hot vector is power of 2
        if 2**self.qubits_count != len(self.state):
            raise ValueError(f'initial state vector size must be power of 2, but {len(self.state)} size given')

    def apply_operation(self, operation: Operation):
        """
        Applies quantum operation on current state of the one-hot vector
        :param operation: Quantum operation to apply
        """
        # verifies qubit positions is initialized
        if not operation.qubit_positions:
            raise RuntimeError('qubit positions not initialized')

        # verifies number of qubit positions within supported range
        num_qubits = len(operation.qubit_positions)
        if num_qubits not in [1, 2]:
            raise RuntimeError('only operations on 1 or 2 qubits are supported')

        # calculate full operation matrix
        op_matrix = operation.op_matrix.copy()
        if num_qubits == 2:
            if operation.qubit_positions[0] == operation.qubit_positions[1]+1:
                pass
            elif operation.qubit_positions[0]+1 == operation.qubit_positions[1]:
                op_matrix[[0, 1, 2, 3]] = op_matrix[[0, 2, 3, 1]]
            else:
                raise NotImplementedError('applying on contiguous qubits implemented only')
        pos = min(operation.qubit_positions)
        eye1 = np.eye(2**pos, dtype=complex)
        eye2 = np.eye(2**(self.qubits_count - pos - len(operation.qubit_positions)), dtype=complex)
        matrix_full = np.kron(eye2, np.kron(op_matrix, eye1))

        # apply matrix on current state vector
        self.state = np.matmul(matrix_full, self.state)
