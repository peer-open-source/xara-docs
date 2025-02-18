FrameLoad
=========

.. function:: model.applied("FrameLoad", n, [r, m], /, pattern, basis, shape)

.. math::

   \boldsymbol{p}_{In} = - \int  N_I(x) \boldsymbol{p}_{n}(x) \, d x

and

.. math::

   \boldsymbol{p}_{Im} = - \int  N_I(x) \boldsymbol{p}_{m}(x) \, d x

where

.. math::

   \boldsymbol{p}_{n}(x) = \sum Q_i(x) \boldsymbol{n}_{i}


``Dirac``
=========

:math:`P_i = \delta(x - x_i)` so that :math:`\boldsymbol{p}_I = N_I(x_i) \boldsymbol{p}_i`


``Heaviside``
=============


Let $\left\{\xi_i, w_i\right\}$ be your standard quadrature nodes and weights on $[0,1]$. You define the new variable $x$ by an affine transformation:

$$
x=r+(1-r) \xi
$$

which maps $\xi=0$ to $x=r$ and $\xi=1$ to $x=1$.
The differential transforms as:

$$
d x=(1-r) d \xi
$$

so the weights must be scaled by $(1-r)$.

