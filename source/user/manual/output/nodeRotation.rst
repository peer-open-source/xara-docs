.. _nodeRotation:

nodeRotation
^^^^^^^^^^^^

.. tabs::
   
   .. tab:: Python
      
      .. py:method:: Model.nodeRotation(tag)

         Return the current rotation at a node.

         :param int tag: The tag of the :ref:`node` from which to obtain the rotation.
         :return: A |list| of four float components of a normalized quaternion representing the rotation of the node.
   
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



References 
----------

* Perez, C.M. and Filippou, F.C. (2024) ‘On nonlinear geometric transformations of finite elements’, International Journal for Numerical Methods in Engineering, p. e7506. Available at: https://doi.org/10.1002/nme.7506.

Code Developed by: |cmp|