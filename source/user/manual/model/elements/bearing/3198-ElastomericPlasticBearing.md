# Elastomeric Bearing (Plasticity, AS2006)


The element can have zero length or the appropriate bearing height. 
The bearing has unidirectional (2D)
or coupled (3D) plasticity properties for the shear deformations, and
force-deformation behaviors defined by UniaxialMaterials in the
remaining two (2D) or four (3D) directions. By default (sDratio = 0.5)
$P-\Delta$ moments are equally distributed to the two end-nodes. 
To avoid the introduction of artificial viscous damping in the isolation system
(sometimes referred to as "damping leakage in the isolation system"),
the bearing element does not contribute to the Rayleigh damping by
default. 
If the element has non-zero length, the local $x$-axis is
determined from the nodal geometry unless the optional $x$-axis vector is
specified in which case the nodal geometry is ignored and the
user-defined orientation is utilized.

For a 2D problem:

```tcl
element elastomericBearingPlasticity $tag $iNode
        $jNode $kInit $qd $alpha1 $alpha2 $mu -P $matTag -Mz $matTag 
        < -orient $x1 $x2 $x3 $y1 $y2 $y3 > < -shearDist $sDratio >
        < -doRayleigh > < -mass $m >
```

For a 3D problem:

```tcl
element elastomericBearingPlasticity $tag $iNode $jNode $kInit $qd $alpha1 $alpha2 
        $mu -P $matTag -T $matTag -My $matTag -Mz $matTag 
        < -orient < $x1 $x2 $x3 > $y1 $y2 $y3 >
        < -shearDist $sDratio > < -doRayleigh > < -mass $m >
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">tag</code></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">iNode jNode</code></p></td>
<td><p>end nodes</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">kInit</code></td>
<td><p>initial elastic stiffness in local shear direction</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">qd</code></td>
<td><p>characteristic strength</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">alpha1</code></p></td>
<td><p>post yield stiffness ratio of linear hardening component</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">alpha2</code></p></td>
<td><p>post yield stiffness ratio of non-linear hardening
component</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">mu</code></td>
<td><p>exponent of non-linear hardening component</p></td>
</tr>
<tr class="even">
<td><p><code>-P $matTag</code></p></td>
<td><p>tag associated with previously-defined UniaxialMaterial in axial
direction</p></td>
</tr>
<tr class="odd">
<td><p><code>-T $matTag</code></p></td>
<td><p>tag associated with previously-defined UniaxialMaterial in
torsional direction</p></td>
</tr>
<tr class="even">
<td><p><code>-My $matTag</code></p></td>
<td><p>tag associated with previously-defined UniaxialMaterial in moment
direction around local y-axis</p></td>
</tr>
<tr class="odd">
<td><p><code>-Mz $matTag</code></p></td>
<td><p>tag associated with previously-defined UniaxialMaterial in moment
direction around local z-axis</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">x1 x2 x3</code></p></td>
<td><p>vector components in global coordinates defining local x-axis
(optional)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">y1 y2 y3</code></p></td>
<td><p>vector components in global coordinates defining local y-axis
(optional)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">sDratio</code></td>
<td><p>shear distance from iNode as a fraction of the element length
(optional, default = 0.5)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-flag">-doRayleigh</code></p></td>
<td><p>to include Rayleigh damping from the bearing (optional, default =
no Rayleigh damping contribution)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">m</code></td>
<td><p>element mass (optional, default = 0.0)</p></td>
</tr>
</tbody>
</table>

<figure>
<img src="/_static/wiki/ElastomericBearingPlasticityFig01.png"
title="ElastomericBearingPlasticityFig01.png" width="600"
alt="ElastomericBearingPlasticityFig01.png" />
<figcaption
aria-hidden="true">ElastomericBearingPlasticityFig01.png</figcaption>
</figure>

<hr />

## Notes

1) If the element has zero length and optional orientation vectors
  are not specified, the local element axes coincide with the global axes.
  Otherwise the local $z$-axis is defined by the cross product between the
  $x$- and $y$-vectors specified on the command line.

2) Elastomeric bearings are very stiff in compression, but not rigid.
  It is not a good idea to specify an extremely large axial stiffness
  (such as 1E10), because it can lead to problems with numerical
  sensitivity. Always specify a realistic value for the stiffness of the
  material that is assigned along the axial direction. To assign different
  compression and tension stiffness the <a href="http://opensees.berkeley.edu/wiki/index.php/Elastic_Material">Elastic</a>
  or <a href="http://opensees.berkeley.edu/wiki/index.php/ElasticMultiLinear_Material">ElasticMultiLinear</a>
  material can be used.

3) The valid queries to an elastomeric bearing element when creating
  an ElementRecorder object are `force,` `localForce,` `basicForce,`
  `localDisplacement,` `basicDisplacement` and `material $matNum args ...` Where `matNum` is the number associated with the material whose data is to be output.

<hr />

## Examples

For a 2D elastomeric bearing:

```tcl
element elastomericBearingPlasticity 1 1 2 20.0 2.50 0.02 0.0 3.0 -P 1 -Mz 2; 
```

For a 3D elastomeric bearing:

```tcl
element elastomericBearingPlasticity 1 1 2 20 2.50 0.02 0.0 3.0 -P 1 -T 2 -My 3 -Mz 4; 
```

<hr />

<p>Code developed by: <span style="color:blue"> Andreas
Schellenberg, University of California, Berkeley. </span></p>

