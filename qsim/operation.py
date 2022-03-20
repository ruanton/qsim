import numpy as np
import copy
from qsim import Circuit


class Operation:
    """
    Operation on circuit
    """
    def __init__(self, circuit: Circuit, op_matrix: np.array):
        """
        Initializes operation on qubits
        :param circuit: circuit to operate on
        :param op_matrix: operation matrix
        """
        # verify correctness of parameters
        shape = op_matrix.shape
        if len(shape) != 2:
            raise ValueError(f'op_matrix must be 2-dimensional, given {len(shape)} dimensions')
        if shape[0] != shape[1]:
            raise ValueError(f'op_matrix must be square, given {shape[0]}x{shape[1]} matrix')

        # qubits count operation operates on
        self.qubits_count = int(np.log2(shape[0]))

        # verify op_matrix size is power of 2
        if 2**self.qubits_count != shape[0]:
            raise ValueError(f'op_matrix size must be power of 2, but matrix with size {shape[0]} given')

        # save operation matrix
        self.op_matrix: np.ndarray = op_matrix

        # positions of qubits to operate on, array of integers
        self.qubit_positions = None

        # save circuit link
        self.circuit = circuit

    def on(self, *qubit_positions: int):
        """
        Adds operation to the circuit and fixes it on given qubit positions
        :param qubit_positions: list of qubit positions as positional arguments
        """
        # verify circuit has enough qubits
        if self.qubits_count > self.circuit.qubit_count:
            raise ValueError(
                f'operation requires {self.qubits_count} qubits, but circuit has {self.circuit.qubit_count}')

        # verify number of qubit positions correspond to number of qubits operation operates on
        if len(qubit_positions) != self.qubits_count:
            raise ValueError(f'length of qubits positions list must be equal to {self.qubits_count}')

        # verify all qubit positions point to existing circuit qubits
        if any([x >= self.circuit.qubit_count or x < 0 for x in qubit_positions]):
            raise ValueError(f'all positions must be in range {0}..{self.circuit.qubit_count-1}')

        # create shallow copy of operation
        o = copy.copy(self)

        # set qubit positions
        o.qubit_positions = qubit_positions

        # append the operation copy to the sequence of operations in the circuit
        self.circuit.operations.append(o)
