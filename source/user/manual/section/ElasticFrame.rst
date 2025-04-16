.. _ElasticFrame:

ElasticFrame
^^^^^^^^^^^^

The **ElasticFrame** section implements a general linear elastic :ref:`Frame <Frame>` cross-section.

.. tabs::

   .. tab:: Python (RT)

      .. py:method:: Model.section("ElasticFrame", tag, **kwds)
         :no-index:

         :param E: Young's modulus
         :param G: Shear modulus (see :ref:`ElasticIsotropic`)
         :param A: cross sectional area
         :param I1: Moment of inertia about the :math:`\color{green}{1}` axis
         :param I2: Moment of inertia about the :math:`\color{blue}{2}` axis
         :param J: Torsion constant
         :param Qy,Qz: First moments of area
         :param Am: density times area
         :param Im: density weighted polar moment of inertia


   .. tab:: Tcl

      .. function:: section ElasticFrame $tag $E $A $I2 $I1 $G $J

      The required arguments are:

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|,	  unique section tag

In 2D:

.. tabs::

   .. tab:: Python (RT)

      .. py:method:: Model.section("ElasticFrame", tag, **kwds)
         :no-index:

         :param E: Young's modulus
         :param G: Shear modulus (see :ref:`ElasticIsotropic`)
         :param A: cross sectional area
         :param I: Moment of inertia
         :param Iy: Moment of inertia about the :math:`\color{blue}{y}` axis
         :param J: Torsion constant
         :param Qy,Qz: First moments of area
         :param Am: density times area
         :param Im: density weighted polar moment of inertia


   .. tab:: Tcl

      .. function:: section ElasticFrame $tag $E $A $I

      The required arguments are:

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|,	  unique section tag


The valid :ref:`eleResponse` queries are 

* ``"force"``, and 
* ``"deformation"``. 

.. note::

   This section is appropriate for *any* homogeneous section. It is capable of
   representing asymmetric sections, shear warping and torsional warping.


Formulation
-----------


Examples
--------


The following syntax is supported in 2D models for backwards compatibility:

.. tabs::

   .. tab:: Python

      .. code-block:: Python
         
         model.section("ElasticFrame", 1, E, A, I)


References
----------

