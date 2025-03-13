.. _element:

Element
*******

This method is used to construct an element and add it to the :class:`Model`. 

.. tabs::

   .. tab:: Python

      .. function:: model.element(type, tag, nodes, *args, **kwds)

         :param type: string defining the type of element
         :param tag: integer tag identifying the element
         :param nodes: tuple of integer tags identifying the nodes that form the element
         :param args, kwds: arguments particular to the element ``type``


   .. tab:: Tcl

      .. function:: element $type $tag (num $nodes) $args ...

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         ``type``, |string|,      element type
         ``tag``,  |integer|,     unique element tag.
         ``nodes``,   |integerlist|, a list of element nodes with number dependent on ele type
         ``args``, |list|,        a list of element arguments with number dependent on ele type


The type of element created and the additional arguments required depends on the **$type** provided.

The following subsections contain information about ``type`` and the number of nodes and args required for each of the available element types:

.. toctree::
   :maxdepth: 2

   elements/frame/index
   elements/plane/index
   elements/shell/index
   elements/solid/index
   elements/joint/index
   elements/other/index

2. Truss Elements

.. toctree::
   :maxdepth: 1

   elements/Truss


