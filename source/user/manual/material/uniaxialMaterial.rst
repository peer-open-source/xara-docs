.. _uniaxialMaterial:

Uniaxial Materials
******************

Uniaxial materials define a mathematical relationship between two scalar quantities. 
These quantities are typically stress and strain, but can also be force and deformation, or any other two scalar quantities.

.. tabs::
 
   .. tab:: Python

      .. function:: model.uniaxialMaterial(type, tag, *args)

         :param type: string, material type
         :param tag: integer, unique material tag.
         :param args: list, a list of material arguments with number dependent on material type

   .. tab:: Tcl

      .. function:: uniaxialMaterial $type $tag $args

      .. csv-table:: 
      :header: "Argument", "Type", "Description"
      :widths: 10, 10, 40

      $type, |string|,      material type
      $tag,  |integer|,     unique material tag.
      $args, |list|,        a list of material arguments with number dependent on material type


The following subsections contain information about **$type** 

..
      #. Some Standard Uniaxial Materials

      .. toctree::
            :maxdepth: 1
                  
            uniaxialMaterials/Elastic
            uniaxialMaterials/ElasticPP
            uniaxialMaterials/ElasticPP_Gap
            uniaxialMaterials/ElasticNoTension
            uniaxialMaterials/ElasticBilin
            uniaxialMaterials/ElasticMultiLinear
            uniaxialMaterials/Hardening
            uniaxialMaterials/MultiLinear


#. Steel & Reinforcing-Steel Materials

   .. toctree::
      :maxdepth: 1

      uniaxialMaterials/Steel01
      uniaxialMaterials/Steel02
      uniaxialMaterials/Steel4
      uniaxialMaterials/DoddRestrepo
      uniaxialMaterials/RambergOsgoodSteel

..
      uniaxialMaterials/ReinforcingSteel
      uniaxialMaterials/SteelMPF
      uniaxialMaterials/SteelFractureDI
      uniaxialMaterials/DuctileFracture
      uniaxialMaterials/UVCuniaxial

#. Concrete Materials

   .. toctree::
      :maxdepth: 1

      uniaxialMaterials/Concrete01
      uniaxialMaterials/Concrete02
      uniaxialMaterials/Concrete04
      uniaxialMaterials/ASDConcrete1D
      uniaxialMaterials/GMG_CyclicReinforcedConcrete
      uniaxialMaterials/Creep
	  
..    uniaxialMaterials/Concrete06
      uniaxialMaterials/Concrete07
      uniaxialMaterials/ConfinedConcrete01
      uniaxialMaterials/ConcreteD
      uniaxialMaterials/FRPConfinedConcrete
      uniaxialMaterials/ConcreteCM

      
#. Generic Multilinear Hysteretic Materials

   .. toctree::
      :maxdepth: 1
      
      uniaxialMaterials/Hysteretic
      uniaxialMaterials/HystereticSM
      uniaxialMaterials/IMKBilin
      uniaxialMaterials/IMKPeakOriented
      uniaxialMaterials/IMKPinching
      uniaxialMaterials/SLModel
	  
..    uniaxialMaterials/Pinching4

      
#. Wrapper Uniaxial Materials

.. toctree::
      :maxdepth: 1
      
      uniaxialMaterials/Parallel
      uniaxialMaterials/Series
      uniaxialMaterials/Fatigue

..
      uniaxialMaterials/InitialStrain
      uniaxialMaterials/InitialStress
      uniaxialMaterials/MinMax
      uniaxialMaterials/PathIndependent


#. Other Uniaxial Materials

   .. toctree::
      :maxdepth: 1

      uniaxialMaterials/BoucWenInfill
      uniaxialMaterials/CoulombDamper
      uniaxialMaterials/HertzDamp
      uniaxialMaterials/JankowskiImpact

..
      uniaxialMaterials/HystereticPoly
      uniaxialMaterials/HystereticAsym
      uniaxialMaterials/DowelType
      uniaxialMaterials/ViscoelasticGap
      uniaxialMaterials/Ratchet
      uniaxialMaterials/FlagShape
      uniaxialMaterials/HystereticSmooth
      uniaxialMaterials/CastFuse
      uniaxialMaterials/ViscousDamper
      uniaxialMaterials/BilinearOilDamper
      uniaxialMaterials/SAWS
      uniaxialMaterials/BARSLIP
      uniaxialMaterials/Bond_SP01 - - Strain Penetration Model for Fully Anchored Steel Reinforcing Bars
      uniaxialMaterials/Impact
      uniaxialMaterials/Hyperbolic Gap
      uniaxialMaterials/LimitState
      uniaxialMaterials/Engineered Cementitious Composites
      uniaxialMaterials/SelfCentering
      uniaxialMaterials/Viscous
      uniaxialMaterials/BoucWen
      uniaxialMaterials/BWBN (Pinching Hysteretic Bouc-Wen)



#. PyTzQz uniaxial materials for p-y, t-z and q-z elements 

.. toctree::
   :maxdepth: 1

   uniaxialMaterials/PySimple1
   uniaxialMaterials/TzSimple1
   uniaxialMaterials/QzSimple1
   uniaxialMaterials/PyLiq1
   uniaxialMaterials/TzLiq1
   uniaxialMaterials/QzLiq1
   uniaxialMaterials/TzSandCPT
   uniaxialMaterials/QbSandCPT

.. uniaxialMaterials/KikuchiAikenHDR
   uniaxialMaterials/KikuchiAikenLRB
   uniaxialMaterials/AxialSp
   uniaxialMaterials/AxialSpHD
   uniaxialMaterials/PinchingLimitState
   uniaxialMaterials/CFSWSWP
   uniaxialMaterials/CFSSSWP
   uniaxialMaterials/PySimple1Gen
   uniaxialMaterials/TzSimple1Gen

