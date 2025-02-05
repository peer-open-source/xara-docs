Plain Numberer
^^^^^^^^^^^^^^

This command is used to construct a Plain degree-of-freedom numbering object to provide the mapping between the degrees-of-freedom at the nodes and the equation numbers. A Plain numberer just takes whatever order the domain gives it nodes and numbers them, this ordering is both dependent on node numbering and size of the model. The command to construct a Plain numberer is a follows:

.. tabs::

   .. tab:: Python

      .. function:: model.numberer("Plain")

   .. tab:: Tcl

      .. function:: numberer Plain

For very small problems and for the sparse matrix solvers which provide their own numbering scheme, order is not really important so plain numberer is just fine. 
For large models and analysis using solver types other than the sparse solvers, the order will have a major impact on performance of the solver and the plain handler is a poor choice.


Example 

The following example shows how to construct a plain numberer

1. **Tcl Code**

   .. code-block:: tcl

      numberer Plain


2. **Python Code**

   .. code-block:: python

      model.numberer("Plain")



Code Developed by: |fmk|
