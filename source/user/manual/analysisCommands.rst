.. _lblAnalysisCommands:


Analysis
--------

Similar to modeling commands, all analysis commands should be executed as methods of the :ref:`Model <modelClass>` class.

The primary methods which determine *what* analysis is performed are:

#. :ref:`integrator <integrator>` Specifies the equations to solve, the predictive steps, and the method for updating node responses based on the solution to :math:`\boldsymbol{A}x=b`.
#. :ref:`algorithm <algorithm>` Outlines the sequence of steps to resolve the non-linear equations at each time step.

Analysis is performed by invoking the :ref:`analyze <analyze>` method:

.. code:: Python

   model.analyze(1)

 
OpenSees provides detailed control over several additional aspects of the analysis procedure. These include:

#. **Constraint Handler** – Manages the enforcement of constraint equations during the analysis, handling boundary conditions and imposed displacements.
#. **DOF Numberer** – Establishes the correspondence between equation numbers in the system of equations and the degrees of freedom at the nodes.
#. **SystemOfEqn & Solver** – Defines the storage and solution method for the system of equations :math:`\boldsymbol{A}x=b`.
#. **Convergence Test** – Identifies when the analysis has achieved convergence.


.. toctree::
   :maxdepth: 1

   analysis/algorithm
   analysis/integrator
   analysis/analysis
   analysis/analyze
   analysis/constraints
   analysis/numberer
   analysis/system
   analysis/test
   analysis/eigen
   analysis/modalProperties
   analysis/responseSpectrumAnalysis



