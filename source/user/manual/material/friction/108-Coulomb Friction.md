# Coulomb Friction

Coulomb's Law of Friction states that kinetic friction is
independent of the sliding velocity.

```tcl
frictionModel Coulomb $tag $mu
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">tag</code></td>
<td><p>unique friction model object tag</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">mu</code></td>
<td><p>coefficient of friction</p></td>
</tr>
</tbody>
</table>
<figure>
<img src="/_static/wiki/CoulombFriction.png" alt="CoulombFriction.png" />
<figcaption aria-hidden="true">Constant coefficient of friction.</figcaption>
</figure>
<hr />

## Examples

```tcl
frictionModel Coulomb 1 0.163
```


<hr />
<p>Code Developed by: <span style="color:blue"> Andreas
Schellenberg, University of California, Berkeley. </span></p>
