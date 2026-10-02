.. _UniaxialFiber:


UniaxialFiber
^^^^^^^^^^^^^


.. py:class:: xara.FrameSection("UniaxialFiber", shape, *, fibers)
   :noindex:

   Create an inelastic frame section that integrates the response of :py:class:`xara.UniaxialMaterial` objects distributed over the section shape.


   :param shape: A :ref:`Shape <FrameShape>` object defining the cross-sectional geometry.
   :param fibers: An *optional* dictionary describing the distribution of fibers over the cross-section. By default fibers will be generated automatically.
   :type fibers: dict, optional
