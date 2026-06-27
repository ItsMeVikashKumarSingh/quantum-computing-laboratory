# Quantum Computing Laboratory

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ItsMeVikashKumarSingh/quantum-computing-laboratory/a38e9ae9d566c3cc7ca9f9cc7ffb50bc2798bdb3?urlpath=lab/tree/quantum_laboratory.ipynb)

A simulation-based Jupyter notebook workspace designed to explore the fundamentals of quantum computing, quantum gates, multi-qubit registers, entanglement, and algorithmic complexity using Qiskit 1.x and Python.

---

## Introduction & Quantum Basics

Quantum computing operates on the principles of quantum mechanics:
*   **Qubits:** Unlike classical bits which can be either 0 or 1, a quantum bit (qubit) can exist in a linear combination of states represented as $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$, where $\alpha$ and $\beta$ are complex numbers satisfying $|\alpha|^2 + |\beta|^2 = 1$.
*   **Superposition:** The ability of a qubit to exist in multiple states simultaneously until a measurement collapses the state vector.
*   **Entanglement:** A non-classical correlation where the state of one qubit cannot be described independently of the state of the other, enabling parallel information processing.
*   **Quantum Gates:** Unitary transformations ($U^\dagger U = I$) that rotate qubit vectors on the Bloch Sphere.

---

## Environment Setup & Installation

Follow these instructions to set up the workspace locally and run the notebook.

### 1. Prerequisite
Ensure Python 3.9, 3.10, or 3.11 is installed on your machine.

### 2. Create a Virtual Environment
Navigate to the repository root directory and create an isolated Python virtual environment:
```bash
# Windows
python -m venv venv

# macOS / Linux
python3 -m venv venv
```

### 3. Activate the Environment
Activate the environment to ensure dependencies are isolated:
```bash
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (Command Prompt)
.\venv\Scripts\activate.bat

# macOS / Linux
source venv/bin/activate
```

### 4. Install Dependencies
Install Qiskit, the Aer simulator, plotting libraries, and Jupyter notebook utilities:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Register the Jupyter Kernel
Register your virtual environment with Jupyter so the notebook can select the correct execution backend:
```bash
python -m ipykernel install --user --name=quantum-lab --display-name="Python (Quantum Lab)"
```

### 6. Run the Workspace
Launch Jupyter Notebook to open and execute the simulation suite:
```bash
jupyter notebook
```
Double-click `quantum_laboratory.ipynb`, select the kernel named **Python (Quantum Lab)** from the top-right menu, and run the cells.

### Alternative: Run Console Validation (Without Jupyter)
If you do not have Jupyter installed, you can execute the entire simulation suite directly in your terminal using:
```bash
python test_lab.py
```
This will run all 11 experiments in sequence on the simulator and output text-based circuit diagrams and measurement distributions directly to your console.


---

## Workspace Structure

```
quantum-computing-laboratory/
├── requirements.txt
├── README.md
├── test_lab.py
└── quantum_laboratory.ipynb
```

---

## Implemented Experiments

The workspace contains 11 core experiments structured within a single master Jupyter Notebook:
1.  **Quantum Gates Playground:** Single-qubit Pauli ($X, Y, Z$), Hadamard ($H$), and phase/rotation gates.
2.  **Superposition (Single Qubit):** State preparation and statevector probability collapses.
3.  **Bell State (Two Qubits):** maximally entangled EPR pair generation.
4.  **Quantum Entanglement & GHZ State:** Three-qubit CNOT cascades.
5.  **Quantum Circuits & Composition:** Composing multi-qubit register architectures.
6.  **Deutsch Algorithm:** Demonstrating quantum oracle evaluation speedup.
7.  **Grover Search Simulation:** Oracle and diffusion operator construct for unstructured search.
8.  **Quantum Fourier Transform (QFT):** Replicating discrete Fourier transformations in the quantum phase domain.
9.  **Shor Algorithm Simulation:** Factoring 15 using simplified 3-qubit modular exponentiation circuits.
10. **Quantum Measurement:** Analyzing projective measurement outcomes in computational bases.
11. **Noise Simulation:** Modeling physical processor errors using amplitude and phase damping noise channels.

---

## Resume Bullets

*   **Developed a Simulation-based Quantum Computing Lab** using Qiskit 1.x and Python to model qubits, superposition, entanglement, and state decoherence.
*   **Programmed and verified foundational quantum algorithms** including Deutsch's oracle evaluation and Grover's search on local Aer simulators.
*   **Implemented physical hardware noise models** simulating quantum decoherence effects (amplitude and phase damping channels) on quantum circuit fidelity.
