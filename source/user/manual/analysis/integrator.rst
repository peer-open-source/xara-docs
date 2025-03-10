.. _integrator:

integrator
**********

This method is used to define an *integrator*. 
In the context of dynamic analysis, the integrator implements a time-stepping algorithm for ordinary differential equations.
In the context of static analysis, the integrator implements a *numerical continuation* method.
More specifically, the integrator performs the following:

#. determine the predictive step for time :math:`t+\Delta t`, :math:`\Delta \boldsymbol{u}` in static analysis, :math:`\Delta \boldsymbol{u}`, :math:`\Delta \dot U`, and :math:`\Delta \ddot U` in a transient analysis.
#. specify the residual and tangent at any iteration, i.e. what constitutes the :math:`\boldsymbol{A}` matrix and :math:`\boldsymbol{b}` vector in :math:`Ax=b`.
#. determine the corrective step based on the x vector, i.e. given :math:`x` what is :math:`\Delta \boldsymbol{u}` in :ref:`StaticAnalysis` analysis, :math:`\Delta \boldsymbol{u}`, :math:`\Delta \dot{\boldsymbol{u}}`, and :math:`\Delta \ddot{\boldsymbol{u}}` in a transient analysis.

.. tabs::
   
   .. tab:: python

      .. function:: model.integrator(type, *args)

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




.. [1] Clarke, M.J. and Hancock, G.J. (1990) ‘A study of incremental‐iterative strategies for non‐linear analyses’, International Journal for Numerical Methods in Engineering, 29(7), pp. 1365–1391. Available at: https://doi.org/10.1002/nme.1620290702 .

Code developed by: |fmk|

