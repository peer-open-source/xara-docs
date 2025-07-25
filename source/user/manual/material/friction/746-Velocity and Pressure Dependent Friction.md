# Velocity and Pressure Dependent Friction

This command is used to construct a *VelPressureDep* friction model
object.

```tcl
frictionModel VelPressureDep $tag $muSlow $muFast0 $A $deltaMu $alpha $transRate
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">tag</code></td>
<td><p>unique friction model object tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">muSlow</code></td>
<td><p>coefficient of friction at low velocity</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">muFast0</code></td>
<td><p>initial coefficient of friction at high velocity</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">A</code></td>
<td><p>nominal contact area</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">deltaMu</code></td>
<td><p>pressure parameter calibrated from experimental data</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">alpha</code></td>
<td><p>pressure parameter calibrated from experimental data</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">transRate</code></td>
<td><p>transition rate from low to high velocity</p></td>
</tr>
</tbody>
</table>
<hr />

## Examples

```Tcl
frictionModel VelPressureDep 1 0.085 0.163 7.0686 0.05 0.08 0.77
```
<hr />

## References

<p>[1] Tsopelas P., and Constantinou M. C. (1996). "Experimental Study
of FPS System in Bridge Seismic Isolation." Earthquake Eng. and
Structural Dynamics, VOL. 25, 65-78.</p>
<p>[2] Constantinou M. C., Tsopelas P., Kasalanati A., and Wolff E. D.
(1999). Property Modification Factors for Seismic Isolation Bearings.
Technical Report MCEER-99-0012, University of Buffalo, Buffalo, New
York.</p>
<hr />

<hr />
<p>Code Developed by: <span style="color:blue"> Andreas
Schellenberg, University of California, Berkeley. </span></p>
