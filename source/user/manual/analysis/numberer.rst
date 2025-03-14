.. _numberer:

numberer
^^^^^^^^

This command configures a **DOF_Numberer**. 
This determines the mapping between equation numbers in the system of equations and the degrees-of-freedom at the nodes, basically how degrees-of-freedom are numbered.


.. tabs::
   
   .. tab:: Python
      
      .. py:method:: Model.numberer(type, *args)
   
   .. tab:: Tcl

      .. function:: numberer type arg1? ...

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40
      
         $numbererType, |string|,  the numberer type
         $args, |list|,   a sequence of arguments for that type


The following contain information about ``type`` and the args required for each of the available numberers:

.. toctree::
   :maxdepth: 1

   numberer/PlainNumberer
   numberer/RCM
   numberer/AMD

Code developed by: |fmk|
