.. _system:

system
******

This command configures the ``LinearSOE`` and ``LinearSolver`` which store and solve the linearized system of equations, :math:`\boldsymbol{A}\boldsymbol{x}=\boldsymbol{b}` during each step.

.. function:: system type? arg1? ...

The type of ``LinearSOE`` created and the additional arguments required depends on the ``type`` provided in the command.

The following contain information about type? and the args required for each of the available systems:

.. toctree::
   :maxdepth: 1

   system/BandGeneral
   system/BandSPD
   system/ProfileSPD
   system/SuperLU
   system/Umfpack
   system/FullGeneral
   system/SparseSYM
   system/Mumps

