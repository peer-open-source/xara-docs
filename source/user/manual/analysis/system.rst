.. _system:

system
******

.. tabs::

   .. tab:: Python 

      .. py:method:: Model.system(type, *args)

         Set the system type to be used by the :class:`Model`.

         :param |string| type: The system type.
         :param args: A sequence of arguments for that type.
   
   .. tab:: Tcl

      .. function:: system type? arg1? ...

This command configures the ``LinearSOE`` and ``LinearSolver`` which store and solve the linearized system of equations, :math:`\boldsymbol{A}\boldsymbol{x}=\boldsymbol{b}` during each step.


The following systems are available:

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

