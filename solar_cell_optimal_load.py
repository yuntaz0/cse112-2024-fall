import numpy as np
import matplotlib.pyplot as plt


def ideal_diode_model():
    I_O = 5e-4
    I_s = 1e-15
    V_T = 0.026
    V_d = np.linspace(0, 1, 1000)
    R_L_values = (10_000, 5_000, 2_000, 1_000)

    plt.figure(figsize=(10, 6))
    for R_L in R_L_values:
        I_L_from_load = V_d / R_L
        plt.plot(V_d, I_L_from_load, linestyle='--', label=f'I_L from load for R_L={R_L}Ω')
    I_d = I_s * (np.e ** (V_d / V_T) - 1)
    I_L_from_diode = I_O - I_d
    plt.plot(V_d, I_L_from_diode, label='I_L from diode')
    plt.xlabel('Voltage (V)')
    plt.ylabel('Current (A)')
    plt.title('I_L from and diode and current vs V_d for different R_L values')
    plt.axhline(0, color='black', linewidth=0.5)  # Horizontal axis
    plt.axvline(0, color='black', linewidth=0.5)  # Vertical axis
    plt.ylim(0, 1.1e-3)
    plt.legend()
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.show()


def on_off_model():
    # TODO: apply part b
    V_d = np.linspace(0, 1, 1000)
    R_L_values = (10_000, 5_000, 2_000, 1_000)
    I_O = 5e-4
    for R_L in R_L_values:
        I_L_from_load = V_d / R_L
        plt.plot(V_d, I_L_from_load, linestyle='--', label=f'I_L from load for R_L={R_L}Ω')
    I_L = np.zeros_like(V_d) + I_O
    plt.plot(V_d[V_d < 0.7], I_L[V_d < 0.7], label='I_L = I_O for V_d < 0.7', color='cyan')
    plt.axvline(0.7, ymax=I_O/1.1e-3, color='cyan', label='V_d = 0.7')
    plt.xlabel('Voltage (V)')
    plt.ylabel('Current (A)')
    plt.title('I_L from and diode and current vs V_d for different R_L values')
    plt.axhline(0, color='black', linewidth=0.5)  # Horizontal axis
    plt.axvline(0, color='black', linewidth=0.5)  # Vertical axis
    plt.ylim(0, 1.1e-3)
    plt.legend()
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.show()


if __name__ == '__main__':
    on_off_model()
