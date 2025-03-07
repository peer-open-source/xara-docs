.. _shells:

Shells
^^^^^^

.. toctree::
   :maxdepth: 1

   ASDShellQ4
   ASDShellT3

..
   Shell
   ShellDKGQ
   ShellNLDKGQ
   ShellNL
   ShellDKGT
   ShellNLDKGT


Theory
------

The first two general assumptions of plate theory are:
- The domain $\Omega$ has the following special form :

$$
\Omega:=\left\{\left(x_1, x_2, z\right) \in \mathbb{R}^3 \text { such that } z \in\left[-\frac{h}{2}, \frac{h}{2}\right] \text { and }\left(x_1, x_2\right) \in A \subset \mathbb{R}^2\right\} .
$$

- The plane stress hypothesis: $\sigma_{33}=0$.

In all future discussions, any Greek indices $\alpha, \beta, \ldots$ range from 1 to 2 only.

The three dimensional displacement field $u_i$ is assumed to be defined by

$$
\left.\begin{array}{rl}
u_1 & :=-z \theta_1\left(x_1, x_2\right)+\bar{u}_1\left(x_1, x_2\right) \\
u_2 & :=-z \theta_2\left(x_1, x_2\right)+\bar{u}_2\left(x_1, x_2\right) \\
u_3 & :=\bar{u}_3\left(x_1, x_2\right)
\end{array}\right\}
$$

where $\bar{u}_i$ is the translation of the plate mid-surface and $\theta_i$ are rotations of fibers initially normal to the mid-surface of the plate.

Strains
-------

Define the curvature tensor as

$$
\kappa_{\alpha \beta}:=\frac{1}{2}\left(\theta_{\alpha, \beta}+\theta_{\beta, \alpha}\right),
$$

the membrane strain tensor as

$$
\bar{\epsilon}_{\alpha \beta}:=\frac{1}{2}\left(\bar{u}_{\alpha, \beta}+\bar{u}_{\beta, \alpha}\right),
$$

and the transverse shear strains as

$$
\gamma_\alpha:=-\theta_\alpha+\tilde{u}_{3, \alpha}
$$


Then, the physical strains are

$$
\epsilon_{\alpha \beta}=\frac{1}{2}\left(u_{\alpha, \beta}+u_{\beta, \alpha}\right)=-z \kappa_{\alpha \beta}+\bar{\epsilon}_{\alpha \beta}
$$

and

$$
\epsilon_{\alpha 3}=\epsilon_{3 \alpha}=\frac{1}{2}\left(u_{\alpha, 3}+u_{3, \alpha}\right)=\frac{1}{2} \gamma_\alpha .
$$


Stress
------

3.1 Membrane

Definte the membrane stress resultant tensor as

$$
p_{\alpha \beta}:=\int_{-\frac{h}{2}}^{\frac{h}{2}} \sigma_{\alpha \beta} \mathrm{d} z
$$

3.2 Bending

Define the moment tensor as

$$
m_{\alpha \beta}:=\int_{-\frac{\hbar}{2}}^{\frac{h}{2}} z \sigma_{\alpha \beta} \mathrm{d} z
$$

3.3 Shear

Define the transverse shear forces as

$$
q_\alpha:=\int_{-\frac{h}{2}}^{\frac{h}{2}} \sigma_{\alpha 3} \mathrm{~d} z
$$

Assume a linear elastic three-dimensional continuum constitutive response is given by

$$
\sigma_{i j}=\mathfrak{C}_{i j k l} \cdot \epsilon_{k l}
$$

where $\mathfrak{C}$ is the symmetric (major and minor) rank-four elasticity tensor. Enforcement of the plane stress condition $\sigma_{33}=0$ yields a condensed elasticity tensor $\mathbb{C}$ such that

$$
\left.\begin{array}{rl}
\sigma_{i j} & =\mathbb{C}_{i j k l} \cdot \epsilon_{k l} \\
\mathbb{C}_{i j k l} & =\mathfrak{C}_{i j k l}-\mathfrak{C}_{i j 33}\left(\mathfrak{C}_{3333}\right)^{-1} \mathfrak{C}_{33 k l}
\end{array}\right\}
$$


The modified tensor $\mathbb{C}$ is now appropriate for plate analysis.

Integration through the thickness yields the stress resultant constitutive response parameters.

$$
\begin{aligned}
p_{\alpha \beta} & =\int_{-\frac{h}{2}}^{\frac{h}{2}} \sigma_{\alpha \beta} \mathrm{d} z \\
& =\int_{-\frac{h}{2}}^{\frac{h}{2}} \mathbb{C}_{\alpha \beta k l} \cdot \epsilon_{k l} \mathrm{~d} z \\
& =\int_{-\frac{h}{2}}^{\frac{h}{2}}\left[\mathbb{C}_{\alpha \beta \delta \gamma} \cdot \epsilon_{\delta \gamma}+\mathbb{C}_{\alpha \beta \delta 3} \cdot 2 \epsilon_{\delta 3}\right] \mathrm{d} z \\
& =\int_{-\frac{h}{2}}^{\frac{h}{2}}\left[\mathbb{C}_{\alpha \beta \delta \gamma} \cdot\left(-z \kappa_{\delta \gamma}+\bar{\epsilon}_{\delta \gamma}\right)+\mathbb{C}_{\alpha \beta \delta 3} \cdot 2 \epsilon_{\delta 3}\right] \mathrm{d} z \\
& =\left[\int_{-\frac{h}{2}}^{\frac{h}{2}}-z \mathbb{C}_{\alpha \beta \delta \gamma} \mathrm{d} z\right] \cdot \kappa_{\delta \gamma}+\left[\int_{-\frac{h}{2}}^{\frac{h}{2}} \mathbb{C}_{\alpha \beta \delta \gamma} \mathrm{d} z\right] \cdot \bar{\epsilon}_{\delta \gamma}+\left[\int_{-\frac{h}{2}}^{\frac{h}{2}} \mathbb{C}_{\alpha \beta \delta 3} \mathrm{~d} z\right] \cdot \gamma_\delta
\end{aligned}
$$

$$
\begin{aligned}
m_{\alpha \beta} & =\int_{-\frac{h}{2}}^{\frac{h}{2}} z \sigma_{\alpha \beta} \mathrm{d} z \\
& =\int_{-\frac{h}{2}}^{\frac{h}{2}} z \mathbb{C}_{\alpha \beta k l} \cdot \epsilon_{k l} \mathrm{~d} z \\
& =\int_{-\frac{h}{2}}^{\frac{h}{2}} z\left[\mathbb{C}_{\alpha \beta \delta \gamma} \cdot \epsilon_{\delta \gamma}+\mathbb{C}_{\alpha \beta \delta 3} \cdot 2 \epsilon_{\delta 3}\right] \mathrm{d} z \\
& =\int_{-\frac{h}{2}}^{\frac{h}{2}} z\left[\mathbb{C}_{\alpha \beta \delta \gamma} \cdot\left(-z \kappa_{\delta \gamma}+\bar{\epsilon}_{\delta \gamma}\right)+\mathbb{C}_{\alpha \beta \delta 3} \cdot 2 \epsilon_{\delta 3}\right] \mathrm{d} z \\
& =\left[\int_{-\frac{h}{2}}^{\frac{h}{2}}-z^2 \mathbb{C}_{\alpha \beta \delta \gamma} \mathrm{d} z\right] \cdot \kappa_{\delta \gamma}+\left[\int_{-\frac{h}{2}}^{\frac{h}{2}} z \mathbb{C}_{\alpha \beta \delta \gamma} \mathrm{d} z\right] \cdot \bar{\epsilon}_{\delta \gamma}+\left[\int_{-\frac{h}{2}}^{\frac{h}{2}} z \mathbb{C}_{\alpha \beta \delta 3} \mathrm{~d} z\right] \cdot \gamma_\delta
\end{aligned}
$$


$$
\begin{aligned}
q_\alpha & =\int_{-\frac{h}{2}}^{\frac{h}{2}} \sigma_{\alpha 3} \mathrm{~d} z \\
& =\int_{-\frac{h}{2}}^{\frac{h}{2}} \mathbb{C}_{\alpha 3 k l} \cdot \epsilon_{k l} \mathrm{~d} z \\
& =\int_{-\frac{h}{2}}^{\frac{h}{2}}\left[\mathbb{C}_{\alpha 3 \delta \gamma} \cdot \epsilon_{\delta \gamma}+\mathbb{C}_{\alpha 3 \delta 3} \cdot 2 \epsilon_{\delta 3}\right] \mathrm{d} z \\
& =\int_{-\frac{h}{2}}^{\frac{h}{2}}\left[\mathbb{C}_{\alpha 3 \delta \gamma} \cdot\left(-z \kappa_{\delta \gamma}+\bar{\epsilon}_{\delta \gamma}\right)+\mathbb{C}_{\alpha 3 \delta 3} \cdot 2 \epsilon_{\delta 3}\right] \mathrm{d} z \\
& =\left[\int_{-\frac{h}{2}}^{\frac{h}{2}}-z \mathbb{C}_{\alpha 3 \delta \gamma} \mathrm{~d} z\right] \cdot \kappa_{\delta \gamma}+\left[\int_{-\frac{h}{2}}^{\frac{h}{2}} \mathbb{C}_{\alpha 3 \delta \gamma} \mathrm{~d} z\right] \cdot \bar{\epsilon}_{\delta \gamma}+\left[\int_{-\frac{h}{2}}^{\frac{h}{2}} \mathbb{C}_{\alpha 3 \delta 3} \mathrm{~d} z\right] \cdot \gamma_\delta
\end{aligned}
$$
