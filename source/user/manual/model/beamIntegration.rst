.. _beamIntegration:

Beam integration
****************

This command is used to construct a beam integration for :ref:`Frame <Frame>` elements. 

.. tabs::

   .. tab:: Python
      .. py:method:: Model.beamIntegration(name, tag, *args)
         :no-index:

         Construct a beam integration for :ref:`Frame <Frame>` elements.

   .. tab:: Tcl
      .. function:: beamIntegration $name $tag $args ...

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $name, |string|, integration type
         $tag,  |integer|, unique beam integration tag.
         $args, |list|,  a list of arguments with number dependent on integration type


The following types are available:

.. toctree::
   :caption: Distributed Inelasticity.
   :maxdepth: 1

   beamIntegrations/Lobatto
   beamIntegrations/Legendre
   beamIntegrations/NewtonCotes
   beamIntegrations/Radau
   beamIntegrations/Trapezoidal
   beamIntegrations/CompositeSimpson
   beamIntegrations/userDefined
   beamIntegrations/FixedLocation
   beamIntegrations/LowOrder
   beamIntegrations/MidDistance
   
2. Concentrated Inelasticity.
   Plastic hinge integration methods confine material inelasticity to regions of the element of specified length while the remainder of the element is linear elastic. 
   A summary of plastic hinge integration methods is provided in (Scott and Fenves 2006).

.. toctree::
   :caption: Concentrated Inelasticity.
   :maxdepth: 1

   beamIntegrations/ConcentratedPlasticity	      
   beamIntegrations/ConcentratedCurvature
   beamIntegrations/UserHinge
   beamIntegrations/HingeMidpoint
   beamIntegrations/HingeRadau
   beamIntegrations/HingeRadauTwo
   beamIntegrations/HingeEndpoint   
   
