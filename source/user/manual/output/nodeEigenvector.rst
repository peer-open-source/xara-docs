.. _nodeEigenvector:

nodeEigenvector
^^^^^^^^^^^^^^^

.. tabs::

   .. tab:: Python 

      .. py:method:: Model.nodeEigenvector(tag, dof=None)
         
         :param tag: The tag of a :ref:`node` at which the eigenvector is desired.
         :type tag: |integer|
         :param dof: The degree of freedom at which the eigenvector is desired.
         :type dof: |integer|
         :returns: A list containing the eigenvector at the node.
