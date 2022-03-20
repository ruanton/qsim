import numpy as np
from qsim import Circuit, Executor, Operation


# subclass Executor
class CustomExecutor(Executor):
    """
    Custom quantum operation executor for external backend, for example, based on GPU.
    """
    def __init__(self, initial_state: np.ndarray):
        # TODO: implement custom logic for state initialization
        super().__init__(initial_state=initial_state)

    def apply_operation(self, operation: Operation):
        # TODO: implement custom logic for operation execution
        super().apply_operation(operation=operation)


# create circuit
c = Circuit(qubit_count=2)

# inject custom backend
c.executor = CustomExecutor

# now use the circuit as usual
c.initialize([1, 0])
c.h.on(0)

state = c.execute()
print(f'one-hot vector state: {state}')
