.. _PlaneStrain:

PlaneStrain
^^^^^^^^^^^

A *PlaneStrain* section maintains a condition of plane strain in a 2D solid element.

.. tabs::

   .. tab:: Python 

      .. function:: Model.section("PlaneStrain", tag, material, thickness)

         :param tag: integer tag identifying the section
         :type tag: int
         :param material: integer tag identifying a :ref:`nDMaterial`
         :type material: int
         :param thickness: section thickness
         :type thickness: float

The plane strain condition is characterized by the constraints:

.. math::

   \mathbf{g}_n \cdot \boldsymbol{E}\mathbf{g}_n = 0

Example
=======


