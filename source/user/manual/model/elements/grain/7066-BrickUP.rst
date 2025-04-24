Brick u-p
=========



BrickUP is an 8-node hexahedral linear isoparametric element. Each node
has 4 degrees-of-freedom (DOF): DOFs 1 to 3 for solid displacement (u)
and DOF 4 for fluid pressure (p). This element is implemented for
simulating dynamic response of solid-fluid fully coupled material, based
on Biot’s theory of porous medium.

Please click here for examples.





OUTPUT INTERFACE:





Pore pressure can be recorded at an element node using OpenSees Node
Recorder:





recorder Node <-file :math:`fileName&gt; &lt;-time&gt; &lt;-node
(`\ nod1 $nod2 …)> -dof 3 vel





See OpenSees command manual (McKenna and Fenves 2001) for nodal
displacement, velocity, or acceleration recorders.





The valid queries to a BrickUP element when creating an ElementRecorder
are ‘force’, ‘stiffness’, or ‘material matNum matArg1 matArg2 …’, where
matNum represents the material object at the corresponding integration
point.



.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>



element brickUP $eleTag $Node1 $Node2 $Node3 :math:`Node4`\ Node5 $Node6
$Node7 $Node8 $matTag $bulk $fmass $PermX $PermY :math:`PermZ
&lt;`\ bX=0 $bY=0 :math:`bZ=0&gt;</strong></p></td>
</tr>
</tbody>
</table>
<p><a href="image:Brick.png" title="wikilink">image:Brick.png</a></p>
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">eleTag</code></td>
<td><p>A positive integer uniquely identifying the element among all
elements</p></td>
</tr>
<tr class="even">
<td><p><strong>`\ Node1,… :math:`Node8</strong></p></td>
<td><p>Eight element node (previously defined) numbers (see figure above
for order of numbering).</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">matTag</code></td>
<td><p>Tag of an NDMaterial object (previously defined) of which the
element is composed</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">bulk</code></td>
<td><p>Combined undrained bulk modulus B&lt;sub&gt;c&lt;/sub&gt;
relating changes in pore pressure and volumetric strain, may be
approximated by:</p>
<p>B&lt;sub&gt;c&lt;/sub&gt; &amp;asymp; B&lt;sub&gt;f&lt;/sub&gt;/n</p>
<p>where B&lt;sub&gt;f&lt;/sub&gt; is the bulk modulus of fluid phase
(2.2x10&lt;sup&gt;6&lt;/sup&gt; kPa (or 3.191x10&lt;sup&gt;5&lt;/sup&gt;
psi) for water), and n the initial porosity.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">fmass</code></td>
<td><p>Fluid mass density</p></td>
</tr>
<tr class="even">
<td><p><strong>`\ permX, $permY, :math:`permZ</strong></p></td>
<td><p>Permeability coefficients in x, y, and z directions
respectively.</p></td>
</tr>
<tr class="odd">
<td><p><strong>`\ bX, $bY, $bZ



.. raw:: html

   </td>

.. raw:: html

   <td>



Optional gravity acceleration components in x, y, and z directions
directions respectively (defaults are 0.0)



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



NOTE:





This element requires 4 degrees-of-freedom (ndf=4), the 4th
degree-of-freedom being pore pressure. The Pore pressure can be recorded
at an element node using OpenSees Node Recorder:





recorder Node <-file
:math:`fileName&gt; &lt;-time&gt; &lt;-node (`\ nod1 $nod2 …)> -dof 4
vel





The valid queries to a BrickUP element when creating an ElementRecorder
are ‘force’, and ‘material matNum matArg1 matArg2 …’, where matNum
represents the material object at the corresponding integration point.





TYPICAL RANGE OF PERMEABILITY COEFFICIENT (cm/s)



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



Code Developed by: UC San Diego (Dr. Zhaohui Yang):



.. raw:: html

   <hr />



UC San Diego Soil Model:


