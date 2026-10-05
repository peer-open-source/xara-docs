.. _units:

Units
^^^^^

.. py:module:: xara.units
   :synopsis: Predefined constants for common unit systems.

OpenSees/|xara| does not assume or enforce any unit system internally. 
All model inputs (coordinates, mass, forces, stiffness, etc.) are numeric values, and the user must take care to maintain consistency in the unit system used. 

The *xara.units* submodule contains predefined constants that can help with keeping track of units. 


.. autofunction:: xara.units.create_units


.. autoclass:: xara.units.Units

   .. rubric:: Length
      :name: UnitLength

   .. autosummary::

      ~Units.meter
      ~Units.inch
      ~Units.foot
      ~Units.yard

   .. rubric:: Force
      :name: UnitForce

   .. autosummary::

      ~Units.newton
      ~Units.pound_force
      ~Units.kilopound


   .. rubric:: Stress
      :name: UnitStress

   .. autosummary::

      ~Units.pascal
      ~Units.gigapascal
      ~Units.megapascal
      ~Units.psi
      ~Units.psf
      ~Units.ksi
      ~Units.ksf

   .. rubric:: Mass
      :name: UnitMass

   .. autosummary::

      ~Units.kilogram
      ~Units.pound_mass
      ~Units.slug


   .. rubric:: Acceleration

   .. autosummary::

      ~Units.gravity
      ~Units.centimeter_per_second_squared
   

   .. rubric:: Mass Density
      :name: UnitDensity

   A unit of *density* is obtained by dividing a unit of mass by a unit of volume. 

   .. autosummary::

      ~Units.kilogram_per_cubic_meter

   It is often convenient to calculate these manually as a ratio of :ref:`mass <UnitMass>` on :ref:`length <UnitLength>` cubed, eg, 

   .. code-block:: python

      rho = 2643.0 * kg / (meter ** 3)

   In the US customary system, density is often available as a :ref:`unit weight <UnitWeight>`. In this case, an appropriate mass density is obtained by dividing by the acceleration due to gravity,

   .. code-block:: python

      rho = 150.0 * pcf / gravity


   .. rubric:: Weight Density
      :name: UnitWeight

   .. autosummary::

      ~Units.pcf



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

Examples
========

