# BoucWen

This command is used to construct a uniaxial Bouc-Wen smooth hysteretic material.
This material model is an extension of the
original Bouc-Wen model that includes stiffness and strength degradation
(Baber and Noori (1985)).



<hr />
<table>
<tbody>
<tr class="even">
<td><code class="parameter-table-variable">n</code></td>
<td><p>parameter that controls transition from linear to nonlinear range
(as n increases the transition becomes sharper; n is usually grater or
equal to 1)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">gamma beta</code></p></td>
<td><p>parameters that control shape of hysteresis loop; depending on
the values of $\gamma$ and
$\beta$ softening, hardening or quasi-linearity
can be simulated (look at the NOTES)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">Ao deltaA</code></p></td>
<td><p>parameters that control tangent stiffness</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">deltaNu deltaEta</code></p></td>
<td><p>parameters that control material degradation</p></td>
</tr>
</tbody>
</table>

