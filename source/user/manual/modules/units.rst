.. _units:

Units
^^^^^

.. py:module:: xara.units
   :synopsis: Predefined constants for common unit systems.

xara does not assume or enforce any unit system.
All model inputs (coordinates, mass, forces, stiffness, etc.) are numeric values; the user must choose a consistent unit system and apply it throughout the model.
The *xara.units* submodule contains predefined constants that can help with keeping track of units, ensuring consistency.


.. autoclass:: xara.units.Units

   .. rubric:: Length

   .. autosummary::

      ~Units.meter
      ~Units.inch
      ~Units.foot

   .. rubric:: Force

   .. autosummary::

      ~Units.newton
      ~Units.pound_force
      ~Units.kilopound

   .. rubric:: Stress

   .. autosummary::

      ~Units.pascal
      ~Units.kilopascal
      ~Units.psi
      ~Units.ksi

   .. rubric:: Mass

   .. autosummary::

      ~Units.newton
      ~Units.pound_force

   .. rubric:: Mass

   .. autosummary::

      ~Units.kilogram

   .. rubric:: Acceleration

   .. autosummary::

      ~Units.gravity
   


Systems
=======


The idiom for importing constants from a system takes the form:

.. code-block:: Python

   from xara.units.<system> import <symbols>...

where ``<system>`` is one of the implemented systems. 
For example, to import the symbols ``inch``, ``kip``, ``N`` and ``Pa`` from the ``us`` system,

.. code-block:: Python

   from xara.units.us import inch, kip, N, Pa

Occasionally it is convenient to import all symbols using a *star-import*

.. code-block:: Python

   from xara.units.us import *

Note, however, that this is generally considered bad programming style.


.. .. _UnitSymbols:

.. Symbols
.. =======

.. Each submodule exports the following symbols:


.. .. _LengthUnits:

.. Length 
.. ------

.. .. csv-table::
..    :header: "Symbols", "Description"
..    :widths: 20, 40

..    ``mm``    (also ``millimeter``)   ,  Milimeter
..    ``cm``    (also ``centimeter``)   ,  Centimeter
..    ``m``     (also ``meter``)        ,  Meter
..    ``km``    (also ``kilometer``)    ,  Kilometer
..    ``inch``                          , 
..    ``ft``    (also ``foot``)         ,  International foot
..    ``yd``    (also ``yard``)         ,  International yard
..    ``mi``    (also ``mile``)         ,  Mile


.. Force 
.. -----

.. .. csv-table::
..    :header: "Symbols", "Description"
..    :widths: 20, 40

..     ``N``    (also ``newton`` )      , Newton (force)
..     ``dyn``  (also ``dyne``   )      , Dyne
..     ``pdl``  (also ``poundal``)      , Poundal
..     ``lbf``  (also ``poundf`` )      ,
..     ``kip``  (also ``klbf``   )      ,


.. Stress 
.. -------

.. .. csv-table::

..    Pa           , pascal       ,  "Pascal, N/m:sup:`2`"
..    torr         ,              , 
..    kPa          , kilopascal   ,  "Kilopascal, 10:sup:`3` Pa"
..    MPa          , megapascals  ,  "Megapascal, N/mm:sup:`2` = 10:sup:`6` Pa"
..    bar          ,              , 
..    atm          , atmosphere   ,  Standard atmosphere
..    MPa          , megapascal   , 
..    GPa          , gigapascal   , 
..    psi          ,              ,  Pound-square-inch
..    ksi          ,              , 



.. Mass 
.. --------

.. .. csv-table::

..    slug         ,              , 
..    lbm          , lbm          ,  International avoirdupois pound
..    gm           , gram         , 
..    kg           , kilogram     ,  Kilogram
..    tonne        ,              ,  "Metric tonne, 10 :sup:`3` kg"
..    oz           , ounce        ,  International avoirdupois ounce




.. Angular Velocity 
.. ----------------

.. .. csv-table::

..    rpm          , revpm        ,  Revolution per minute
..    radps        ,              ,  Radian per second

