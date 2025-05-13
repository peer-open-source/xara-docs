.. _uniaxialMaterial:

Uniaxial
********

Uniaxial materials define a mathematical relationship between two scalar quantities. 
These quantities are typically stress and strain, but can also be force and deformation, or any other two scalar quantities.

.. tabs::
 
   .. tab:: Python

      .. py:method:: Model.uniaxialMaterial(type, tag, *args)

         :param type: material type
         :type type: string
         :param tag: unique material tag.
         :type tag: integer
         :param args: additional arguments dependent on material ``type``

   .. tab:: Tcl

      .. function:: uniaxialMaterial $type $tag $args

      .. csv-table:: 
          :header: "Argument", "Type", "Description"
          :widths: 10, 10, 40

          $type, |string|,      material type
          $tag,  |integer|,     unique material tag.
          $args, |list|,        a list of material arguments with number dependent on material type


The following subsections contain information about ``type`` 



#. Steel & Metallic Materials

   .. toctree::
      :maxdepth: 1

      Steel/index
      Steel01/index
      Steel02/index


..
      uniaxialMaterials/Steel4
      uniaxialMaterials/DoddRestrepo
      uniaxialMaterials/RambergOsgoodSteel
      uniaxialMaterials/ReinforcingSteel
      uniaxialMaterials/SteelMPF
      uniaxialMaterials/SteelFractureDI
      uniaxialMaterials/DuctileFracture
      uniaxialMaterials/UVCuniaxial

#. Concrete

   .. toctree::
      :maxdepth: 1

      Concrete01/index
      Concrete02/index
      Concrete04
      ASDConcrete1D

#. Wrappers 

   .. toctree::
      :maxdepth: 1

      InitialStrain
      InitialStress