import numpy as np
from qsim import Circuit, Operation


# subclass base Operation
class OperationS(Operation):
    """
    Quantum S operation
    """
    def __init__(self, circuit: Circuit):
        op_matrix = np.array([
            [1, 0],
            [0, 1j]])
        super().__init__(circuit, op_matrix)


# create new quantum circuit and initialize it with initial state
c = Circuit(qubit_count=2)
c.initialize([1, 1])

# add new operation type to the circuit
c.s = OperationS(c)

# can now use this custom operation
c.s.on(0)
c.s.on(1)

state = c.execute()
print(f'one-hot vector state: {state}')
