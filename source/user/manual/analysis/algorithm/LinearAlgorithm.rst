.. _LinearAlgorithm:

Linear
^^^^^^

This command is used to set a Linear algorithm which takes one iteration to solve the system of equations.

.. tabs::

   .. tab:: Python

      .. function:: model.algorithm("Linear", [initial=False, factorOnce=False])
         :no-index:
         
         :param initial: optional flag to indicate to use initial stiffness
         :type initial: |bool|
         :param factorOnce: optional flag to indicate to only set up and factor matrix once
         :type factorOnce: |bool|

   .. tab:: Tcl

      .. function:: algorithm Linear <-initial> <-factorOnce>
      
      
      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40
      
         -initial, |string|,  optional flag to indicate to use initial stiffness
         -factorOnce, |string|, optional flag to indicate to only set up and factor matrix once


.. note:: 
   
   As the tangent matrix typically will not change during the analysis in case of an elastic system it is highly advantageous to use the ``factorOnce`` option. 
   Do not use this option if you have a nonlinear system and you want the tangent used to be actual tangent at time of the analysis step.

   The Linear algorithm requires no :ref:`test` and will complain if one is provided. This means that convergence is not checked.

   Certain transient explicit :ref:`integrators <integrator>` require a Linear algorithm.


Example
-------

The following examples demonstrate the command to create a Linear solution algorithm.

.. tabs::

   .. tab:: Tcl

      .. code-block:: tcl

         algorithm Linear

   .. tab:: Python

      .. code-block:: python

         model.algorithm('Linear')


Code Developed by: |fmk|
