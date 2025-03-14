fixZ
^^^^

.. tabs::

   .. tab:: Python

      .. py:method:: Model.fixZ(z, constr, tol=0)

         Fix the degrees-of-freedom at all nodes in the model whose :math:`z`-coordinate lies within a specified distance from a specified coordinate.

         :param float z: z-coordinate of nodes to be constrained
         :param list constr: ndf constraint values (0 or 1) corresponding to the :py:attr:`Model.ndf` degrees-of-freedom.
            0 unconstrained (or free)
            1 constrained (or fixed)
         :param float tol: user-defined tolerance (optional: default = 1e-10)

   .. tab:: Tcl

      .. function:: fixZ $z (ndf $ConstrValues) <-tol $tol>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $zCoordinate, |float|, z-coordinate of nodes to be constrained
         $constrValues, |intList|, "| ndf constraint values (0 or 1) corresponding to the :py:attr:`Model.ndf` 
         | degrees-of-freedom.
         | 0 unconstrained (or free)
         | 1 constrained (or fixed) "
         $tol, |float|, user-defined tolerance (optional: default = 1e-10)

This command imposes multiple homogeneous single-point boundary constraints for all nodes whose :math:`z`-coordinate lies within a specified distance from a specified coordinate.

Example
-------

The following example demonstrate the command to fix the first 3 degrees-of-freedom at all nodes in the model at :math:`z` location **30.0**.

1. **Tcl Code**

   .. code-block:: none

      fixZ 30.0 1 1 1 0 0 0 

2. **Python Code**

   .. code-block:: none

      model.fixZ(30.0, 1, 1, 1, 0, 0, 0)

Code Developed by: |fmk|
