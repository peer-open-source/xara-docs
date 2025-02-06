
``MixedFrame``
^^^^^^^^^^^^^^

Mixed finite element formulation for 3D frame elements.

.. tabs::

   .. tab:: Python (RT)

      .. py:function:: Model.element("MixedFrame", tag, nodes, section=None, transform=None, *args)

         :param tag: unique element tag
         :type tag: int
         :param nodes: two integer node tags
         :type nodes: tuple
         :param section: section tag
         :type section: int
         :param transform: identifier for previously-defined coordinate-transformation
         :type transform: int


