SSPbrickUP
==========


.. code:: tcl

   element SSPbrickUP $eleTag $iNode $jNode $kNode $lNode
           $mNode $nNode $pNode $qNode $matTag $fBulk $fDen $k1 $k2 $k3 $void
           $alpha < $b1 $b2 $b3 >

.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>

eleTag

.. raw:: html

   </td>

.. raw:: html

   <td>



unique integer tag identifying element object



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="even">

.. raw:: html

   <td>



$iNode $jNode $kNode $lNode $mNode $nNode :math:`pNode`\ qNode



.. raw:: html

   </td>

.. raw:: html

   <td>



the eight nodes defining the element, input in counterclockwise order
(same node numbering scheme as for the brickUP Element) (-ndm 3 -ndf 4)



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>

matTag

.. raw:: html

   </td>

.. raw:: html

   <td>



unique integer tag associated with previously-defined nDMaterial object



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="even">

.. raw:: html

   <td>

fBulk

.. raw:: html

   </td>

.. raw:: html

   <td>



bulk modulus of the pore fluid



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>

fDen

.. raw:: html

   </td>

.. raw:: html

   <td>



mass density of the pore fluid



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="even">

.. raw:: html

   <td>



k1 k2 k3



.. raw:: html

   </td>

.. raw:: html

   <td>



permeability coefficients in global x-, y-, and z-directions,
respectively



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>

void

.. raw:: html

   </td>

.. raw:: html

   <td>



voids ratio



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="even">

.. raw:: html

   <td>

alpha

.. raw:: html

   </td>

.. raw:: html

   <td>



spatial pressure field stabilization parameter (see discussion below for
more information)



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>



b1 b2 b3



.. raw:: html

   </td>

.. raw:: html

   <td>



constant body forces in global x-, y-, and z-directions, respectively
(optional, default = 0.0) - See Note 3



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

.. raw:: html

   <hr />



The SSPbrickUP element is an extension of the SSPbrick Element for use
in dynamic 3D analysis of fluid saturated porous media. 
A mixed displacement-pressure (u-p) formulation is used, based upon the work of
Biot as extended by Zienkiewicz and Shiomi (1984).


The physical stabilization necessary to allow for reduced integration
incorporates an enhanced assumed strain field, resulting in an element
which is free from volumetric and shear locking. The elimination of
shear locking results in greater coarse mesh accuracy in bending
dominated problems, and the elimination of volumetric locking improves
accuracy in nearly-incompressible problems. Analysis times are generally
faster than corresponding full integration elements.





Equal-order interpolation is used for the displacement and pressure
fields, thus, the SSPbrickUP element does not inherently pass the
inf-sup condition, and is not fully acceptable in the
incompressible-impermeable limit (the brickUP Element has the same
issue). A stabilizing parameter is employed to permit the use of
equal-order interpolation for the SSPbrickUP element. This parameter
alpha can be computed as

alpha = h^2/(4\ *(Ks + (4/3)*\ Gs))


where h is the element size, and Ks and Gs are the bulk and shear moduli
for the solid phase. The alpha parameter should be a small number. With
a properly defined alpha parameter, the SSPbrickUP element can produce
comparable results to a higher-order element such as the 20_8_BrickUP
Element at a significantly lower computational cost and with a greater
ease in mesh generation.





NOTES:



.. raw:: html

   <ol>

.. raw:: html

   <li>

The SSPbrickUP element will only work in dynamic analysis.

.. raw:: html

   </li>

.. raw:: html

   <li>

For saturated soils, the mass density input into the associated
nDMaterial object should be the saturated mass density.

.. raw:: html

   </li>

.. raw:: html

   <li>

When modeling soil, the body forces input into the SSPbrickUP element
should be the components of the gravitational vector, not the unit
weight.

.. raw:: html

   </li>

.. raw:: html

   <li>

Fixing the pore pressure degree-of-freedom (dof 4) at a node is a
drainage boundary condition at which zero pore pressure will be
maintained throughout the analysis. Leaving the fourth dof free allows
pore pressures to build at that node.

.. raw:: html

   </li>

.. raw:: html

   <li>

Valid queries to the SSPbrickUP element when creating an
ElementalRecorder object correspond to those for the nDMaterial object
assigned to the element (e.g., ‘stress’, ‘strain’). Material response is
recorded at the single integration point located in the center of the
element.

.. raw:: html

   </li>

.. raw:: html

   <li>

The SSPbrickUP element was designed with intentions of duplicating the
functionality of the brickUP Element. If an example is found where the
SSPbrickUP element cannot do something that works for the brickUP
Element, e.g., material updating, please contact the developers listed
below so the bug can be fixed.

.. raw:: html

   </li>

.. raw:: html

   </ol>



EXAMPLES:





SSPbrickUP element definition with element tag 1, nodes 1, 2, 3, 4, 5,
6, 7, and 8, material tag 1, bulk modulus of water (kPa), mass density
of water (Mg/m^3), isotropic permeability of 1e-3, voids ratio of 0.7,
alpha parameter of 6e-5, x- and y-directed body forces of zero, and
z-directed body force of -9.81





element SSPbrickUP 1 1 2 3 4 5 6 7 8 1 2.2e6 1.0 1.0e-3 1.0e-3 1.0e-3
0.7 6.0e-5 0.0 0.0 -9.81





Elemental recorders for stress and strain when using the SSPbrickUP
element (note the difference from the brickUP Element)





recorder Element -eleRange 1 $numElem -time -file stress.out stress
recorder Element -eleRange 1 $numElem -time -file strain.out strain





Pore pressure recorder for the SSPbrickUP element (pore pressure is the
fourth degree-of-freedom)





recorder Node -nodeRange 1 $numNode -time -file porePressure.out -dof 4
vel



References
----------



Zienkiewicz, O.C. and Shiomi, T. (1984). “Dynamic behavior of saturated
porous media; the generalized Biot formulation and its numerical
solution.” International Journal for Numerical Methods in Geomechanics,
8, 71-96.



.. raw:: html

   <hr />



Code Developed by: Chris McGann, Pedro Arduino, & Peter
Mackenzie-Helnwein, at the University of Washington



.. raw:: html

   <hr />
