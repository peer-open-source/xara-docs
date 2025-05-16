
# FariaPlasticDamage

![Failure surface in plane stress](FariaSurface.png)

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
\dot{\boldsymbol{\varepsilon}}_p = \beta \frac{E L}{\|\overline{\boldsymbol{\sigma}}\|}\left(\mathbb{C}_{\mathrm{e}}^{-1} \overline{\boldsymbol{\sigma}}\right)
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

-------------

Let

$$
\alpha = \frac{r_{n0}}{r_n},\quad 
x = B_n\Bigl(1 - \frac{r_n}{r_{n0}}\Bigr)
$$

Then the original

$$
d_n = 1  - \frac{r_{n0}}{r_n} (1 - A_n) - A_n \exp(B_n (1 - r_n/r_{n0}));
$$

can be rewritten as

$$
d_n = (1-\alpha)\,(1 - A_n)\;-\;A_n\bigl(\exp(x)-1\bigr)
$$

In this form:

* $(1-\alpha)$ is often small but computed in one go.
* $\mathrm{expm1}(x)$ accurately gives $\exp(x)-1$ even when $x\approx 0$.


------------


When $\displaystyle r_p \approx r_{p0}$, directly computing

$$
d_p = 1  - (r_{p0}/r_p)   \exp\!\bigl(A_p (1 - r_p/r_{p0})\bigr);
$$

will suffer cancellation. A more accurate form is:

1. **Introduce**

   $$
     \alpha \triangleq \frac{r_{p0}}{r_p}, 
     \quad
     x = A_p\Bigl(1 - \frac{r_p}{r_{p0}}\Bigr)
       = A_p\Bigl(1 - \frac1\alpha\Bigr).
   $$

2. **Rewrite**

   $$
     d_p = 1 - \alpha\, e^x
        = \bigl(1-\alpha\bigr)\;-\;\alpha\,(e^x-1)
   $$

3. **Use**

   * `std::expm1(x)` for $e^x - 1$ when $|x|\ll1$.
   * `std::fma(a,b,c)` for $a\cdot b + c$ in one rounding step.


## Examples

The properties of confined concrete were used for the boundaries, and those of unconfined concrete for the web (with $f^{\prime}_c= 45 \mathrm{Mpa}$ and $E_c=36,900 \mathrm{MPa}$ [45]). 
For unconfined concrete the following material parameters were adopted: $E_c=36,900 \mathrm{Mpa}, \nu=0.2$ $F_c=25.6$ МPa, $F_t=5 \mathrm{Mpa}, B_n=0.75, \beta=0.5, A_n=5, A_p=0.1$, whereas for confined concrete $F_t$ and $\beta$ were kept the same and the remaining parameters were modified as follows: $F_c=28 \mathrm{Mpa}, B_n=0.7$, $A_n=3, A_p=0.05$. 



## References

- R. Faria, J. Oliver, M. Cervera "A Strain-Based Plastic Viscous-Damage Model for Massive Concrete Structures". Int. J. Solids Structures 1998;35(14):1533–58. [doi: 10.1016/S0020-7683(97)00119-4](https://doi.org/10.1016/S0020-7683(97)00119-4)
- F Petrone, F McKenna, T Do, D McCallen  "A versatile numerical model for the nonlinear analysis of squat-to-tall reinforced-concrete shear walls" Engineering Structures, 2021 [doi: 10.1016/j.engstruct.2021.112406](https://doi.org/10.1016/j.engstruct.2021.112406)

