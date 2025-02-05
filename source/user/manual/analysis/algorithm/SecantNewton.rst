.. _SecantNewton:

Secant Newton
-------------

.. function:: algorithm SecantNewton <-iterate $tangIter> <-increment $tangIncr> <-maxDim $maxDim> 

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

This command is used to construct a SecantNewton algorithm object which uses the two-term update to accelerate the convergence of the modified newton method. 

.. note::

   * The default "cut-out" values recommended by Crisfield (R1=3.5, R2=0.3) are used. 

Example
-------

The following examples demonstrate the command to create a SecantNewton solution algorithm.

.. tabs::

   .. tab:: Tcl

      .. code-block:: tcl

         algorithm SecantNewton -iterate current -increment current -maxDim 3

   .. tab:: Python

      .. code-block:: python

         model.algorithm('SecantNewton', iterate='current', increment='current', maxDim=3)


References
----------

* Crisfield, M.A. "Non-linear Finite Element Analysis of Solids and Structures", Vol. 1, Wiley, 1991. 
  
