from qiskit import QuantumCircuit
from qiskit.circuit.library import StatePreparation
from qiskit import transpile
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
from itertools import combinations
import numpy as np

def generate_target_state(n):
    dim = 2**n
    state_vector = np.zeros(dim, dtype=complex)
    
    def calculate_unnormalized_coeff(j1, j2, n):
        term1 = np.sin(np.pi * j1 / (n + 1)) * np.sin(2 * np.pi * j2 / (n + 1))
        term2 = np.sin(np.pi * j2 / (n + 1)) * np.sin(2 * np.pi * j1 / (n + 1))
        return term1 - term2

    for idx_pair in combinations(range(n), 2):
        j1, j2 = idx_pair[0] + 1, idx_pair[1] + 1
        
        decimal_idx = (1 << idx_pair[0]) + (1 << idx_pair[1])
        
        coeff = calculate_unnormalized_coeff(j1, j2, n)
        state_vector[decimal_idx] = coeff

    norm = np.linalg.norm(state_vector)
    if norm > 0:
        state_vector = state_vector / norm
    
    return state_vector

depthqsp=np.zeros(10)
depthhwp=np.zeros(10)

for n in range(4,10):
    target_state = generate_target_state(n)          # 2^n
    prep = StatePreparation(target_state)
    qc = QuantumCircuit(n)
    qc.append(prep, range(n))
    decomposed_qc = transpile(qc, basis_gates=['u', 'cx'], optimization_level=3)
    stats = decomposed_qc.count_ops()
    print(n)
    depthqsp[n]=np.log2(decomposed_qc.depth())
    depthhwp[n]=np.log2(16+12*np.ceil(np.log2(n*(n-1)/2)).astype(int))

plt.xlabel(r'Number of Qubits ($n$)', fontsize=12)
plt.ylabel('Log Transpiled Circuit Depth', fontsize=12)
indices = range(4, len(depthqsp))
plt.plot(indices, depthqsp[4:], label='General QSP (Qiskit)',marker='o')
plt.plot(indices, depthhwp[4:], label='This Work',marker='s')
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.legend()
plt.show()

