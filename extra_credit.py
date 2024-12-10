import numpy as np
import matplotlib.pyplot as plt

# Redefine the CMOS simulation functions and parameters

def mos_current(V_GS, V_DS, V_th: float, k: float):
    """
    Calculate MOSFET current for NMOS or PMOS.
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


def simulate_cmos(V_in, V_dd, V_th, k_n, k_p, C_L, time_step):
    """
    Simulates the output voltage of a CMOS inverter given an input waveform.
    Args:
        V_in: Input voltage waveform (numpy array).
        V_dd: Supply voltage.
        V_th: Threshold voltage (assumes Vtn = |Vtp|).
        k_n: NMOS transconductance parameter.
        k_p: PMOS transconductance parameter.
        C_L: Load capacitance.
        time_step: Time step for simulation.
    Returns:
        V_out: Output voltage waveform (numpy array).
    """
    V_out = np.zeros_like(V_in)  # Initialize output voltage array
    for i in range(1, len(V_in)):
        V_GS_N = V_in[i]  # NMOS V_GS = V_in
        V_SG_P = V_dd - V_in[i]  # PMOS V_GS = V_in - V_dd
        V_DS_N = V_out[i - 1]  # NMOS V_DS = V_out
        V_SD_P = V_dd - V_out[i - 1]  # PMOS V_DS = V_out - V_dd

        I_N = mos_current(V_GS_N, V_DS_N, V_th, k_n)
        I_P = mos_current(V_SG_P, V_SD_P, V_th, k_p)

        I_net = I_P - I_N  # Net current charging/discharging C_L
        dV_out = (I_net / C_L) * time_step  # Voltage change on the capacitor
        V_out[i] = V_out[i - 1] + dV_out  # Update V_out considering the time step

    return V_out


# Simulation parameters
T = 10e-9  # Period of the input square wave
V_dd = 5.0  # Supply voltage
V_th = 1.0  # Threshold voltage
k_n = 1e-3  # NMOS transconductance (1 mA/V^2)
k_p = 1e-3  # PMOS transconductance (1 mA/V^2)
C_L = 1e-12  # Load capacitance (1 pF)
time_step = 1e-12  # Time step (1 ps)

# Input square wave
duration = 5 * T
time = np.arange(0, duration, time_step)
V_in = 5 * (np.sign(np.sin(2 * np.pi * (1 / T) * time)) > 0).astype(float)

# First CMOS simulation
V_out = simulate_cmos(V_in, V_dd, V_th, k_n, k_p, C_L, time_step)

# Use the output as the new input and simulate again
V_in_new = V_out.copy()
V_out_new = simulate_cmos(V_in_new, V_dd, V_th, k_n, k_p, C_L, time_step)

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(time * 1e9, V_in, label="Original V_in (Square Wave)", linestyle="--", color="blue")
plt.plot(time * 1e9, V_out, label="First V_out (CMOS Output)", color="orange")
plt.plot(time * 1e9, V_out_new, label="Second V_out (New CMOS Output)", color="green")
plt.xlabel("Time (ns)")
plt.ylabel("Voltage (V)")
plt.title("CMOS Inverter Chain Simulation")
plt.legend()
plt.grid()
plt.show()
