.. _ElasticShell:

ElasticShell
^^^^^^^^^^^^

An ElasticShell section is meant to be used with :ref:`shells` and 
represents a Gauss point with thickness and that
is homogeneous with an :ref:`ElasticIsotropic` material.

.. tabs::

   .. tab:: Python (RT)

      .. py:function:: model.section("ElasticShell", tag, E, nu, thickness)
         :no-index:
      
         :param tag: integer tag identifying the section
         :type tag: int
         :param E: Young's modulus
         :type E: float
         :param nu: Poisson's ratio
         :type nu: float
         :param thickness: section thickness
         :type thickness: float


The constitutive relationship of a linear elastic isotropic shell is

.. math::

  \left(\begin{array}{c}
  \boldsymbol{p} \\
  \boldsymbol{m} \\
  \boldsymbol{q}
  \end{array}\right)
  =\underbrace{\left[\begin{array}{cccccccc}
  M & \nu M & 0 & 0 & 0 & 0 & 0 & 0 \\
  \nu M & M & 0 & 0 & 0 & 0 & 0 & 0 \\
  0 & 0 & G & 0 & 0 & 0 & 0 & 0 \\
  0 & 0 & 0 & -D & -\nu D & 0 & 0 & 0 \\
  0 & 0 & 0 & -\nu D & -D & 0 & 0 & 0 \\
  0 & 0 & 0 & 0 & 0 & -\frac{1}{2}(1-\nu) D & 0 & 0 \\
  0 & 0 & 0 & 0 & 0 & 0 & k G & 0 \\
  0 & 0 & 0 & 0 & 0 & 0 & 0 & k G
  \end{array}\right]}_{\mathrm{D}}
  \left(\begin{array}{c}
  \overline{\boldsymbol{\epsilon}} \\
  \boldsymbol{\kappa} \\
  \boldsymbol{\gamma}
  \end{array}\right)

where :math:`M \triangleq \frac{E h}{1-\nu^2}` is the membrane modulus, 
:math:`G \triangleq \frac{E h}{2(1+\nu)}` is the shear modulus, 
:math:`D \triangleq \frac{E h^3}{12\left(1-\nu^2\right)}` is the bending modulus 
and :math:`k \triangleq \frac{5}{6}` the shear correction factor. 


