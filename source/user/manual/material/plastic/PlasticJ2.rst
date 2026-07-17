.. _PlasticJ2:

Plastic
^^^^^^^


.. tabs::

   .. tab:: Python
      
      .. py:class:: xara.MultiaxialMaterial("PlasticJ2", E, nu, Fy, ...)
         :no-index:

         :gparam Elastic E: Young's modulus, :math:`E` [1]_
         :gtype E: |float|
         :gparam Elastic nu: Poisson's ratio, :math:`\nu` [1]_
         :gtype nu: |float|
         :gparam Plastic Fy: Initial yield stress, :math:`F_y` [1]_
         :gparam "Isotropic Hardening" Hiso: linear isotropic hardening modulus
         :gtype Hiso: |float|
         :gparam "Nonlinear Hardening" Fs: Saturation yield stress
         :gtype Fs: |float|
         :gparam "Nonlinear Hardening" Hsat: exponential hardening parameter
         :gtype Hsat: |float|
   
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

.. [1] These arguments are supported by the :ref:`parameter <parameter>` commands.
