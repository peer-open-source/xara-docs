BbarQuad u-p
============



bbarQuadUP is a four-node plane-strain mixed volume/pressure element,
which uses a tri-linear isoparametric formulation. This element is
implemented for simulating dynamic response of solid-fluid fully coupled
material, based on Biot’s theory of porous medium. Each element node has
3 degrees-of-freedom (DOF): DOF 1 and 2 for solid displacement (u) and
DOF 3 for fluid pressure (p).





Please click here for examples.





OUTPUT INTERFACE: Pore pressure can be recorded at an element node using
OpenSees Node Recorder:





recorder Node <-file :math:`fileName&gt; &lt;-time&gt; &lt;-node
(`\ nod1 $nod2 …)> -dof 3 vel





See OpenSees command manual (McKenna and Fenves 2001) for nodal
displacement, velocity, or acceleration recorders.





The valid queries to a bbarQuadUP element when creating an
ElementRecorder are ‘force’, ‘stiffness’, or ‘material matNum matArg1
matArg2 …’, where matNum represents the material object at the
corresponding integration point.



.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr class="odd">

.. raw:: html

   <td>



element bbarQuadUP $eleTag $iNode $jNode $kNode :math:`lNode`\ thick
$matTag $bulk $fmass $hPerm :math:`vPerm &lt;`\ b1=0 :math:`b2=0`\ t=0>



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



$iNode, $jNode, $kNode, :math:`lNode</strong></p></td>
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
<td><p>Combined undrained bulk modulus B&lt;sub&gt;c&lt;/sub&gt;
relating changes in pore pressure and volumetric strain, may be
approximated by:</p>
<p>B&lt;sub&gt;c&lt;/sub&gt; &amp;asymp; B&lt;sub&gt;f&lt;/sub&gt;/n</p>
<p>where B&lt;sub&gt;f&lt;/sub&gt; is the bulk modulus of fluid phase
(2.2x10&lt;sup&gt;6&lt;/sup&gt; kPa (or 3.191x10&lt;sup&gt;5&lt;/sup&gt;
psi) for water), and n the initial porosity.</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">fmass</code></td>
<td><p>Fluid mass density</p></td>
</tr>
<tr class="odd">
<td><p><strong>`\ hPerm, :math:`vPerm</strong></p></td>
<td><p>Permeability coefficient in horizontal and vertical directions
respectively.</p></td>
</tr>
<tr class="even">
<td><p><strong>`\ b1, $b2



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



>1.0x10<sup>-1</sup> cm/s (or 3.94x10<sup>-2</sup> in/s)



.. raw:: html

   </td>

.. raw:: html

   <td>



1.0x10<sup>-3</sup> cm/s (or 3.94 x10<sup>-4</sup> in/s) ~
1.0x10<sup>-1</sup> cm/s (or 3.94 x10<sup>-2</sup> in/s)



.. raw:: html

   </td>

.. raw:: html

   <td>



1.0x10<sup>-5</sup> cm/s (or 3.94 x10<sup>-6</sup> in/s) ~
1.0x10<sup>-3</sup> cm/s (or 3.94 x10<sup>-4</sup> in/s)



.. raw:: html

   </td>

.. raw:: html

   <td>



1.0x10<sup>-7</sup> cm/s (or 3.94 x10<sup>-8</sup> in/s) ~
1.0x10<sup>-5</sup> cm/s (or 3.94 x10<sup>-6</sup> in/s)



.. raw:: html

   </td>

.. raw:: html

   <td>



<1.0x10<sup>-7</sup> cm/s (or 3.94x10 <sup>-8</sup> in/s)



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


