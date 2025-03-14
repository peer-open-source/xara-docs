.. _solid:

Solids
^^^^^^

.. toctree::
   :maxdepth: 1

   brick
   bbarBrick
   SSPbrick
   FourNodeTetrahedron
   TenNodeTetrahedron

Theory
------

A solid element represents a 3D continuum embedded in 3D ambient Euclidean space.
A configuration of a solid is described by a vector field of deformed positions :math:`\boldsymbol{x}`.
The governing equation is

.. math::

   \operatorname{Div} \boldsymbol{F}\boldsymbol{S} + \boldsymbol{b} = \rho \ddot{\boldsymbol{x}}

