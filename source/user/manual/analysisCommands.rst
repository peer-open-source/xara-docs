.. _lblAnalysisCommands:

Analysis
--------

.. _lblAnalysisCommands:

Analysis
--------
 
In OpenSees, an analysis is constructed by combining various component objects. These components determine the specific type of analysis executed on the model. As illustrated in the figure below, the component classes include:

#. **Constraint Handler** – Manages the enforcement of constraint equations during the analysis, handling boundary conditions and imposed displacements.
#. **DOF Numberer** – Establishes the correspondence between equation numbers in the system of equations and the degrees of freedom at the nodes.
#. **SystemOfEqn & Solver** – Defines the storage and solution method for the system of equations :math:`Ax=b`.
#. **Convergence Test** – Identifies when the analysis has achieved convergence.
#. **Solution Algorithm** – Outlines the sequence of steps to resolve the non-linear equations at each time step.
#. **Integrator** – Specifies the equations to solve, the predictive steps, and the method for updating node responses based on the solution to :math:`Ax=b`.

Similar to modeling commands, all analysis commands should be executed as methods of the ``Model`` class.

.. toctree::
   :maxdepth: 1

   analysis/constraints
   analysis/numberer
   analysis/system
   analysis/test
   analysis/algorithm
   analysis/integrator
   analysis/analysis
   analysis/analyze
   analysis/eigen
   analysis/modalProperties
   analysis/responseSpectrumAnalysis



.. toctree::
   :maxdepth: 1

   analysis/constraints
   analysis/numberer
   analysis/system
   analysis/test
   analysis/algorithm
   analysis/integrator
   analysis/analysis
   analysis/analyze
   analysis/eigen
   analysis/modalProperties
   analysis/responseSpectrumAnalysis


