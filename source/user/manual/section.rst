.. _section:

Sections
********

This command is used to construct a Section, which represents force-deformation (or resultant stress-strain) relationships at beam-column and plate sample points.

.. tabs::

   .. tab:: Python (RT)

      .. function:: model.section(type, tag, *args)

         :param type: section type
         :type type: string
         :param tag: unique section tag
         :type tag: integer
         :param args: additional arguments dependent on section ``type``

   .. tab:: Tcl

      .. function:: section type? tag? arg1? ...

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $type,    |string|,      section type
         $tag,     |integer|,     unique section tag.
         $secArgs, |list|,        a list of material arguments with number dependent on section type

The type of section created and the additional arguments required depends on the ``type`` provided in the command.

The following contain information about ``type`` and the ``args`` required for each of the available section types:

.. toctree::
   :maxdepth: 1

   section/ElasticFrame
   section/ShearFiber

.. _PlaneSection:

For :ref:`PlaneElements` elements, the following section types are available:

.. toctree::
   :maxdepth: 1

   section/PlaneStrain
   section/PlaneStress


.. toctree::
   :maxdepth: 1

   section/PlateFiberSection
   section/ElasticShell
   section/Isolator2springSection
   section/ReinforcedConcreteLayeredMembraneSection
   section/LayeredMembraneSection
   section/ASDCoupledHinge3D

..
   section/ParallelSection
   section/SectionAggregator
   section/UniaxialSection
