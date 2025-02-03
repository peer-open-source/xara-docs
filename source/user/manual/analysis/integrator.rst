.. _integrator:

integrator
**********

This method is used to define an *integrator*. The Integrator object is used for the following:

 #. determine the predictive step for time t+dt, :math:`\Delta U` in static analysis, :math:`\Delta U`, :math:`\Delta \dot U`, and :math:`\Delta \ddot U` in a transient analysis.
 #. specify the tangent matrix and residual vector at any iteration, i.e. what constitutes the :math:`A` matrix and :math:`b` vector in :math:`Ax=b`.
 #. determine the corrective step based on the x vector, i.e. given :math:`x` what is :math:`\Delta U` in static analysis, :math:`\Delta U`, :math:`\Delta \dot U`, and :math:`\Delta \ddot U` in a transient analysis.

.. tabs::
   
   .. tab:: python

      .. code-block:: python

         integrator(type, *args)

   .. tab:: tcl

      .. code-block:: tcl

         integrator $type < $args > 


.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40
   
	``type``, |string|,  the integrator type
	``args``, |list|,   a list of arguments for that type


The type of integrator used in the analysis is dependent on whether it is a static analysis or transient analysis. 
The following contain information about ``type`` and the args required for each of the available integrator types:

Static Integrators:

.. toctree::
   :maxdepth: 1

   integrator/LoadControl
   integrator/DisplacementControl
   integrator/MinimumUnbalancedDisplacementNorm
   integrator/ArcLength


Transient Integrators:

.. toctree::
   :maxdepth: 1

   integrator/CentralDifference
   integrator/Newmark
   integrator/HHT
   integrator/GeneralizedAlpha
   integrator/TRBDF2
   integrator/ExplicitDifference


Utility Integrators:

.. toctree::
   :maxdepth: 1

   integrator/gimmeMCK

Code developed by: |fmk|

