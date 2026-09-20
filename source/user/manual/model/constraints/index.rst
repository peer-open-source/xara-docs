.. _ModelConstraints:

Constraints
***********


Single point constraints are constraints that define the response of a single degree-of-freedom at a node. 
These constraints can be homogeneous (ie, equal to zero) or non-homogeneos. 
Non homogeneous single-point constraints, which define the non-zero response of the degree-of-freedom, can be constant or time varying. 


*Multi-point constraints* (MP_Constraints) are constraints that allow the user to define the relationship between the response of a set of the degrees-of-freedom at one node (the constrained node) in relation to the response of the degrees-of-freedom at another node (the retained node).
In structural analysis MP_Constraints are used to enforce rigid-diaphragm constraints, equal constraints (response of degrees-of-freedom at two nodes move the same), or rotated constraints (response of degrees-of-freedom at two nodes related through a rotation matrix).


.. toctree::
   :maxdepth: 1

   constrain
   equalDOF
   diaphragm
   rigidLink


