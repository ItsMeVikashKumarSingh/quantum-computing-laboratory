import os
import sys
import numpy as np

# Ensure stdout handles formatting
sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None

print("======================================================================")
print("             QUANTUM COMPUTING LABORATORY VALIDATION SUITE            ")
print("======================================================================\n")

try:
    from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
    from qiskit.quantum_info import Statevector
    from qiskit_aer import AerSimulator
    from qiskit_aer.noise import NoiseModel, phase_damping_error
except ImportError as e:
    print(f"Error: Missing Qiskit dependencies. {str(e)}")
    print("Please install requirements first: pip install -r requirements.txt")
    sys.exit(1)

sim = AerSimulator()

# 1. Gates Playground
print("--------------------------------------------------")
print("Experiment 1: Quantum Gates Playground")
print("--------------------------------------------------")
qc1 = QuantumCircuit(1)
qc1.h(0)
qc1.z(0)
print("Circuit Text Diagram:")
print(qc1.draw(output='text'))
sv1 = Statevector.from_instruction(qc1)
print(f"Resulting Qubit Statevector:\n{sv1.data}\n")

# 2. Superposition
print("--------------------------------------------------")
print("Experiment 2: Single Qubit Superposition")
print("--------------------------------------------------")
qc2 = QuantumCircuit(1, 1)
qc2.h(0)
qc2.measure(0, 0)
print("Circuit Text Diagram:")
print(qc2.draw(output='text'))
counts2 = sim.run(qc2, shots=1000).result().get_counts()
print(f"Measurement outcomes (1000 shots): {counts2}\n")

# 3. Bell State
print("--------------------------------------------------")
print("Experiment 3: Bell State Maximally Entangled EPR Pair")
print("--------------------------------------------------")
qc3 = QuantumCircuit(2, 2)
qc3.h(0)
qc3.cx(0, 1)
qc3.measure([0, 1], [0, 1])
print("Circuit Text Diagram:")
print(qc3.draw(output='text'))
counts3 = sim.run(qc3, shots=1000).result().get_counts()
print(f"Bell measurement outcomes (1000 shots): {counts3}\n")

# 4. GHZ State
print("--------------------------------------------------")
print("Experiment 4: GHZ Multi-Qubit Entanglement State")
print("--------------------------------------------------")
qc4 = QuantumCircuit(3, 3)
qc4.h(0)
qc4.cx(0, 1)
qc4.cx(1, 2)
qc4.measure([0, 1, 2], [0, 1, 2])
print("Circuit Text Diagram:")
print(qc4.draw(output='text'))
counts4 = sim.run(qc4, shots=1000).result().get_counts()
print(f"GHZ measurement outcomes (1000 shots): {counts4}\n")

# 5. Circuits Composition
print("--------------------------------------------------")
print("Experiment 5: Circuit Composition")
print("--------------------------------------------------")
qc5_prep = QuantumCircuit(2)
qc5_prep.h(0)
qc5_prep.cx(0, 1)
qc5_ops = QuantumCircuit(2)
qc5_ops.x(0)
qc5_ops.z(1)
composed = qc5_prep.compose(qc5_ops)
print("Composed Circuit Text Diagram:")
print(composed.draw(output='text'))
print("\n")

# 6. Deutsch Algorithm
print("--------------------------------------------------")
print("Experiment 6: Deutsch Algorithm (Balanced Oracle)")
print("--------------------------------------------------")
oracle6 = QuantumCircuit(2)
oracle6.cx(0, 1) # CNOT represents a balanced function f(x) = x
qc6 = QuantumCircuit(2, 1)
qc6.x(1)
qc6.h([0, 1])
qc6.barrier()
qc6.compose(oracle6, inplace=True)
qc6.barrier()
qc6.h(0)
qc6.measure(0, 0)
print("Deutsch Circuit Text Diagram:")
print(qc6.draw(output='text'))
counts6 = sim.run(qc6, shots=1000).result().get_counts()
print(f"Deutsch output (should measure '1' for Balanced): {counts6}\n")

# 7. Grover Search
print("--------------------------------------------------")
print("Experiment 7: Grover Search for Target State |11>")
print("--------------------------------------------------")
qc7 = QuantumCircuit(2, 2)
qc7.h([0, 1])
qc7.barrier()
qc7.cz(0, 1) # Oracle flips phase of state |11>
qc7.barrier()
qc7.h([0, 1])
qc7.z([0, 1])
qc7.cz(0, 1)
qc7.h([0, 1])
qc7.barrier()
qc7.measure([0, 1], [0, 1])
print("Grover Circuit Text Diagram:")
print(qc7.draw(output='text'))
counts7 = sim.run(qc7, shots=1000).result().get_counts()
print(f"Grover search outcome (Target '11' probability): {counts7}\n")

# 8. QFT
print("--------------------------------------------------")
print("Experiment 8: 3-Qubit Quantum Fourier Transform")
print("--------------------------------------------------")
qc8 = QuantumCircuit(3)
qc8.h(2)
qc8.cp(np.pi/2, 1, 2)
qc8.cp(np.pi/4, 0, 2)
qc8.h(1)
qc8.cp(np.pi/2, 0, 1)
qc8.h(0)
qc8.swap(0, 2)
print("QFT Circuit Text Diagram:")
print(qc8.draw(output='text'))
print("\n")

# 9. Shor's Simplified Exponentiation
print("--------------------------------------------------")
print("Experiment 9: Shor's Simplified Exponentiation (a=7, N=15)")
print("--------------------------------------------------")
c_reg = QuantumRegister(3, name='control')
t_reg = QuantumRegister(4, name='target')
meas = ClassicalRegister(3, name='meas')
qc9 = QuantumCircuit(c_reg, t_reg, meas)
qc9.x(t_reg[0])
qc9.h(c_reg)
qc9.ccx(c_reg[0], t_reg[0], t_reg[2])
qc9.ccx(c_reg[0], t_reg[1], t_reg[3])
qc9.swap(c_reg[0], c_reg[2])
qc9.h(c_reg[0])
qc9.cp(-np.pi/2, c_reg[0], c_reg[1])
qc9.h(c_reg[1])
qc9.cp(-np.pi/4, c_reg[0], c_reg[2])
qc9.cp(-np.pi/2, c_reg[1], c_reg[2])
qc9.h(c_reg[2])
qc9.measure(c_reg, meas)
print("Simplified Shor Circuit Text Diagram:")
print(qc9.draw(output='text'))
counts9 = sim.run(qc9, shots=1000).result().get_counts()
print(f"Measured period phase distributions: {counts9}\n")

# 10. Quantum Measurement (Z vs X basis)
print("--------------------------------------------------")
print("Experiment 10: Quantum Measurement Bases")
print("--------------------------------------------------")
qc10 = QuantumCircuit(1, 2)
qc10.h(0)
qc10.measure(0, 0) # Computational Z measurement
qc10.h(0)
qc10.measure(0, 1) # Diagonal X measurement
print("Measurement Bases Circuit Text Diagram:")
print(qc10.draw(output='text'))
counts10 = sim.run(qc10, shots=1000).result().get_counts()
print(f"Z basis (right bit) vs X basis (left bit) outcomes: {counts10}\n")

# 11. Decoherence Noise Simulation
print("--------------------------------------------------")
print("Experiment 11: Phase Damping Decoherence Simulation")
print("--------------------------------------------------")
error = phase_damping_error(0.15)
noise_model = NoiseModel()
noise_model.add_all_qubit_quantum_error(error, ['h'])

qc11 = QuantumCircuit(2, 2)
qc11.h(0)
qc11.cx(0, 1)
qc11.measure([0, 1], [0, 1])

clean_counts = AerSimulator().run(qc11, shots=1000).result().get_counts()
noisy_counts = AerSimulator(noise_model=noise_model).run(qc11, shots=1000).result().get_counts()
print(f"Ideal Bell State Measurement: {clean_counts}")
print(f"Noisy Bell State (15% phase damping): {noisy_counts}\n")

print("======================================================================")
print("                    VALIDATION SUITE COMPLETED                        ")
print("======================================================================")
