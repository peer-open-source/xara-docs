Units
^^^^^

The *xara.units* submodule contains predefined constants that can help with keeping track of units.
Each submodule exports the following symbols:


Systems
=======

The idiom for importing constants from a system takes the form:

.. code-block:: Python

   from xara.units.<system> import <symbols>...

where ``<system>`` is one of the implemented systems. 
For example, to import the symbols ``inch`` and ``kip`` from the ``iks`` system,

.. code-block:: Python

   from xara.units.iks import inch, kip, iks

Occasionally it is convenient to import all symbols using a *star-import*

.. code-block:: Python

   from xara.units.iks import *

Note, however, that this is generally considered bad programming style.


Symbols
=======


Length 
------

.. csv-table::

   mm           , millimeter   ,  Milimeter
   cm           , centimeter   ,  Centimeter
   m            , meter        ,  Meter
   km           , kilometer    ,  Kilometer
   inch         ,              , 
   ft           , foot         ,  International foot
   yd           , yard         ,  International yard
   mi           , mile         ,  Mile


Force 
-----

.. csv-table::

    N            , newton       , Newton (force)
    dyn          , dyne         , Dyne
    pdl          , poundal      , Poundal
    lbf          , poundf       ,
    kip          , klbf         ,


Mass 
--------

.. csv-table::

   slug         ,              , 
   lbm          , lbm          ,  International avoirdupois pound
   gm           , gram         , 
   kg           , kilogram     ,  Kilogram
   tonne        ,              ,  Metric tonne
   oz           , ounce        ,  International avoirdupois ounce


Pressure 
-----------

.. csv-table::

   Pa           , pascal       ,  Pascal
   torr         ,              , 
   kPa          , kilopascal   , 
   bar          ,              , 
   atm          , atmosphere   ,  Standard atmosphere
   MPa          , megapascal   , 
   GPa          , gigapascal   , 
   psi          ,              ,  Pound-square-inch
   ksi          ,              , 
   pci          ,              , 
   pcf          ,              ,  Pounds per cubic foot



Area 
----

.. csv-table::

   mm2          ,              ,  Square millimeter
   m2           ,              ,  Square meter
   cm2          ,              ,  Square centimeter
   km2          ,              ,  Square kilometer
   in2          , inch2        ,  Square inch
   ft2          , feet2        ,  Square foot
   yd2          , yard2        ,  Square yard
   mi2          , mile2        ,  Square mile


Volume 
------

.. csv-table::

   mm3          ,              ,   
   m3           ,              ,   
   cm3          ,              ,   
   km3          ,              ,   
   in3          , inch3        ,   
   ft3          , foot3        ,   
   cyd          , yard3        ,   
   mi3          , mile3        ,   


Velocity 
---------

.. csv-table::

   mmps         ,              ,  Millimeter per second
   cps          , cmps         ,  Centimeter per second
   mps          ,              ,  Meter per second
   kps          ,              ,  Kilometer per second
   ips          , inchps       ,  Inch per second
   fps          , footps       ,  Foot per second
   yps          ,              ,  Yard per second
   mph          ,              ,  mile per hour


Acceleration 
------------

.. csv-table::

   mmps2        ,              , 
   cps2         , cmps2        , 
   mps2         ,              , 
   kps2         ,              , 
   ips2         , inchps2      , 
   fps2         , footps2      , 
   yps2         ,              , 
   mph2         ,              , 
   gravity      ,              ,  Standard gravity


Angular Velocity 
----------------

.. csv-table::

   rpm          , revpm        ,  Revolution per minute
   radps        ,              ,  Radian per second

