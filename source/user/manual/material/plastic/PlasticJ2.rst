.. _PlasticJ2:

PlasticJ2
^^^^^^^^^


.. tabs::

   .. tab:: Python
      
      .. py:class:: xara.MultiaxialMaterial("PlasticJ2", E, nu, Fy, ...)
         :no-index:

         :gparam Elastic E: Young's modulus, :math:`E` [1]_. Units of :ref:`stress <UnitStress>`.
         :gtype E: |float|
         :gparam Elastic nu: Poisson's ratio, :math:`\nu` [1]_
         :gtype nu: |float|
         :gparam Plastic Fy: Initial yield stress, :math:`F_y` [1]_. Units of :ref:`stress <UnitStress>`.
         :gparam "Isotropic Hardening" Hiso: linear isotropic hardening modulus
         :gtype Hiso: |float|
         :gparam "Nonlinear Hardening" Fs: Saturation yield stress
         :gtype Fs: |float|
         :gparam "Nonlinear Hardening" b: exponential hardening parameter
         :gtype b: |float|
         :gparam "Nonlinear Hardening" C: Nonlinear kinematic hardening parameter
         :gtype C: |float|
         :gparam "Nonlinear Hardening" gamma: Nonlinear kinematic hardening parameter
         :gtype gamma: |float|
         :gparam Density density: Mass density. Units of :ref:`density <UnitDensity>`.
         :gtype density: |float|

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


Examples
--------

.. ref-gallery::

   examples/material/material-0011
   examples/frames/frame-2007
   examples/plane/plane-2001
