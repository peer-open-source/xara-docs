.. _constraints:

constraints
^^^^^^^^^^^

This command is used to configure the ConstraintHandler. 
The ConstraintHandler determines how the constraint equations are enforced in the analysis. 
Constraint equations define a specified value for a DOF, or a relationship between DOFs.

.. tabs::
   
   .. tab:: Python
      .. py:function:: model.constraints(type, *args)

   .. tab:: Tcl
      .. function:: constraints type? arg1? ...

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40
         
         ``type``, |string|,  the constraints type
         ``args``, |list|,   a list of arguments for that type


The following contain information about ``type`` and the ``args`` required for each of the available constraint handlers:

.. toctree::
   :maxdepth: 1

   constraint/PlainConstraints
   constraint/PenaltyMethod
   constraint/TransformationMethod
   constraint/lagrangeMultipliers
   constraint/Auto
