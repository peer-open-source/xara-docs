FrameLoad
^^^^^^^^^

.. tabs::

   .. tab:: Python

      .. autoclass:: xara.FrameLoad
         :members:


   .. tab:: OpenSeesPy

      .. py:method:: Model.eleLoad("FrameLoad", distr, n, [r, m], /, basis, shape)
         :no-index:

         :param distr: key defining the distribution of the load. Options are ``"Uniform"`` and ``"Point"``
         :type distr: str 
         :param n: force values 
         :param basis: string defining the coordinate basis of the load arguments ``n`` and ``m``. Options are ``"local"``, ``"global"``, and ``"director"``


.. note::
   
   This loading is intended to supesede the preexisting beam loads. Currently it is only supported by :ref:`ExactFrame`



Examples
--------


.. ref-gallery::

    examples/frames/frame-1020
