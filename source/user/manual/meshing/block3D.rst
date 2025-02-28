
block3D
^^^^^^^

The block3D command generates three-dimensional meshes of :ref:`solid` elements.

.. tabs::

   .. tab:: Python 
      
      .. py:function:: model.block3D(div, start, element, args, block)
      
         :param div: tuple of three integers specifying the number of divisions in each direction
         :type div: tuple
         :param start: tuple of two integers specifying the starting :ref:`node` and :ref:`element` tags.
         :param args: tuple of arguments to be passed to each element
         :type args: tuple
         :param dict block: dictionary of reference node locations 

