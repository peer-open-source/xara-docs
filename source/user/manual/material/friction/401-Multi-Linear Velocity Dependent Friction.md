# Multi-Linear Velocity Dependent Friction

This command is used to construct a VelDepMultiLinear friction model
object. The friction-velocity relationship is given by a multi-linear
curve that is define by a set of points. The slope given by the last two
specified points on the positive velocity axis is extrapolated to
infinite positive velocities. Velocity and friction points need to be
equal or larger than zero (no negative values should be defined). 
The number of provided velocity points needs to be equal to the number of
provided friction points.

```tcl
frictionModel VelDepMultiLinear $tag -vel $velocityPoints -frn $frictionPoints
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">tag</code></td>
<td><p>unique friction model object tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">velocityPoints</code></td>
<td><p>array of velocity points along friction-velocity curve</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">frictionPoints</code></td>
<td><p>array of friction points along friction-velocity curve</p></td>
</tr>
</tbody>
</table>
<figure>
<img src="/_static/wiki/VelDepMultiLinear.png" title="VelDepMultiLinear.png"
width="500" alt="VelDepMultiLinear.png" />
<figcaption aria-hidden="true">A multi-linear friction response.</figcaption>
</figure>
<hr />

## Examples

```Tcl
frictionModel VelDepMultiLinear 1 -vel 0.0 0.1 2.0 8.0 10.0 -frn 0.163 0.085 0.150 0.163 0.163
```
<hr />

<hr />
<p>Code Developed by: <span style="color:blue"> Andreas
Schellenberg, University of California, Berkeley. </span></p>
