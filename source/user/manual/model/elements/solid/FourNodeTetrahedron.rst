.. _FourNodeTetrahedron:

FourNodeTetrahedron Element
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct an four-node tetrahedron element object, which uses the standard isoparametric formulation.

.. function:: element FourNodeTetrahedron $eleTag $node1 $node2 $node3 $node4 $matTag <$b1 $b2 $b3> <doInitDisp?>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|,	unique :ref:`Element` tag
   $node1 .. $node4, 4 |integer|, nodes of tet (ordered as shown in fig below)
   $matTag, |integer|, tag of nDMaterial
   $b1 $b2 $b3, |listFloat|, optional: body forces in global x y z directions
   <-doInitDisp $value>, |bool|, optional: consider initial displacements if $value is 0

This is the simplest possible continuum finite element for 3-D analysis. It's based on linear interpolation of nodal quantities, this means that the strain and stress field inside the element are constant. The single Gauss point results can be interpreted as constant within the element. Because of this, the element has a tendency to lock up when used for simulating bending. In the incompressible limit (caution for materials with :math:`\nu \rightarrow 0.5` or metal plasticity) this element will also lock up. Therefore, caution is warranted when using this element as un-careful mesh refinement might not guarantee a convergence to the mathematical solution or a fast-enough convergence rate. If possible, use a higher-order element like the :ref:`TenNodeTetrahedron`. 


.. figure:: figures/FourNodeTetrahedron/FourNodeTetrahedron.png
	:align: center
	:figclass: align-center

	FourNodeTetrahedron element node numbering


.. note::

   This element can only be defined after a :class:`Model` with **ndm=3, ndf=3**


The valid :ref:`eleResponse` queries to a ``FourNodeTetrahedron`` element are ``"forces"``, ``"stresses"``, ``"strains"`` and ``"material $matNum matArg1 matArg2 ..."`` Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.


Example 
-------

The following example constructs a FourNodeTetrahedron element with tag **1** between nodes **1, 2, 3, 4** with an nDMaterial of tag **1** and body forces given by varaiables **b1, b2, b3**.

1. **Tcl Code**

   .. code-block:: tcl

      element FourNodeTetrahedron 1 1 2 3 4 1 $b1 $b2 $b3

2. **Python Code**

   .. code-block:: python

      model.element('FourNodeTetrahedron',1, (1,2,3,4), 1, (b1, b2, b3))

Code Developed by: `José Antonio Abell <www.joseabell.com>`_ (UANDES). For issues, start a new issue on the `OpenSees github repo <https://github.com/OpenSees/OpenSees>`_ and tag me (@jaabell). 
