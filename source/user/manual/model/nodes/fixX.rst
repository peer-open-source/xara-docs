.. _fixX:

fixX
^^^^

This command is used to construct multiple homogeneous single-point boundary constraints for all nodes whose :math:`x`-coordinate lies within a specified distance from a specified coordinate.

.. function:: fixX $x (ndf $ConstrValues) <-tol $tol>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $xCoordinate, |float|, x-coordinate of nodes to be constrained
   $constrValues, |listInt|, "| ndf constraint values (0 or 1) corresponding to the ndf 
   | degrees-of-freedom.
   | 0 unconstrained (or free)
   | 1 constrained (or fixed)"
   $tol, |float|, user-defined tolerance (optional: default = 1e-10)


Example
-------

The following example demonstrate the command to fix the first 3 degrees-of-freedom at all nodes in the model at :math:`x=0`.

.. tabs::

   .. tab:: Python

      .. code-block:: python

         model.fixX(0.0, 1, 1, 1, 0, 0, 0)

   .. tab:: Tcl

      .. code-block:: none

         fixX 0.0 1 1 1 0 0 0 


Code Developed by: **fmk**



