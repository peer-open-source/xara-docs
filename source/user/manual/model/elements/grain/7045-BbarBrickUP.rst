BbarBrick u-p
=============


bbarBrickUP is a 8-node mixed volume/pressure element, which uses a
tri-linear isoparametric formulation.





Each node has 4 degrees-of-freedom (DOF): DOFs 1 to 3 for solid
displacement (u) and DOF 4 for fluid pressure (p). This element is
implemented for simulating dynamic response of solid-fluid fully coupled
material, based on Biot’s theory of porous medium.





Please click here for examples.





OUTPUT INTERFACE:





Pore pressure can be recorded at an element node using OpenSees Node
Recorder:



recorder Node <-file :math:`fileName&gt; &lt;-time&gt; &lt;-node (`\ nod1 $nod2 …)> -dof 3 vel



The valid queries to a bbarBrickUP element when creating an
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



element bbarBrickUP $eleTag $Node1 $Node2 $Node3 :math:`Node4`\ Node5
$Node6 $Node7 $Node8 $matTag $bulk $fmass $PermX $PermY :math:`PermZ
&lt;`\ bX=0 $bY=0 :math:`bZ=0&gt;</strong></p></td>
</tr>
</tbody>
</table>
<figure>
<img src="/OpenSeesRT/contrib/static/BrickUp.png" title="BrickUp.png" alt="BrickUp.png" />
<figcaption aria-hidden="true">BrickUp.png</figcaption>
</figure>
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



Code Developed by: UC San Diego (Dr. Zhaohui Yang):



.. raw:: html

   <hr />



UC San Diego Soil Model:


