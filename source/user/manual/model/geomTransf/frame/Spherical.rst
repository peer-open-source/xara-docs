Spherical
^^^^^^^^^

A *Spherical* transformation is used to enforce strain objectivity in the geometrically exact frame element.
The procedure is invariant to node-numbering.

.. note::

   For two nodes, the procedure implements spherical linear interpolation (SLERP):
   
   .. math::
   
      \operatorname{SLERP}\left(\boldsymbol{\Lambda}_I, \boldsymbol{\Lambda}_J, \xi\right)=\boldsymbol{\Lambda}_I \exp \left(\frac{\xi}{L} \log \left(\boldsymbol{\Lambda}_I^\mathrm{t} \boldsymbol{\Lambda}_J\right)\right)
   
   The SLERP construction is a geodesic on :math:`\mathrm{SO}(3)`, i.e. a
   walk along the shortest path, on the manifold, between the two
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

The nodal spin matrices :math:`\boldsymbol{W}_a` have the form:

.. math::


   \boldsymbol{W}_a = \left[\boldsymbol{0} ~~ \boldsymbol{W}_{a\scriptscriptstyle{\Lambda}}\right]

where :math:`\boldsymbol{W}_{a\scriptscriptstyle{\Lambda}} = \boldsymbol{0}` for
:math:`a \notin \{I,J\}` and otherwise:

.. math::


   \operatorname{Exp} \bar{\boldsymbol{\Psi}}_i= \boldsymbol{R}^{\mathrm{t}} \boldsymbol{\Lambda}_i \quad \longrightarrow \quad \bar{\boldsymbol{\Psi}}_i ; \quad i=1, \ldots, N .


.. note::

   :math:`\mathbf{T}` s of Crisfield and Jelenic are inv-transposed


.. math::


   \begin{aligned}
   \boldsymbol{\omega}_Q
   &= \boldsymbol{R}\left[\mathbf{T}_I+\mathbf{T}^\mathrm{t}_I\right]^{-1} \mathbf{T}_I \boldsymbol{R}^\mathrm{t} \boldsymbol{\omega}_I 
   + \boldsymbol{R}\left[\mathbf{T}_J+\mathbf{T}^\mathrm{t}_J\right]^{-1} \mathbf{T}_J \boldsymbol{R}^\mathrm{t} \boldsymbol{\omega}_J \\
   &= \boldsymbol{R} \bar{\boldsymbol{W}}_I \boldsymbol{R}^\mathrm{t} \boldsymbol{\omega}_I + \boldsymbol{R} \bar{\boldsymbol{W}}_J\boldsymbol{R}^\mathrm{t} \boldsymbol{\omega}_J \\
   \end{aligned}

.. math::


   \begin{aligned}
   \boldsymbol{W}_{I \Lambda} &= \frac{1}{2}\left(\boldsymbol{1} + \frac{1}{t} \tan \frac{t}{4} \, \boldsymbol{t}^{\wedge}\right) \\
   %
   \boldsymbol{W}_{J \Lambda} &=\frac{1}{2}\left(\boldsymbol{1} -\frac{1}{t} \tan \frac{t}{4} \, \boldsymbol{t}^{\wedge}\right)
   \end{aligned}

with :math:`t = \|\boldsymbol{t}\|`.

--------------

.. math::


   \begin{aligned}
   \tilde{\mathbf{I}}^i(\xi) &=\phi^i(\xi) \boldsymbol{\Lambda}_r \mathbf{T}^{-1}_\xi \mathbf{T}_i \boldsymbol{\Lambda}_r^\mathrm{t} \\
   & +\delta^{i l} \boldsymbol{\Lambda}_r\left[\mathbf{1}-\mathbf{T}^{-1}_\xi \sum_{j=1}^{n_{\Lambda}} \phi^j(\xi) \mathbf{T}_j\right] \mathbf{v}^I \boldsymbol{\Lambda}_r^\mathrm{t} \\
   & +\delta^{i J} \boldsymbol{\Lambda}_r\left[\mathbf{1}-\mathbf{T}^{-1}_\xi\sum_{j=1}^{n_{\Lambda}} \phi^j(\xi) \mathbf{T}_j\right] \mathbf{v}^J \boldsymbol{\Lambda}_r^\mathrm{t} \\
   &=\Delta_k^{i j} \Lambda_r\left\{\left(\delta_I^k+\delta_J^k\right)\left[1-T^{-1}_\xi \tilde{T}\right] v_J+T^{-1}_\xi \phi^k_\xi T_j\right\} \Lambda_r^\mathrm{t}
   \end{aligned}

