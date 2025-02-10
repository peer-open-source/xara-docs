.. _ElasticIsotropic:

Elastic Isotropic
^^^^^^^^^^^^^^^^^

This command is used to construct an *ElasticIsotropic* material.

.. tabs::

   .. tab:: Python

      .. function:: model.material("ElasticIsotropic", tag, E, v, rho=0.0)

         :param tag: integer tag identifying material
         :param E: Young's elastic modulus
         :param v: Poisson's ratio
         :param rho: mass density. optional default = 0.0.

   .. tab:: Tcl

      .. function:: nDMaterial ElasticIsotropic $tag $E $v <$rho>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|,	   unique tag identifying material
         $E, |float|,	   elastic Modulus
         $v, |float|,	   Poisson's ratio
         $rho, |float|, mass density. optional default = 0.0.


..
  The material formulations for the ElasticIsotropic object are "ThreeDimensional", "PlaneStrain," "Plane Stress," "AxiSymmetric," and "PlateFiber."


Theory
------

A linear isotropic function can be expressed in terms of two parameters :math:`\lambda` and :math:`\mu` as follows :cite:p:`gurtin1981introduction`:

.. math::

   \boldsymbol{S} = \lambda \text{tr}(\boldsymbol{E}) \boldsymbol{1} + 2\mu \boldsymbol{E}




Code Developed by: |mhs|

