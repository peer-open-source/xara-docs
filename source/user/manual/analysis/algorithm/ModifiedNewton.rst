.. _ModifiedNewton:

Modified Newton
---------------

.. function:: algorithm ModifiedNewton <-initial> 

.. list-table:: 
   :widths: 10 10 40
   :header-rows: 1

   * - Argument
     - Type
     - Description
   * - -initial
     - |string|
     - optional flag to indicate to use initial stiffness iterations

This command is used to construct a ModifiedNewton algorithm, which uses the modified newton-raphson algorithm to solve the nonlinear residual equation. 

Example 
-------

The following examples demonstrate the command to create a ModifiedNewton solution algorithm.

.. tabs::

   .. tab:: Tcl

      .. code-block:: tcl

         algorithm ModifiedNewton -initial

   .. tab:: Python

      .. code-block:: python

         model.algorithm('ModifiedNewton', '-initial')
