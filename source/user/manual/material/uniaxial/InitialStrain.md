# InitialStrain

The stress-strain behaviour for this material is defined by another
material. Initial Strain Material enables definition of initial strains
for the material under consideration. The stress that corresponds to the
initial strain will be calculated from the other material.

```tcl
uniaxialMaterial InitStrainMaterial $tag $other $value
```
<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">tag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">other</code></td>
<td><p>tag of the other material</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">initStrain</code></td>
<td><p>initial strain</p></td>
</tr>
</tbody>
</table>
