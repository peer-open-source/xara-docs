SSPquadUP
=========



This command is used to construct a SSPquadUP element object.



.. code:: tcl

   element SSPquadUP $eleTag $iNode $jNode $kNode $lNode
           $matTag $thick $fBulk $fDen $k1 $k2 $void $alpha &lt;$b1
           $b2&gt;




The SSPquadUP element is an extension of the SSPquad Element for use in
dynamic plane strain analysis of fluid saturated porous media. A mixed
displacement-pressure (u-p) formulation is used, based upon the work of
Biot as extended by Zienkiewicz and Shiomi (1984).





The physical stabilization necessary to allow for reduced integration
incorporates an assumed strain field in which the volumetric dilation
and the shear strain associated with the the hourglass modes are zero,
resulting in an element which is free from volumetric and shear locking.
The elimination of shear locking results in greater coarse mesh accuracy
in bending dominated problems, and the elimination of volumetric locking
improves accuracy in nearly-incompressible problems. Analysis times are
generally faster than corresponding full integration elements.





Equal-order interpolation is used for the displacement and pressure
fields, thus, the SSPquadUP element does not inherently pass the inf-sup
condition, and is not fully acceptable in the incompressible-impermeable
limit (the QuadUP Element has the same issue). A stabilizing parameter
is employed to permit the use of equal-order interpolation for the
SSPquadUP element. This parameter alpha can be computed as





alpha = 0.25\ *(h^2)/(den*\ c^2)





where h is the element size, c is the speed of elastic wave propagation
in the solid phase, and den is the mass density of the solid phase. The
alpha parameter should be a small number. With a properly defined alpha
parameter, the SSPquadUP element can produce comparable results to a
higher-order element such as the 9_4_QuadUP Element at a significantly
lower computational cost and with a greater ease in mesh generation.





The full formulation for the SSPquadUP element can be found in McGann et
al. (2012) along with several example applications.





NOTES:



.. raw:: html

   <ol>

.. raw:: html

   <li>

The SSPquadUP element will only work in dynamic analysis.

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

When modeling soil, the body forces input into the SSPquadUP element
should be the components of the gravitational vector, not the unit
weight.

.. raw:: html

   </li>

.. raw:: html

   <li>

Fixing the pore pressure degree-of-freedom (dof 3) at a node is a
drainage boundary condition at which zero pore pressure will be
maintained throughout the analysis. Leaving the third dof free allows
pore pressures to build at that node.

.. raw:: html

   </li>

.. raw:: html

   <li>

Valid queries to the SSPquadUP element when creating an
ElementalRecorder object correspond to those for the nDMaterial object
assigned to the element (e.g., ‘stress’, ‘strain’). Material response is
recorded at the single integration point located in the center of the
element.

.. raw:: html

   </li>

.. raw:: html

   <li>

The SSPquadUP element was designed with intentions of duplicating the
functionality of the QuadUP Element. If an example is found where the
SSPquadUP element cannot do something that works for the QuadUP Element,
e.g., material updating, please contact the developers listed below so
the bug can be fixed.

.. raw:: html

   </li>

.. raw:: html

   </ol>



EXAMPLES:





SSPquadUP element definition with element tag 1, nodes 1, 2, 3, and 4,
material tag 1, unit thickness, bulk modulus of water (kPa), mass
density of water (Mg/m^3), horizontal and vertical permeabilities of
1e-3, voids ratio of 0.7, alpha parameter of 6e-5, horizontal body force
of zero, and vertical body force of -9.81





element SSPquadUP 1 1 2 3 4 1 1.0 2.2e6 1.0 1.0e-3 1.0e-3 0.7 6.0e-5 0.0
-9.81





Elemental recorders for stress and strain when using the SSPquadUP
element (note the difference from the QuadUP Element)





recorder Element -eleRange 1 $numElem -time -file stress.out stress
recorder Element -eleRange 1 $numElem -time -file strain.out strain





Pore pressure recorder for the SSPquadUP element (pore pressure is the
third degree-of-freedom)





recorder Node -nodeRange 1 $numNode -time -file porePressure.out -dof 3
vel



References
----------



McGann, C. R., Arduino, P., and Mackenzie-Helnwein, P. (2012).
“Stabilized single-point 4-node quadrilateral element for dynamic
analysis of fluid saturated porous media.” Acta Geotechnica, 7(4),
297-311.





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
