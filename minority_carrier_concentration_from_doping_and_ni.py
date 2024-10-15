#!/usr/bin/env python3
import argparse
import sys


# Function to calculate the number of charge carriers based on doping concentration
def num_carrier(doping_concentration, ni=1.5e10):
    return ni ** 2 / doping_concentration


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Calculate the number of charge carriers based on doping concentration.")
    parser.add_argument('doping_concentration', type=float, help='Doping concentration (e.g., 1e17)')
    parser.add_argument('--ni', type=float, default=None, help='Intrinsic carrier concentration (default is 1.5e10 for silicon at 300K)')

    args = parser.parse_args()

    # Check if ni is provided via command-line argument or pipe input
    if args.ni is None:
        if not sys.stdin.isatty():  # Check if there is input from a pipe
            try:
                args.ni = float(sys.stdin.read().strip())  # Read piped input for ni
            except ValueError:
                print("Error: Invalid intrinsic carrier concentration input.", file=sys.stderr)
                sys.exit(1)
        else:
            args.ni = 1.5e10  # Default value if neither --ni nor pipe is provided

    # Calculate the number of charge carriers and output the result
    carrier_concentration = num_carrier(args.doping_concentration, args.ni)
    print("{:e}".format(carrier_concentration))


if __name__ == '__main__':
    main()

