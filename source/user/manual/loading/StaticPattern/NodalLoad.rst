
NodalLoad
=========


.. autoclass:: xara.NodalLoad
   :members:


Examples
--------

.. tabs::
   .. tab:: Python

      .. code-block:: Python

         from xara.load import NodalLoads

         model = xara.Model(ndm=3, ndf=6)

         # Create the nodal loads
         loads = NodalLoads(model, {3: [0, 0, 1.0, 0, 0, 0]})

         # Create a load pattern with the nodal loads
         pattern = xara.StaticPattern(loads)

         # Add the load pattern to the model
         model.pattern(pattern)


.. ref-gallery::

   examples/general/model-0001

