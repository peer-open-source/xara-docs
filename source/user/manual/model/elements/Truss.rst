Truss
=====

This command is used to construct a truss element. There are two
ways to construct a truss element:


One way is to specify an area and a ``UniaxialMaterial`` identifier:

.. code:: tcl

   element truss $eleTag $iNode $jNode $A $matTag 
           < -rho $rho > < -cMass $cFlag > < -doRayleigh $rFlag >

the other is to specify a Section identifier:

.. code:: tcl

   element trussSection $eleTag $iNode $jNode $secTag
           < -rho $rho > < -cMass $cFlag > < -doRayleigh $rFlag >



* The truss element DOES NOT include geometric nonlinearities, even when
  used with beam-columns utilizing P-Delta or Corotational
  transformations.


* When constructed with a UniaxialMaterial object, the truss element
  considers strain-rate effects, and is thus suitable for use as a damping
  element.

* The valid queries to a truss element when creating an ElementRecorder
  object are ‘axialForce,’ ‘forces,’ ‘localForce’, deformations,’
  ‘material matArg1 matArg2…,’ ‘section sectArg1 sectArg2…’ There will be
  more queries after the interface for the methods involved have been
  developed further.



Examples
--------

Create a truss element with tag 1 added between nodes 2 and 4 with area 5.5 that uses material 9.

.. code-block:: Tcl
   element truss 1 2 4 5.5 9; 

Code Developed by: |fmk|

