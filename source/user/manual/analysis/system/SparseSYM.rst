SparseSYM
^^^^^^^^^

This command is used to construct a sparse symmetric system of equations which uses a row-oriented solution method in the solution phase. 

.. function:: system SparseSYM

.. note:: 

   This solver works for negative definite system as well as positive definite.

Example 
-------

The following example shows how to construct a *SparseSYM* system:

1. **Tcl Code**

   .. code-block:: tcl

      system SparseSYM

2. **Python Code**

   .. code-block:: python

      model.system('SparseSYM')


References
----------

* Kincho H. Law and David R. McKay, “A Parallel Row-Oriented Sparse Solution Method for Finite Element Structural Analysis,” International Journal for Numerical Methods in Engineering, 36:2895-2919, 1993.

Code developed by: `J. Peng <https://www.linkedin.com/in/james-peng-a6194b13/>`_

