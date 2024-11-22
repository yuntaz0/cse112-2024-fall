# Lecture Note

## Unit

| Prefix | Symbol | Power of 10 | Example                                 |
| ------ | ------ | ----------- | --------------------------------------- |
| Tera   | T      | $10^{12}$   | 1 terawatt (TW) = $10^{12}$ watts       |
| Giga   | G      | $10^{9}$    | 1 gigahertz (GHz) = $10^9$ hertz        |
| Mega   | M      | $10^{6}$    | 1 megabyte (MB) = $10^6$ bytes          |
| Kilo   | k      | $10^{3}$    | 1 kilometer (km) = $10^3$ meters        |
| -      | -      | $10^{0}$    | 1 meter (m) = $10^0$ meters             |
| Milli  | m      | $10^{-3}$   | 1 millivolt (mV) = $10^{-3}$ volts      |
| Micro  | µ      | $10^{-6}$   | 1 microfarad (µF) = $10^{-6}$ farads    |
| Nano   | n      | $10^{-9}$   | 1 nanometer (nm) = $10^{-9}$ meters     |
| Pico   | p      | $10^{-12}$  | 1 picofarad (pF) = $10^{-12}$ farads    |
| Femto  | f      | $10^{-15}$  | 1 femtoampere (fA) = $10^{-15}$ amperes |
| Atto   | a      | $10^{-18}$  | 1 attosecond (as) = $10^{-18}$ seconds  |

## Formula

- **Resistance**: $$R = \frac{V}{I}$$
- **Conductance**: $$G = \frac{I}{V} = \frac{1}{R}$$ 
- **Resistivity**: $$\rho = R \cdot \frac{A}{l}$$
- **Resistance** in term of resistivity: $$R = \rho \cdot \frac{l}{A}$$
	- $\rho$ : material parameter
	- $L$: length, depends on physical dimension
	- $A$: area, depends on physical dimension

- **Capacity**: $$C = \frac{Q}{V}$$
- **Conductivity**: $$\sigma = \frac{1}{\rho} = ne\mu = \frac{e^2 n \tau}{m}$$
	- reciprocal of resistivity

- **Resistance** in term of conductivity: $$\frac{1}{\sigma} \cdot \frac{l}{A}$$
- Charge density $\rho$: $$\rho = e \cdot n = q \cdot n$$
- Current Density $\vec{J}$: $$\vec{J} = \rho \cdot \vec{v_d} = q \cdot n \cdot \vec{v_d} = \frac{I}{A} = \sigma \cdot E $$
- charge carrier motion: $$m \frac{dv_d}{dt} = -e E - m \frac{v_d}{\tau}$$
- drift velocity $Vd$: $$v_d = -\frac{e \tau}{m} E$$
- carrier mobility $\mu$: $$\mu = \frac{e \tau}{m}$$

## Week 0

### Schedule

- Homework: No required, but good practice
- Quiz: start from Oct.12th, from 9 am to 9 pm. Lowest one drop
- Exam: Mid 1 on week 6 Monday; Mid 2 on week 10 Wed; Final Wed, Dec 11, 4:00-6:00 pm

## Week 1

### Resistor: carbon, metal, nichrome

- **nichrome**: best for high power, high temperature
- **metal**: precision and low noise
- **carbon**: low cost and general purpose
- **carbon composition resistor**: carbon powder mixed with a binding resin or plastic, formed into a cylindrical shape and the ratio of carbon to the binder determines the resistance.
- **carbon file resistor**: ceramic core with a thin carbon file deposited around it. The thickness of the carbon file or cutting a helical groove in the file (width and length) control the resistance.
- **metal file and metal oxide resistor**: ceramic core with a thin metal film or metal oxide layer. The shape of the film determine the resistance
- **wire-wound resistor**: The main resistive component of nichrome wire (resistive alloy) around a ceramic core. handle more current and dissipate more heat due to its high resistance per unit length, high melting point and thermal stability (resistance does not very significantly with temperature). The resistance is controlled by length, diameter of number of turns of the wire
- film: thin layer or coating

### Physical Concept

- **Resistance**: opposition to the flow of electric current
	- Symbol: $R$
	- Unit:
		- Ohm
		- $\Omega$
		- `\Omega`

- **Resistivity**: a material's ability to resist electric current
	- Symbol: $\rho$
	- Pronunciation: "row"
	- Latex Name: `\rho`
	- Unit
		- Ohm-meter
		- $\Omega \cdot m$

- **Capacitance**: the capacity of a material to store electric charge
	- Symbol: $C$
	- Unit:
		- Farad
		- $F$

- **Conductivity**: a material's ability to conduct electric current
	- Symbol: $\sigma$
	- Latex Name: `\sigma`
	- Unit:
		- Siemens per meter
		- $S/m$

- **Power**: the amount of energy transferred per unit time
	- Symbol: $P$
	- Unit:
		- Watt
		- $W$

- **Permittivity**: a measure of the electric polarizability of a dielectric material
	- high permittivity polarizes more in response to an applied electric field
	- Symbol: $\varepsilon, \epsilon$
	- Latex Name: `\varepsilon` or `\epsilon`
	- Unit
		- Farads per meter
		- $F/m$

### Common Material & Their Resistivity

Copper (Cu): $1.7 \times 10 ^ {-8}\Omega \cdot m$ -> conductor
Ni-chrome (Ni & Chrome Alloy): $1.1 \times 10 ^{-6}\Omega \cdot m$ -> resistor, heater
Graphite (Carbon): $10 ^ {-5} \Omega \cdot m$ -> More resistant, electrode material

### Conductivity $\sigma$ Expression

$$J = \rho \cdot v_d = e \cdot n \cdot v_d = \frac{I}{A}$$

The flow of charged particles in a conductive material form the flow of electric current. 
- Charge density $\rho$
	- amount of electric charge per unit volume
	- Coulombs per cubic meter
	- $C/m^3$
	
- Current Density $J$
	- The amount of electric current flowing through a cross-sectional area (per unit area) of a conductor. *Current per unit area*
	- Amperes per square meter
	- $A/m^2$

- Elementary Charge $q$ or $e$
	- The charge of a single carrier; electron $= -1.6 \times 10 ^{-19}C$; hole $= 1.6 \times 10 ^ {19} C$
	- Coulombs
	- $C$

- Charge Carrier Density $n$
	- Number of charge carriers per unit volume in the material
	- fundamental material property
	- Number er cubic meter
	- $m^{-3}$

- Drift Velocity $v_d$
	- the average (slow, guided, net, additional to normal, existed random movement) velocity at which charge carriers move through a material when subjected to electric field.
	- because of collision, electron's drift velocity will sometime drop to 0 and the electron will restart acceleration
	- Meters per second
	- $m/s$

- Direction: 
	- The flow will always be the same as electric field (or conventional current flow or movement of positive charge)
	- positive charge ($q > 0$), drift velocity is in the same direction as electric field
	- negative charge($q<0$), drift velocity is in the opposite direction as electric field

### Motion of a charge carrier

The electric field exerts a **force** on the electron, trying to **accelerate** it in a direction opposite to the field. As the electron moves, it encounters **collisions** with atoms in the conductor. After each collision, the drift velocity drops, and the electric field **re-accelerate** the electron. The **steady-state drift velocity** is achieved when the **acceleration** caused by the **electric force** is balanced by the **damping effects** due to collisions.

$$F = ma$$

$$-e E = m \frac{dv_d}{dt} + m \frac{v_d}{\tau}$$

$$m \frac{dv_d}{dt} = -e E - m \frac{v_d}{\tau}$$

- Electric force $-e E$
	- Accelerate the charge carrier
	- The charge of an electron $-e$
		- $-1.6 \times 10 ^ {-19} C$
	
	- The electric field applied across the conductor $E$
		- Vole per meter $V/m$
		- Newton per coulomb $N/C$

- Acceleration Force $m \frac{dv_d}{dt}$
	- Mass of the charge carrier $m$
		- typically is an election: $9.11 \times 10 ^ {-31} kg$
		- kilogram
		- $kg$
	
	- Acceleration of the charged carrier $\frac{dv_d}{dt}$
		- $d$: infinitesimal change, how quantity is changing with respect to another
		- the rate of change of drift velocity ($v_d$) with respect to time ($t$)

- Damping Force $- m \frac{v_d}{\tau}$
	- slow down the charge carrier
	- resistive force due to collisions between the charged carriers and atoms in the conductor
	- $\tau$
		- relaxation (average) time between successive collisions
		- `\tau`

- The higher $V_d$, the smaller $\frac{dV_d}{dt}$ . So exact drift velocity can be consider as approximate as **steady-state drift velocity**

### Steady-state Drift Velocity ($\frac{dv_d}{dt} = 0$)

- The electric force accelerate the charge carrier and the damping force slowing down the charge carriers reach as balance
- $\frac{d v_d}{dt} = 0$, and $v_d$ become a constant.

$$m \frac{v_d}{\tau}= -e E$$
$$v_d = -\frac{e \tau}{m} E$$

Substitute ${v_d}$ into the current density equation:

$$J = \rho \cdot v_d = q \cdot n \cdot v_d$$
$$J = (-e) \cdot n \cdot \left( -\frac{e \tau}{m} E \right)$$
$$J = \frac{e^2 n \tau}{m} E$$

- The current density $J$ is directly proportional to the electric field $E$
- $\frac{e^2 n \tau}{m}$ is effective a proportionality constant, conductivity $\sigma$
- This is Ohm's Law in different form: **the current density in proportional to electric field**, with the conductivity $\sigma$ being the proportionality constant.

$$\sigma = \frac{e^2 n \tau}{m}$$
$$\vec{J} = \vec{\sigma} \cdot \vec{E}$$

- $e$ - Elementary charge of an electron ($-1.6 \times 10^{-19}C$)
- $n$ - Number density of charge carriers in ($m^{-3}$), which represents how many charge carrier are present per unit volume of the material
- $\tau$ - Relaxation time; average time between collisions between electrons and atoms in the conductor
- $m$ - Mass of the charge carrier, typically the mass of an electron $9.11 \times 10 ^ {-31}kg$
- For a given material at constant temperature, $e$, $m$, $\tau$ can be considered as constants together called **carrier mobility $\mu = \frac{e \tau}{m}$**; $n$, however, can vary based on **doping**; 
	- higher carrier density allows for a better response to an electric field
	- carrier density is important to determining the current-carrying capability and heat dissipation
- $\mu$ - Carrier Mobility represents the velocity of a charge carrier per unit electric field applied
	- the magnitude of the mobility so negative sign is omitted
	- $$v_d = -\frac{e \tau}{m} E=-\mu E$$
	- $$v_{\text{p-drift}} = \mu E$$
	
	- $$\mu = \frac{e \tau}{m}=\frac{vd}{E}$$
$$\sigma=ne\mu$$
	- $q$ - Charge of the carrie

### Doping - alter the electrical properties of a semiconductor

adding impurities to a pure semiconductor; increase **the number of free charge carriers ${n}$**

- dopants: impurity atoms that **replace** some of the silicon atoms at lattice position, becoming the part of the crystal structure and long-range order (repeating pattern)
	- Long-Range Order in Crystal
		- Each silicon atom is bonded in a regular tetrahedral structure to four neighboring silicon atoms
		- In a crystal, the atoms are arranged in a periodic structure that repeats in a predictable way over long distance throughout the entire material
		- each atom has a well-defined position relative to its neighbors
		- this arrangement extends uniformly across the crystal lattice
		- results of its electrical, optical, and mechanical characteristic
- a well-controlled modification of electric properties
	- Ion implantation - bombarding the silicon crystal with dopant ions at high energy, allows dopant ions to penetrate the crystal and take up positions within the lattice
	- Diffusion - silicon crystal is exposed to a dopant gas at high temperature, allowing the dopant atoms to diffuse into the silicon and replace some silicon
	- **Human control** over doping lies in the ability to **precisely control the concentration** of dopant atoms, the **depth** to which they penetrate the silicon, and the **uniformity** of their distribution.
	- **Modern semiconductor manufacturing** is highly advanced and uses tools like **ion implanters** that can precisely control the dose and energy of the dopant ions to achieve a specific **doping profile**.
	- **Annealing** involves heating the silicon to allow any disruptions in the lattice caused by the introduction of dopant atoms to settle, ensuring that the dopant atoms properly integrate into substitutional positions without causing defects.
- doping levels are very low - typically on the order of parts per million (ppm) - so doping atoms do NOT significantly change the material's crystal structure or physical characteristics
	- Alloying
		- purpose is to enhance mechanical properties.
		- the atoms of the alloying elements are **mixed into** the crystal structure of the base metal, which significantly alters the crystal lattice
		- the concentration of the alloying elements is much higher compared to doping (x percent)

#### Charge Carriers

- hole concentration $p$, electron concentration $n$
- intrinsic carrier concentration $n_i$
	- because every electron that is thermally excited from the valence band to the conduction band leaves behind a hole
		- $$n = p = n_i$$
		- electrons are constantly being thermally excited from the valence band to the conduction band, creating electron-hole pairs. At the same time, electrons in the conduction band recombine with holes in the valence band. The rates of generation and recombination are balanced in thermal equilibrium.
	- $p \cdot n = {n_i}^2$ where $n_i$ is the number of charge carriers in a unit volume of intrinsic silicon at a given temperature
	- $n_i$ depends on temperature
		- $$n_i = B \cdot T ^ {\frac{3}{2}} \cdot e^{\frac{E_g}{2k \cdot T}} \approx 10^{10}$$
		- At room temperature (300 Kelvin)
		- $E_g = 1.12eV$
		- $K = \frac{0.026}{300}ev/Kelvin$
		- $K \cdot T = 0.026eV$
- **N-type Semiconductor**
	- Dopant: an element with more valence electrons that the host
	- Concentration of **donor** atom ($N_D$) is *the number of charge carriers of N-type silicon* as the donor atom concentration is much larger than the number of natural charge carriers:$$n_n \simeq N_D \gg n_i$$ 
	- hence: $$p_n \simeq \frac{{n_i}^2}{N_D}$$
	- **Free carrier: electrons**
- **P-type Semiconductor**
	- Dopant: an element with fewer valence electrons than the host
	- Concentration of **acceptor** atom ($N_A$) is the number of charge carriers of P-type silicon as the concentration of acceptor atom is much larger than the number of natural charge carrier: $$p_p \simeq N_A \gg n_i$$
	- **Free carrier: holes**
- P and N type semiconductor are both **neutral** 
- **Law of mass action**: under thermal equilibrium, the product of the free electron concentration $n$ and the free hole concentration $p$ is equal to a constant square of intrinsic carrier concentration $n$. The intrinsic carrier concentration is a function of temperature.
	- $$p \cdot n = {n_i}^2$$
	- $$p_n \cdot n_n = n_i ^ 2$$
	- $$p_p \cdot n_p = n_i ^ 2$$

##### Key Factors Balancing Carriers

1. **Thermal Generation and Recombination**:
    - In a semiconductor, free electrons and holes are continuously generated and recombine. At equilibrium, the rate of thermal generation of electron-hole pairs is exactly balanced by the recombination rate.
    - Doping increases the concentration of one type of carrier (either electrons for n-type or holes for p-type). However, the presence of more electrons (for example) increases the **recombination rate** because **more free electrons are available to recombine with holes**. This increased recombination reduces the number of holes, so the product $n \cdot p$ remains constant at ${n_i}^2$​.
2. **Fermi Level Shift**:
    - Doping changes the **Fermi level**, which is a measure of the probability that energy states are occupied by electrons.
    - In **n-type** semiconductors, the Fermi level moves closer to the conduction band, increasing the number of electrons $n$. Because the Fermi level moves, it decreases the probability of finding electrons in the valence band, which results in fewer holes $p$.
    - In **p-type** semiconductors, the Fermi level moves closer to the valence band, increasing the hole concentration $p$ and reducing the electron concentration $n$.
    - The shift in Fermi level is a key factor that causes an inverse relationship between the concentrations of electrons and holes, ensuring that $n \cdot p$ stays balanced.
3. **Exponential Dependence on Energy Gap**:
    - The concentration of carriers (both electrons and holes) is **exponentially dependent** on the difference between the Fermi level and the energy band edges (conduction band for electrons, valence band for holes).
    - This means that a small shift in the Fermi level (due to doping) causes a large change in the concentration of electrons or holes.
    - Because of this exponential relationship, when one carrier type increases due to doping, the other carrier type decreases exponentially, which helps maintain the equilibrium condition $n⋅p=n_i^2​$.

###### Understanding the Balance Mechanism

Let’s use **n-type doping** as an example:

- When donor atoms are introduced, they contribute extra free electrons to the conduction band, increasing $n$. However, these additional electrons increase the likelihood of recombination with holes.
- As electrons recombine with holes more frequently, the hole concentration $p$ decreases. The material cannot support an unlimited increase in free electrons without reducing the hole concentration because the two types of carriers recombine.
- Since $n \cdot p$ must remain equal to $n_i^2$​, if $n$ increases due to doping, $p$ must decrease proportionally to maintain the equilibrium.

The same explanation applies to **p-type doping**, where the introduction of acceptor atoms increases the hole concentration $p$, causing a reduction in the electron concentration $n$ to balance the equation.

###### Summary

In either case (n-type or p-type), the balance between the increase in one type of carrier and the decrease in the other is governed by the following mechanisms:

- Increased recombination due to higher carrier concentrations.
- Shifts in the Fermi level that alter the relative concentrations of electrons and holes.
- The exponential relationship between carrier concentration and energy levels.

### Current density $J$ in Other Form

Previously,

- $$v_d = -\frac{e \tau}{m} E=-\mu E$$
- $$J = \rho \cdot v_d = q \cdot n \cdot v_d$$

Now,
- $$v_{\text{p-drift}} = \mu_p E$$
- $$v_{\text{n-drift}} = -\mu_n E$$

- P-Type
	- where $e = q$ (magnitude of electron charge) and $n = p$ (the concentration of charged carrier):
	
	- For positive charge carriers: $$J_p = \frac{I_p}{A} = qp \mu _p E$$
	- For negative charge carriers: $$J_n = \frac{I_n}{A} = qn \mu _n E$$
	- Total drift current density: $$J = J_p + J_n = q(p \mu _p +n \mu_n)E = \sigma E = \frac{E}{\rho}$$
	- Conductivity: $$\sigma = q(p \mu _p +n \mu_n)$$
	- Resistivity: $$\rho = \frac{E}{J} = \frac{1}{q(p \mu _p +n \mu_n)}$$

### P-N Junction

Connecting the two materials causes creation of a *depletion region* near the boundary, as the free electrons fill the available holes, which in turn allows electric current to pass through the junction only in one direction.

#### Depletion Region - charge carriers that can move are depleted,


- How is it form
	By definition, the N-type semiconductor has an excess of free electrons (in the conduction band compared to the P-type semiconductor, and the P-type has an excess of holes (in the valence band) compared to the N-type. Therefore, when N-doped and P-doped semiconductors are placed together to form a junction, free electrons in the N-side conduction band migrate (diffuse) into the P-side conduction band, and holes in the P-side valence band migrate into the N-side valence band.
	
	Following transfer, the diffused electrons come into contact with holes and are eliminated by recombination in the P-side. Likewise, the diffused holes are recombined with free electrons so eliminated in the N-side. The net result is that the diffused electrons and holes are gone. In a N-side region near to the junction interface, free electrons in the conduction band are gone due to (1) the diffusion of electrons to the P-side and (2) recombination of electrons to holes that are diffused from the P-side. Holes in a P-side region near to the interface are also gone by a similar reason. As a result, majority charge carriers (free electrons for the N-type semiconductor, and holes for the P-type semiconductor) are depleted in the region around the junction interface, so this region is called the **depletion region** or **depletion zone**. Due to the majority charge carrier diffusion described above, the depletion region is charged; the N-side of it is positively charged and the P-side of it is negatively charged. This creates an electric field that provides a force opposing the charge diffusion. When the electric field is sufficiently strong to cease further diffusion of holes and electrons, the depletion region reaches the equilibrium. Integrating the electric field across the depletion region determines what is called the **built-in voltage** (also called the junction voltage or barrier voltage or contact potential) around $0.7V$.
	- **Diffusion**: the movement of electrons and holes from areas of high concentration to areas of low concentration; electron from N-type to P-type and holes from P-type to N-type
	- **Recombination**: the process where electrons and holes meet in the middle and neutralize each other, leaving behind immobile ions, causing depletion region
	- **Drift**: the movement of electrons and holes under the influence of the built-in electric field
- Bias
	- Forward bias: P-type (currently negative) is applied positive voltage and N-type (currently positive) is applied negative voltage; the external voltage is opposite of built-in voltage
		- Depletion region is reduced
		- Lower potential barrier 
		- **Most** electron can pass through
	- Reverse bias: P-type (currently negative) is applied negative voltage and N-type (currently positive) is applied positive voltage; the external voltage is reinforcing built-in voltage
		- Depletion region is widen
		- Increase potential barrier
		- **Few** electron can pass through
- 0 State: depletion layer
- 1 State: depletion layer is overcome by added voltage 
	
## Diode - P-N junction in circuit

$$I_d(V_d) = I_s(e^{\frac{V_d}{V_T}}-1)$$
- ―⯈⊢
- `2015`, `2bc8`, `22a2`

## MOSFET

### NMOS

- $V_{th} = V_{tn}$
- IF $V_{GS} < V_{th}$ THEN NMOS is in "cutoff" mode: $$I_{DS} = 0$$
- ELSE IF $V_{GS} \geq V_{th} \quad \text{and} \quad  V_{DS} < V_{GS} - V_{th} \quad \text{or} \quad V_{GD} \gt V_{th}$ THEN NMOS is in **TRIODE** mode: $$I_{DS} = k_n \left((V_{GS} - V_{th}) \times V_{DS} - \frac{1}{2} V_{DS}^2 \right)$$
- ELSE IF $V_{GS} \geq V_{th} \quad \text{and} \quad V_{DS} \geq V_{GS} - V_{th} \quad \text{or} \quad V_{GD} \leq V_{th}$ THEN NMOS is in **SATURATION** mode: $$I_{DS} = \frac{k_n}{2} (V_{GS} - V_{th})^2$$

### PMOS

- $V_{th} = -V_{tp}$
- IF $V_{SG} < V_{th}$ THEN PMOS is in "cutoff" mode: $$I_{SD} = 0$$
- ELSE IF $V_{SG} \geq V_{th} \quad \text{and} \quad  V_{SD} < V_{SG} - V_{th} \quad \text{or} \quad V_{DG} \gt V_{th}$ THEN NMOS is in **TRIODE** mode: $$I_{SD} = k_p \left((V_{SG} - V_{th}) \times V_{SD} - \frac{1}{2} V_{SD}^2 \right)$$
- ELSE IF $V_{SG} \geq V_{th} \quad \text{and} \quad V_{SD} \geq V_{SG} - V_{th} \quad \text{or} \quad V_{DG} \leq V_{th}$ THEN NMOS is in **SATURATION** mode: $$I_{SD} = \frac{k_p}{2} (V_{SG} - V_{th})^2$$

- Transconductance parameter: $$k = k' \times \frac{W}{L}$$
$$k'=C_{ox} \times \mu$$
- Oxide Capacitance per unit area: $$C_{ox} = \frac{\epsilon _{ox}}{t_{ox}} = \frac{\epsilon _r \times \epsilon _0}{t_{ox}} = \frac{3.9 \times 8.854 \times10 ^ {-14}}{t_{ox}}$$
- $\mu$: electron mobility
- $W$: Gate width of the transistor
- $L$: Gate length of the transistor
