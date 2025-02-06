.. _algorithm:

algorithm
^^^^^^^^^

This method is used to define a ``SolutionAlgorithm``, which determines the sequence of steps taken to solve the non-linear equation.

.. tabs::

   .. tab:: Python

      .. function:: model.algorithm(name, *args)

   .. tab:: Tcl

      .. function:: algorithm name? arg1? ...


where ``name`` is a string indentifying one of the following algorithms:

.. toctree::
   :maxdepth: 1

   algorithm/LinearAlgorithm
   algorithm/Newton
   algorithm/NewtonLineSearch
   algorithm/ModifiedNewton
   algorithm/KrylovNewton
   algorithm/SecantNewton
   algorithm/BFGS
   algorithm/Broyden
   algorithm/ExpressNewton

