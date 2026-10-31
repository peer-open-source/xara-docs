.. _DruckerPrager:

DruckerPrager01
^^^^^^^^^^^^^^^


.. tabs::

   .. tab:: Python
      .. py:method:: Model.nDMaterial("DruckerPrager", tag, K, G, Fy, Rvol, Rbar, Fs, Fo, Hsat, Hten, Hmix, theta, density, atm=101.0)
         :no-index:

         Construct a Drucker-Prager material.

         :param tag: integer tag identifying material
         :param K: bulk modulus, :math:`\kappa`
         :type K: |float|
         :param G: shear modulus, :math:`\mu`
         :type G: |float|
         :param Fy: Initial yield stress, :math:`F_y \geq 0`
         :type Fy: |float|
         :param Rvol: frictional strength parameter, :math:`\rho \gt 0`
         :type Rvol: |float|
         :param Rbar: controls evolution of plastic volume change: :math:`0 \leq \bar{\rho} \leq \rho`
         :type Rbar: |float|
         :param Fs: Saturation stress for nonlinear isotropic strain hardening: :math:`F_{s} \geq 0`
         :type Fs: |float|
         :param Fo: nonlinear isotropic strain hardening parameter: :math:`F_o \geq 0`
         :type Fo: |float|
         :param Hsat: nonlinear isotropic strain hardening parameter: :math:`\delta_1 \geq 0`
         :type Hsat: |float|
         :param Hten: tension softening parameter: :math:`\delta_2 \geq 0`
         :type Hten: |float|
         :param Hmix: mixed linear strain hardening parameter: :math:`H \geq 0`
         :type Hmix: |float|
         :param theta: controls relative proportions of isotropic and kinematic hardening: :math:`0 \leq \theta \leq 1`
         :type theta: |float|
         :param density: mass density of the material
         :type density: |float|
         :param atm: optional atmospheric pressure for update of elastic bulk and shear moduli (default = 101 kPa)
         :type atm: |float|


   .. tab:: Tcl

      .. function:: nDMaterial DruckerPrager tag k G sigmaY rho rhoBar Kinf Ko delta1 delta2 H theta density <atmPressure>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         tag, |float|, integer tag identifying material
         k, |float|,	bulk modulus
         G, |float|, shear modulus
         sigmaY, |float|, yield stress
         rho, |float|, frictional strength parameter
         rhoBar, |float|, controls evolution of plastic volume change: 0 ≤ rhoBar ≤ rho
         Kinf, |float|, nonlinear isotropic strain hardening parameter: Kinf ≥ 0
         Ko, |float|, nonlinear isotropic strain hardening parameter: Ko ≥ 0
         delta1, |float|, nonlinear isotropic strain hardening parameter: delta1 ≥ 0
         delta2, |float|, tension softening parameter: delta2 ≥ 0
         H, |float|, linear strain hardening parameter: H ≥ 0
         theta, |float|, controls relative proportions of isotropic and kinematic hardening: 0 ≤ theta ≤ 1
         density, |float|, mass density of the material
         <atmPressure>, |float|, optional atmospheric pressure for update of elastic bulk and shear moduli (default = 101 kPa)

Theory
------

Yield Condition
"""""""""""""""

The yield condition for the Drucker-Prager model can be 
expressed in terms of positive material constants :math:`F_y` and :math:`\rho` as ([Drucker-Prager1952]_ and [Chen-Saleeb1994]_)

.. math::

   f_1\left(\boldsymbol{\sigma}, h^{\mathrm{iso}}, \boldsymbol{x}\right) = \left\| \boldsymbol{s} - \boldsymbol{x} \right\| 
   + \rho \operatorname{tr}\,\boldsymbol{\sigma} - \sqrt{\frac{2}{3}} h^{\mathrm{iso}} \leq 0

where the deviatoric stress tensor :math:`\boldsymbol{s}` is defined by

.. math:: 

   \boldsymbol{s} \triangleq \boldsymbol{\sigma} - \mathrm{tr} \boldsymbol{\sigma} \mathbf{1}


The yield condition for the tension cutoff yield surface is defined as

.. math:: 

   f_2(\boldsymbol{\sigma}, q^{ten}) = \mathrm{tr} \boldsymbol{\sigma} + q^{ten} \leq 0

where

.. math:: 

   q^{\mathrm{ten}} = T_o \exp(-\delta_2^{} \kappa^{\mathrm{ten}})
   \qquad \text{and} \quad
   T_o = \sqrt{\frac{2}{3}} \frac{F_y}{\rho}


Flow Rule
"""""""""

.. math::

   \dot{\boldsymbol{\varepsilon}}^p = \dot{\lambda} \boldsymbol{g}
   \qquad\text{with}\qquad \boldsymbol{g} = \mathbf{n}+\bar{\rho} \mathbf{1}

Hardening
"""""""""

The isotropic hardening is defined by

.. math:: 
   
   h^{\mathrm{iso}} = F_{\mathrm{y}}^{} + \theta H_{\mathrm{mix}} \kappa^{iso} + (F_{\infty} - F_0) \left(1 - \exp(-H_{\mathrm{sat}} \kappa^{iso}) \right)


The back-stress is defined as

.. math:: 

   \boldsymbol{x} = \frac{2}{3} \, (1 - \theta)  H_{\mathrm{mix}} \, \mathbb{I}^{\mathrm{dev}} : \boldsymbol{\kappa}^{\mathrm{kin}}


Parameter Calibration
----------------------

:math:`\alpha`
  The parameter :math:`\alpha` is the frictional strength parameter that controls the rate of plastic deformation. It has units of *inverse stress*.

  In the OpenSees documentation for DruckerPrager, the parameter :math:`\alpha` is referred to as ``rho`` (:math:`\rho`).


The Drucker-Prager strength parameters :math:`\alpha` and :math:`F_y` can be related to the Mohr-Coulomb friction angle, :math:`\phi`, and cohesive intercept, :math:`c`, by evaluating the yield surfaces in a deviatoric plane as described by Chen and Saleeb (1994). 
By relating the two yield surfaces in triaxial compression, the following expressions are determined

.. math:: 

   \rho = \frac{2 \sqrt{2} \sin \phi}{\sqrt{3} (3 - \sin \phi)}


.. math::

   F_y = \frac{6 c \cos \phi}{\sqrt{2} (3 - \sin \phi)}


Output
------

The valid queries to the Drucker-Prager material when creating an ElementRecorder are ``'strain'`` and ``'stress'`` as well as ``'state'``. 
The query ``'state'`` records a vector of state variables during a particular analysis. 
The columns of this vector are as follows. (Note: If the option ``-time`` is included in the creation of the recorder, the first column will be the time variable for each recorded point and the columns below are shifted accordingly.)

* Column 1 - First invariant of the stress tensor, :math:`I_1 = \mathrm{tr}(\boldsymbol{\sigma})`.
* Column 2 - The following tensor norm, :math:`\left\| \boldsymbol{s} + \boldsymbol{x} \right\|`, where :math:`\boldsymbol{s}` is the deviatoric stress tensor and :math:`\boldsymbol{x}` is the back-stress tensor.
* Column 3 - First invariant of the plastic strain tensor, :math:`\mathrm{tr}(\boldsymbol{\varepsilon}^p)`.
* Column 4 - Norm of the deviatoric plastic strain tensor, :math:`\left\| \mathbf{e}^p \right\|`.



Examples
--------


.. ref-gallery::
   
   examples/material/model-5012


.. This example provides the input file and corresponding results for a confined triaxial compression (CTC) test using a single 8-node brick element and the Drucker-Prager constitutive model.
.. A schematic representation of this test is shown below, (a) depicts the application of hydrostatic pressure, and (b) depicts the application of the deviator stress. 
.. Also shown is the stress path resulting from this test plotted on the meridian plane. 
.. As shown, the element is loaded until failure, at which point the model can no longer converge, as this is a stress-controlled analysis.

.. .. figure:: DruckerPrager.png
..    :align: center
..    :width: 800px
..    :figclass: align-center

..    Triaxial compression test with the Drucker-Prager model.

.. .. literalinclude:: DruckerPragerExample.tcl
..    :language: bash



References
----------

.. [Patek] Patek

.. [Drucker-Prager1952] Drucker, D. C. and Prager, W., "Soil mechanics and plastic analysis for limit design." Quarterly of Applied Mathematics, vol. 10, no. 2, pp. 157–165, 1952.

.. [Chen-Saleeb1994] Chen, W. F. and Saleeb, A. F., Constitutive Equations for Engineering Materials Volume I: Elasticity and Modeling. Elsevier Science B.V., Amsterdam, 1994.


Code Developed by: |peter| and |pedro| at U.Washington.