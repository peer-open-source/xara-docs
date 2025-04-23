# InitialStress

The stress-strain behaviour for this material is defined by another material. 
Initial Stress Material enables definition of initial stress
for the material under consideration. 
The strian that corresponds to the
initial stress will be calculated from the other material.

```tcl
uniaxialMaterial InitialStress tag? other? value?
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">tag</code></td>
<td><p>integer tag identifying material</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">otherTag</code></td>
<td><p>tag of the other material</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">value</code></td>
<td><p>initial stress</p></td>
</tr>
</tbody>
</table>
<hr />
