.. _KrylovNewton:

Krylov-Newton
^^^^^^^^^^^^^

.. tabs::
   
   .. tab:: Python 
      
      .. function:: algorithm('KrylovNewton', iterate='current', increment='current', maxDim=3)
         
          :param iterate: tangent to iterate on, options are ``current``, ``initial``, ``noTangent``. default is ``current``. 
          :type iterate: string
          :param increment: tangent to increment on, options are ``current``, ``initial``, ``noTangent``. default is ``current`` 
          :type increment: string
          :param maxDim: max number of iterations until the tangent is reformed and acceleration restarts (default = 3)  of iterations within a time step until a new tangent is formed
          :type maxDim: float
   
   .. tab:: Tcl
      
      .. function:: algorithm KrylovNewton <-iterate $tangIter> <-increment $tangIncr> <-maxDim $maxDim> 

      .. list-table:: 
        :widths: 10 10 40
        :header-rows: 1

        * - Argument
          - Type
          - Description
        * - $tangIter
          - |string|
          - tangent to iterate on, options are current, initial, noTangent. default is current. 
        * - $tangIncr
          - |string|
          - tangent to increment on, options are current, initial, noTangent. default is current 
        * - $maxDim
          - |float|
          - max number of iterations until the tangent is reformed and acceleration restarts (default = 3)  of iterations within a time step until a new tangent is formed
      


This command is used to construct a KrylovNewton algorithm which uses a modified :ref:`Newton` method with Krylov subspace acceleration to advance to the next time step. 

References:

* Scott, M.H. and G.L. Fenves. "A Krylov Subspace Accelerated Newton Algorithm: Application to Dynamic Progressive Collapse Simulation of Frames." Journal of Structural Engineering, 136(5), May 2010. DOI 
