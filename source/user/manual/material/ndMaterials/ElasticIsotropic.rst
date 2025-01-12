.. _ElasticIsotropic:

Elastic Isotropic Material
^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct an ElasticIsotropic material object.

.. function:: nDMaterial ElasticIsotropic $matTag $E $v <$rho>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|,	   unique tag identifying material
   $E, |float|,	   elastic Modulus
   $v, |float|,	   Poisson's ratio
   $rho, |float|, mass density. optional default = 0.0.

.. note::
   The material formulations for the ElasticIsotropic object are "ThreeDimensional," "PlaneStrain," "Plane Stress," "AxiSymmetric," and "PlateFiber."


Formulations
============

A linear isotropic function can be expressed in terms of two parameters :math:`\lambda` and :math:`\mu` as follows :cite:p:`gurtin1981introduction`:

.. math::
   \boldsymbol{S}




Code Developed by: |mhs|

