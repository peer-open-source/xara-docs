
``MixedFrame``: Frame with force-interpolation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mixed finite element formulation for 3D frame elements.

.. tabs::

   .. tab:: Python (RT)

      .. py:function:: Model.element("MixedFrame", tag, nodes, section=None, transform=None, integration=None, *args)

         :param tag: unique element tag
         :type tag: int
         :param nodes: tuple of *two* integer node tags (see :ref:`node`)
         :type nodes: tuple
         :param section: integer tag identifying a :ref:`section`.
         :type section: int
         :param transform: identifier for previously-defined :ref:`geomTransf`
         :type transform: int
         :param integration: identifier for previously-defined integration rule.


This formulation supports higher order strain measures and shear deformations.