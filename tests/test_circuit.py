import numpy as np
from qsim import Circuit


def test_circuit():
    c = Circuit(2)
    assert np.array_equal(c.initial_state, [1, 0, 0, 0])


def test_initialize():
    c = Circuit(2)
    c.initialize([0, 1])
    assert np.array_equal(c.initial_state, [0, 0, 1, 0])
    c.initialize([1, 0])
    assert np.array_equal(c.initial_state, [0, 1, 0, 0])
    c.initialize([1, 1])
    assert np.array_equal(c.initial_state, [0, 0, 0, 1])


def test_initialize_incorrect1():
    c = Circuit(2)
    try:
        c.initialize([0, 0, 1])
    except ValueError:
        pass
    else:
        assert False


def test_initialize_incorrect2():
    c = Circuit(3)
    try:
        c.initialize([0, 3, 1])
    except ValueError:
        pass
    else:
        assert False


def test_base_operations():
    c = Circuit(3)
    c.x.on(0)
    c.y.on(1)
    c.z.on(2)
    c.i.on(0)
    c.h.on(1)
    c.r.on(2, angle=np.pi/4)
    c.cnot.on(1, 2)
    c.swap.on(0, 1)
    assert len(c.operations) == 8
    assert np.array_equal(c.operations[2].op_matrix, np.array([[1, 0], [0, -1]]))
    assert c.operations[0].qubit_positions == (0,)
    assert c.operations[1].qubit_positions == (1,)
    assert c.operations[2].qubit_positions == (2,)
    assert c.operations[3].qubit_positions == (0,)
    assert c.operations[4].qubit_positions == (1,)
    assert c.operations[5].qubit_positions == (2,)
    assert c.operations[6].qubit_positions == (1, 2)
    assert c.operations[7].qubit_positions == (0, 1)


def test_execute():
    c = Circuit(qubit_count=4)
    c.initialize([0, 1, 0, 0])
    c.h.on(0)
    c.cnot.on(0, 1)
    c.cnot.on(1, 2)
    c.z.on(2)
    c.cnot.on(2, 3)
    state = c.execute()
    expected_state = [0, 0.5**0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -0.5**0.5, 0]
    diff = state - expected_state
    assert abs(max(diff.max(), diff.min(), key=abs)) < 0.000001
