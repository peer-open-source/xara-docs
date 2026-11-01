.. _RambergOsgoodSteel:

Ramberg Osgood
^^^^^^^^^^^^^^



A popular envelope model for metalic materials was developed by \citep{ramberg1943description} who proposed the following equation:

.. math::

    \varepsilon = \frac{\sigma}{E} + a\left(\frac{\sigma}{F_y}\right)^n,


where :math:`E` is the elastic modulus, :math:`F_y` is the yield stress, assumed to be at the 0.2\% offset strain, :math:`n` is a parameter controlling the transition to yield, and :math:`a` is a yield offset parameter, typically taken as 0.002.

Note that the stress :math:`\sigma` is defined implicitly in terms of strain :math:`\varepsilon` in this model and must be solved for numerically.

