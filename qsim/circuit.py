import numpy as np


class Circuit:
    """
    Quantum circuit
    """
    def __init__(self, qubit_count: int):
        """
        Initializes quantum circuit object with initial state all qubits zeros.
        :param qubit_count: number of qubits
        """

        # number of qubits in the circuit
        self.qubit_count = qubit_count

        # initial state of the one-hot vector
        self.initial_state = np.zeros(2**qubit_count, dtype=complex)
        self.initial_state[0] = 1

        # sequence of operations
        self.operations = []

        # add base quantum operations
        from qsim import OperationX, OperationY, OperationZ, OperationIdentity
        from qsim import OperationHadamard, OperationCNOT, OperationR
        self.x = OperationX(self)
        self.y = OperationY(self)
        self.z = OperationZ(self)
        self.i = OperationIdentity(self)
        self.h = OperationHadamard(self)
        self.r = OperationR(self)
        self.cnot = OperationCNOT(self)

        # set default quantum operation executor backend
        from qsim import Executor
        self.executor = Executor

    def initialize(self, qubits: list):
        """
        Initializes circuit with initial state of the one-hot vector.
        :param qubits: array of initial qubit states, 0s or 1s accepted
        """
        if len(qubits) != self.qubit_count:
            raise ValueError(f'unexpected number of qubits, given: {len(qubits)}, circuit has {self.qubit_count}')

        # create one-hot state with length 2^(qubits count) and fills with zeros
        self.initial_state = np.zeros(2**self.qubit_count, dtype=complex)

        # calculating initial one-hot vector state
        vector_pos = 0
        for pos in range(len(qubits)):
            if qubits[pos] == 0:
                pass
            elif qubits[pos] == 1:
                vector_pos += 2**pos
            else:
                raise ValueError(f'unexpected qubit state {qubits[pos]} at position {pos}, 0s and 1s accepted only')
        self.initial_state[vector_pos] = 1

    def execute(self):
        """
        Executes quantum circuit
        :return: final state of the one-hot vector
        """
        # using executor execute every operation in the circuit sequentially
        executor = self.executor(initial_state=self.initial_state)
        for operation in self.operations:
            executor.apply_operation(operation)

        # return the final quantum state
        return executor.state

    def optimize_circuit(self):
        """
        Optimizes circuit: removes mutually exclusive operations, etc.
        """
        raise NotImplementedError
