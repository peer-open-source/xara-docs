.. _J2Plasticity:

J2 Plasticity
^^^^^^^^^^^^^

*J2Plasticity* is a multi dimensional material model that employs the von Mises :math:`J_2` yield criterion and isotropic hardening.

.. tabs::

   .. tab:: Python
      
      .. py:method:: nDMaterial('J2Plasticity', tag, K, G, sig0, sigInf, delta, H)
         :no-index:

         :param int tag: unique tag identifying material
         :param |float| K: bulk modulus
         :param |float| G: shear modulus
         :param |float| sig0: initial yield stress
         :param |float| sigInf: final saturation yield stress
         :param |float| delta: exponential hardening parameter
         :param |float| H: linear hardening parameter
   
   .. tab:: OpenSees

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

The theory for the non hardening case can be found in [[1]].
The elastic model is an :ref:`ElasticIsotropic` formulation:

.. math::

   \boldsymbol{S} = K \operatorname{tr}(\boldsymbol{E}_e) + 2 G \operatorname{dev}(\boldsymbol{E}_e)

The yield function :math:`\phi` is 

.. math::

   \phi (\boldsymbol{S},q) = || \operatorname{dev} \boldsymbol{S} || - \sqrt{\tfrac{2}{3}} q(\boldsymbol{\xi})

where :math:`q` is the *saturation isotropic hardening* given by:

.. math::
   
   q(\boldsymbol{\xi}) = \sigma_0 + (\sigma_\inf - \sigma_0) \exp (-\delta\boldsymbol{\xi}) + H \boldsymbol{\xi}

Flow rules are

.. math::

   \dot{\boldsymbol{E}}_{\mathrm{p}} = \gamma  \frac{\partial \phi}{\partial \sigma}

   \dot \xi = -\gamma  \frac{\partial \phi}{\partial q}

linear viscosity is exhibited with :math:`\gamma = \frac{\phi}{\eta}` ( if :math:`\phi > 0` )

Backward Euler integration is employed in the implementation.

For rate independent cases, set :math:`\eta = 0`.

References
----------

Code Developed by: **Ed Love**
