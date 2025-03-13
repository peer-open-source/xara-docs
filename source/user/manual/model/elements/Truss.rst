Truss
^^^^^

This command is used to construct a truss element. 
There are two ways to construct a truss element:


One way is to specify an area and a ``UniaxialMaterial`` identifier:

.. code:: tcl

   element truss $eleTag $iNode $jNode $A $matTag 
           < -rho $rho > < -cMass $cFlag > < -doRayleigh $rFlag >

the other is to specify a Section identifier:

.. code:: tcl

   element trussSection $eleTag $iNode $jNode $secTag
           < -rho $rho > < -cMass $cFlag > < -doRayleigh $rFlag >



* The truss element *does not* include geometric nonlinearities.


* When constructed with a UniaxialMaterial object, the truss element
  considers strain-rate effects, and is thus suitable for use as a damping
  element.

* The valid queries to a truss element when creating an ElementRecorder
  object are 
  * ``"axialForce"``, 
  * ``"forces"`` 
  * ``"localForce"``, 
  * ``"deformations"``, 
  * ``"material *$args"`` 
  * ``"section *$args"``



Examples
--------

Create a truss element with tag 1 added between nodes 2 and 4 with area 5.5 that uses material 9.

.. tabs::

  .. tab:: Python

     .. code-block:: Python

        model.element("Truss", 1, (2, 4), 5.5, 9)
  
  .. tab:: Tcl

     .. code-block:: Tcl

        element Truss 1 2 4 5.5 9;

Code Developed by: |fmk|

