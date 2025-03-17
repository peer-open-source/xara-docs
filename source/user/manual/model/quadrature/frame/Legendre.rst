.. _Legendre-BeamIntegration:

Legendre  
^^^^^^^^

Gauss-Legendre quadrature is more accurate than :ref:`Gauss-Lobatto <Lobatto-BeamIntegration>`; however, it is not common in force-based elements because there are no integration points at the element ends. 
The formulation places ``N`` integration points along the element. 
The order of accuracy for Gauss-Legendre integration is :math:`2N-1`.

.. tabs::

   .. tab:: Python

      .. py:method:: Model.beamIntegration("Legendre", tag, section, N)
         :no-index:

         :param |string| name: The integration type.
         :param |integer| tag: Unique object tag.
         :param |integer| section: A previous-defined section.
         :param |integer| N: Number of Integration Points along the element.

   .. tab:: Tcl

      .. function:: beamIntegration "Legendre" tag secTag N

      .. csv-table::
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         "$tag",       "|integer|",    "Unique object tag"
         "$sectTag",   "|integer|",    "A previous-defined section"
         "$N",         "|integer|",    "Number of Integration Points along the elementa"
         

Example
-------

The following examples demonstrate the command in Tcl and Python script to add a Legendre beam integration with tag 2 and 6 integration points that uses the previously defined section whose tag is 1.

1. **Tcl Code**

   .. code-block:: tcl

      beamIntegration "Legendre" 2 1 6


2. **Python Code**

   .. code-block:: python

      model.beamIntegration("Legendre",2,1,6)

