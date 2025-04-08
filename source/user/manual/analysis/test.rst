.. _test:

test
****

This command is used to define the *Convergence Test*. 
The convergence test is that object the :ref:`algorithm` uses to detect if convergence has been achieved. 
The convergence test is applied to the matrix equation, :math:`Ax=b` stored in the :ref:`system`. 
In the finite element setting and under normal integration schemes and algorithms, the :math:`x` corresponds to the displacement increment and :math:`b` the equilbrium residual. 

.. tabs::
   .. tab:: Python
      .. py:method:: Model.test(type, *args)

         :param type: the type of convergence test to be used
         :type type: str
         :param args: the arguments required for the specified convergence test
         :return: None
         :rtype: None

   .. tab:: Tcl

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
