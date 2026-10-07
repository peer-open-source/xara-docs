.. _Tri31:

Triangle
^^^^^^^^

``Tri31`` is a constant strain triangular element which uses three nodes and one integration points.

.. py:method:: Model.element("Triangle", tag, nodes, *, section, [pressure, rho, b1, b2])
   :no-index:

   :param tag: unique :ref:`Element` tag
   :type tag: |integer|
   :param nodes: a list of three element nodes in counter-clockwise order
   :type nodes: tuple of |integer|
   :param section: Section object defining element material, thickness, and plane stress/strain conditions.
   :type section: :py:class:`xara.PlaneSection`
   :param pressure: Surface pressure (optional, default = 0.0)
   :type pressure: |float|, optional
   :param rho: Element mass density (per unit volume) from which a lumped element mass matrix is computed (optional, default=0.0)
   :type rho: |float|, optional
   :param b1: constant body forces defined in the domain (optional, default=0.0)
   :type b1: |float|, optional
   :param b2: constant body forces defined in the domain (optional, default=0.0)
   :type b2: |float|, optional

The valid queries to a Tri31 element through :ref:`eleResponse` are 

#. ``"forces"``, 
#. ``"stresses"``, and 
#. ``"material $mat args..."`` 

Where ``$mat`` refers to the material object at the integration point corresponding to the node numbers in the domain.


Examples
--------

.. ref-gallery::

   examples/material/material-0012
