.. _Frame:

Frame
^^^^^


Frame elements are used to model slender structural members like beams and columns.
All frame elements are constructed with the form

.. py:method:: Model.element(name, tag, nodes, *, section, transform)
   :noindex:

   Add a frame element to the model.


Available frame elements include

.. csv-table:: 
    :header: "Name", "Description"
    :widths: 10, 40

    :ref:`elasticBeamColumn`, "Prismatic linear-elastic frame"
    :ref:`ForceFrame`, "Force formulation"
    :ref:`HermiteFrame`, "Cubic displacement formulation without shear. :version-added:`0.1.33`"
    :ref:`LagrangeFrame`, "Lagrange displacement formulation with shear. :version-added:`0.1.33`"
    :ref:`ExactFrame`, "Geometrically exact displacement formulation"

.. toctree::
   :maxdepth: 1
   :hidden:

   PrismFrame
   ForceFrame
   ExactFrame
   HermiteFrame
   LagrangeFrame


Defining a frame element involves the following steps:

#. Define :ref:`nodes <Node>` with appropriate coordinates
#. Create a :ref:`coordinate transformation <geomTransf>` with the element orientation
#. Define :ref:`section <FrameSection>` behavior for the element
#. Optionally define an :ref:`integration rule <beamIntegration>`, if supported by the element type
#. Create the frame element, connecting it to nodes, sections, and a transformation
#. Optionally apply :ref:`element loads <FrameLoad>`

The available frame elements are summarized in the table below:

.. csv-table:: 
   :header: "Name", "Shear", "Geometry", "Integration", "Interpolation"
   :widths: 8, 8, 8, 8, 8

   :ref:`elasticBeamColumn`, "Elastic", "Basic",    "None", "None"
   :ref:`ForceFrame`,    "Optional", "Basic", "User", "Fixed"
   :ref:`HermiteFrame`,  "No",  "Basic", "User", "Fixed"
   :ref:`LagrangeFrame`, "Yes", "Basic", "Fixed", "Nodes"
   :ref:`ExactFrame`,    "Yes", "Exact", "Fixed", "Nodes"

..
   :ref:`PlasticFrame`,  "Elastic",  "Basic", "None", "None"


In view of these capabilities:

* :ref:`elasticBeamColumn` is ideal for *elastic* members of any shape that are expected to undergo *small to moderate displacements*.
* :ref:`ForceFrame` is an ideal general-purpose frame element for inelastic members undergoing *small to moderate displacements*.
  In this setting the element can achieve exceptional accuracy with minimal mesh subdivisions. 
  Unlike displacement formulations, shear effects can be conveniently toggled in this element using the ``shear`` option. 
  However, this element involves local iteration that may fail to converge on occation. 
* :ref:`ExactFrame` is typically ideal for members undergoing *large displacements* and *rotations*. 
* :ref:`HermiteFrame` is a suitable fallback when :ref:`ForceFrame` fails to converge in a problem **without** significant shear effects. 
  However, in order to achieve comparable accuracy with :ref:`ForceFrame`, a finer mesh is typically required.
* :ref:`LagrangeFrame` is a suitable fallback when :ref:`ForceFrame` fails to converge in a problem **with** shear effects. 
  However, in order to achieve comparable accuracy with :ref:`ForceFrame`, a finer mesh is typically required.



..
   Theory
   ------

   A frame element represents a directed medium with a scalar characteristic coordinate :math:`\xi`.
   The embedding in space is described by:

   * A vector field :math:`\boldsymbol{x}(\xi)` identifying positions in space,
   * A rotation field :math:`\boldsymbol{\Lambda}(\xi)`, and
   * A vector field :math:`\boldsymbol{\alpha}(\xi)` identifying cross-sectional warping.


   Some phenomena that can be modeled with frame elements include:

   * Distrubuted loads
   * Follower loads 
   * Plastic hinges
   * Arbitrarily large rotations
   * Lateral-torsional buckling of beams,
   * Restrained torsional warping 

