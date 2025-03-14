.. _TenNodeTetrahedron:

TenNodeTetrahedron
^^^^^^^^^^^^^^^^^^

This command is used to construct an ten-node tetrahedron, which uses the standard isoparametric formulation.

.. tabs::

   .. tab:: Python (RT)

      .. py:method:: Model.element("TenNodeTetrahedron", tag, nodes, material, *args)
         :no-index:

         :param tag: integer tag identifying the element
         :param nodes: tuple of integer tags identifying the nodes that form the element
         :param material: integer tag identifying the nDMaterial
         :param args: optional arguments
         :param kwargs: optional keyword arguments

   .. tab:: Tcl

      .. function:: element TenNodeTetrahedron $tag $node1 $node2 $node3 $node4 $node5 $node6 $node7 $node8 $node9 $node10 $matTag <$b1 $b2 $b3> <doInitDisp?>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|,	unique element object tag
         $node1 .. $node10, 10 |integer|, nodes of tet (ordered as shown in fig below)
         $matTag, |integer|, tag of nDMaterial
         $b1 $b2 $b3, |listFloat|, optional: body forces in global x y z directions
         <-doInitDisp $value>, |bool|, optional: consider initial displacements if $value is 0


This element is based on second-order interpolation of nodal quantities, this means that the strain and stress field inside the element are linearly interpolated. Four Gauss-points inside the element are used for integration. 


.. figure:: figures/TenNodeTetrahedron/TenNodeTetrahedron.png
   :align: center
   :figclass: align-center

   TenNodeTetrahedron element node numbering


The valid :ref:`eleResponse` queries to a ``TenNodeTetrahedron`` element are ``"forces"``, ``"stresses"``, and ``"material $tag $args..."`` 


.. note::

   This element can only be defined with a :class:`Model` where ``ndm=3`` and ``ndf=3``

Examples
--------

The following example constructs a TenNodeTetrahedron element with tag ``1`` between nodes **1, 2, 3, 4, 5, 6, 7, 8, 9, 10** with an nDMaterial of tag **1** and body forces given by varaiables **b1, b2, b3**.

1. **Tcl Code**

.. code-block:: tcl

  element TenNodeTetrahedron 1 1 2 3 4 5 6 7 8 9 10 1 $b1 $b2 $b3

2. **Python Code**

.. code-block:: python

  model.element('TenNodeTetrahedron',1, (1,2,3,4,5,6,7,8,9,10), 1, (b1, b2, b3))


Code Developed by: `José Antonio Abell <www.joseabell.com>`_ and José Luis Larenas (UANDES). 
For bugs and features, start a new issue on the `GitHub repo <https://github.com/OpenSees/OpenSees>`_ and tag me (@jaabell). 


