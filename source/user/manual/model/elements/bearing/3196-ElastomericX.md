# ElastomericX (MK2012)

This command is used to construct an ElastomericX bearing element in three-dimensions. 
The 3D continuum geometry of an elastomeric
bearing is modeled as a 2-node, 12 DOF discrete element. 
This elements extends the formulation of <a href="Elastomeric_Bearing_(Bouc-Wen)_Element">Elastomeric_Bearing_(Bouc-Wen)_Element</a> element.
However, instead of the user providing material models as input
arguments, it only requires geometric and material properties of an
elastomeric bearing as arguments. 
The material models in six direction
are formulated within the element from input arguments. 
The time-dependent values of mechanical properties (e.g., shear stiffness,
buckling load capacity) can also be recorded using the "parameters" <a href="#Recorders" title="wikilink">recorder</a>.

For a 3D problem:

```tcl
element ElastomericX $tag $Nd1 $Nd2 $Fy $alpha $Gr
        $Kbulk $D1 $D2 $ts $tr $n < < $x1 $x2 $x3 > $y1 $y2 $y3 >
        < $kc > < $PhiM > < $ac > < $sDratio > < $m >
        < $cd > < $tc > < $tag1 > < $tag2 > < $tag3 >
        < $tag4 >
```

<hr />
<table>
<tbody>
<tr class="odd">
<td><code class="parameter-table-variable">tag</code></td>
<td><p>unique element object tag</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">Nd1 Nd2</code></p></td>
<td><p>end nodes</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Fy</code></td>
<td><p>yield strength</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">alpha</code></td>
<td><p>post-yield stiffness ratio</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">Gr</code></td>
<td><p>shear modulus of elastomeric bearing</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">Kbulk</code></td>
<td><p>bulk modulus of rubber</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">D1</code></p></td>
<td><p>internal diameter</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">D2</code></p></td>
<td><p>outer diameter (excluding cover thickness)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">ts</code></td>
<td><p>single steel shim layer thickness</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">tr</code></td>
<td><p>single rubber layer thickness</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">n</code></td>
<td><p>number of rubber layers</p></td>
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
<td><code class="parameter-table-variable">kc</code></td>
<td><p>cavitation parameter (optional, default = 10.0)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">PhiM</code></td>
<td><p>damage parameter (optional, default = 0.5)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">ac</code></td>
<td><p>strength reduction parameter (optional, default = 1.0)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">sDratio</code></td>
<td><p>shear distance from iNode as a fraction of the element length
(optional, default = 0.5)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">m</code></td>
<td><p>element mass (optional, default = 0.0)</p></td>
</tr>
<tr class="odd">
<td><code class="parameter-table-variable">cd</code></td>
<td><p>viscous damping parameter (optional, default = 0.0)</p></td>
</tr>
<tr class="even">
<td><code class="parameter-table-variable">tc</code></td>
<td><p>cover thickness (optional, default = 0.0)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">tag1</code></p></td>
<td><p>Tag to include cavitation and post-cavitation (optional, default
= 0)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">tag2</code></p></td>
<td><p>Tag to include buckling load variation (optional, default =
0)</p></td>
</tr>
<tr class="odd">
<td><p><code class="parameter-table-variable">tag3</code></p></td>
<td><p>Tag to include horizontal stiffness variation (optional, default
= 0)</p></td>
</tr>
<tr class="even">
<td><p><code class="parameter-table-variable">tag4</code></p></td>
<td><p>Tag to include vertical stiffness variation (optional, default =
0)</p></td>
</tr>
</tbody>
</table>

<strong>Important note:</strong>
Because default values of heating parameters are in SI units, user
must override the default heating parameters values if using Imperial
units
User should distinguish between yield strength of
elastomeric bearing ($F_y$) and characteristic strength $Q_d=F_y*(1-\alpha)$

<h2>Physical Model and Mechanical Properties</h2>

The material models in six directions are:

<ul>
<li>Axial direction: a new mathematical model that captures the behavior
under cyclic tension <a
href="http://onlinelibrary.wiley.com/doi/10.1002/eqe.2431/abstract">Link</a></li>
<li>Two shear directions: a special case of the Bouc-Wen model extended
by Nagarajaiah et al.(1991) for seismic isolation bearings</li>
<li>Torsion: a linear elastic model</li>
<li>Two rotational directions: linear elastic models</li>
</ul>

In addition to the behavior captured by existing bearing elements, this element can capture following characteristics:

<ol>
<li>Cavitation and post-cavitation behavior in tension (tag1)</li>
<li>Variation in critical buckling load capacity due to lateral
displacement (tag2)</li>
<li>Variation in horizontal shear stiffness with axial load on the
bearing (tag3)</li>
<li>Variation in vertical axial stiffness with horizontal displacement
(tag4)</li>
</ol>
<p>User may choose to include an individual or a combination of these
behaviors through user tags (include:1, exclude:0) in their
analysis.</p>
<p>For the full capabilities of this element, users are referred to: <a
href="http://onlinelibrary.wiley.com/doi/10.1002/eqe.2431/abstract">EESD
Article</a></p>

<h2>Characteristics to include under extreme loading</h2>

<p>A recent paper by <a
href="http://www.sciencedirect.com/science/article/pii/S002954931500254X">Kumar
et. al (2015)</a> explains which of the four tags should be included in
the analysis. Although the analysis presented in the paper is for the
base-isolated NPP, the conclusions are valid for design earthquake and
maximum considered earthquake for regular building structures as well. 
Following are few thumb rules that can be followed: tag 1: Unless you
are investigating the tensile behavior, the effect of the tensile model
on shear response is insignificant. tag 2: It is recommended to use tag
to include variable buckling load capacity. It affects the compression
capacity and shear stiffness. The apparent softening in shear
force-deformation behavior at high axial load is due to this. A constant
buckling load will show less softening. tag 3: Recommended if axial load
expected during the loading is more than 10% of the buckling load
capacity. tag2+tag3 provide greater softening. tag 4: Unless you are
investigating the axial behavior, the effect of the tensile model on
shear response is insignificant.</p>
<h2 id="verification_and_validation">Verification and validation</h2>
<p>This is element has been verified per ASME guidelines. Users are
referred to the <a
href="https://www.researchgate.net/publication/280841152_Verification_and_validation_of_models_of_elastomeric_seismic_isolation_bearings">SMiRT23
Paper</a> and chapter 4 of the Manish Kumar's <a
href="http://www.manishkumar.org/manishkumar/research/Dissertation_Manish_Kumar.pdf">Dissertation</a>
for complete details.</p>

<h2>Recorders</h2>
<p>In addition to regular recorders provided by the bearing elements (<a
href="Element_Recorder" title="wikilink"> Element Recorder</a>), this
element can also record instantaneous values of cavitation force (Fcn),
buckling load capacity (Fcrn), vertical stiffness (Kv) and horizontal
stiffness (ke) using the "Parameters" recorder in that order.

```tcl
recorder Element -file param.out -time -ele 1 Parameters
```

To check if bearing has buckled or cavitated, an user can obtain the
histories of Fcn and Fcrn as described above and divide the axial force
(obtained from basicForce recorder, qb(2)) by Fcn and Fcrn at each time
step, which provides demand vs capacity (D/C) ratios at each time step.
If $Fcn/qb(0) > 1.0$ : Cavitation, or Fcrn/qb(0)&gt;1.0 : Buckling.</p>

<h2 id="examples">Examples</h2>

An example is presented here in which a low damping rubber bearing
(LDR 5 in Warn(2006)) is subjected to a tensile harmonic loading in
laboratory (SEESL at UB). 
The response obtained from ElastomericX
element in OpenSees is compared with the experimental results. The
behavior of elastomeric bearing in shear and compression is well
established, and is not explored here.

```tcl
element ElastomericX 1 1 2 $Fy_h $alpha $G $K $D1 $D2 $ts $tr $n 0 1 \
    0 1 0 0 $kc $PhiM $ac 0.5 0.0 $cd $tc 1 0 0 0
```

<p>Excitation files: <embed src="Excitation_Warn.zip"
title="Excitation_Warn.zip" /> </p>
<p>Tcl files: <img src="EBgravity.tcl" title="EBgravity.tcl"
alt="EBgravity.tcl" /> <img src="EBtest.tcl" title="EBtest.tcl"
alt="EBtest.tcl" /></p>
<figure>
<img src="/_static/wiki/EBWarnComparison.jpg"
title="inline|Numerical and experimental response comparison"
height="400"
alt="inline|Numerical and experimental response comparison" />
<figcaption aria-hidden="true">inline|Numerical and experimental
response comparison</figcaption>
</figure>
<p>More examples of this element would be uploaded soon!</p>

<h2 id="references">References</h2>

<ol>
<li>Kumar, M., Whittaker, A., and Constantinou, M. (2014). "An advanced
numerical model of elastomeric seismic isolation bearings." Earthquake
Engineering &amp; Structural Dynamics, 43(13), 1955-1974. <a
href="http://onlinelibrary.wiley.com/doi/10.1002/eqe.2431/abstract">Link</a></li>
<li>Kumar, M., Whittaker, A., and Constantinou, M. (2015). "Experimental
investigation of cavitation in elastomeric seismic isolation bearings."
Engineering Structures, 101, 290-305. <a
href="http://www.sciencedirect.com/science/article/pii/S0141029615004575">Link</a></li>
<li>Kumar, M., Whittaker, A., and Constantinou, M. (2015). "Response of
base-isolated nuclear structures to extreme earthquake shaking." Nuclear
Engineering and Design (In press). <a
href="http://www.sciencedirect.com/science/article/pii/S002954931500254X">Link</a></li>
<li>Warn, G. P. (2006). "The coupled horizontal-vertical response of
elastomeric and lead-rubber seismic isolation bearings." PhD
Dissertation, Civil, Structural and Environmental Engineering,
University at Buffalo.</li>
<li>Koh, C. G., and Kelly, J. M. (1987). "Effects of axial load on
elastomeric isolation bearings." EERC/UBC 86/12, Earthquake Engineering
Research Center, University of California, Berkeley, United States,
108p.</li>
<li>Nagarajaiah, S., Reinhorn, A. M., and Constantinou, M. C. (1991).
"Nonlinear dynamic analysis of 3-d-base-isolated structures." Journal of
structural engineering New York, N.Y., 117(7), 2035-2054.</li>
<li>Ryan, K. L., Kelly, J. M., and Chopra, A. K. (2005). "Nonlinear
model for lead-rubber bearings including axial-load effects." Journal of
Engineering Mechanics, 131(12), 1270-1278.</li>
</ol>

<hr />

<p>Code Developed by: <span style="color:blue"> Manish Kumar,
University at Buffalo, SUNY. </span></p>
<p>Any bugs in this element can be reported to mkumar2 AT buffalo dot
edu</p>
