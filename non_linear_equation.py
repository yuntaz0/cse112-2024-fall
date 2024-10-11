from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt  # Optional, for plotting


# Define the equation
def equation(Vd):
    return 10**-12 * (np.exp(Vd / 0.026) - 1) * 1 + Vd - 5


# Use fsolve to find the root
initial_guess = 0.5
Vd_solution = fsolve(equation, initial_guess)

# Print the solution
print(f"The value of Vd is approximately: {Vd_solution[0]}")

# Optional: Plot the equation to visualize the function behavior
Vd_values = np.linspace(0, 1, 100)
equation_values = [equation(vd) for vd in Vd_values]
plt.plot(Vd_values, equation_values)
plt.axhline(0, color='red', linestyle='--')  # Add y=0 line for reference
plt.title("Visualization of the equation")
plt.xlabel("Vd")
plt.ylabel("Equation Value")
plt.show()

