.. _PlaneStrain:

PlaneStrain
^^^^^^^^^^^

A *PlaneStrain* section maintains a condition of plane strain in a 2D solid element.

.. tabs::

   .. tab:: Python 

      .. function:: Model.section("PlaneStrain", tag, material, thickness)
         :no-index:

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

.. code-block:: Python

   model = ops.Model(ndm=2, ndf=2)

   model.material("ElasticIsotropic", 1, E=29e3, v=0.3)
   model.section("PlaneStrain", 1, 1, 2.5)

A complete example is available at the STAIRLab `gallery <https://gallery.stairlab.io/examples/example6/>`_.


