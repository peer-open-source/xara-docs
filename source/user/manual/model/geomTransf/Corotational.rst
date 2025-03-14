.. _CorotTR:

Corotational
^^^^^^^^^^^^

The corotational coordinate transformation performs a geometric transformation of beam stiffness and resisting force from a *basic* system [1]_ to the global coordinate system. [2]_

.. tabs::

   .. tab:: Python

      .. py:method:: Model.geomTransf("Corotational", tag, vecxz, [offi, offj])
         :no-index:

         :param integer tag: integer tag identifying transformation
         :type tag: int
         :param vecxz: X, Y, and Z components of vecxz, the vector used to define the local x-z plane of the local-coordinate system, **required in 3D**. The local y-axis is defined by taking the cross product of the vecxz vector and the x-axis.
         :type vecxz: tuple of floats
         :param offi: joint offset values -- offsets specified with respect to the global coordinate system for element-end node i (optional, the number of arguments depends on the dimensions of the current model).
         :type offi: tuple of floats
         :param offj: joint offset values -- offsets specified with respect to the global coordinate system for element-end node j (optional, the number of arguments depends on the dimensions of the current model).
         :type offj: tuple of floats

   .. tab:: Tcl
      .. function:: geomTransf Corotational $transfTag < $vecxzX $vecxzY $vecxzZ > <-jntOffset $dXi $dYi $dZi $dXj $dYj $dZj>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $transfTag, |integer|, integer tag identifying transformation
         $vecxzX $vecxzY $vecxzZ,  |float|,  "X, Y, and Z components of vecxz, the vector used to define the local x-z plane of the local-coordinate system. The local y-axis is defined by taking the cross product of the vecxz vector and the x-axis.
         
         These components are specified in the global-coordinate system X,Y,Z and define a vector that is in a plane parallel to the x-z plane of the local-coordinate system.
         
         These items need to be specified for the three-dimensional problem."
         $dXi $dYi $dZi, |float|, "joint offset values -- offsets specified with respect to the global coordinate system for element-end node i (optional, the number of arguments depends on the dimensions of the current model)."
         $dXj $dYj $dZj, |float|, "joint offset values -- offsets specified with respect to the global coordinate system for element-end node j (optional, the number of arguments depends on the dimensions of the current model)."

.. note::
	
	The element coordinate system and joint offset values are specified as in the :ref:`linearTR`.

References
----------

.. [1] Perez, Claudio M., and Filip C. Filippou. “On Nonlinear Geometric Transformations of Finite Elements.” International Journal for Numerical Methods in Engineering 125, no. 17 (September 15, 2024): e7506. https://doi.org/10.1002/nme.7506.

.. [2] De Souza, R. M. "Force-based finite element for large displacement inelastic analysis of frames" University of California, Berkeley (2000)

Code Developed by: |rms|, |cmp|

