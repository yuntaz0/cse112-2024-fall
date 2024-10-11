#!/usr/bin/env python3
import argparse
import sys


# Function to calculate the number of charge carriers based on doping concentration
def num_carrier(doping_concentration, n_i=1.5e10):
    return n_i ** 2 / doping_concentration


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Calculate the number of charge carriers based on doping concentration.")
    
    # Required positional argument for doping concentration
    parser.add_argument('doping_concentration', type=float, help='Doping concentration (e.g., 1e17)')
    
    # Optional positional argument for n_i with a default value
    parser.add_argument('n_i', type=float, nargs='?', default=1.5e10, help='Intrinsic carrier concentration (default is 1.5e10 for silicon at 300K)')

    args = parser.parse_args()

    # Calculate the number of charge carriers and output the result
    carrier_concentration = num_carrier(args.doping_concentration, args.n_i)
    print("{:e}".format(carrier_concentration))


if __name__ == '__main__':
    main()
