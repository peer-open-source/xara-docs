.. _Spherical:

Spherical
^^^^^^^^^

A *Spherical* transformation is used to enforce strain objectivity in the geometrically exact frame element (:ref:`ExactFrame`).



.. version-note::
   :version: 0.1.33
   :type: added



Theory
------



For two nodes, the procedure implements spherical linear interpolation (SLERP):

.. math::

   \operatorname{SLERP}\left(\boldsymbol{\Lambda}_I, \boldsymbol{\Lambda}_J, \xi\right)=\boldsymbol{\Lambda}_I \exp \left(\frac{\xi}{L} \log \left(\boldsymbol{\Lambda}_I^\mathrm{t} \boldsymbol{\Lambda}_J\right)\right)

The SLERP construction is a geodesic on :math:`\mathrm{SO}(3)`, i.e. a walk along the shortest path, on the manifold, between the two
rotations.

The procedure begins by selecting two node indices :math:`I` and
:math:`J` for an :math:`n`-noded element as follows:

.. math::


   I=\operatorname{floor}\left(\frac{1}{2}(n+1)\right)  \quad \text { and } \quad  J=\operatorname{floor}\left(\frac{1}{2}(n+2)\right).

An intermediate vector
:math:`\mathbf{t} = \operatorname{Log}\boldsymbol{\Lambda}_I^{\mathrm{t}} \boldsymbol{\Lambda}_J`
is formed, and the coordinate rotation is given by:

.. math::


   \left.\begin{array}{rl}
   \boldsymbol{R} &= \boldsymbol{\Lambda}_I \operatorname{Exp} \left(\frac{1}{2} \mathbf{t}\right). \\
   \end{array}\right.


Examples
--------

.. ref-gallery::

   examples/frames/frame-1001


References
----------

.. [1] Jelenić G, Crisfield MA (1999) "Geometrically exact 3D beam theory: implementation of a strain-invariant finite element for statics and dynamics." Computer Methods in Applied Mechanics and Engineering,  171(1–2):141–171.  https://doi.org/10/dj37b3
.. [2] Perez, C.M. and Filippou, F.C. (2024) ‘On nonlinear geometric transformations of finite elements’, International Journal for Numerical Methods in Engineering, p. e7506. Available at: https://doi.org/10.1002/nme.7506.

