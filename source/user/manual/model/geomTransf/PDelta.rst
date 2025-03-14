.. _PDeltaTR:

PDelta
^^^^^^

This command is used to construct the *PDelta* coordinate transformation, which performs a geometric transformation of a :ref:`Frame <Frame>` element's response considering second-order :math:`P-\Delta` effects.

.. tabs::

   .. tab:: Python

      .. py:method:: Model.geomTransf("PDelta", tag, vecxz, [offi, offj])
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
      .. function:: geomTransf PDelta $transfTag < $vecxzX $vecxzY $vecxzZ > <-jntOffset $dXi $dYi $dZi $dXj $dYj $dZj>

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

   The stiffness for the :math:`P-\Delta` transformation is not the true tangent to the element response. 
   Consequently :ref:`Newton` iterations may not converge quadratically.

The element coordinate system and joint offset values are specified as in the :ref:`linearTR`.


Code Developed by: |rms|
