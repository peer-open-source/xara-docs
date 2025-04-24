FourNodeQuad u-p Element
========================



This command is used to construct an eFourNodeQuadUP element object. A
FourNodeQuadUP element is a four-node plane-strain element using
bilinear isoparametric formulation. This element is implemented for
simulating dynamic response of solid-fluid fully coupled material, based
on Biot’s theory of porous medium. Each element node has 3
degrees-of-freedom (DOF): DOF 1 and 2 for solid displacement (u) and DOF
3 for fluid pressure (p). The arguments for the construction of this
element are:



.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>



element quadUP $eleTag $Node1 $Node2 $Node3 $Node4 :math:`thick`\ matTag
$bulk $fmass $PermX :math:`PermY &lt;`\ b1=0 :math:`b2=0`\ t=0>



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



unique element object tag



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="even">

.. raw:: html

   <td>



$Node1 .. :math:`Node4</strong></p></td>
<td><p>Four element node (previously defined) numbers in
counter-clockwise order around the element</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">thick</code></td>
<td><p>Element thickness</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>Tag of an NDMaterial object (previously defined) of which the
element is composed</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">bulk</code></td>
<td><p>Combined undrained bulk modulus Bc relating changes in pore
pressure and volumetric strain, may be approximated by: where Bf is the
bulk modulus of fluid phase (2.2x106 kPa for water), and n the initial
porosity.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fmass</code></td>
<td><p>Fluid mass density</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">PermX</code></td>
<td><p>Permeability coefficient in X direction</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">PermY</code></td>
<td><p>Permeability coefficient in Y direction</p></td>
</tr>
<tr class="odd">
<td><p><strong>`\ bX, $bY



.. raw:: html

   </td>

.. raw:: html

   <td>



Optional gravity acceleration components in X and Y directions
respectively (defaults are 0.0)



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr class="even">

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



NOTE:



.. raw:: html

   <ol>

.. raw:: html

   <li>

This element requires 3 degrees-of-freedom (ndf=3), the 3rd
degree-of-freedom being pore pressure. The Pore pressure can be recorded
at an element node using OpenSees Node Recorder:

.. raw:: html

   </li>

.. raw:: html

   </ol>



recorder Node <-file
:math:`fileName&gt; &lt;-time&gt; &lt;-node (`\ nod1 $nod2 …)> -dof 3
vel



.. raw:: html

   <ol>

.. raw:: html

   <li>

The valid queries to a quadUP element when creating an ElementRecorder
are ‘force’, and ‘material matNum matArg1 matArg2 …’, where matNum
represents the material object at the corresponding integration point.

.. raw:: html

   </li>

.. raw:: html

   <li>

TYPICAL RANGE OF PERMEABILITY COEFFICIENT (cm/s)

.. raw:: html

   </li>

.. raw:: html

   </ol>

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



>1.0x10-1



.. raw:: html

   </td>

.. raw:: html

   <td>



1.0x10-3 ~ 1.0x10-1



.. raw:: html

   </td>

.. raw:: html

   <td>



1.0x10-5 ~ 1.0x10-3



.. raw:: html

   </td>

.. raw:: html

   <td>



1.0x10-7 ~ 1.0x10-5



.. raw:: html

   </td>

.. raw:: html

   <td>



<1.0x10-7



.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

Examples
--------



Please visit http://cyclic.ucsd.edu/opensees for examples.



References
----------

.. raw:: html

   <hr />



Code Developed by: Zhaohui Yang, UC San Diego


