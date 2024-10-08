# Lecture Note

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

### Formula

- Resistance: $$R = \frac{V}{I}$$
- Resistivity: $$\rho = R \cdot \frac{A}{l}$$
- Resistance in term of resistivity: $$ R = \rho \cdot \frac{l}{A}$$
	- $\rho$ : material parameter
	- $L$: length, depends on physical dimension
	- $A$: area, depends on physical dimension

- Capacity: $$C = \frac{Q}{V}$$
- Conductivity: $$\sigma = \frac{1}{\rho}$$
	- reciprocal of resistivity

- Resistance in term of conductivity: $$\frac{1}{\sigma} \cdot \frac{l}{A}$$

### Common Material & Their Resistivity

Copper (Cu): $1.7 \times 10 ^ {-8}\Omega \cdot m$ -> conductor
Ni-chrome (Ni & Chrome Alloy): $1.1 \times 10 ^{-6}\Omega \cdot m$ -> resistor, heater
Graphite (Carbon): $10 ^ {-5} \Omega \cdot m$ -> More resistant, electrode material

### Conductivity $\sigma$ Expression

$$\mathbf{J} = \rho \cdot \mathbf{v}_d = q \cdot \mathbf{n} \cdot \mathbf{v}_d = \frac{I}{A}$$

The flow of charged particles in a conductive material form the flow of electric current. 
- Current Density $\mathbf{J}$
	- The amount of electric current flowing through a cross-sectional area (per unit area) of a conductor. *Current per unit area*
	- Amperes per square meter
	- $A/m^2$

- Elementary Charge $q$
	- The charge of a single carrier; electron $= -1.6 \times 10 ^{-19}C$; hole $= 1.6 \times 10 ^ {19} C$
	- Coulombs
	- $C$

- Charge Carrier Density $\mathbf{n}$
	- Number of charge carriers per unit volume in the material
	- fundamental material property
	- Number er cubic meter
	- $m^{-3}$

- Drift Velocity $\mathbf{v}_d$
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

$$m \frac{d\mathbf{v}_d}{dt} + m \frac{\mathbf{v}_d}{\tau}= -e \mathbf{E}$$

$$m \frac{d\mathbf{v}_d}{dt} = -e \mathbf{E} - m \frac{\mathbf{v}_d}{\tau}$$

- Electric force $-e \mathbf{E}$
	- Accelerate the charge carrier
	- The charge of an electron $-e$
		- $-1.6 \times 10 ^ {-19} C$
	
	- The electric field applied across the conductor $\mathbf{E}$
		- Vole per meter $V/m$
		- Newton per coulomb $N/C$

- Acceleration Force $m \frac{d\mathbf{v}_d}{dt}$
	- Mass of the charge carrier $m$
		- typically is an election: $9.11 \times 10 ^ {-31} kg$
		- kilogram
		- $kg$
	
	- Acceleration of the charged carrier $\frac{d\mathbf{v}_d}{dt}$
		- $d$: infinitesimal change, how quantity is changing with respect to another
		- the rate of change of drift velocity ($\mathbf{v}_d$) with respect to time ($t$)

- Damping Force $- m \frac{\mathbf{v}_d}{\tau}$
	- slow down the charge carrier
	- resistive force due to collisions between the charged carriers and atoms in the conductor
	- $\tau$
		- relaxation (average) time between successive collisions
		- `\tau`

- The higher $V_d$, the smaller $\frac{dV_d}{dt}$ . So exact drift velocity can be consider as approximate as **steady-state drift velocity**

### Steady-state Drift Velocity ($dt = \tau$)

The electric force accelerate the charge carrier and the damping force slowing down the charge carriers reach as balance -> steady-state drift velocity -> $\frac{dV_d}{dt} = 0$, and $V_d$ become a constant.

$$m \frac{\mathbf{v}_d}{\tau}= -e \mathbf{E}$$
$$\mathbf{v}_d = -\frac{e \tau}{m} \mathbf{E}$$

Substitute ${\mathbf{v}_d}$ into the current density equation:

$$\mathbf{J} = \rho \cdot \mathbf{v}_d = q \cdot \mathbf{n} \cdot \mathbf{v}_d$$
$$\mathbf{J} = (-e) \cdot n \cdot \left( -\frac{e \tau}{m} \mathbf{E} \right)$$
$$\mathbf{J} = \frac{e^2 n \tau}{m} \mathbf{E}$$

- The current density $\mathbf{J}$ is directly proportional to the electric field $\mathbf{E}$
- $\frac{e^2 n \tau}{m}$ is effective a proportionality constant, conductivity $\sigma$
- This is Ohm's Law in different form: **the current density in proportional to electric field**, with the conductivity $\sigma$ being the proportionality constant.

$$\sigma = \frac{e^2 n \tau}{m}$$

- $e$ - Elementary charge of an electron ($-1.6 \times 10^{-19}C$)
- $n$ - Number density of charge carriers in ($m^{-3}$), which represents how many charge carrier are present per unit volume of the material
- $\tau$ - Relaxation time; average time between collisions between electrons and atoms in the conductor
- $m$ - Mass of the charge carrier, typically the mass of an electron $9.11 \times 10 ^ {-31}kg$
- For a given material at constant temperature, $e$, $m$, $\tau$ can be considered as constants together called **carrier mobility $\mu = \frac{e \tau}{m}$**; $n$, however, can vary based on **doping**; 
	- higher carrier density allows for a better response to an electric field
	- carrier density is important to determining the current-carrying capability and heat dissipation
- $\mu$ - Carrier Mobility represents the velocity of a charge carrier per unit electric field applied
	- the magnitude of the mobility so negative sign is omitted
	- $$\mathbf{v}_d = -\frac{e \tau}{m} \mathbf{E}=-\mu\mathbf{E}$$
	- $$\mu = \frac{e \tau}{m}=\frac{\mathbf{v_d}}{\mathbf{E}}$$
$$\sigma=nq\mu$$
	- $q$ - Charge of the carrier
### Doping - alter the electrical properties of a semiconductor

adding impurities to a pure semiconductor; increase the number of free charge carriers

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
- N-type Semiconductor
	- Dopant: an element with more valence electrons that the host
	- Free carrier: electrons
- P-type Semiconductor
	- Dopant: an element with fewer valence electrons than the host
	- Free carrier: holes