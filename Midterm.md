# Midterm

## Particle Physics

$$R = \rho \cdot \frac{l}{A}$$
$$n_i = B \cdot T ^ {\frac{3}{2}} \cdot e^{\frac{E_g}{2k \cdot T}} \approx 10^{10}$$
$$n_n \simeq N_D \gg n_i$$
$$p_p \simeq N_A \gg n_i$$
$$p_n \cdot n_n(N_D) = n_i ^ 2$$
$$p_p (N_A)\cdot n_p = n_i ^ 2$$
$$\sigma = q(p \mu _p +n \mu_n)$$
$$v_d = -\frac{e \tau}{m} E = -\mu E$$
$$E = \frac{V}{L}$$
$$\vec{J} = \vec{\sigma} \cdot \vec{E} = \frac{I}{A}$$

## Diode

- Turn on voltage: $V_f$
- Voltage drop: $V_d$
- ON / OFF Model
$$I_d(V_d) = I_s(e^{\frac{V_d}{V_T}}-1)$$
## MOSFET

 IF $V_{GS} < V_{th}$ THEN NMOS is in "cutoff" mode: $$I_{ds} = 0$$
- ELSE IF $V_{GS} \geq V_{th} \quad \text{and} \quad  V_{DS} < V_{GS} - V_{th} \quad \text{or} \quad V_{GD} \gt V_{th}$ THEN NMOS is in **TRIODE** mode: $$I_{DS} = k_n \times \left((V_{GS} - V_{th}) \times V_{DS} - \frac{1}{2} V_{DS}^2 \right)$$
- ELSE IF $V_{GS} \geq V_{th} \quad \text{and} \quad V_{DS} \geq V_{GS} - V_{th} \quad \text{or} \quad V_{GD} \leq V_{th}$ THEN NMOS is in **SATURATION** mode: $$I_{DS} = \frac{k_n}{2} (V_{GS} - V_{th})^2$$
- Transconductance parameter: $$k_n = k_n' \times \frac{W}{L}$$
$$k_n'=C_{ox} \times \mu_n$$
- Oxide Capacitance per unit area: $$C_{ox} = \frac{\epsilon _{ox}}{t_{ox}} = \frac{\epsilon _r \times \epsilon _0}{t_{ox}} = \frac{3.9 \times 8.854 \times10 ^ {-14}}{t_{ox}}$$
- $\mu_n$: electron mobility
- $W$: Gate width of the transistor
- $L$: Gate length of the transistor

$$g_{DS} = k_n(V_{DS} -V_{th} - V_{DS})$$