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

## Resistor to Semiconductor

- **Resistance**: $$R = \frac{V}{I}$$
- **Conductance**: $$G = \frac{I}{V} = \frac{1}{R}$$ 
- **Resistivity**: $$\rho = R \cdot \frac{A}{l}$$
- **Resistance** in term of resistivity: $$ R = \rho \cdot \frac{l}{A}$$
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

### Steady-state Drift Velocity

- ($\frac{dv_d}{dt} = 0$)
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
	- $q$ - Charge of the carrier

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



### Doping - alter the electrical properties of a semiconductor

- charge carriers in semiconductors can be either negatively charged (electron; n-type) or positively charge (hole: lack of the electron; p-type)
- adding impurities to a pure semiconductor; increase **the number of free charge carriers** ${N}$
	- carrier concentration
		- $n$: negative carrier concentration -> donor atoms -> n-type semiconductor
		- $p$: positive carrier concentration -> acceptor atoms -> p-type semiconductor
- dopant: impurity atoms that **replace** some of the silicon atoms at lattice position, becoming the part of the crystal structure and long-range order (repeating pattern)
	- Long-Range Order in Crystal
		- Each silicon atom is bonded in a regular tetrahedral structure to four neighboring silicon atoms
		- In a crystal, the atoms are arranged in a periodic structure that repeats in a predictable way over long distance throughout the entire material
		- each atom has a well-defined position relative to its neighbors
		- this arrangement extends uniformly across the crystal lattice
		- results of its electrical, optical, and mechanical characteristic
	- Common **Acceptor** P type semiconductor
	    - B (Boron), Al (Aluminum), Ga (Gallium), In (Indium)
	- Common **Donor** N type semiconductor
	    - N (Nitrogen), P (Phosphorus), As (Arsenic), Sb (Antimony)
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
#### Law of mass action

- electron-hole pair generation: every electron that is thermally excited from the valence band to the conduction band leaves behind a hole. electrons in the valence band cannot conduct current as electrons in the conduction band.
	- In the **conduction band**, electrons have enough energy to move freely within the material, allowing for electrical conductivity.
	- In the **valence band**, electrons are restricted by covalent bonds and cannot move freely.
	- Current in a semiconductor is due to the combined movement of free electrons in the conduction band and holes in the valence band.
		- $$n = p = n_i$$
		- electrons are constantly being thermally excited from the valence band to the conduction band, creating electron-hole pairs. At the same time, electrons in the conduction band recombine with holes in the valence band. The rates of generation and recombination are balanced in thermal equilibrium.
	- $p \cdot n = {n_i}^2$ where $n_i$ is the number of charge carriers in a unit volume of intrinsic silicon at a given temperature
	- $n_i$ depends on temperature
		- $$n_i = B \cdot T ^ {\frac{3}{2}} \cdot e^{\frac{E_g}{2k \cdot T}} \approx 10^{10}$$
		- At room temperature (300 Kelvin)
		- $E_g = 1.12eV$
		- $K = \frac{0.026}{300}ev/Kelvin$
		- $K \cdot T = 0.026eV$

#### Extrinsic Semiconductor

##### N-type Semiconductor

- Dopant: an element with more valence electrons that the host
- Common **Donor** N type semiconductor: N (Nitrogen), P (Phosphorus), As (Arsenic), Sb (Antimony)
- Concentration of **donor** atom ($N_D$) is *the number of charge carriers of N-type silicon* as the donor atom concentration is much larger than the number of natural charge carriers:$$n_n \simeq N_D \gg n_i$$ 
- Law of mass action: $$p_n \simeq \frac{{n_i}^2}{N_D}$$
- **Free carrier: electrons**

##### P-type Semiconductor

- Dopant: an element with fewer valence electrons than the host
- Common **Acceptor** P type semiconductor: B (Boron), Al (Aluminum), Ga (Gallium), In (Indium)
- Concentration of **acceptor** atom ($N_A$) is the number of charge carriers of P-type silicon as the concentration of acceptor atom is much larger than the number of natural charge carrier: $$p_p \simeq N_A \gg n_i$$
- **Free carrier: holes**

- $$p \cdot n = {n_i}^2$$
- $$p_n \cdot n_n = n_i ^ 2$$
- $$p_p \cdot n_p = n_i ^ 2$$
- P and N type semiconductor are both **neutral** 

##### Compensated Semiconductors

- doped with both $N_d$ and $N_a$
- The overall conductivity and type of the material depend on the relative concentrations of these dopants
- Charge neutrality$$n + n_a^- = n_d^+ + p$$

- **Case 1: $N_d > N_a$​ (Donors Outnumber Acceptors)**
	- Electrons from donor atoms ($N_d$​) fill available acceptor sites ($N_a$​) to form $N_a^-$ (negatively charged acceptors) and $N_d^+$​ (positively charged donors).
	- After all acceptor states are filled, the **excess electrons** from $N_d - N_a$ remain in the conduction band as free electrons.
	- This makes the semiconductor **n-type**, with electrons as the majority carriers and holes as the minority carriers.
	- Since all acceptors are filled and the remaining electrons are free, the total free electron concentration $n$ is: $n = N_d - N_a$
	- The concentration of holes $p$ is calculated using the **Law of Mass Action**: $$p \cdot n = n_i^2 \implies p = \frac{n_i^2}{n}$$
	- **Summary**:
		- **Majority carriers**: Electrons
		- **Minority carriers**: Holes
		- The semiconductor behaves like an **n-type semiconductor**.
- **Case 2: $N_a > N_d$​ (Acceptors Outnumber Donors)**
    - Electrons from donor atoms ($N_d$​) fill available acceptor sites ($N_a​$), forming $N_a^-$ (negatively charged acceptors) and $N_d^+$​ (positively charged donors).
    - Once the donor states are all "used up" (all electrons from $N_d$ have been captured by the acceptors), there are still unfilled acceptor sites.
    - These unfilled acceptor sites create "holes" in the valence band, which behave as **mobile positive charge carriers**.
    - Since there are more acceptors than donors, the excess acceptor states $N_a - N_d$ determine the number of free holes in the valence band.
    - The total free hole concentration $p$ is: $p = N_a - N_d$
    - The concentration of free electrons $n$ is calculated using the **Law of Mass Action**: $$p \cdot n = n_i^2 \implies n = \frac{n_i^2}{p}$$
    - **Summary**:
        - **Majority carriers**: Holes
        - **Minority carriers**: Electrons
        - The semiconductor behaves like a **p-type semiconductor**.
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

### Mobility and Resistivity with Doping Concentration

#### N-type
$$\sigma_n = q (\mu_n n + \mu_p p) \approxeq q \mu_n N_d$$
$$\rho_n = \frac{1}{q \mu_n N_d}$$

#### P-type

$$\sigma_p = q (\mu_n n + \mu_p p) \approxeq q \mu_p N_a$$
$$\rho_n = \frac{1}{q \mu_p N_a}$$

### P-N Junction

Connecting p-type and n-type semiconductor causes creation of a **depletion region** near the boundary, as the free electrons fill the available holes, which in turn allows electric current to pass through the junction only in one direction.

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
	
## Diode

### Function

- A diode allows current to flow in **one direction only** (from p-side to n-side) and blocks current in the reverse direction.
- It works as a **rectifier** to convert AC to DC in power supplies.

### Structure

- **p-n junction**: The diode consists of a p-type semiconductor joined with an n-type semiconductor.
- **Depletion region**: At the junction, electrons and holes combine, creating a depletion region that acts as a barrier to current flow.
- **Forward bias**: When a positive voltage is applied to the p-side relative to the n-side, the depletion region shrinks, and current flows.
- **Reverse bias**: When a negative voltage is applied to the p-side, the depletion region widens, blocking current flow.

### Operation

- **Forward-biased**: Current flows (similar to a one-way street for charge carriers).
- **Reverse-biased**: Current is blocked (like a closed gate).

### Key Equations

- **Current-voltage relationship**: I=Is(eqVkT−1)I = I_s \left( e^{\frac{qV}{kT}} - 1 \right)I=Is​(ekTqV​−1) where IsI_sIs​ is the saturation current, qqq is the electron charge, VVV is the applied voltage, kkk is Boltzmann's constant, and TTT is temperature.

### Applications

- **Rectification**: Converts AC to DC.
- **Clamping & Clipping**: Modifies signal waveforms.
- **Voltage protection**: Prevents reverse current in circuits.

---

## LED (Light Emitting Diode)

### Function

- A **LED** (Light Emitting Diode) emits **light** (visible or infrared) when a current flows through it.
- This is due to the recombination of electrons and holes, which releases energy as photons (light) — a process called **electroluminescence**.

### Structure

- **p-n junction** similar to a diode, but the semiconductor material is chosen to emit photons when electrons and holes recombine.
- Materials like **GaAs (infrared), GaP (red, yellow), GaN (blue, green)** are used for different colors.
- LEDs have a **transparent package** to allow light to escape.

### Operation

- When forward-biased, electrons from the n-side and holes from the p-side recombine in the **depletion region**.
- The released energy corresponds to a photon of light. The **wavelength of light** depends on the bandgap energy of the semiconductor material.
- Larger bandgap = shorter wavelength = blue/violet light.
- Smaller bandgap = longer wavelength = red/infrared light.

### Key Equations

- **Photon energy**: E=hν=hcλE = h \nu = \frac{hc}{\lambda}E=hν=λhc​ Where hhh is Planck's constant, ccc is the speed of light, and λ\lambdaλ is the wavelength of light.

### Applications

- **Lighting**: LEDs are energy-efficient light sources for homes, offices, and streets.
- **Displays**: Used in LED TVs, computer screens, and large outdoor displays.
- **Indicators**: Used in devices like power indicators.
- **Optoelectronics**: Infrared LEDs are used in remote controls.

---

## Solar Cell

### Function

- A **solar cell** converts **light energy into electrical energy** using the **photovoltaic effect**.
- Instead of using electrical energy to produce light (as in an LED), the solar cell does the opposite — it uses light to generate electrical energy.

### Structure

- **p-n junction** similar to a diode, but designed to absorb sunlight.
- **Antireflective coating** to prevent light reflection and maximize absorption.
- **Transparent top electrode** allows sunlight to pass through to the junction.
- **Back electrode** collects the electrons and serves as a contact.

### Operation

1. **Photon Absorption**: When sunlight (photons) hits the p-n junction, energy from the photon excites an electron from the valence band to the conduction band, leaving behind a **hole**.
2. **Electron-Hole Separation**: The electric field in the depletion region drives electrons to the **n-side** and holes to the **p-side**.
3. **Current Generation**: The movement of electrons and holes generates a **current** through an external circuit.

### Key Equations

- **Open-circuit voltage** VocV_{oc}Voc​: Voc=kTqln⁡(Iph+IsIs)V_{oc} = \frac{kT}{q} \ln \left( \frac{I_{ph} + I_s}{I_s} \right)Voc​=qkT​ln(Is​Iph​+Is​​) Where IphI_{ph}Iph​ is the photocurrent generated by the light, and IsI_sIs​ is the saturation current.
- **Power Output**: P=I⋅VP = I \cdot VP=I⋅V The maximum power point (MPP) is the point where the solar cell produces the maximum power.

### Applications

- **Solar panels**: Used in renewable energy systems to convert sunlight into electricity.
- **Spacecraft**: Solar panels power satellites and spacecraft.
- **Portable power**: Used in calculators, solar chargers, and small electronic devices.

## Key Differences Between Diode, LED, and Solar Cell

|**Feature**|**Diode**|**LED**|**Solar Cell**|
|---|---|---|---|
|**Primary Purpose**|Control current direction|Emit light (electroluminescence)|Convert light to electricity (photovoltaic)|
|**Energy Flow**|Electrical → Heat|Electrical → Light (Photons)|Light (Photons) → Electrical|
|**Bias Requirement**|**Forward bias** for current|**Forward bias** for light|**Reverse bias** for power generation|
|**Output**|Electrical current|Light (photons)|Electrical current (DC)|
|**Key Process**|Electron flow|Electron-hole recombination|Electron-hole generation|
|**Wavelength Control**|No control (no light)|Controlled via bandgap (different colors)|Sunlight (broad spectrum)|
|**Depletion Region**|Used to block current|Used for light generation|Used to separate charges|
|**Efficiency**|~50-90% (current)|~20-40% (light emission)|~20-30% (energy conversion)|
|**Applications**|Rectifiers, protection|Lighting, displays, indicators|Solar panels, space power|

## Summary

|**Device**|**Function**|**Energy Flow**|**Operation**|
|---|---|---|---|
|**Diode**|Allows current in one direction|Electrical → Heat|Current flows only in forward bias|
|**LED**|Emits light|Electrical → Light (photons)|Electron-hole recombination releases light|
|**Solar Cell**|Converts light to electricity|Light (photons) → Electrical|Photons excite electrons to conduction band, creating current|

## Transistor

## Logic Circuit with Transistor