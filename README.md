# Preparation of Hamming-Weight-Preserving Quantum States With Log-depth Quantum Circuits

This repository provides the official implementation, numerical verification, and benchmarking code for the algorithms presented in the manuscript: **"Preparation of Hamming-Weight-Preserving Quantum States With Log-depth Quantum Circuits"**.

## Overview

Hamming-Weight-Preserving (HWP) states, $|\psi_{H}\rangle = \sum_{\text{HW}(x)=k} \alpha_{x} |x\rangle$, represent a fundamental class of quantum states in fixed-excitation sectors, including the Bethe eigenstates of integrable models. Our work provides a definitive solution that simultaneously saturates the information-theoretic lower bounds for both circuit depth $\Theta(\log \binom{n}{k})$ and size $\Theta(\binom{n}{k})$.

This repository is organized into two modules:
1.  **Numerical Verification (Mathematica)**: Proving the algebraic stability of the resource-thrifty scheme.
2.  **Performance Benchmarking (Python/Qiskit)**: Comparing our HWP-specific circuits against general-purpose protocols.

---

## Repository Structure

### 1. Verification (Mathematica)
* `supplement.nb`: The primary notebook used to verify the non-singularity of reduced Krawtchouk matrices $M^{(j)}$ for all relevant parameters up to **$n = 273$**.
* 
### 2. Benchmarking (Python)
* `Qiskit_Comparison.py`: A benchmarking tool to compare our HWP-specific algorithm against Qiskit’s standard `initialize()` and isometry-based methods.

---

## Getting Started

### Prerequisites
* **Mathematica**: Version 12.0 or higher.
* **Python**: 3.8 or higher.
* **Libraries**:
    ```bash
    pip install qiskit qiskit-aer numpy matplotlib
    ```

### Usage
1. **Verification**: Open the `.nb` files in Mathematica and run the "Evaluate Notebook" command to replicate the $n \le 273$ stability results.
2. **Benchmarking**: Run the Python script to generate a depth-comparison plot:

---

## Key Results

* **Algebraic Stability**: We address the potential singularity of Krawtchouk matrices through exhaustive numerical verification, ensuring the robustness of our $O(\log~k)$ ancilla scheme.
* **Theoretical Optimality**: Our protocols provide the "theoretical floor" for HWP state preparation, significantly reducing decoherence-prone deep layers in NISQ-era simulations
