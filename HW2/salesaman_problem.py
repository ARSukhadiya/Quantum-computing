import pennylane as qml
from pennylane import numpy as np

# Define the problem: Molecular simulation
# Example Hamiltonian for H2 molecule in STO-3G basis
H = np.array([[-1.053, 0.396, 0.0, -0.395],
              [0.396, -1.478, -0.395, 0.0],
              [0.0, -0.395, -1.478, 0.396],
              [-0.395, 0.0, 0.396, -1.053]])

# Define the number of qubits
num_qubits = 2

# Initialize the Pennylane device
dev = qml.device('default.qubit', wires=num_qubits)

# Define the ansatz circuit
def ansatz(params, wires):
    qml.BasisState(np.array([1, 1]), wires=wires)
    qml.DoubleExcitation(params, wires=[0, 1])

# Define the cost function (expected value of the Hamiltonian)
@qml.qnode(dev)
def cost_fn(params):
    ansatz(params, wires=range(num_qubits))
    return qml.expval(qml.Hermitian(H, wires=[0, 1]))

# Initialize the optimizer
opt = qml.GradientDescentOptimizer(stepsize=0.4)

# Number of optimization steps
steps = 100

# Random initial parameters
init_params = np.random.uniform(low=-np.pi, high=np.pi, size=(2,))

# Optimization loop
params = init_params
for i in range(steps):
    # Update the circuit parameters
    params = opt.step(cost_fn, params)

    # Compute the energy at the current iteration
    energy = cost_fn(params)

    if (i + 1) % 10 == 0:
        print(f"Step {i + 1}: Energy = {energy}")

# Print the final optimized parameters and energy
print("\nOptimized parameters:")
print(params)
print("Optimized energy:", energy)
