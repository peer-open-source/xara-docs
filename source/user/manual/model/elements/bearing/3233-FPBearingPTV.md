```{eval-rst}
.. _FPBearingPTV:
```

# FPBearingPTV (MK2014)

The *FPBearingPTV* element represents a single Friction Pendulum bearing, which is capable of accounting for the changes in the
coefficient of friction at the sliding surface with instantaneous values
of the sliding velocity, axial pressure and temperature at the sliding
surface. 
The constitutive modeling is similar to the existing *singleFPBearing* element, otherwise. 


```tcl
element FPBearingPTV $tag $iNode $jNode $MuRef
        $IsPressureDependent $pRef $isTemperatureDependent $Diffusivity
        $Conductivity $IsVelocityDependent $rateParameter $ReffectiveFP
        $Radius_Contact $kInitial $matA $matB $matC
        $matD $x1 $x2 $x3 $y1 $y2 $y3 $shearDist $doRayleigh $mass $iter
        $tol $unit
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
<td><p>End nodes</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">MuRef</code></td>
<td><p>Reference coefficient of friction</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">IsPressureDependent</code></td>
<td><p>1.0 if the coefficient of friction is a function of instantaneous
axial pressure</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">pRef</code></td>
<td><p>Reference axial pressure (the bearing pressure under static
loads)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">IsTemperatureDependent</code></td>
<td><p>1.0 if the coefficient of friction is a function of instantaneous
temperature at the sliding surface</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Diffusivity</code></td>
<td><p>Thermal diffusivity of steel</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Conductivity</code></td>
<td><p>Thermal conductivity of steel</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">IsVelocityDependent</code></td>
<td><p>1.0 if the coefficient of friction is a function of instantaneous
velocity at the sliding surface</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">rateParameter</code></td>
<td><p>The exponent that determines the shape of the coefficient of
friction vs. sliding velocity curve</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">ReffectiveFP</code></td>
<td><p>Effective radius of curvature of the sliding surface of the
FPbearing</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Radius_Contact</code></td>
<td><p>Radius of contact area at the sliding surface</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">kInitial</code></td>
<td><p>Lateral stiffness of the sliding bearing before sliding
begins</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">theMaterialA</code></td>
<td><p>Tag for the uniaxial material in the axial direction</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">theMaterialB</code></td>
<td><p>Tag for the uniaxial material in the torsional direction</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">theMaterialC</code></td>
<td><p>Tag for the uniaxial material for rocking about local Y
axis</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">theMaterialD</code></td>
<td>Tag for the uniaxial material for rocking about local Z
axis</td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">x1 x2 x3</code></p></td>
<td>Vector components to define local X axis</td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">y1 y2 y3</code></p></td>
<td><p>Vector components to define local Y axis</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">shearDist</code></td>
<td><p>Shear distance from iNode as a fraction of the length of the
element</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">doRayleigh</code></td>
<td><p>To include Rayleigh damping from the bearing</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">mass</code></td>
<td><p>Element mass</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">iter</code></td>
<td><p>Maximum number of iterations to satisfy the equilibrium of
element</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">tol</code></td>
<td><p>Convergence tolerance to satisfy the equilibrium of the
element</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">unit</code></td>
<td><p>Tag to identify the unit from the list below.</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>1: N, m, s, C</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>2: kN, m, s, C</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>3: N, mm, s, C</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>4: kN, mm, s, C</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>5: lb, in, s, C</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>6: kip, in, s, C</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>7: lb, ft, s, C</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>8: kip, ft, s, C</p></td>
</tr>
</tbody>
</table>


The *FPBearingPTV* element has been verified and validated in accordance with the ASME guidelines, details of which are presented in Chapter 4 of Kumar et al. (2015a).


<p>NOTE: Updating the coefficient of friction during analysis</p>

The coefficient of friction at the sliding surface of a sliding
bearing changes continuously with instantaneous values of sliding
velocity, temperature at the sliding surface and axial pressure. The
following definition of the coefficient of friction is implemented in
the element.

$$k_v=1-0.5e^{-av} \quad (1)$$
$$k_p = 0.70^{(p-p_0)/50} \quad (2)$$

$$k_t = 0.79(0.70^{T/50} + 0.40) \qquad (3)$$

where $k_v$, $k_p$ and $k_t$ and are the factors to account for the effects of
sliding velocity, axial pressure and temperature at the sliding surface,
respectively, $v$,$p$ and $T$ are velocity of sliding, axial pressure and
temperature at the sliding surface, respectively, controls the shape of
the $k_v$ vs. $v$ curve, and $p_0$ is the reference axial pressure.

The reference coefficient of friction, $\mu_{\mathrm{ref}}$ , is defined as the
coefficient of friction at a reference axial pressure on the bearing $p_0$,
measured at 20˚C at a high velocity of sliding (e.g., 1000 mm/s).
The coefficient of friction, adjusted for the effects of sliding velocity,
axial pressure and temperature, $\mu(p,T,v)$, is obtained as follows.

$$\mu (p,T,v) = \mu_{\mathrm{ref}}\, k_p k_t k_v \qquad (4)$$

where all parameters were defined previously. More details on this
definition of the coefficient of friction are presented in Kumar et al.
(2015a, 2015b).

## Output

The global and local forces, displacements, velocities and
accelerations can be output through node and element recorders. In
addition, temperature, three friction factors ( in sequence), and
adjusted coefficient of friction can be output using the element
recorder with tags `Temperature`, `FrictionFactors`, `MuAdjusted`,
respectively. 
Examples are given below.

```tcl
recorder Element -file Results/Temperature.out -time -ele 1 Temperature;
recorder Element -file Results/Mu.out -time -ele 1 MuAdjusted;
recorder Element -file Results/MuFactors.out -time -ele 1 MuFactors;
```

<hr />

## Examples

All numbers are in SI units (kg, m, C, S)

```tcl
set iNode 1;
set jNode 2;
set R 2.2352 ;
set Mu_Ref 0.06 ;
set p_Ref 50000000 ;
set kp_Factor 1 ;
set kT_Factor 1 ;
set kv_Factor 1 ;
set DF 4.44e-6;
set TK 18.0;
set a 100.0;
set Radius 0.2;
set pi [expr 22.0/7.0];
set Mass_Slider [expr $p_Ref*1.0*$pi*$Radius*$Radius/9.81];
set kInit [expr $Mass_Slider*$accelGravity*$Mu_Ref/$uy];
element FPBearingPTV 1 $iNode $jNode $Mu_Ref $kp_Factor $p_Ref $kT_Factor $DF \
    $TK $kv_Factor $a $R $Radius $kInit 1 2 3 4 0.0 0.0 1.0 1.0 0.0 0.0 \
    0.0 0 0.0 100 1.0E-8 1 ;
```

FPWithUpdate.tcl files models a single concave sliding bearing with
the mass concentrated on the slider. Download the example file and the
ground motions.

<hr />

## References

<p>Kumar, M., Whittaker, A. S., and Constantinou (2015a). “Seismic
isolation of nuclear power plants using sliding bearings,” Report
MCEER-15- 0006, University at Buffalo, State University of New York,
Buffalo, NY.</p>
<p>Kumar, M., Whittaker, A. S., and Constantinou, M. C. (2015b).
&amp;quot;Characterizing friction in sliding isolation
bearings,&amp;quot; Earthquake Engineering &amp;amp; Structural
Dynamics, Vol. 44, No. 9, pp. 1409-1425.</p>
