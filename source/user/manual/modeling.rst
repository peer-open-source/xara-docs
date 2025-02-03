.. _modeling:

Modeling
--------

A finite element model consists of **Nodes**, **Elements**, **Constraints**, and **Loads**. 
In OpenSees the Constraints are divided into two types: single-point constraints (**SP_Constraints)** for specifying the boundary condition for a specific degree-of-freedom at a node and multiple-point constraints (**MP_Constraints**) for specifying the relationship between the responses between the degrees-of-freedom at two separate nodes. The loads in OpenSees are assigned to **LoadPatterns**. Also associated with load patterns are **TimeSeries** objects ans sometime **SP_Constraints** when the user wants to specify time-varying **SP_Constraints**. 

In OpenSees there are commands to add each of these types of objects to a domain:


.. toctree::
   :maxdepth: 1

   model/model_class
   model/spConstraints
   material/index
   section
   model/element
   model/geomTransf
   model/beamIntegrations
   model/mpConstraints
   model/timeSeries
   model/pattern
   model/damping
   model/mass
   model/region
   model/block

