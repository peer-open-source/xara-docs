.. _Frame:

Frame
^^^^^


Frame elements are used to model slender structural members like beams and columns.
All frame elements are constructed with the form

.. py:method:: Model.element(name, tag, nodes, section, transform)
   :noindex:

   Add a frame element to the model.


Available frame elements include

.. csv-table:: 
    :header: "Name", "Description"
    :widths: 10, 40

    :ref:`elasticBeamColumn`, "Prismatic linear-elastic frame"
    :ref:`ForceFrame`, "*Force* formulation"
    :ref:`CubicFrame`, "cubic displacment formulation"
    :ref:`ExactFrame`, "geometrically exact displacement formulation"

.. toctree::
   :maxdepth: 1
   :hidden:

   PrismFrame
   ForceFrame
   CubicFrame
   ExactFrame

Loads include

.. toctree::
   :maxdepth: 1

   FrameLoad


Theory
------

A frame element represents a directed medium with a scalar characteristic coordinate :math:`\xi`.
The embedding in space is described by:

* A vector field :math:`\boldsymbol{x}(\xi)` identifying positions in space,
* A rotation field :math:`\boldsymbol{\Lambda}(\xi)`, and
* A vector field :math:`\boldsymbol{\alpha}(\xi)` identifying cross-sectional warping.


