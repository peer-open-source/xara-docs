.. _Lobatto-BeamIntegration:
   

Lobatto
^^^^^^^

Gauss-Lobatto integration is the most common approach for evaluating the response of inelastic :ref:`Frame <Frame>` elements because it places an integration point at each end of the element, where bending moments are largest in the absence of interior element loads.

.. tabs::

   .. tab:: Python

      .. py:method:: Model.beamIntegration("Lobatto",tag,section,N)
         :noindex:

         Create a Lobatto beam integration.

         :param |integer| tag: Unique object tag
         :param |integer| section: A previously-defined :ref:`section <Section>` tag
         :param |integer| N: Number of integration points along the element

   .. tab:: Tcl

      .. function:: beamIntegration "Lobatto" tag secTag N

      .. csv-table::
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         "$tag",       "|integer|",    "Unique object tag"
         "$sectTag",   "|integer|",    "A previous-defined section"
         "$N",         "|integer|",    "Number of integration points along the elements"


Example
-------

The following examples demonstrate the command in Tcl and Python script to add a Lobatto beam integration with tag 2 and 6 integration points that uses the previously defined section whose tag is 1.

.. tabs::
   
   .. tab:: Tcl

      .. code-block:: tcl

         beamIntegration "Lobatto" 2 1 6


   .. tab:: Python

      .. code-block:: python

         model.beamIntegration("Lobatto", 2, 1, 6)

