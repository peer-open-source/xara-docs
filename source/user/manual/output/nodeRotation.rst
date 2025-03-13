.. _nodeRotation:

nodeRotation
============

.. tabs::
   
   .. tab:: Python
      
      .. py:function:: model.nodeRotation(tag)
      
         :param model: A Model object
         :type model: :class:`Model`
         :param int tag: The tag of the :ref:`node`

         :return: A list of four float components of a normalized quaternion representing the rotation of the node.
   
   .. tab:: Tcl
      
      .. function:: nodeRotation tag
   
         :param int tag: The tag of the :ref:`node`


This method is used to obtain the current rotation state of a node during an analysis with finite rotations.
Rotations are represented with `quaternions <https://en.wikipedia.org/wiki/Quaternion>`_. 
Note that by convention, the *scalar* part of the quaternion is stored at the *end* of the returned list.

This method can be used with the `veux <https://veux.io>`_ package to visualize 3D cross sectional deformations in
frame elements, as demonstrated with `this <https://gallery.stairlab.io/examples/framecircle/>`_ example.


.. note::

   In small deformation analysis, rotations are typically obtained using :ref:`nodeDisp`. However,
   when large rotations are involved, these values cannot be used reliably. This is because the
   values returned by ``nodeDisp`` are defined as the algebraic sum of all increments to the solution;
   this is not valid for 3D rotational degrees of freedom.


This method is available in ``sees`` version ``0.1.15``.

