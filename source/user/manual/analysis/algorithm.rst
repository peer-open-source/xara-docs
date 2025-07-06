.. _algorithm:

algorithm
^^^^^^^^^

.. tabs::

   .. tab:: Python

      .. py:method:: Model.algorithm(name, *args)

         Configure a root-finding algorithm to solve the nonlinear residual equations.

   .. tab:: Tcl

      .. function:: algorithm name? arg1? ...


where ``name`` is a string indentifying one of the following algorithms:


.. toctree::
   :maxdepth: 1

   algorithm/LinearAlgorithm
   algorithm/Newton
   algorithm/NewtonLineSearch
   algorithm/ModifiedNewton
   algorithm/AcceleratedNewton
   algorithm/Broyden
   algorithm/ExpressNewton


