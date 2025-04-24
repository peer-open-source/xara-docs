# Velocity Dependent Friction

This command is used to construct a VelDependent friction model. It is useful for modeling the behavior of [<a href="http://en.wikipedia.org/wiki/Polytetrafluoroethylene%22PTFE">PTFE</a>]
or PTFE-like materials sliding on a stainless steel surface. 
For a detailed presentation on the velocity dependence of such interfaces
please refer to Constantinou et al. (1999).

```tcl
frictionModel VelDependent $tag $muSlow $muFast $transRate
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
<td><code class="parameter-table-variable">muFast</code></td>
<td><p>coefficient of friction at high velocity</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">transRate</code></td>
<td><p>transition rate from low to high velocity</p></td>
</tr>
</tbody>
</table>

<span
class="math display"><em>μ</em> = <em>μ</em><sub><em>f</em><em>a</em><em>s</em><em>t</em></sub> − (<em>μ</em><sub><em>f</em><em>a</em><em>s</em><em>t</em></sub>−<em>μ</em><sub><em>s</em><em>l</em><em>o</em><em>w</em></sub>) ⋅ <em>e</em><sup>−<em>t</em><em>r</em><em>a</em><em>n</em><em>s</em><em>R</em><em>a</em><em>t</em><em>e</em> ⋅ |<em>v</em>|</sup></span>

<figure>
<img src="/_static/wiki/VDependentFriction01.png" alt="VDependentFriction01.png" />
<figcaption aria-hidden="true">Velocity dependent friction model response.</figcaption>
</figure>
<figure>
<img src="/_static/wiki/VDependentFrictionCurveFit.png" alt="VDependentFrictionCurveFit.png" />
<figcaption aria-hidden="true">VDependentFrictionCurveFit.png</figcaption>
</figure>
<hr />

## Examples

```Tcl
frictionModel VelDependent 1 0.05 0.163 0.615
```

<hr />

## References

<p>Constantinou, M.C., Tsopelas, P., Kasalanati, A., and Wolff, E.D.
(1999). “Property modification factors for seismic isolation bearings”.
Report MCEER-99-0012, Multidisciplinary Center for Earthquake
Engineering Research, State University of New York.</p>

<hr />

<p>Code Developed by: <span style="color:blue"> Andreas
Schellenberg, University of California, Berkeley. </span></p>
