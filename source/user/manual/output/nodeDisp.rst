.. _nodeDisp:

nodeDisp
********


.. tabs::

   .. tab:: Python 

      .. py:method:: Model.nodeDisp(tag, dof=None)

         Return the displacement at a specified node.

         :param |integer| tag: The tag of the :ref:`node` whose displacements are sought.
         :param |integer| dof: Optional: specific degree of freedom at the node (between 1 and :py:attr:`Model.ndf`, inclusive).
         :returns: A |list| of the displacement components at the node when ``dof=None``, otherwise a |float|.

   .. tab:: Tcl

      .. function:: nodeDisp $tag <$dof>


      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         tag, |integer|, tag identifying node whose displacements are sought
         dof, |integer|, optional: specific dof at the node (1 through ndf)



If optional $dof is not provided, an array containing all displacement components for every dof at the node is returned.


Example
-------

The following example is used to set the variable ``disp1`` to the nodal displacement at node given by the variable **tag** in the **1** degree-of-freedom direction.

1. **Tcl Code**

   .. code-block:: tcl

      set disp1 [nodeDisp $tag 1]

2. **Python Code**

   .. code-block:: python

      u1 = model.nodeDisp(tag,1)


Code developed by: |fmk|
