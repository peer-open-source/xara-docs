.. _J2Plasticity:

J2 Plasticity
^^^^^^^^^^^^^

*J2Plasticity* is a multi dimensional material model that employs the von Mises :math:`J_2` yield criterion and isotropic hardening.

.. tabs::

   .. tab:: Python
      
      .. py:method:: Model.nDMaterial('J2Plasticity', tag, K, G, Fy, Fsat, delta, Hiso)
         :no-index:

         :param |integer| tag: unique tag identifying material
         :param |float| K: Bulk modulus, :math:`\kappa`
         :param |float| G: Shear modulus, :math:`\mu`
         :param |float| Fy: Initial yield stress
         :param |float| Fsat: Saturation yield stress
         :param |float| delta: exponential hardening parameter
         :param |float| Hiso: linear isotropic hardening modulus
   
   .. tab:: OpenSees

      .. function:: nDMaterial J2Plasticity $tag $K $G $sig0 $sigInf $delta $Hiso <$eta>;

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         tag, |integer|, unique tag identifying material
         K, |float|,	   bulk modulus
         G, |float|,	   shear modulus
         sig0, |float|,	   initial yield stress
         sigInf, |float|,	   final saturation yield stress
         delta, |float|,	   exponential hardening parameter
         H, |float|,linear hardening parameter


Theory 
------

The theory for the non hardening case can be found in [1].
The elastic model is an :ref:`ElasticIsotropic` formulation:

.. math::

   \boldsymbol{T} = K \operatorname{tr} \boldsymbol{E}_e + 2 G \operatorname{dev} \boldsymbol{E}_e

The yield function :math:`f` is 

.. math::

   f (\boldsymbol{T},q) = \| \operatorname{dev} \boldsymbol{T} \| - \sqrt{\tfrac{2}{3}} \, Y(\bar{\epsilon}_{\mathrm{p}})

where :math:`\bar{\epsilon}_{\mathrm{p}}` is the scalar *equivalent plastic tensile strain*, and :math:`Y` is a scalar function that defines the *saturation isotropic hardening* given by:

.. math::
   
   Y(\bar{\epsilon}_{\mathrm{p}}) = H_{\mathrm{iso}} \bar{\epsilon}_{\mathrm{p}} + Y_{\infty}  + (Y_0 - Y_{\infty}) \exp \left(-\delta \bar{\epsilon}_{\mathrm{p}} \right)

The flow rules are

.. math::

   \dot{\boldsymbol{E}}_{\mathrm{p}} = \gamma  \frac{\partial f}{\partial \boldsymbol{T}}

..
   \dot{\bar{\epsilon}}_{\mathrm{p}} = - \gamma  \frac{\partial f}{\partial Y}

where :math:`\gamma` is the plastic consistency parameter and :math:`\boldsymbol{E}_{\mathrm{p}}` is the plastic strain tensor.
linear viscosity is exhibited with :math:`\gamma = \frac{\phi}{\eta}` ( if :math:`\phi > 0` )

Backward Euler integration is employed in the implementation.

.. note::

   * For linear isotropic hardening, set :math:`Y_{\infty} = Y_0`
   * For rate independent cases, set :math:`\eta = 0`.

References
----------

Code Developed by: **Ed Love**
