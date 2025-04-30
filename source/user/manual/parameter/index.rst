Parameters
^^^^^^^^^^

OpenSees provides a flexible parameter system for updating model properties during or between analyses. 
Parameters are identified by tags and can be linked to material, element, or section attributes—enabling sensitivity studies, calibration routines, or simulation of gradual changes such as aging or damage. These parameters can be updated dynamically within analysis loops using commands like updateParameter, allowing time-dependent behavior or repeated simulations with varying properties.

.. toctree::
   :maxdepth: 1

   parameter
   setParameter
   addToParameter
   updateParameter
   getParamTags
   getParamValue

References
----------

*  Scott M.H., Haukaas T. (2008). "Software framework for parameter updating and finite element response sensitivity analysis." Journal of Computing in Civil Engineering, 22(5):281-291.

