.. _test:

test
****

This command is used to construct the **Convergence Test**. The convergence test is that object the :ref:`algorithm` uses to detect if convergence has been achieved. The convergence test is applied to the matrix equation, :math:`Ax=b` stored in the :ref:`system`. In the finite element setting and under normal integration schemes and algorithms, the :math:`x` corresponds to the displacement increment and :math:`b` the unbalanced forces. 


.. function:: test type? args? ...

The following contain information about ``type`` and the ``args`` required for each of the available system types:

.. toctree::
   :maxdepth: 1

   test/NormUnbalance
   test/NormDispIncr
   test/NormEnergyIncr
   test/RelativeNormUnbalance
   test/RelativeNormDispIncr
   test/RelativeEnergyIncr
   test/TotalRelativeNormDisplacementIncrement
   test/FixedNumberIterations
