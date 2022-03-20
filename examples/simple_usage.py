from qsim import Circuit

c = Circuit(qubit_count=2)
c.initialize([0, 1])
c.h.on(0)
c.x.on(1)
state = c.execute()
print(f'one-hot vector state: {state}')
