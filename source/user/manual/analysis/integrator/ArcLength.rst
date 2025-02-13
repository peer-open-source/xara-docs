.. _ArcLengthControl:

Arc-Length Control
^^^^^^^^^^^^^^^^^^

.. tabs::
   
   .. tab:: Python 
      
      .. py:function:: model.integrator("ArcLength", s, alpha, det=False, exp=0.0, iterScale=1.0)
      
         :param float s: the initial arc-Length
         :param float alpha:  a scaling factor on the reference loads.
         :param bool det:  if True, use the determinant to choose incrementation sign [1]_.
         :param float exp: exponent parameter from [1]_
         :param iterScale: |float|, a scaling factor on the arc-length incrementation.

   .. tab::Tcl

      .. function:: integrator ArcLength $s $alpha < -det > < -exp $exp > < -iterScale $iterScale >

      .. list-table:: 
        :widths: 10 10 40

        * - Argument
          - Type
          - Description
        * - ``$s``
          - |float|
          - the arcLength
        * - ``$alpha``
          - |float|
          - a scaling factor on the reference loads. 
        * - ``-det``
          - Flag
          - use the determinant to choose incrementation sign.
        * - ``$exp``
          - |float|
        * - ``$iterScale``
          - |float|
          - a scaling factor on the arc-length incrementation. 
      

This command is used to construct an ArcLength integrator object. In an
analysis step with ArcLength we seek to determine the time step that will
result in our constraint equation being satisfied. 


Examples
--------

.. code-block:: python

   import sees.openseespy as ops
   model = ops.Model(ndm=2, ndf=3)

   ...

   model.integrator("ArcLength", 1, det=True, exp=0.5)


.. code-block:: tcl

   integrator ArcLength 1 -det -exp 0.5

.. code-block:: tcl

   integrator ArcLength 1 -exp 0.5

References
----------

.. [1] Clarke, M.J. and Hancock, G.J. (1990) ‘A study of incremental‐iterative strategies for non‐linear analyses’, International Journal for Numerical Methods in Engineering, 29(7), pp. 1365–1391. Available at: https://doi.org/10.1002/nme.1620290702 .
