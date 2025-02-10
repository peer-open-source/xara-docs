
.. _bbarQuad:

MixedQuad
^^^^^^^^^

This command is used to construct a four-node quadrilateral element object, which uses a bilinear isoparametric formulation along with a mixed volume/pressure B-bar assumption. This element is for plane strain problems only.

.. tabs::

   .. tab:: Python

      .. function:: model.element("bbarQuad", tag, nodes, section, *args, **kwargs)

         :param tag: integer tag identifying the element
         :param nodes: tuple of integer tags identifying the nodes that form the element
         :param section: tuple or int. If int, it is the tag of a previously defined :ref:`PlaneSection`. If tuple, it is a tuple of the form (``thick``, ``type``, ``material``) where 
           
             ===================================   ==============================================================================================================
             ``thick`` |float|                     element thickness
             ``type`` |str|                        string representing material behavior. The type parameter can be either ``'PlaneStrain'`` or ``'PlaneStress'``
             ``material`` |integer|                tag of an :ref:`nDMaterial`
             ===================================   ==============================================================================================================
   

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


The valid :ref:`eleResponse` queries to this element are 

* ``'forces'``, 
* ``'stresses'`` and 
* ``'material $matNum matArg1 matArg2 ...'`` Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.


Code Developed by: **Edward Love, Sandia National Laboratories**

