.. _eleLoad:

eleLoad
^^^^^^^

The eleLoad command is used to define distributed loads within elements
that are associated with an enclosing Plain load pattern.

.. function:: eleLoad {*}$args ...

.. note::

   The load values are reference loads values; it is the time series that provides the load factor. The load factor times the reference values is the load that is actually applied to the node.


.. warning::

   At the moment, eleLoads do not work with 3D beam-column elements if Corotational geometric transformation is used.


Examples
--------

.. code:: tcl

   set width 20.0
   set W 4000.0;
   timeSeries Linear 1
   pattern Plain 1 1 {
       eleLoad -ele 3 -type -beamUniform [expr -$W/$width]
   }

.. code:: Python

   width = 20.0;
   W = 4000.0;
   model.pattern("Plain",1,"Linear")
   model.eleLoad("-ele",3, "-type", "-beamUniform", W/width)

Code Developed by: |fmk|

