Nodes
*****

Single point constraints are constraints that define the response of a single degree-of-freedom at a node. 
These constraints can be homogeneous (ie, equal to zero) or non-homogeneos. 
Non homogeneous single-point constraints, which define the non-zero response of the degree-of-freedom, can be constant or time varying. 


.. toctree::
   :maxdepth: 1

   nodes/node
   nodes/fix
   nodes/fixX
   nodes/fixY
   nodes/fixZ

Non-homogeneous constraints are added with wither :ref:`sp_constraint/sp` or :ref:`imposedMotion` commands inside the :ref:`plainPattern` or :ref:`multisupportExcitation` commands.

