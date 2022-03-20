# Simple quantum circuit state vector simulator


## Usage
```python
from qsim import Circuit

c = Circuit(qubit_count=2)
c.initialize([0, 1])
c.h.on(0)
c.x.on(1)
state = c.execute()
print(f'one-hot vector state: {state}')
```

## Features

Number of qubits and initial state can be set:
```python
from qsim import Circuit

c = Circuit(qubit_count=4)
c.initialize([0, 1, 0, 1])
```

Supports parametrized quantum operations:
```python
import numpy as np
from qsim import Circuit

c = Circuit(qubit_count=2)
c.r.on(0, angle=np.pi/2)
```

Supports two-qubit operations:
```python
from qsim import Circuit

c = Circuit(qubit_count=2)
c.cnot.on(0, 1)
```

Supports custom quantum operations (see example in the
examples/custom_operation.py).

Supports circuit optimization: remove mutually
exclusive operations, etc. Not implemented yet. Usage:
```python
from qsim import Circuit

c = Circuit(qubit_count=2)
c.z.on(0)
c.z.on(0)
c.optimize_circuit()
```

Supports custom backends for quantum operation execution
by subclassing Executor and injecting it into Circuit object.
See prototype in examples/custom_backend.py

## Examples

See more examples in examples folder.

## Tests

To run unit tests:
```shell
pytest tests
```

## Authors

* **Anton Benderskiy** - *Initial work* - loderan (at) ruservice.ru.
