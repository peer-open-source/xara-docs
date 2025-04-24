# YamamotoBiaxialHDR


This element can be used to represent the isotropic behavior of high-damping rubber bearing in the local y-z plane.

```tcl
element YamamotoBiaxialHDR $tag $iNode $jNode $Tp $DDo
        $DDi Hr? <-coRS cr? cs?> <-orient <x1? x2? x3? > y1? y2?
        y3?> <-mass m? >;
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">tag</code></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">inode jnode</code></p></td>
<td><p>end nodes</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Tp</code></td>
<td><p>compound type</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>= <strong>1</strong> : X0.6R manufactured by Bridgestone
corporation.</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">DDo</code></td>
<td><p>outer diameter [m]</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">DDi</code></td>
<td><p>bore diameter [m]</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Hr</code></td>
<td><p>total thickness of rubber layer [m]</p></td>
</tr>
<tr class="even">
<td><p>Optional Data</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">cr cs</code></p></td>
<td><p>coefficients for shear stress components of
$\tau_{r}$ and
&lt;math&gt;\tau_{s}&lt;/math&gt;</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">x1 x2 x3</code></p></td>
<td><p>vector components in global coordinates defining local
x-axis</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">yp1 yp2 yp3</code></p></td>
<td><p>vector components in global coordinates defining vector yp which
lies in the local x-y plane for the element</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">m</code></td>
<td><p>element mass [kg]</p></td>
</tr>
</tbody>
</table>


## Notes

1. The valid queries to a YamamotoBiaxialHDR element when creating an
ElementRecorder object are 'globalForce', 'localForce', 'basicForce',
'localDisplacement' and 'basicDeformation'.

<figure>
<img src="/_static/wiki/YamamotoBiaxialHDR_Model.png"
title="YamamotoBiaxialHDR_Model.png" width="150"
alt="YamamotoBiaxialHDR_Model.png" />
<figcaption aria-hidden="true">YamamotoBiaxialHDR_Model.png</figcaption>
</figure>


## Examples

```tcl
element YamamotoBiaxialHDR 1 1 2 1 1.300 0.030 0.261 -orient 0 0 1 1 0 0
```

<p><a href="Media:YamamotoBiaxialHDR_Sample.tcl"
title="wikilink">YamamotoBiaxialHDR_Sample.tcl</a>, <a
href="Media:YamamotoBiaxialHDR_input_X.tcl"
title="wikilink">YamamotoBiaxialHDR_input_X.tcl</a>, <a
href="Media:YamamotoBiaxialHDR_input_Y.tcl"
title="wikilink">YamamotoBiaxialHDR_input_Y.tcl</a></p>
<p><img src="/_static/wiki/Bidirectional-Disp_pattern.png"
title="Bidirectional-Disp_pattern.png" width="250"
alt="Bidirectional-Disp_pattern.png" />
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; <img
src="/_static/wiki/Unidirectional.png" title="Unidirectional.png" width="250"
alt="Unidirectional.png" /></p>
<p><img src="/_static/wiki/Bidirectional-X.png" title="Bidirectional-X.png"
width="250" alt="Bidirectional-X.png" />
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; <img
src="/_static/wiki/Bidirectional-Y.png" title="Bidirectional-Y.png" width="250"
alt="Bidirectional-Y.png" /></p>

## References

<p>Masashi Yamamoto, Shigeo Minewaki, Harumi Yoneda and Masahiko
Higashino, "Nonlinear behavior of high-damping rubber bearings under
horizontal bidirectional loading: full-scale tests and analytical
modeling", <em>Earthquake Engineering and Structural Dynamics</em>,
<strong>41</strong>, 1845-1860, 2012.</p>
<hr />

<p>Code Developed by: <span style="color:blue"> mkiku
</span></p>
