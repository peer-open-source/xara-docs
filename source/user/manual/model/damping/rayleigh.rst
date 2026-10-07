.. _rayleigh:

Rayleigh Damping
^^^^^^^^^^^^^^^^

.. tabs::
 
   .. tab:: Python

      .. py:method:: Model.rayleigh(cM, cK, cKInit, cKcomm)

         :param cM: factor :math:`\alpha_{m}` applied to the mass matrix
         :type cM: float
         :param cK: factor :math:`\beta_{k}` applied to the current stiffness matrix
         :type cK: float
         :param cKInit: factor :math:`\beta_{K_{init}}` applied to the initial stiffness matrix
         :type cKInit: float
         :param cKcomm: factor :math:`\beta_{K_{comm}}` applied to the committed stiffness matrix
         :type cKcomm: float

   .. tab:: Tcl

      .. function:: rayleigh $alphaM $betaK $betaKInit $betaKcomm

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         alphaM, |float|,      factor applied to elements or nodes mass matrix
         betaK,  |float|,     factor applied to elements current stiffness matrix.
         betaKInit, |float|,     factor applied to elements initial stiffness matrix
         betaKcomm, |float|,     factor applied to elements committed stiffness matrix


This command is used to assign damping to all previously-defined elements and nodes. 
When using Rayleigh damping, the damping matrix for an element or node, :math:`\boldsymbol{C}`, is specified as a combination of stiffness and mass-proportional damping matrices: 

.. math::
   
   \boldsymbol{C} = \alpha_m M + \beta_k K_{current} + \beta_{k_{init}} K_{init} + \beta_{K_{comm}} K_{last commit}



