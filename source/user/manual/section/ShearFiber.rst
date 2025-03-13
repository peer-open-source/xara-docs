
ShearFiber
^^^^^^^^^^

A ``ShearFiber`` section is used to model a fiber section with shear deformation. 
The section is defined by a collection of fibers that are discretized in the cross-section. 

.. tabs::

   .. tab:: Python (RT)
    
      .. py:function:: model.section("ShearFiber", tag, **kwds)
         :no-index:
         
         :param tag: unique section tag
         :type tag: |integer|


   .. tab:: Tcl

      .. function:: section ShearFiber $tag {}
         
         :param tag: unique section tag


The ``fiber`` method is used to populate the section with fibers. The required arguments are:

.. tabs::

   .. tab:: Python
    
      .. function:: model.fiber((y, z), A, tag, warp, section)

         :param y: :math:`y`-coordinate of the fiber
         :type y: float
         :param z: :math:`z`-coordinate of the fiber
         :type z: float
         :param A: area of the fiber
         :type A: float
         :param tag: tag of a preexisting material created with the :ref:`material` method.
         :type tag: int
         :param warp: tuple of up to three warping modes
         :type warp: tuple
         :param section: tag of the section to which the fiber belongs. This argument must be passed by keyword.
         :type section: int


In general, the ``warp`` modes are scaled by independent amplitude fields which introduce additional degrees of freedom.
When no additional degrees of freedom are provided by the model, elements in the :ref:`Frame` library will constrain these fields to match an appropriate strain field.


The valid :ref:`eleResponse` queries are 

* ``'force'``, and 
* ``'deformation'``. 
