.. _solid:

Solids
^^^^^^

.. py:method:: Model.element(type, tag, nodes, *, material)
   :noindex:

   Add a solid element to the model.

   :param type: type of the solid element
   :type type: |string|
   :param tag: unique :ref:`element` tag
   :type tag: |integer|
   :param nodes: tuple of node tags forming the solid element
   :param material: material assigned to the solid element
   :type material: :py:class:`xara.MultiaxialMaterial`



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

