Twenty Eight Node Brick u-p
===========================

Twenty_Eight_Node_BrickUP is a 20-node hexahedral isoparametric element.

The eight corner nodes have 4 degrees-of-freedom (DOF) each: DOFs 1 to 3
for solid displacement (u) and DOF 4 for fluid pressure (p). The other
nodes have 3 DOFs each for solid displacement. This element is
implemented for simulating dynamic response of solid-fluid fully coupled
material, based on Biot’s theory of porous medium.


OUTPUT INTERFACE:


Pore pressure can be recorded at an element node using OpenSees Node
Recorder:

.. code:: tcl

   recorder Node < -file $fileName > < -time > < -node ($nod1 $nod2 …) > -dof 3 vel

See OpenSees command manual (McKenna and Fenves 2001) for nodal
displacement, velocity, or acceleration recorders.


The valid queries to a ``Twenty_Eight_Node_BrickUP`` element when
creating an ElementRecorder are ``'force'``, ``'stiffness'``, or
``'material matNum matArg1 matArg2 ...'``, where matNum represents the
material object at the corresponding integration point.



Code Developed by: UC San Diego (Dr. Zhaohui Yang):
