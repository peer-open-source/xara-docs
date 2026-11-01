CamClayPlastic
^^^^^^^^^^^^^^

.. py:method:: xara.MultiaxialMaterial("CamClayPlastic", nd, rho, Gr, Br, M, lamda, kappa, e0, p0)
   :noindex:

   :param E: Young's modulus
   :type E: |float|
   :param nu: Poisson's ratio
   :type nu: |float|
   :param lamda: :math:`\lambda` parameter in the Cam-Clay model
   :type lamda: |float|
   :param kappa: :math:`\kappa` parameter in the Cam-Clay model
   :type kappa: |float|
   :param c: :math:`c` parameter in the Cam-Clay model
   :type c: |float|
   :param M: :math:`M` parameter in the Cam-Clay model
   :type M: |float|
   :param p0: :math:`\pi_0` parameter in the Cam-Clay model
   :type p0: |float|
   :param density: Density of the material.
   :type density: |float|


.. math::

    f\left(p, q, \pi_{p}\right) = q^2 + M^2 p\left(p-\pi_{p}\right)

with hardening of the internal variable :math:`\pi_{p}` governed by:

.. math::

    H_{p}(\boldsymbol{\sigma}, \pi_{p}) = \frac{\partial \pi_{p}}{\partial \lambda} = \frac{\left(1+e_0\right)(\pi_{p}+c)}{\lambda-\kappa}\left((c-p)-\frac{\pi_{p}+c}{2}\right) / \sqrt{\left.\left((c-p)-\frac{\pi_{p}+c}{2}\right)^2+\left(\frac{q}{M}\right)^2\right.}


Plastic flow is associated.

The material employs the *cutting-plane algorithm* described by [R2]_.


References
==========

.. [R2] Ortiz, M. and Simo, J.C. (1986) "An analysis of a new class of integration algorithms for elastoplastic constitutive relations" International Journal for Numerical Methods in Engineering, Vol. 23, pp. 353-366.
