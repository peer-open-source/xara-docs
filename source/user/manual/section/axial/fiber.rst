Fiber (*AxialFiber*)
^^^^^^^^^^^^^^^^^^^^


.. tabs::

   .. tab:: Python
    
      .. py:method:: Model.fiber((y, z), A, tag, warp, section)

         :param y: :math:`y`-coordinate of the fiber
         :type y: float
         :param z: :math:`z`-coordinate of the fiber
         :type z: float
         :param A: area of the fiber
         :type A: float
         :param material: tag of a preexisting material created with the :ref:`material` method.
         :type material: |integer|
         :param section: tag of the section to which the fiber belongs. This argument must be passed by keyword.
         :type section: |integer|
