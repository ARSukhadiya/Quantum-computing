# pip install qiskit
# pip install qiskit-aer

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator  
from qiskit.visualization import plot_histogram

circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0,1], [0,1])

Qsimulator = AerSimulator()       
job = Qsimulator.run(circuit, shots=1000)

result = job.result()
counts = result.get_counts(circuit)

print("Measurement results:", counts)

plot_histogram(counts)
