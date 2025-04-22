.. _NewtonCotes-BeamIntegration:
   

NewtonCotes
^^^^^^^^^^^

Newton-Cotes places integration points uniformly along the element, including a point at each end of the element.  
The weights for the uniformly  spaced integration points are tabulated in references on numerical analysis. 
The force deformation response at each integration point is defined by the section.
The order of accuracy for Gauss-Radau integration is :math:`N-1`.

.. function:: beamIntegration "NewtonCotes" tag section N

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   "tag",       "|integer|",    "Unique object tag"
   "section",   "|integer|",    "Previously defined section tag"
   "N",         "|integer|",    "Number of integration points along the elementa"
   

Examples
--------

The following examples demonstrate the command in Tcl and Python script to add a NewtonCotes beam integration with tag 2 and 6 integration points that uses the previously defined section whose tag is 1.

.. tabs::
   
   .. tab:: Tcl

      .. code-block:: tcl

         beamIntegration "NewtonCotes" 2 1 6


   .. tab:: Python

      .. code-block:: python

         model.beamIntegration("NewtonCotes", 2, 1, 6)


