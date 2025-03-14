
.. _FixedLocation-BeamIntegration:


FixedLocation
^^^^^^^^^^^^^

.. py:method:: Model.beamIntegration("FixedLocation", tag, N, secTags, locs)
   :noindex:

   :param |integer| tag: tag of the beam integration.
   :param |integer| N: number of integration points along the element.
   :param |integerTuple|: A tuple of previous-defined :ref:`Sections <Section>`.
   :param |floatTuple| locs: Locations of integration points along the element.

This option allows user-specified locations of the integration points. The associated integration
weights are computed by the method of undetermined coefficients (Vandermonde system)

.. math::

   \sum^N_{i=1}x_i^{j-1}w_i = \int_0^1x^{j-1}dx = \frac{1}{j},\qquad (j=1,...,N)


Note that :ref:`NewtonCotes-BeamIntegration` integration is recovered when the integration point locations are equally spaced.

Places ``N`` integration points along the element, whose locations are defined in ``locs``.
on the natural domain [0, 1]. The force-deformation response at each integration point is defined by the ``secs``. 
Both the ``locs`` and ``secs`` should be of length ``N``. 
The order of accuracy for Fixed Location integration is :math:`N-1`.

