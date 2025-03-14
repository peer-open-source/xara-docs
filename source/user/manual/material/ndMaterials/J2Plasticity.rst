.. _J2Plasticity:

J2 Plasticity
^^^^^^^^^^^^^

This command is used to construct a multi dimensional material that has a von Mises (J2) yield criterion and isotropic hardening.

.. function:: nDMaterial J2Plasticity $matTag $K $G $sig0 $sigInf $delta $H

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, unique tag identifying material
   $K, |float|,	   bulk modulus
   $G, |float|,	   shear modulus
   $sig0, |float|,	   initial yield stress
   $sigInf, |float|,	   final saturation yield stress
   $delta, |float|,	   exponential hardening parameter
   $H, |float|,linear hardening parameter



Theory 
------

The theory for the non hardening case can be found [[1]]

J2 isotropic hardening material class

Elastic Model

.. math::

   \boldsymbol{S} = K \operatorname{tr}(\boldsymbol{E}_e) + 2 G \operatorname{dev}(\boldsymbol{E}_e)

The yield function :math:`\phi` is 

.. math::

   \phi (\boldsymbol{S},q) = || \operatorname{dev} \boldsymbol{S} || - \sqrt{\tfrac{2}{3}} q(\boldsymbol{\xi})

where :math:`q` is the *saturation isotropic hardening* given by:

.. math::
   
   q(\boldsymbol{\xi}) = \sigma_0 + (\sigma_\inf - \sigma_0) \exp (-\delta\boldsymbol{\xi}) + H \boldsymbol{\xi}

Flow Rules

.. math::

   \dot{\boldsymbol{E}}_{\mathrm{p}} = \gamma  \frac{\partial \phi}{\partial \sigma}

   \dot \xi = -\gamma  \frac{\partial \phi}{\partial q}

Linear Viscosity: :math:`\gamma = \frac{\phi}{\eta}` ( if :math:`\phi > 0` )

Backward Euler integration is employed.

For rate independent cases, set :math:`\eta = 0`.

References
----------

Code Developed by: **Ed Love**
