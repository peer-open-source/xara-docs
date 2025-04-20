.. _DruckerPrager:

Drucker Prager
^^^^^^^^^^^^^^

Code Developed by: |peter| and |pedro| at U.Washington.

This command is used to construct an inelastic material that has a Drucker-Prager yield criterion.

.. tabs::
   .. tab:: Python
      .. py:method:: Model.nDMaterial("DruckerPrager", tag, k, G, sigmaY, rho, rhoBar, Kinf, Ko, delta1, delta2, H, theta, density, atmPressure=101.0)
         :no-index:

         Constructs a Drucker-Prager material with the specified parameters.

         :param tag: integer tag identifying material
         :param k: bulk modulus
         :param G: shear modulus
         :param sigmaY: yield stress
         :param rho: frictional strength parameter
         :param rhoBar: controls evolution of plastic volume change: :math:`0 \leq \bar{\rho} \leq \rho`
         :param Kinf: nonlinear isotropic strain hardening parameter: :math:`K_{\infty} \geq 0`
         :param Ko: nonlinear isotropic strain hardening parameter: :math:`K_o \geq 0`
         :param delta1: nonlinear isotropic strain hardening parameter: :math:`\delta_1 \geq 0`
         :param delta2: tension softening parameter: :math:`\delta_2 \geq 0`
         :param H: linear strain hardening parameter: :math:`H \geq 0`
         :param theta: controls relative proportions of isotropic and kinematic hardening: :math:`0 \leq \theta \leq 1`
         :param density: mass density of the material
         :param atmPressure: optional atmospheric pressure for update of elastic bulk and shear moduli (default = 101 kPa)

   .. tab:: Tcl
         .. function:: nDMaterial DruckerPrager $tag $k $G $sigmaY $rho $rhoBar $Kinf $Ko $delta1 $delta2 $H $theta $density <$atmPressure>

         .. csv-table:: 
            :header: "Argument", "Type", "Description"
            :widths: 10, 10, 40

            $tag, |float|, integer tag identifying material
            $k, |float|,	bulk modulus
            $G, |float|, shear modulus
            $sigmaY, |float|, yield stress
            $rho, |float|, frictional strength parameter
            $rhoBar, |float|, controls evolution of plastic volume change: 0 ≤ $rhoBar ≤ $rho
            $Kinf, |float|, nonlinear isotropic strain hardening parameter: $Kinf ≥ 0
            $Ko, |float|, nonlinear isotropic strain hardening parameter: $Ko ≥ 0
            $delta1, |float|, nonlinear isotropic strain hardening parameter: $delta1 ≥ 0
            $delta2, |float|, tension softening parameter: $delta2 ≥ 0
            $H, |float|, linear strain hardening parameter: $H ≥ 0
            $theta, |float|, controls relative proportions of isotropic and kinematic hardening: 0 ≤ $theta ≤ 1
            $density, |float|, mass density of the material
            <$atmPressure>, |float|, optional atmospheric pressure for update of elastic bulk and shear moduli (default = 101 kPa)

.. note::

   The material formulations for the Drucker-Prager object are ``"ThreeDimensional"`` and ``"PlaneStrain"``


The yield condition for the Drucker-Prager model can be expressed as ([Drucker-Prager1952]_ and [Chen-Saleeb1994]_)

.. math:: 

   f\left(\boldsymbol{\sigma}, q^{iso}, \mathbf{q}^{kin}\right) = \left\| \boldsymbol{\sigma}^{\mathrm{dev}} + \mathbf{q}^{kin} \right\| + \rho I_1 + \sqrt{\frac{2}{3}} q^{iso} - \sqrt{\frac{2}{3}} \sigma_Y^{} \leq 0


where the deviatoric stress tensor :math:`\boldsymbol{\sigma}^{\mathrm{dev}}` is defined by

.. math:: 

   \boldsymbol{\sigma}^{\mathrm{dev}} \triangleq \boldsymbol{\sigma} - \mathrm{tr} \boldsymbol{\sigma} \mathbf{1}


and the parameters :math:`\rho_{}^{}` and :math:`\sigma_Y^{}` are positive material constants.

The isotropic hardening stress is defined as

.. math:: 
   
   q^{iso} = \theta H \alpha^{iso} + (K_{\infty} - K_o) \exp(-\delta_1 \alpha^{iso})


The kinematic hardening stress (or back-stress) is defined as

.. math:: 

   \mathbf{q}^{kin} = -(1 - \theta) \frac{2}{3} H \mathbb{I}^{dev} : \boldsymbol{\alpha}^{kin}


The yield condition for the tension cutoff yield surface is defined as

.. math:: 

   f_2(\boldsymbol{\sigma}, q^{ten}) = \mathrm{tr} \boldsymbol{\sigma} + q^{ten} \leq 0

where

.. math:: 

   q^{ten} = T_o \exp(-\delta_2^{} \alpha^{ten})
   \qquad \text{and} \quad
   T_o = \sqrt{\frac{2}{3}} \frac{\sigma_Y}{\rho}


and

.. math:: 


The valid queries to the Drucker-Prager material when creating an ElementRecorder are 'strain' and 'stress' as well as 'state'. The query 'state' records a vector of state variables during a particular analysis. The columns of this vector are as follows. (Note: If the option ``-time`` is included in the creation of the recorder, the first column will be the time variable for each recorded point and the columns below are shifted accordingly.)

* Column 1 - First invariant of the stress tensor, :math:`I_1 = \mathrm{tr}(\boldsymbol{\sigma})`.
* Column 2 - The following tensor norm, :math:`\left\| \mathbf{s} + \mathbf{q}^{kin} \right\|`, where :math:`\mathbf{s}` is the deviatoric stress tensor and :math:`\mathbf{q}^{\mathrm{kin}}` is the back-stress tensor.
* Column 3 - First invariant of the plastic strain tensor, :math:`\mathrm{tr}(\boldsymbol{\varepsilon}^p)`.
* Column 4 - Norm of the deviatoric plastic strain tensor, :math:`\left\| \mathbf{e}^p \right\|`.

The Drucker-Prager strength parameters :math:`\rho` and :math:`\sigma_Y` can be related to the Mohr-Coulomb friction angle, :math:`\phi`, and cohesive intercept, :math:`c`, by evaluating the yield surfaces in a deviatoric plane as described by Chen and Saleeb (1994). By relating the two yield surfaces in triaxial compression, the following expressions are determined

.. math:: 

   \rho = \frac{2 \sqrt{2} \sin \phi}{\sqrt{3} (3 - \sin \phi)}


.. math::

   \sigma_Y = \frac{6 c \cos \phi}{\sqrt{2} (3 - \sin \phi)}


Example
-------

This example provides the input file and corresponding results for a confined triaxial compression (CTC) test using a single 8-node brick element and the Drucker-Prager constitutive model. A schematic representation of this test is shown below, (a) depicts the application of hydrostatic pressure, and (b) depicts the application of the deviator stress. Also shown is the stress path resulting from this test plotted on the meridian plane. As shown, the element is loaded until failure, at which point the model can no longer converge, as this is a stress-controlled analysis.

   .. figure:: DruckerPrager.png
      :align: center
      :width: 800px
      :figclass: align-center

      Drucker Prager Example

   .. literalinclude:: DruckerPragerExample.tcl
      :language: bash


References
----------

.. [Drucker-Prager1952] Drucker, D. C. and Prager, W., "Soil mechanics and plastic analysis for limit design." Quarterly of Applied Mathematics, vol. 10, no. 2, pp. 157–165, 1952.

.. [Chen-Saleeb1994] Chen, W. F. and Saleeb, A. F., Constitutive Equations for Engineering Materials Volume I: Elasticity and Modeling. Elsevier Science B.V., Amsterdam, 1994.

