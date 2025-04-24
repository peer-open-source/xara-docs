# Bearings

## Elastomer

The physical model of an elastomeric bearing is considered as a
two-node, twelve degrees-of-freedom discrete element. 
The two nodes are connected by six springs that represent the mechanical behavior in the six basic directions of a bearing. The degrees of freedom and discrete spring representation of an elastomeric bearing are shown in the below
figures.

<p><img src="/_static/wiki/Elastomeric3DModel.png"
title="inline|Physical continuum model" height="300"
alt="inline|Physical continuum model" /> <img
src="/_static/wiki/ElastomericDiscreteSpring.png"
title="inline|Discrete spring representation" height="300"
alt="inline|Discrete spring representation" /></p>

The general form of element force vector, $f_b$,
and element stiffness matrix, $K_b$, for element
representation considered above is given by equation below:

$$
f_b=\left[ \begin{matrix} Axial \\ Shear1 \\ Shear2 \\
Torsion \\ Rotation1 \\ Rotation2 \\ \end{matrix} \right]
$$
$$
K_b=\left[ \begin{matrix} Axial & 0 & 0 & 0 & 0 & 0 \\
0 & Shear1 & Shear12 & 0 & 0 & 0 \\ 0 & Shear21
& Shear2 & 0 & 0 & 0 \\ 0 & 0 & 0 & Torsion
& 0 & 0 \\ 0 & 0 & 0 & 0 & Rotation1 & 0 \\
0 & 0 & 0 & 0 & 0 & Rotation2 \\ \end{matrix}
\right]
$$


The coupling of the two shear springs is considered directly by using a coupled bidirectional model. All other springs are uncoupled. 

The coupling of vertical and horizontal directions are considered indirectly by using expressions for mechanical properties in one direction that are dependent on the response parameters in the other direction. 

Linear uncoupled springs are considered in the torsion and the two rotational
springs as they are not expected to significantly affect the response of
an elastomeric bearing. 
The off-diagonal terms due to coupling between
axial and shear, and axial and rotation, are not considered in the
two-spring model (Koh and Kelly, 1987) used here. An exact model would
have non-zero values of these off-diagonal terms. A discussion on the
formulation of the two-spring model and the exact model is presented in
Ryan et al.(1991). 
The subscript $b$ refers to the element’s basic coordinate system. 
Response quantities are transformed between the
basic, local and global coordinates to perform computations.


The mechanical
properties of the six springs are defined using analytical solutions available from the
analysis of elastomeric bearings. 
The expression for mechanical
properties, including stiffness and buckling load capacity, are derived
using explicit consideration for geometric nonlinearity due to large
displacement effects. 


```{eval-rst}

.. toctree::
    :maxdepth: 1

    3197-ElastomericBoucWenBearing
    3198-ElastomericPlasticBearing
    3196-ElastomericX
```

## Sliding

```{eval-rst}
.. toctree::
    :maxdepth: 1
    :caption: Single

    3651-SingleFrictionPendulumBearing
    3233-FPBearingPTV

.. toctree::
    :maxdepth: 1
    :caption: Triple

    3714-TripleFrictionPendulumBearing
    3715-TripleFrictionPendulum
    TripleFrictionPendulumX

.. toctree::
    :maxdepth: 1
    :caption: Other

    3251-FlatSliderBearing
    3568-RJ-Watson-EQS-Bearing

..
    3406-MultipleShearSpring
```


## Other 

```{eval-rst}

.. toctree::
    :maxdepth: 1

    320-HDR
    361-LeadRubberX
    3057-YamamotoBiaxialHDR
    354-KikuchiBearing.
```


## References

This page is adapted from the documentation of the *HDR*, *LeadRubberX* and *ElastomericX* elements by Manish Kumar.
