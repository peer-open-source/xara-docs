.. _PlaneStress:

PlaneStress
^^^^^^^^^^^

.. tabs::

   .. tab:: Python 
      
      .. function:: Model.section("PlaneStress", tag, material, thickness)
         :no-index:

         :param tag: integer tag identifying the section
         :type tag: int
         :param material: integer tag identifying a :ref:`nDMaterial`
         :type material: int
         :param thickness: section thickness
         :type thickness: float


A PlaneStress section imposes a plane stress condition on the response of it's material.
