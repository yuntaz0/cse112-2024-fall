import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    I_O = 5e-4
    I_s = 1e-15
    V_T = 0.026
    V_d = np.linspace(0, 1, 1000)
    R_L_values = (10_000, 5_000, 2_000, 1_000)

    plt.figure(figsize=(10, 6))
    for R_L in R_L_values:
        I_d = I_s * (np.e ** (V_d / V_T) - 1)
        I_spy = I_O - I_d
        I_L = V_d / R_L
        plt.plot(V_d, I_spy, label=f'I_spy for R_L={R_L} Ω')
        plt.plot(V_d, I_L, linestyle='--', label=f'I_L for R_L={R_L} Ω')

    plt.xlabel('Voltage (V)')
    plt.ylabel('Current (A)')
    plt.title('I_d and I_L vs V_d for different R_L values')
    plt.axhline(0, color='black', linewidth=0.5)  # Horizontal axis
    plt.axvline(0, color='black', linewidth=0.5)  # Vertical axis
    plt.ylim(0, 1e-3)
    plt.legend()
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.show()
