"""
MOSFET VI Calculator
"""
import numpy as np
import matplotlib.pyplot as plt


def mos_current(V_GS, V_DS, V_th: float, k: float):
    """
    Args:
        V_GS: Gate-source voltage(s). Can be a single value or an array.
        V_DS: Drain-source voltage(s). Must match the shape of V_GS.
        V_th: Threshold voltage.
        k: Transconductance parameter.

    Returns:
        np.array: Calculated drain-source current(s) I_DS
    """
    I_DS = np.zeros_like(V_GS)
    triode_mode = (V_GS >= V_th) & (V_DS < V_GS - V_th)
    saturation_mode = (V_GS >= V_th) & (V_DS >= V_GS - V_th)

    I_DS[triode_mode] = k * ((V_GS[triode_mode] - V_th) * V_DS[triode_mode] - 0.5 * V_DS[triode_mode]**2)
    I_DS[saturation_mode] = 0.5 * k * (V_GS[saturation_mode] - V_th)**2

    return I_DS


def HW5_Q1():
    V_dd = 5
    V_ss = 0
    count = 100
    V_out = np.linspace(V_ss, V_dd, count)
    V_in_values = range(0, 6)

    # Parameters
    V_th = 1.0  # Threshold voltage
    k_n = 1.0   # NMOS Transconductance parameter
    k_p = 0.5   # PMOS Transconductance parameter

    plt.figure(figsize=(10, 6))

    # Plot PMOS curve
    V_SG = 5
    V_SD = 5 - V_out
    I_SD = mos_current(np.full_like(V_out, V_SG), V_SD, V_th, k_p)
    plt.plot(V_out, I_SD, label="PMOS", linestyle="--", color="black")

    # Plot NMOS curves for varying V_in values
    for V_in in V_in_values:
        V_GS = np.full_like(V_out, V_in)
        V_DS = V_out
        I_DS = mos_current(V_GS, V_DS, V_th, k_n)
        plt.plot(V_out, I_DS, label=rf"$V_{{in}} = {V_in}$ V")

    plt.xlabel(r"$V_{out}$ (V)", fontsize=16)
    plt.ylabel(r"$I_{DS}$ (mA)", fontsize=16)
    plt.title(r"I vs $V_{out}$ for Different $V_{in}$", fontsize=16)
    plt.legend(fontsize=14)
    plt.grid(True)

    plt.show()

def Quiz4_Q2():
    V_dd = 5
    V_ss = 0
    count = 100
    k_n = 1
    V_th = 1

    V_in = np.linspace(V_ss, V_dd, count)
    V_SG = V_dd - V_in
    V_SD = V_dd - I_SD
    plt.plot(V_out, V_out / 5.0, label=r"$V_{{out}} = I_{DS} * 5$ V")

    V_in_values = range(0, 6)
    for V_in in range(0, 6):
        V_GS = V_in - V_out
        V_DS = 5 - V_out
        I_DS = mos_current(np.full_like(V_out, V_GS), V_DS, V_th, k_n)
        plt.plot(V_out, I_DS, label=rf"$V_{{in}} = {V_in}$ V")

    plt.xlabel(r"$V_{out}$ (V)", fontsize=16)
    plt.ylabel(r"$I_{DS}$ (mA)", fontsize=16)
    plt.title(r"I vs $V_{out}$ for Different $V_{in}$", fontsize=16)
    plt.legend(fontsize=14)
    plt.grid(True)

    plt.show()

if __name__ == '__main__':
    HW5_Q1()
