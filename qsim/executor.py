import numpy as np
from qsim import Operation, OperationSWAP


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

    def apply_matrix_at_pos(self, op_matrix: np.ndarray, pos: int):
        """
        Applies given matrix on the current one-hot vector state at given qubit position.
        :param op_matrix: operation matrix
        :param pos: position of qubit to apply
        """
        # construct full matrix
        eye1 = np.eye(2 ** pos, dtype=complex)
        eye2 = np.eye(2 ** (self.qubits_count - pos - int(np.log2(op_matrix.shape[0]))), dtype=complex)
        matrix_full = np.kron(eye2, np.kron(op_matrix, eye1))

        # apply matrix on current state vector
        self.state = np.matmul(matrix_full, self.state)

    def apply_swap(self, pos_l: int, pos_r: int):
        """
        Applies SWAP operation on qubits in positions pos1, pos2
        """
        if pos_l > pos_r:
            pos_l, pos_r = pos_r, pos_l
        if pos_l == pos_r:
            raise ValueError(f'incorrect qubit positions gives, must be different')
        if pos_l < 0 or pos_r >= self.qubits_count:
            raise ValueError(f'incorrect qubit positions gives, must be in range {0}..{self.qubits_count-1}')

        # matrix for swap operation
        swap_matrix = OperationSWAP.get_swap_matrix()

        if pos_l+1 == pos_r:
            # if qubits are adjacent apply SWAP matrix as usual
            self.apply_matrix_at_pos(swap_matrix, pos_l)
        else:
            # if qubits are not adjacent emulate with several swap operations on adjacent qubits
            # TODO: realize more optimal algorithm for swapping qubits
            for pos in range(pos_l, pos_r):
                self.apply_matrix_at_pos(swap_matrix, pos)
            for pos in range(pos_r - 2, pos_l - 1, -1):
                self.apply_matrix_at_pos(swap_matrix, pos)

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

        if num_qubits == 1:
            # one qubit operation
            self.apply_matrix_at_pos(operation.op_matrix, operation.qubit_positions[0])

        else:  # two qubit operation
            # qubit positions
            pos1, pos2 = operation.qubit_positions

            # if qubits are not adjacent, we swap relevant qubits to make it adjacent
            pos1_original = pos1
            if abs(pos2 - pos1) != 1:
                pos1 = pos2 + 1
                if pos1 >= self.qubits_count:
                    pos1 = pos2 - 1
                self.apply_swap(pos1_original, pos1)

            # calculate and apply operation matrix
            op_matrix = operation.op_matrix.copy()
            if pos1+1 == pos2:
                # transform operations matrix to correspond reversed qubits order
                op_matrix[[0, 1, 2, 3]] = op_matrix[[0, 2, 1, 3]]  # swap rows 2 and 3
                op_matrix[:, [1, 2]] = op_matrix[:, [2, 1]]        # swap columns 2 and 3

            # apply operation matrix on the one-hot vector
            self.apply_matrix_at_pos(op_matrix, min(pos1, pos2))

            # if we swapped qubits, swap its back
            if pos1_original != pos1:
                self.apply_swap(pos1_original, pos1)
