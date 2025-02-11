.. _ArcLengthControl:

Arc-Length Control
^^^^^^^^^^^^^^^^^^

.. tabs::
   
   .. tab:: Python 
      
      .. py:function:: model.integrator("ArcLength", s, alpha, det=False, exp=0.0, iterScale=1.0)
      
         :param s: the arc-Length
         :type s: float
         :param alpha:  a scaling factor on the reference loads.
         :type alpha: float
         :param det: |bool|, use the determinant to choose incrementation sign.
         :param exp: |float|
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
