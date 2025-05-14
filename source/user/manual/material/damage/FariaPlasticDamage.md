
# FariaPlasticDamage

```{eval-rst}
.. function:: nDMaterial PlasticDamageConcrete3d tag? E? nu? Ft? Fc? <beta? Ap? An? Bn?>

```

| E | Young's modulus |
| :--- | :--- |
| nu | Poisson ratio |
| Ft | tensile yield strength |
| Fc | Compressive yield strength |
| beta | parameter controlling plastic strain rate/post-yield hardening parameter |
| Ap | parameter controlling tensile fracture energy |
| An | parameter controlling ductility of the compressive response |
| Bn | parameter controlling ductility and peak strength of the compressive response |

## Theory

This model is a 2-parameter damage-plasticity formulation based on the work of Faria et al. (1998).
The plastic strain evolution assumes that plastic strain evolves in the same direction as the elastic strain (Faria et al. 1998):

$$
\dot{\boldsymbol{\varepsilon}}_p = \beta \frac{E L}{\|\overline{\boldsymbol{\sigma}}\|}\left(C^{-1}: \overline{\boldsymbol{\sigma}}\right)
$$

where $\beta$ is the plastic strain coefficient, $L$ is a scalar that depends on the effective stress tensor and the strain rate tensor, $\bar{\sigma}$ is the effective stress tensor, $E$ is the Young's modulus, and C is the elastic stiffness tensor.

The following exponential damage evolution rules are adopted to describe the dependence of the damage variables $d^{ \pm}$ on the equivalent stresses $r^{ \pm}$:

$$
\begin{aligned}
& d^{+}=1-\left(\frac{r_0^{+}}{r^{+}}\right) \exp \left[A_p\left(1-\frac{r^{+}}{r_0^{+}}\right)\right] \\
& d^{-}=1-\sqrt{\frac{r_0^{-}}{r^{-}}}\left(1-A_n\right)-A_n \exp \left[B_n\left(1-\sqrt{\frac{r^{-}}{r_0^{-}}}\right)\right]
\end{aligned}
$$
where $A_p, A_n$, and $B_n$ are damage parameters that describe the softening behavior of the stress-strain relation, as reported in *Faria et al. (1998)*.


## Examples

The properties of confined concrete were used for the boundaries, and those of unconfined concrete for the web (with $f^{\prime}_c= 45 \mathrm{Mpa}$ and $E_c=36,900 \mathrm{MPa}$ [45]). 
For unconfined concrete the following material parameters were adopted: $E_c=36,900 \mathrm{Mpa}, \nu=0.2$ $F_c=25.6$ МPa, $F_t=5 \mathrm{Mpa}, B_n=0.75, \beta=0.5, A_n=5, A_p=0.1$, whereas for confined concrete $F_t$ and $\beta$ were kept the same and the remaining parameters were modified as follows: $F_c=28 \mathrm{Mpa}, B_n=0.7$, $A_n=3, A_p=0.05$. 
For reinforcing steel, the Giuffre-Menegotto-Pinto (Menegotto and Pinto, 1973) [48,49] uniaxial steel material with isotropic strain hardening was employed (Steel02), with the following parameters: $f_y=560 \mathrm{MPa}$, $E_s=200,000 \mathrm{MPa}, b=0.01, R_0=18$, $C_{R 1}=0.925, C_{R 2}=0.15$. 


## References

- R. Faria, J. Oliver, M. Cervera "A Strain-Based Plastic Viscous-Damage Model for Massive Concrete Structures". Int. J. Solids Structures 1998;35(14):1533–58. [doi: 10.1016/S0020-7683(97)00119-4](https://doi.org/10.1016/S0020-7683(97)00119-4)
- F Petrone, F McKenna, T Do, D McCallen  "A versatile numerical model for the nonlinear analysis of squat-to-tall reinforced-concrete shear walls" Engineering Structures, 2021 [doi: 10.1016/j.engstruct.2021.112406](https://doi.org/10.1016/j.engstruct.2021.112406)