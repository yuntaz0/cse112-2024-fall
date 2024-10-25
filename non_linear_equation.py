from scipy.optimize import fsolve
from math import e
import numpy as np


def equation(x):
    return 0.0028 - 1e-14 * e ** (x/0.025)


def main():
    print(fsolve(equation, 1))


if __name__ == '__main__':
    main()
