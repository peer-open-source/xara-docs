.. _ElasticFrame:

ElasticFrame
^^^^^^^^^^^^^^^^

The **ElasticFrame** section implements a general linear elastic frame section.

.. tabs::

   .. tab:: Python (RT)

      .. py:method:: Model.section("ElasticFrame", tag, **kwds)
         :no-index:

         :param E: Young's modulus
         :param A: cross sectional area
         :param J: Torsion constant
         :param Im: density weighted polar moment of inertia


   .. tab:: Tcl

      .. function:: section ElasticFrame $tag $E $A $Iz $Iy $G $J

      The required arguments are:

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|,	  unique section tag


The valid :ref:`eleResponse` queries are 

* ``'force'``, and 
* ``'deformation'``. 
