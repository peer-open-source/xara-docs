.. _ElasticSection:

Elastic
^^^^^^^


The **ElasticFrame** section implements a general linear elastic :ref:`Frame <Frame>` cross-section.

.. figure:: figures/section-axes.png
   :width: 30%
   :align: center

   Local axes of a 3D cross section


.. tabs::

   .. tab:: Shape

      .. py:class:: xara.FrameSection("Elastic", shape)
         :noindex:

         :param shape: A :ref:`shape <FrameShape>` object representing the cross-sectional geometry.


   .. tab:: Properties

      .. py:class:: xara.FrameSection("Elastic", **kwds)
         :noindex:

         :param E,G: Young's modulus :math:`E` and shear modulus :math:`G` (see :ref:`ElasticIsotropic`) [1]_
         :param float A: cross sectional area :math:`A` [1]_ [2]_. Units of length :sup:`2`.
         :param float Iy: Moment of inertia about the :math:`\color{green}{y}` axis, :math:`I_y` [1]_ [2]_
         :param float Iz: Moment of inertia about the :math:`\color{blue}{z}` axis, :math:`I_z` [1]_ [3]_
         :param float J: Torsion constant [3]_. Units of length :sup:`4`.
         :param float Ay: Shear area in the :math:`\color{green}{y}` direction, :math:`A_y`. Optional, defaults to :math:`A`. Units of length :sup:`2`.
         :param float Az: Shear area in the :math:`\color{blue}{z}` direction, :math:`A_z`. Optional, defaults to :math:`A`. Units of length :sup:`2`.



      .. [1] These arguments are supported by the :ref:`parameter <parameter>` commands.
      .. [2] These arguments are *always* required.
      .. [3] These arguments are required in 3D.

