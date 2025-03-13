.. _section:

Section
^^^^^^^

This command configures a Section, which represents a constitutive model between stress and strain *resultants*.

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


Library
-------

The following section types are valid for :ref:`frame` elements:

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


The following section types are valid for :ref:`shells`:

.. toctree::
   :maxdepth: 1

   section/ShellFiber
   section/ElasticShell


..
   .. toctree::
      :maxdepth: 1
   
      section/PlateFiberSection
      section/Isolator2springSection
      section/ReinforcedConcreteLayeredMembraneSection
      section/LayeredMembraneSection
      section/ASDCoupledHinge3D
      section/ParallelSection
      section/SectionAggregator
      section/UniaxialSection
