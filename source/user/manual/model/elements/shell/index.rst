.. _shells:

Shells
^^^^^^

.. toctree::
   :maxdepth: 1

   ASDShellQ4
   ASDShellT3

..
   Shell
   ShellDKGQ
   ShellNLDKGQ
   ShellNL
   ShellDKGT
   ShellNLDKGT


Theory
------

A shell element is representative of a 2D solid domain :math:`\Omega` 
embedded in a 3D ambient Euclidean space.
A linearized 3D displacement field is parameterized by the translation :math:`\bar{u}_i` of the plate mid-surface and
rotations :math:`\theta_i` of fibers initially normal to the mid-surface of the plate.

Deformation is characterized by the *curvature tensor* :math:`\boldsymbol{\kappa}`, 
*membrane tensor* :math:`\bar{\boldsymbol{\epsilon}}`,
and *shear strains* :math:`\boldsymbol{\gamma}` with expressions:

.. math::

   \kappa_{\alpha \beta} \triangleq \frac{1}{2}\left(\theta_{\alpha, \beta}+\theta_{\beta, \alpha}\right),
   \quad
   \bar{\epsilon}_{\alpha \beta} \triangleq \frac{1}{2}\left(\bar{u}_{\alpha, \beta}+\bar{u}_{\beta, \alpha}\right),
   \quad\text{and}\quad
   \gamma_{\alpha} \triangleq -\theta_\alpha+\tilde{u}_{3, \alpha}


