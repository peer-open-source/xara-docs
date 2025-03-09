.. _geomTransf:

Transformations
***************

A geometric-transformation models a configuration-dependent transformation of a finite element's response. 
This is particularly useful for modeling large-displacement effects in constrained structural members like beams and shells. 

.. tabs::

   .. tab:: Python

      .. function:: model.geomTransf(type, tag, *args)

         :param type: string, transformation type
         :param tag: integer, unique transformation tag.
         :param args: list, a list of transformation arguments with number dependent on transformation type

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
   
   geomTransf/Linear
   geomTransf/PDelta
   geomTransf/Corotational
   geomTransf/Spherical


Code Developed by: |fmk|

