.. _FourNodeTetrahedron:

Tetrahedron
^^^^^^^^^^^

Construct a four-node tetrahedron element, which uses the standard isoparametric formulation.

.. function:: element FourNodeTetrahedron $eleTag $node1 $node2 $node3 $node4 $matTag <$b1 $b2 $b3> <doInitDisp?>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|,	unique :ref:`Element` tag
   $node1 .. $node4, 4 |integer|, nodes of tet (ordered as shown in fig below)
   $matTag, |integer|, tag of nDMaterial
   $b1 $b2 $b3, |listFloat|, optional: body forces in global x y z directions
   <-doInitDisp $value>, |bool|, optional: consider initial displacements if $value is 0


Theory
------

The linear tetrahedron was introduced by Gallagher et al. (1962)
It employs a linear interpolation of nodal quantities. 
The element has a tendency to lock up both in bending, and in the incompressible limit :math:`\nu \rightarrow 0.5`. 


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

      element FourNodeTetrahedron 1 1 2 3 4 1

2. **Python Code**

   .. code-block:: python

      model.element("FourNodeTetrahedron", 1, (1,2,3,4), 1)


References 
----------

* R. H. Gallagher, J. Padlog, and P. P. Bijlaard, "Stress analysis of Heated Complex Shapes" American Rocket Society Journal, 32, no. 5 (1962), 700-707 DOI: https://doi.org/10.2514/8.6128

Code Developed by: `José Antonio Abell <www.joseabell.com>`_ (UANDES). For issues, start a new issue on the `OpenSees github repo <https://github.com/OpenSees/OpenSees>`_ and tag me (@jaabell). 

