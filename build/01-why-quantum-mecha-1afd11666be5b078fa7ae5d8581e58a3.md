# Why Quantum Mechanics?

:::{note} What you need to know

- **Quantum mechanics is the fundamental theory of nature**, governing atoms, molecules, and subatomic particles.
- Quantum theories (quantum mechanics + quantum field theory) are **complete descriptions of physical reality**, and they’ve never failed an experimental test since their discovery!
- Predictions of quantum mechanics have been verified to an **astonishing degree of accuracy**.
  :::

:::{figure} ./images/qm.png
:label: fig-why-quantum-mechanics-1
:alt: qm-whomi
:width: 100%

Quantum mechanics describes and predicts the behavior of the smallest particles, so long as they don’t travel near the speed of light.
:::

### Beware: Quantum Mechanics is Weird 🤯

- Saying QM is “weird” is an understatement. Don’t just take my word for it, consider Richard Feynman:

:::{figure} ./images/feynman.png
:label: fig-why-quantum-mechanics-2
:alt: ch1-feynman
:width: 300px

[Richard Feynman](https://en.wikipedia.org/wiki/Richard_Feynman), awarded the 1965 Nobel Prize in Physics for his work on quantum electrodynamics.
:::

> “I think I can safely say that nobody understands quantum mechanics.” (Richard Feynman)

- Be prepared to let go of the comforting notion that “things make sense.” In quantum land, they often don’t! But that doesn’t stop us from **mastering the logic** of quantum mechanics and applying it everywhere, from chemistry to computing.

> Bottom line: if you feel you don’t fully understand QM, don’t worry, you’re in good company… with *everyone else*!

### How Does Quantum Mechanics Compare to Other Theories?

:::{figure} ./images/qm-joke1.jpg
:label: fig-why-quantum-mechanics-3
:alt: qm-mechanic-joke
:width: 300px

“There are no quantum mechanicians. Electrons don’t break down, but your car does!”
:::

Even though discovered by physicists, QM isn’t just “another” physical theory like electromagnetism or relativity.

In the usual hierarchy of sciences (biology → chemistry → physics → math), quantum mechanics occupies a unique position, like the **operating system** on which other theories run as “apps.” Translating a theory into this OS is what physicists call *quantization*.

> Scott Aaronson, *Quantum Computing Since Democritus* (2013)

### Chemistry runs on quantum mechanics

One year after the Schrödinger equation appeared, Paul Dirac declared the game over [@dirac1929]:

> "The underlying physical laws necessary for the mathematical theory of a large part of physics and the whole of chemistry are thus completely known, and the difficulty is only that the exact application of these laws leads to equations much too complicated to be soluble."

That second half is the story of modern chemistry: every bond, reaction barrier, molecular color, and spectrum **is** a solution of the Schrödinger equation, and a century of cleverness (plus computers) has gone into extracting those solutions.

:::{figure} ./images/qc-applied.png
:label: fig-why-quantum-mechanics-4
:alt: qm-apps
:width: 300px

Applications in Quantum Chemistry
:::

- Chemical bonds, molecular structure, reactivity, color, material properties
- Spectroscopy (NMR, UV-Vis, IR, lasers...)
- Modern electronic structure calculations
- Condensed matter physics
- Everyday hardware: the transistors in your phone, LEDs, lasers, MRI scanners, solar cells, and the atomic clocks behind GPS all exist because we mastered quantum rules

### Watching molecules move, atom by atom

Dirac's "too complicated to be soluble" is no longer entirely true. Below, a water molecule vibrates in a simulation computed **for this course**: at every time step, the electrons' Schrödinger equation is solved from scratch to obtain the forces on the nuclei. This technique, ab initio molecular dynamics, and its bigger sibling QM/MM (quantum region embedded in a classical environment, Nobel Prize 2013 to Karplus, Levitt, and Warshel) let chemists watch enzymes catalyze and materials fail, one femtosecond at a time.

:::{figure} ./images/aimd_water.gif
:label: fig-why-quantum-mechanics-aimd
:alt: ab initio molecular dynamics of a vibrating water molecule with its electronic energy
:width: 100%

Ab initio molecular dynamics of one water molecule (HF/STO-3G, PySCF). Left: the vibrating molecule with hydrogen trails. Right: the electronic energy recomputed at every step. By the end of this course you will understand every ingredient of this simulation.
:::

- **AI has joined the party**: today's machine-learned force fields are neural networks trained on millions of quantum calculations, delivering quantum accuracy at a tiny fraction of the cost. Quantum chemistry is now one of the biggest producers of AI training data in science.

### And then quantum mechanics became a technology

The strangest features of QM, superposition and entanglement, turned out to be **resources**. A qubit is nothing but a two-level quantum system, and a quantum computer is a machine that computes with wavefunctions. Feynman saw it first [@feynman1982]:

> "Nature isn't classical, dammit, and if you want to make a simulation of nature, you'd better make it quantum mechanical."

:::{figure} ./images/qcomp-applied.jpg
:label: fig-why-quantum-mechanics-5
:alt: qcomp-apps
:width: 300px

Applications in Quantum Computing
:::

- Quantum algorithms and simulation (the killer app: simulating molecules, exactly this course's subject)
- Cryptography and security
- Materials and drug discovery

:::{tip} A quantum joke to start the semester
:class: dropdown

A police officer pulls Heisenberg over and asks, "Do you know how fast you were going?"

Heisenberg: "No, but I know exactly where I am."

The officer says, "You were doing 90 miles an hour!"

Heisenberg throws up his hands: "Great. Now I'm lost."
:::

### What Skills Will You Gain?

Studying quantum mechanics will arm you with tools beyond physics:

- **Probabilistic thinking** and comfort with uncertainty
- **Linear algebra + differential equations** at a deeper, applied level
- Ability to **decode electronic structure calculations** in cutting-edge research (chemistry, biochemistry, materials, astrophysics)
- Insight into **chemical bonding, spectroscopy, and reactivity**
- A more nuanced appreciation of the complex world we live in

### And One More Thing…

If none of the above convinces you, remember: studying quantum mechanics also upgrades your meme game.

:::{figure} ./images/qm_meme.jpeg
:label: fig-why-quantum-mechanics-6
:alt: qm-meme
:width: 300px

Have a quantum joke ready for any occasion.
:::
