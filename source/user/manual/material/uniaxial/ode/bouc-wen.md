# Bouc-Wen



```{eval-rst}

.. figure:: figures/bouc-beta.png
   :width: 50%
   :align: center

.. py:method:: Model.uniaxialMaterial("FullBoucWen", tag, E, Fy, r, **options)
   :no-index:

   Construct a uniaxial Bouc-Wen pinching material

   :param tag: unique integer tag for the material
   :type tag: |integer|
   :param E: initial stiffness, :math:`E` [1]_
   :type  E: |float|
   :param Fy: yield force, :math:`F_y` [1]_
   :type  Fy: |float|
   :param alpha: ratio of post-yield stiffness to the initial elastic stiffenss, :math:`0 \leq \alpha \leq 1` [1]_
   :type  alpha: float
   :param beta: hysteretic hardening shape parameter :math:`\beta`, defaults to :math:`\beta=0.5` [1]_
   :type  beta: float, optional
   :param n: sharpness of yield, :math:`n` [1]_
   :type  n: float
   :param strength_rate: strength degradation rate, :math:`\delta_{\nu}` 
   :type  strength_rate: |float|
   :param stiffness_rate: stiffness degradation rate, :math:`\delta_{\eta}`
   :type  stiffness_rate: |float|
   :param pinch_slope: pinching slope, :math:`p`
   :type  pinch_slope: |float|
   :param pinch_start: pinching initiation, :math:`q`
   :type  pinch_start: |float|
   :param pinch_slip: measure of total slip, :math:`\zeta`
   :type  pinch_slip: |float|
   :param pinch_rate: pinching rate, :math:`\delta_{\psi}`
   :type  pinch_rate: |float|
   :param pinch_size: pinching magnitude, :math:`\psi_0`
   :type  pinch_size: |float|
   :param lamda: pinching severity, :math:`\lambda`
   :type  lamda: |float|

```

## Extended Parameters

```{eval-rst}
.. py:class:: BoucWen

   .. py:attribute:: E
      :type: float

      Initial stiffness :math:`E`

   .. py:attribute:: Fy
      :type: float
   
      Yield stress of the hysteretic curve :math:`F_y`. Analogous to :py:attr:`Steel02.Fy`.
   
   .. py:attribute:: beta
      :type: float
      :value: 0.5
   
      Hysteretic shape parameter :math:`\beta`.



.. [1] This argument is supported by the :ref:`parameter <parameter>` commands.

..
  .. py:method:: Model.uniaxialMaterial("FullBoucWen", tag, E, Fy, alpha [, beta, gamma, n] [, detla_v, delta_n, lamda, p, q, zeta, detla_w, po])


```


This material superceeds the following materials, which are supported for legacy purposes:

```{eval-rst}

.. tabs::

   .. tab:: BoucWen

      Bouc-Wen-Baber, written by Terje Haukaas and described by Haukaas and Der Kiureghian (2003).
      
      .. code-block:: Tcl

         uniaxialMaterial BoucWen $tag $b $E $n $gamma $beta $Ao \
                                  $delta_a $delta_v $delta_n

      Note that this version does not expose an :math:`F_y` parameter.


   .. tab:: BoucWenOriginal
      
      Bouc-Wen without pinching or degradation, implemented by A. Schellenberg.

      .. code-block:: Tcl

         uniaxialMaterial BoucWenOriginal tag E? Fy? alphaL? < alphaNL mu=2.0 n=1.0 beta=0.5 gamma=0.5 >

      In order to capture hardening effects that may occur in various hysteretic systems, the Bouc-Wen model was further modified to include Prager's rule (Bouc 1967; Casciati 1989). 

      References:

      * Hybrid Simulation of Seismic Isolation Systems Applied to an APR-1400 Nuclear Power Plant


   .. tab:: BWBN

       Bouc-Wen with Foliente pinching, but no degradation. Implemented by Raquib Hossain

        .. code-block:: Tcl

           uniaxialMaterial BWBN tag \
                            alpha E n $gamma $beta $Ao \
                            $q $zetas $p $Shi $deltaShi $lambda $tol $maxIter
```


<hr />

<figure>
<img src="/_static/wiki/BWBN_YSPD.jpg" title="BWBN_YSPD.jpg" alt="BWBN_YSPD.jpg" />
<figcaption aria-hidden="true">BWBN_YSPD.jpg</figcaption>
</figure>
<p>Fig. Cyclic force displacement relationship of the YSPDs generated
using the BWBN material model</p>
<hr />

## Theory

This material model is an extension of the
original Bouc-Wen model that includes pinching (Baber and Noori (1986) and Foliente (1995)).

$$
\begin{aligned} 
& 
\dot{z}=\frac{h(z, \varepsilon)}{\eta(\varepsilon)} \dot{u}\left[A-|z|^n(\gamma+\beta \operatorname{sgn}(\dot{u} z)) \nu(\varepsilon)\right] \frac{k_0}{F_y} \\ 
& \dot{\varepsilon}=(1-\alpha) F_y z \dot{u}\end{aligned}
$$

When parameterized with $F_y$, the additional constraint $\beta+\gamma=1$ is introduced to assure $F_y$ as the yield strength of the structure.

| Parameter | Description | Bounds |
| :--- | :--- | :--- |
| $E \geq 0$ | Initial stiffness |      |
| $F_y$ | Yield point |     |
| $\alpha$ | Post-yield stiffness ratio | $0 \leq \alpha \leq 0.5$ |
| $\beta$ | Basic hysteretic shape control | $0.01 \leq \beta \leq 0.99$ |
| $n$ | Sharpness of yield | $n \geq 1$ |

- Parameter $\gamma$ is usually in the range
  from -1 to 1 and parameter $\beta$ is usually in
  the range from 0 to 1.

- The hysteresis loop will exhibit *softening* for the following cases:

  1. $\beta + \gamma \gt 0$ and $\beta - \gamma \gt 0$, 
  2. $\beta + \gamma \gt 0$ and $\beta - \gamma \lt 0$, and 
  3. $\beta + \gamma \gt 0$ and $\beta - \gamma = 0$. 
  
- The hysteresis loop will exhibit *hardening* if $\beta + \gamma \lt 0$ and $\beta - \gamma \gt 0$, 

-  *quasi-linearity* is exhibited if $\beta + \gamma = 0$ and $\beta - \gamma \gt 0$.



```{eval-rst}
.. figure:: figures/bouc-beta.png
   :width: 50%
   :align: center
```

### Degradation

The new parameters that control degradation are:

| Parameter | Description | Bounds |
| :--- | :--- | :--- |
| $\delta_{\nu} \geq 0$ | Strength degradation rate | $0 \leq \delta_v \leq 0.36$ |
| $\delta_{\eta} \geq 0$ | Stiffness degradation rate | $0 \leq \delta_\eta \leq 0.39$ |

- $\delta_\nu>0$, 
- $\delta_A>0$, 
- $\delta_\eta>0$,

| Parameter | Description | Bounds |
| :--- | :--- | :--- |
| $\delta_v$ | Strength degradation rate | $0 \leq \delta_v \leq 0.36$ |
| $\delta_\eta$ | Stiffness degradation rate | $0 \leq \delta_\eta \leq 0.39$ |



### Pinching

The following parameters control pinching in the model:

| Parameter | Description | Bounds |
| :--- | :--- | :--- |
| $\zeta_0$ | Measure of total slip | $0 \leq \zeta_0 \leq 1$ |
| $p$ | Pinching slope | $0 \leq p \leq 1.38$ |
| $q$ | Pinching initiation | $0.01 \leq q \leq 0.43$ |
| $\psi$ | Pinching magnitude | $0.1 \leq \psi \leq 0.85$ |
| $\delta_\psi$ | Pinching rate | $0 \leq \delta_\psi \leq 0.09$ |
| $\lambda$ | Pinching severity | $0.01 \leq \lambda \leq 0.8$ |
| $c_{\varepsilon}$ | Hysteretic energy amplification factor | $50 \leq c_{\varepsilon} \leq 500$ |
| $c_h$ | Crack closure coefficient | $0.01 \leq c_h \leq 1.5$ |



$$
h(z)=1-\varsigma_1(\varepsilon) \exp \left(-\frac{\left(z(t) \operatorname{sign}(\dot{u})-q z_u\right)^2}{\left(\varsigma_2(\varepsilon)\right)^2}\right)
$$

$$
\begin{aligned}
&\zeta_1(\varepsilon)=\zeta_0(1-\exp (-p \varepsilon))\\
&\zeta_2(\varepsilon)=\left(\psi+\delta_\psi \varepsilon\right)\left(\lambda+\zeta_1(\varepsilon)\right)
\end{aligned}
$$

$\delta_\nu, \delta_\psi$, and $\lambda$ are rather insensitive parameters.


## Examples

```{.include}
docs/contrib/examples/31-BWBNExample.html
```

## References

- Bouc–Wen class models considering hysteresis mechanism of RC columns in nonlinear dynamic analysis [doi: https://doi.org/10.1016/j.ijnonlinmec.2022.104263](https://doi.org/10.1016/j.ijnonlinmec.2022.104263)

- Haukaas, T. and Der Kiureghian, A. (2003). "Finite element
  reliability and sensitivity methods for performance-based earthquake
  engineering." REER report, PEER-2003/14 <a href="https://peer.berkeley.edu/sites/default/files/0314_t._haukaas_a._der_kiureghian.pdf">link</a>.
- Baber, T. T. and Noori, M. N. (1985). "Random vibration of degrading, pinching systems." Journal of Engineering Mechanics, 111(8), 1010-1026.
<p>Bouc, R. (1971). "Mathematical model for hysteresis." Report to the
Centre de Recherches Physiques, pp16-25, Marseille, France.</p>
- Wen, Y.-K. (1976). \Method for random vibration of hysteretic
systems." Journal of Engineering Mechanics Division, 102(EM2),
249-263.

- <a href="http://www.sciencedirect.com/science/article/pii/S0141029613003568">Hossain,
   M. R., Ashraf, M., &amp; Padgett, J. E. (2013). "Risk-based seismic
   performance assessment of Yielding Shear Panel Device." Engineering
   Structures, 56, 1570-1579.</a>

- <a href="http://www.sciencedirect.com/science/article/pii/S0263823112001206">Hossain,
   M. R., &amp; Ashraf, M. (2012). "Mathematical modelling of yielding
   shear panel device." Thin-Walled Structures, 59, 153-161.</a>

- Baber, T. T., &amp; Noori, M. N. (1986). "Modeling general hysteresis
  behavior and random vibration application." Journal of Vibration
  Acoustics Stress and Reliability in Design, 108, 411.
- Foliente, G. C. (1995). Hysteresis modeling of wood joints and
  structural systems. Journal of Structural Engineering, 121(6), 1013-1022.

<hr />

## Developers

<p><a
href="http://scholar.google.com.au/citations?user=I_li3qkAAAAJ&hl=en&oi=ao">Raquib
Hossain</a>, <a href="http://www.uq.edu.au/">The University of
Queensland (UQ), Australia</a> &amp; <a
href="http://www.buet.ac.bd/">Bangladesh University of Engineering and
Technology (BUET), Bangladesh.</a></p>
