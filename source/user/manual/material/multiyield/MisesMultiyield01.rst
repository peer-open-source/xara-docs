.. _PressureIndependentMultiYield:

MisesMultiyield01
^^^^^^^^^^^^^^^^^


**PressureIndependMultiYield**, also known as *UCSDCLAY*, is an elastic-plastic material in which plasticity exhibits only in the deviatoric stress-strain response. 
The volumetric stress-strain response is linear-elastic and is independent of the deviatoric response. 

This material is implemented to simulate monotonic or cyclic response of materials whose shear behavior is insensitive to the confinement change. 
Such materials include, for example, organic soils or clay under fast (undrained) loading conditions.

During the application of gravity load (and static loads if any), material behavior is linear elastic. 
In the subsequent dynamic (fast) loading phase(s), the stress-strain response is elastic-plastic (see MATERIAL STAGE UPDATE below). 
Plasticity is formulated based on the multi-surface (nested surfaces) concept, with an associative flow rule. 
The yield surfaces are of the Von Mises type.

.. py:class:: xara.MultiaxialMaterial("MisesMultiyield01", nd, rho, Gr, Br, c, es_max, frictionAng=0, pr=100, d=0. nys=20, <r1 Gs1 ...> >)
   :noindex:

   :param nd: number of dimensions (2 for plane-strain, 3 for 3D)
   :type nd: |integer|
   :param rho: saturated soil mass density
   :type rho: |float|
   :param Gr: reference low-strain shear modulus, specified at a reference mean effective confining pressure :math:`p'_r`. Units of :ref:`stress <UnitStress>`.
   :type Gr: |float|
   :param Br: reference bulk modulus, specified at a reference mean effective confining pressure :math:`p'_r`. Units of :ref:`stress <UnitStress>`.
   :type Br: |float|
   :param c: apparent cohesion :math:`c` at zero effective confinement. Units of :ref:`stress <UnitStress>`.
   :type c: |float|
   :param es_max: octahedral shear strain :math:`\gamma_{\mathrm{max}}` at which the maximum shear strength is reached, specified at a reference mean effective confining pressure :math:`p'_r`.
   :type es_max: |float|
   :param frictionAng: friction angle at peak shear strength in degrees (optional, default is 0.0)
   :type frictionAng: |float|
   :param pr: reference mean effective confining pressure :math:`p'_r` at which :math:`G_r`, :math:`B_r`, and :math:`\gamma_{\mathrm{max}}` are defined (optional, default is 100. kPa)
   :type pr: |float|



.. function:: nDmaterial PressureIndependMultiYield tag nd rho Gr Br c es_max <frictionAng=0. pr=100. d=0. nys=20 <r1 Gs1 …> >

.. csv-table:: Arguments
   :header: "Argument", "Type", "Description"
   :widths: 1, 1, 98

   tag, |integer|,  A positive integer uniquely identifying the material among all nDMaterials.
   nd, |integer|, "Number of dimensions, 2 for plane-strain, and 3 for 3D analysis."
   rho, |float|, "Saturated soil mass density."
   Gr, |float|,  "Reference low-strain shear modulus :math:`G_r`, specified at a reference mean effective confining pressure :math:`p'_r` (see below)."
   Br, |float|, "Reference bulk modulus :math:`B_r`, specified at a reference mean effective confining pressure :math:`p'_r` (see below)."
   c (:math:`c`), |float|, "Apparent cohesion :math:`c` at zero effective confinement."
   es_max, |float|, "Octahedral shear strain :math:`\gamma_{\mathrm{max}}` at which the maximum shear strength is reached, specified at a reference mean effective confining pressure :math:`p'_r` (see below)."
   frictionAng (Φ), |float|, "Friction angle at peak shear strength in degrees. (optional: default is 0.0)."
   pr (:math:`p'_r`), |float|, "Reference mean effective confining pressure :math:`p'_r` at which :math:`G_r` and :math:`B_r` and :math:`\gamma_{\mathrm{max}}` are defined. Optional (default is 100. kPa)."
   d, |float|,  "A positive constant :math:`d > 0` defining variations of :math:`G` and :math:`B` as a function of instantaneous effective confinement :math:`p'` (default is 0.0). see notes 4 and 5 below."
   nys, |integer|, "Number of yield surfaces, optional (must be less than 40: default is 20). The surfaces are generated based on the hyperbolic relation defined in Note 2 below."
   r Gs, |float|, "Instead of automatic surfaces generation (Note 2), you can define yield surfaces directly based on desired shear modulus reduction curve. To do so, add a minus sign in front of ``nys``, then provide noYieldSurf pairs of shear strain (γ) and modulus ratio (Gs) values. For example, to define 10 surfaces: … -10γ1Gs1 … γ10Gs10 …"


Notes
=====


The friction angle :math:`\phi` and cohesion :math:`c` define the variation of peak (octahedral) shear strength :math:`\tau_f` as a function of current effective confinement :math:`{p^t}_i`:

.. math::

   \tau_f = \frac{2 \sqrt{2} \sin \phi}{3 - \sin \phi}{p^t}_i + \frac{2 \sqrt{2}}{3}c



Yield Surfaces
++++++++++++++

2. Automatic surface generation: at a constant confinement :math:`p^t`, the shear stress :math:`\tau` (octahedral) - shear strain :math:`\gamma` (octahedral) nonlinearity is defined by a hyperbolic curve (backbone curve):

   .. math::

      \tau = \frac{G \gamma}{1 + \frac{\gamma}{\gamma_r}\left ( \frac{{p^t}_r}{p^t} \right)^d}

   where :math:`\gamma_r` satisfies the following equation at :math:`{p^t}_r`

   .. math::

      \tau_f = \frac{2 \sqrt{2} \sin \phi}{3 - \sin \phi}{p^t}_r + \frac{2 \sqrt{2}}{3}c = \frac{G_r \gamma_{max}}{1 + \gamma_{max}/\gamma_r}


3. (User defined surfaces) The user specified friction angle :math:`\phi = 0`. cohesion c will be ignored. Instead, c is defined by :math:`c=\sqrt 3 \sigma_m / 2`, where :math:`\sigma_m` is the product of the last modulus and strain pair in the modulus reduction curve. Therefore, it is important to adjust the backbone curve so as to render an appropriate c.

   If the user specifies :math:`\gamma` > 0, this :math:`\phi` will be ignored. Instead, :math:`\phi` is defined as follows:

   .. math::

      \sin \phi = \frac{3 (\sqrt 3 \sigma_m - 2c)/{p^t}_r}{6 + (\sqrt 3 \sigma_m - 2c)/{p^t}_r}


   If the resulting :math:`\phi <0`, we set :math:`\phi =0` and :math:`c=\sqrt 3 \sigma_m/2`.

   Also remember that improper modulus reduction curves can result in strain softening response (negative tangent shear modulus), which is not allowed in the current model formulation. Finally, note that the backbone curve varies with confinement, although the variation is small within commonly interested confinement ranges. Backbone curves at different confinements can be obtained using the OpenSees element recorder facility

4. ``presDependCoef``, :math:`d`, defines variations of :math:`G` and :math:`K` as a function of instantaneous effective confinement :math:`p^t` as follows:

   .. math::

      G = G_r \left ( \frac{p^t}{{p^t}_r} \right)^d

      K = B_r \left ( \frac{p^t}{{p^t}_r} \right)^d

5. If :math:`\phi = 0.0`, :math:`d` **is reset to 0.0**.


Output
======

The following information may be extracted for this material at a given integration point, using the OpenSees Element Recorder facility "stress", "strain", "backbone", or "tangent".

* For 2D problems, the stress output follows this order: :math:`\sigma_{xx}`, :math:`\sigma_{yy}`, :math:`\sigma_{zz}`, :math:`\sigma_{xy}`, :math:`\eta_r`, where :math:`\eta_r` is the ratio between the shear (deviatoric) stress and peak shear strength at the current confinement :math:`(0<=\eta_r<=1.0)`. The strain output follows this order: :math:`\epsilon_{xx}`, :math:`\epsilon_{yy}`, :math:`\epsilon_{xy}`

* For 3D problems, the stress output follows this order: :math:`\sigma_{xx}`, :math:`\sigma_{yy}`, :math:`\sigma_{zz}`, :math:`\sigma_{xy}`, :math:`\sigma_{yz}`, :math:`\sigma_{zx}`, :math:`\eta_r` and the strain output follows this order: :math:`\epsilon_{xx}`, :math:`\epsilon_{yy}`, :math:`\epsilon_{zz}`, :math:`\gamma_{xy}`, :math:`\gamma_{yz}`, :math:`\gamma_{zx}`

* The "backbone" option records (secant) shear modulus reduction curves at one or more given confinements. The specific recorder command is as follows:

  .. code::

     recorder Element –ele $eleNum -file $fName -dT $deltaT material $GaussNum backbone $p1 <$p2 …>

  where p1, p2, ... are the confinements at which modulus reduction curves are recorded. In the output file, corresponding to each given confinement there are two columns: shear strain γ and secant modulus Gs. The number of rows equals the number of yield surfaces.


Parameters
==========


.. tabs::
   .. tab:: SI Units
      .. csv-table::
         :header: "Parameters", "Soft Clay", "Medium Clay", "Stiff Clay"
         :widths: 20, 20, 20, 20

         rho, "1.3 ton/m3", "1.5 ton/m3", "1.8 ton/m3"
         Gr, "1.3x104 kPa", "6.0x104 kPa", "1.5x105 kPa"
         Br, "6.5x104 kPa", "3.0x105 kPa", "7.5x105 kPa"
         cohesi, "18 kPa", "37 kPa", "75 kPa "
         "es_max (at p’r=80 kPa)", 0.1 , 0.1, 0.1
         frictionAng, 	0, 	0,	0
         d, 0, 	0,	0

   .. tab:: US Units

      .. csv-table::
         :header: "Parameters", "Soft Clay", "Medium Clay", "Stiff Clay"
         :widths: 20, 20, 20, 20

         rho, "1.217x10-4(lbf)(s2)/in4", "1.404x10-4 (lbf)(s2)/in4", "1.685x10-4 (lbf)(s2)/in4"
         Gr, "1.885x103psi", "8.702x104psi", "2.176x104 psi"
         Br, "9.427x103psi", "4.351x104psi", "1.088x105psi"
         cohesi, "2.611psi", "5.366psi", "10.878psi"
         "es_max (at p’r=11.6 psi)", 0.1 , 0.1, 0.1
         frictionAng, 	0, 	0,	0
         d, 0, 	0,	0


Examples
========

.. ref-gallery::
   :maxdepth: 1
   :hidden:

   examples/soil/model-5101


References
==========

.. [R4] http://soilquake.net/ucsdsoilmodels/

Code Developed by: UC San Diego (**Dr. Zhaohui Yang**)
