.. _uniaxialMaterial:

Uniaxial Materials
******************

Uniaxial materials define a mathematical relationship between two scalar quantities. 
These quantities are typically stress and strain, but can also be force and deformation, or any other two scalar quantities.

.. tabs::
 
   .. tab:: Python

      .. function:: model.uniaxialMaterial(type, tag, *args)

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



#. Steel & Reinforcing-Steel Materials

   .. toctree::
      :maxdepth: 1

      uniaxialMaterials/Steel01
      uniaxialMaterials/Steel02


..
      uniaxialMaterials/Steel4
      uniaxialMaterials/DoddRestrepo
      uniaxialMaterials/RambergOsgoodSteel
      uniaxialMaterials/ReinforcingSteel
      uniaxialMaterials/SteelMPF
      uniaxialMaterials/SteelFractureDI
      uniaxialMaterials/DuctileFracture
      uniaxialMaterials/UVCuniaxial

