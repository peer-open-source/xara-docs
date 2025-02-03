.. _node:

Node
****

This method is used to construct a ``Node`` which stores information about coordinates and mass at a single point. The assignment of mass is optional.

.. tabs::

   .. tab:: Python 

      .. function:: model.node(tag, coords, [mass])

         :param tag: integer tag identifying node
         :param coords: tuple of **ndm** nodal coordinates
         :param mass: tuple of **ndf** nodal mass values

         :return: None

   .. tab:: Tcl 

      .. function:: node $tag [ndm $coords] <-mass [ndf $mass]>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|, unique tag identifying node
         $coords,  |listFloat|,  **ndm** nodal coordinates
         $mass, |listFloat|, optional **ndf** nodal mass values


Example
-------

The following examples demonstrate the commands in a script to add two nodes to domain in which the last model command specified an ``ndm`` of ``2`` and a ``ndf`` of 3. The two nodes to be added have node tags ``3`` and ``4``. Node ``3`` is located at coordinates (168.0, 144.0) and node ``4`` at location ``(168.0,144.0)``. Node ``4`` is assigned a mass of ``(10.0, 10.0, 0.)``.


.. tabs::

   .. tab:: Python

      .. code-block:: python

         model.node(3, (168.0,  0.0))
         model.node(4, (168.0,  0.0), mass=(10.0, 10.0, 0.0))

   .. tab:: Tcl

      .. code-block:: tcl

         node 3 168.0 0.0
         node 4 168.0 144.0 -mass 10.0 10.0 0.0


Code Developed by: |fmk|
