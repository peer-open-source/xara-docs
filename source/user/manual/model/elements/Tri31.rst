=============
Tri31 Element
=============

This command is used to construct a constant strain triangular element (Tri31) which uses three nodes and one integration points.


.. function:: model.element('Tri31', tag, nodes, thick, type, material, <pressure, rho, b1, b2>)
   :noindex:

   ===================================   ===========================================================================
   ``tag``    |integer|                  unique element object tag
   ``nodes`` |listi|                     a list of three element nodes in counter-clockwise order
   ``thick`` |float|                     element thickness
   ``type`` |str|                        string representing material behavior. The type parameter can be either ``'PlaneStrain'`` or ``'PlaneStress'``
   ``material`` |integer|                tag of an :ref:`nDMaterial`
   ``pressure`` |float|                  surface pressure (optional, default = 0.0)
   ``rho`` |float|                       element mass density (per unit volume) from which a lumped element mass matrix is computed (optional, default=0.0)
   ``b1``  ``b2`` |float|                constant body forces defined in the domain (optional, default=0.0)
   ===================================   ===========================================================================


.. note::

   #. Consistent nodal loads are computed from the pressure and body forces.


The valid queries to a Tri31 element when creating an ElementRecorder object are 

#. `"forces"`, 
#. `"stresses"`, and 
#. `"material $matNum matArg1 matArg2 ..."` Where `$matNum` refers to the material object at the integration point corresponding to the node numbers in the domain.


