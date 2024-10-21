#!/usr/bin/env python3
import numpy as np


# Function to calculate intrinsic carrier concentration
def calculate_n_i(T, E_g, B):
    k = 8.62e-5  # Boltzmann constant in eV/K
    n_i = B * T ** (1.5) * np.exp(-E_g / (2 * k * T))
    return n_i


def main():
    T = input("Value of T (default tp 300): ")
    E_g = input("Value of E_g (default to 1.12): ")
    B = input("Value of B (default to 7.3e15): ")
    # Calculate n_i and output the result
    if T == '':
        T = 300
    else:
        T = float(T)
    if E_g == '':
        E_g = 1.12
    else:
        E_g = float(E_g)
    if B == '':
        B = 7.3e15
    else:
        B = float(B)
    n_i = calculate_n_i(T, E_g, B)
    print("{:e}".format(n_i))


if __name__ == '__main__':
    main()
