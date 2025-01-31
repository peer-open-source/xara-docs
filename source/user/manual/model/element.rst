.. _element:

Elements
********

This method is used to construct an element and add it to the :class:`Model`. 

.. tabs::

   .. tab:: Python

      .. function:: model.element(type, tag, nodes, *args, **kwds)

         :param type: string defining the type of element
         :param tag: integer tag identifying the element
         :param nodes: tuple of integer tags identifying the nodes that form the element
         :param args, kwds: arguments particular to the element ``type``


   .. tab:: Tcl

      .. function:: element $type $tag (num $nodes) $args ...

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         ``type``, |string|,      element type
         ``tag``,  |integer|,     unique element tag.
         ``nodes``,   |integerlist|, a list of element nodes with number dependent on ele type
         ``args``, |list|,        a list of element arguments with number dependent on ele type


The type of element created and the additional arguments required depends on the **$type** provided.

The following subsections contain information about ``type`` and the number of nodes and args required for each of the available element types:

2. Truss Elements

.. toctree::
   :maxdepth: 1

   elements/Truss
   elements/CorotationalTruss


3. Beam Column Elements

.. toctree::
   :maxdepth: 2

   elements/frame/index


.. toctree::
   :hidden:
   :maxdepth: 1   

   elements/elasticBeamColumn
   elements/ExactFrame
   elements/ModElasticBeam
   elements/gradientInelasticBeamColumn   
   elements/FlexureShearInteractionDisplacementBasedBeamColumnElement
   elements/dispBeamColumnAsym
   elements/mixedBeamColumnAsym
   elements/MVLEM
   elements/MVLEM_3D
   elements/SFI_MVLEM_3D
   elements/E_SFI
   elements/E_SFI_MVLEM_3D

..
   elements/ForceBasedBeamColumnElement
   elements/DisplacementBasedBeamColumnElement
   elements/ElasticBeamColumnElementWithStiffnessModifiers

4. Plane Elements

.. toctree::
   :maxdepth: 1

   elements/Quad
   elements/Tri31
   elements/SSPquad
   elements/BbarPlaneStrainQuadrilateral
   elements/EnhancedStrainQuadrilateral
   elements/MEFI

5. Shell Elements

.. toctree::
   :maxdepth: 1

   elements/ASDShellQ4
   elements/Shell
   elements/ShellDKGQ
   elements/ShellNLDKGQ
   elements/ShellNL
   elements/ShellDKGT
   elements/ShellNLDKGT
   elements/ASDShellT3

   

6. Solid Elements

.. toctree::
   :maxdepth: 1

   elements/stdBrick
   elements/bbarBrick
   elements/SSPbrick
   elements/FourNodeTetrahedron
   elements/TenNodeTetrahedron


1. Zero-Length Elements

.. toctree::
   :maxdepth: 4

   elements/zeroLength
   elements/zeroLengthSection
   elements/zeroLengthND
   elements/CoupledZeroLength
   elements/zeroLengthContact
   elements/zeroLengthContactNTS2D
   elements/zeroLengthInterface2D
   elements/zeroLengthImpact3D 
   elements/zeroLengthContactASDimplex


8. Joint Elements

.. toctree::
   :maxdepth: 1

   elements/BeamColumnJoint
   elements/ElasticTubularJoint
   elements/Joint2D
   elements/Inno3DPnPJoint
   elements/LehighJoint2D

..
   9. Link Elements
   
      .. toctree::
         :maxdepth: 1
      
         elements/TwoNodeLink

10. Bearing Elements

    .. toctree::
       :maxdepth: 1
    
       elements/TripleFrictionPendulumX
    
    
    ..
       elements/ElastomericBearingBouc-Wen
       elements/FlatSliderBearingElement
       elements/SingleFrictionPendulumBearing
       elements/TripleFrictionPendulumBearing
       elements/TripleFrictionPendulum
       elements/MultipleShearSpring
       elements/KikuchiBearing
       elements/YamamotoBiaxialHDR
       elements/LeadRubberX
       elements/HDR
       elements/RJ-Watson EQS Bearing
       elements/FPBearingPTV
       elements/ElastomericBearingPlasticity

..
   11. U-P Elements (saturated soil)
   
       .. toctree::
          :maxdepth: 1
       
          elements/FourNodeQuadUP
          elements/BrickUP
          elements/bbarQuadUP
          elements/bbarBrickUP
          elements/NineFourNodeQuadUP
          elements/TwentyEightNodeBrickUP
          elements/TwentyNodeBrickUP
          elements/BrickLargeDisplacementUP
          elements/SSPquadUP 
          elements/SSPbrickUP

..
   12. Contact
   
       .. toctree::
          :maxdepth: 1   
       
          elements/SimpleContact2D
          elements/SimpleContact3D
          elements/BeamContact2D
          elements/BeamContact3D
          elements/BeamEndContact3D
          elements/zeroLengthImpact3D
..   
   13. Cable
   
      .. toctree::
         :maxdepth: 1   
      
         elements/CatenaryCableElement


14. Absorbing Elements

.. toctree::
   :maxdepth: 1   

   elements/PML

15. Misc.

.. toctree::
   :maxdepth: 1   

   elements/ShallowFoundationGen
   elements/SurfaceLoad
   elements/VS3D4
   elements/AC3D8
   elements/ASI3D8
   elements/AV3D4
   elements/ASDEmbeddedNodeElement
   elements/ASDAbsorbingBoundary
   elements/RockingBC
   elements/FSIFluidBoundaryElement2D
   elements/FSIFluidElement2D
   elements/FSIInterfaceElement2D



