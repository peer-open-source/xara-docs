.. _reactions:

reactions
^^^^^^^^^

.. py:method:: Model.reactions()
   
   Compute the reaction forces at all nodes.


.. _nodeReaction:


nodeReaction
^^^^^^^^^^^^


.. py:method:: Model.nodeReaction(tag, dof)

   Return the reaction forces at a specific node. The method :py:meth:`Model.reactions()` must be called first to compute the reaction forces.

   :param integer tag: tag identifying node whose reactions are sought
   :param integer dof: optional: specific dof at the node (1 through ndf)


Examples
--------

.. ref-gallery::

   examples/plane/plane-2001

