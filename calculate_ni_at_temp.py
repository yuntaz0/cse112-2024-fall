#!/usr/bin/env python3
import numpy as np
import sys
import argparse


# Function to calculate intrinsic carrier concentration
def N_i(T, E_g=1.12):
    B = 1.66e15  # Material-dependent constant
    k = 8.62e-5  # Boltzmann constant in eV/K
    n_i = B * T ** (1.5) * np.exp(-E_g / (2 * k * T))  # Intrinsic carrier concentration
    return n_i


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Calculate intrinsic carrier concentration (n_i) at a given temperature (T).")
    parser.add_argument('T', type=float, nargs='?', default=None, help='Temperature in Kelvin (T)')
    parser.add_argument('--E_g', type=float, default=1.12, help='Bandgap energy in eV (default is 1.12 eV for silicon)')
    
    args = parser.parse_args()

    # Check if temperature is provided via command-line or pipe input
    if args.T is None:
        if not sys.stdin.isatty():  # Check if there is input from a pipe
            try:
                args.T = float(sys.stdin.read().strip())
            except ValueError:
                print("Error: Invalid temperature input.", file=sys.stderr)
                sys.exit(1)
        else:
            print("Error: Temperature (T) must be provided either as a command-line argument or via standard input.", file=sys.stderr)
            sys.exit(1)

    # Calculate n_i and output the result
    n_i = N_i(args.T, args.E_g)
    print("{:e}".format(n_i))


if __name__ == '__main__':
    main()

