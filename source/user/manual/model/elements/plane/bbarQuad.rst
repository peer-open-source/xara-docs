
.. _bbarQuad:

MixedQuad
^^^^^^^^^

This command is used to construct a four-node quadrilateral element object, which uses a bilinear isoparametric formulation along with a mixed volume/pressure B-bar assumption. This element is for plane strain problems only.

.. tabs::

   .. tab:: Python

      .. function:: model.element("bbarQuad", tag, nodes, thick, matTag, *args, **kwargs)

         :param tag: integer tag identifying the element
         :param nodes: tuple of integer tags identifying the nodes that form the element
         :param thick: float element thickness
         :param matTag: integer tag identifying the nDMaterial object
         :param args: optional arguments
         :param kwargs: optional keyword arguments

   .. tab:: Tcl

      .. function:: element bbarQuad $tag {*}$nodes $thick $matTag

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|,	unique element object tag
         $iNode $jNode $kNode $lNode, |integer|,  four nodes defining element boundaries, input in counter-clockwise order around the element.
         $thick, |float|, element thickness
         $matTag, |integer|, tag of nDMaterial

.. note::

   This element is ``PlainStrain`` only.
   
The valid queries to a Quad element when creating an ElementRecorder object are 'forces', 'stresses,' and 'material $matNum matArg1 matArg2 ...' Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.


Code Developed by: **Edward Love, Sandia National Laboratories**

