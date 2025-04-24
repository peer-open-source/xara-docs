Four Node Quad u-p
==================



FourNodeQuadUP is a four-node plane-strain element using bilinear
isoparametric formulation. This element is implemented for simulating
dynamic response of solid-fluid fully coupled material, based on Biot’s
theory of porous medium. Each element node has 3 degrees-of-freedom
(DOF): DOF 1 and 2 for solid displacement (u) and DOF 3 for fluid
pressure (p).





Please click here for examples.





OUTPUT INTERFACE: Pore pressure can be recorded at an element node using
OpenSees Node Recorder:





recorder Node <-file :math:`fileName&gt; &lt;-time&gt; &lt;-node
(`\ nod1 $nod2 …)> -dof 3 vel





See OpenSees command manual (McKenna and Fenves 2001) for nodal
displacement, velocity, or acceleration recorders.



The valid queries to a quadUP element when creating an ElementRecorder
are ``force``, ``stiffness``, or
``material matNum matArg1 matArg2 ...``, where matNum represents the
material object at the corresponding integration point.

.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>



element quadUP $eleTag $iNode $jNode $kNode $lNode :math:`thick`\ matTag
$bulk $fmass $hPerm :math:`vPerm &lt;`\ b1=0 :math:`b2=0`\ t=0>



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

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



A positive integer uniquely identifying the element among all elements



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="even">

.. raw:: html

   <td>



$iNode, $jNode, $kNode, $lNode



.. raw:: html

   </td>

.. raw:: html

   <td>



Four element node (previously defined) numbers in counter-clockwise
order around the element



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>

thick

.. raw:: html

   </td>

.. raw:: html

   <td>



Element thickness



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="even">

.. raw:: html

   <td>

matTag

.. raw:: html

   </td>

.. raw:: html

   <td>



Tag of an NDMaterial object (previously defined) of which the element is
composed



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>

bulk

.. raw:: html

   </td>

.. raw:: html

   <td>



Combined undrained bulk modulus Bc relating changes in pore pressure and
volumetric strain, may be approximated by:





Bc &asymp; Bf/n





where Bf is the bulk modulus of fluid phase (2.2x106 kPa (or 3.191x105
psi) for water), and ``n`` the initial porosity.



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="even">

.. raw:: html

   <td>

fmass

.. raw:: html

   </td>

.. raw:: html

   <td>



Fluid mass density



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>



\ ``hPerm``, ``vPerm``\ 



.. raw:: html

   </td>

.. raw:: html

   <td>



Permeability coefficient in horizontal and vertical directions
respectively.



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="even">

.. raw:: html

   <td>



\ ``b1``, ``b2``\ 



.. raw:: html

   </td>

.. raw:: html

   <td>



Optional gravity acceleration components in horizontal and vertical
directions respectively (defaults are 0.0)



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>

t

.. raw:: html

   </td>

.. raw:: html

   <td>



Optional uniform element normal traction, positive in tension (default
is 0.0)



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>


TYPICAL RANGE OF PERMEABILITY COEFFICIENT

.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>



Gravel



.. raw:: html

   </td>

.. raw:: html

   <td>



Sand



.. raw:: html

   </td>

.. raw:: html

   <td>



Silty Sand



.. raw:: html

   </td>

.. raw:: html

   <td>



Silt



.. raw:: html

   </td>

.. raw:: html

   <td>



Clay



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="even">

.. raw:: html

   <td>



>1.0x10-1 cm/s (or 3.94x10-2 in/s)



.. raw:: html

   </td>

.. raw:: html

   <td>



1.0x10-3 cm/s (or 3.94 x10-4 in/s) ~ 1.0x10-1 cm/s (or 3.94 x10-2 in/s)



.. raw:: html

   </td>

.. raw:: html

   <td>



1.0x10-5 cm/s (or 3.94 x10-6 in/s) ~ 1.0x10-3 cm/s (or 3.94 x10-4 in/s)



.. raw:: html

   </td>

.. raw:: html

   <td>



1.0x10-7 cm/s (or 3.94 x10-8 in/s) ~ 1.0x10-5 cm/s (or 3.94 x10-6 in/s)



.. raw:: html

   </td>

.. raw:: html

   <td>



<1.0x10-7 cm/s (or 3.94x10 -8 in/s)



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>



Code developed by: UC San Diego (Dr. Zhaohui Yang):



.. raw:: html

   <hr />



UC San Diego Soil Model:


