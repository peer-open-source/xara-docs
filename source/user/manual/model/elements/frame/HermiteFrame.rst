.. _HermiteFrame:

HermiteFrame
^^^^^^^^^^^^

Two-node frame finite element with cubic displacement formulation.

.. tabs::

   .. tab:: Python

      .. py:method:: Model.element("HermiteFrame", tag, nodes, *, section, transform, integration)
         :no-index:

         :param tag: unique :ref:`element` tag
         :type tag: |integer|
         :param nodes: tuple of *two* :ref:`node` tags
         :type nodes: tuple
         :param section: Section object to be created at the element integration points. 
         :type section: :py:class:`xara.FrameSection`
         :param transform: identifier for previously-defined :ref:`frame transformation <geomTransf>`
         :type transform: |integer|
         :param integration: identifier for previously-defined integration rule, optional.
         :type integration: |integer|, optional
