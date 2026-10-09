.. _geomTransf:

Transformations
^^^^^^^^^^^^^^^

A geometric-transformation models a configuration-dependent transformation of a finite element's response. 
This is particularly useful for modeling large-displacement effects in constrained structural members like beams and shells. 

.. tabs::

   .. tab:: Python

      .. py:method:: Model.geomTransf(type, tag, *args)

         :param type: Transformation type
         :type type: str
         :param tag: unique transformation tag.
         :type tag: int
         :param args: Transformation arguments with number dependent on transformation type

   .. tab:: Tcl

      .. function:: geomTransf type? args? ...

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         type, |string|,      transformation type
         tag,  |integer|,     unique transformation tag.
         args, |list|,        a list of transformation arguments with number dependent on transformation type

Each type is outlined below. 

.. toctree::
   :maxdepth: 1

   geomTransf/frame/Linear
   geomTransf/frame/PDelta
   geomTransf/frame/Corotational02
   geomTransf/frame/Spherical
   geomTransf/frame/Identity



.. _FrameJointOffsets:


Joint Offsets
=============


Examples
========

.. ref-gallery::

   examples/frames/frame-1022


References
==========

Code Developed by: |rms|, |cmp|, |fmk|

