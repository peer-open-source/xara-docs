.. _LagrangeFrame:

LagrangeFrame
^^^^^^^^^^^^^

Frame finite element with Lagrange displacement formulation.

.. tabs::

   .. tab:: Python

      .. py:method:: Model.element("LagrangeFrame", tag, nodes, *, section, transform)
         :no-index:

         :param tag: unique :ref:`element` tag
         :type tag: |integer|
         :param nodes: tuple of *two* :ref:`node` tags
         :type nodes: tuple
         :param section: Section object to be created at the element Gauss points. 
         :type section: :py:class:`xara.FrameSection`
         :param transform: identifier for previously-defined :ref:`frame transformation <geomTransf>`
         :type transform: |integer|


Examples 
--------

.. ref-gallery::

   examples/frames/frame-2007
