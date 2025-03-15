.. _PlaneStress:

PlaneStress
^^^^^^^^^^^

.. tabs::

   .. tab:: Python 
      
      .. py:method:: Model.section("PlaneStress", tag, material, thickness)
         :no-index:

         :param tag: integer tag identifying the section
         :type tag: |integer|
         :param material: integer tag identifying a :ref:`nDMaterial`
         :type material: |integer|
         :param thickness: section thickness
         :type thickness: float


A PlaneStress section imposes a plane stress condition on the response of it's material.
