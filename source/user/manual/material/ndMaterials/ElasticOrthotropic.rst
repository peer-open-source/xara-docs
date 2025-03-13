.. _ElasticOrthotropic:

Elastic Orthotropic
^^^^^^^^^^^^^^^^^^^

.. function:: nDMaterial ElasticOrthotropic $matTag $Ex $Ey $Ez $vxy $vyz $vzx $Gxy $Gyz $Gzx <$rho>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, unique tag identifying material
   $Ex $Ey $Ez, 3 |float|, elastic moduli in three mutually perpendicular directions
   $vxy $vyz $vzx, 3 |float|, Poisson's ratios
   $Gxy $Gyz $Gzx, 3 |float|, shear moduli
   $rho, |float|, mass density. optional default = 0.0


The material formulations for the ElasticOrthotropic object are "ThreeDimensional", "PlaneStrain", "Plane Stress", "AxiSymmetric", "BeamFiber", and "PlateFiber".

.. math::

  \mathbf{C}^{-1} = \left[\begin{array}{cccccc}
  \frac{1}{E_1} & -\frac{\nu_{21}}{E_2} & -\frac{\nu_{31}}{E_3} & 0 & 0 & 0 \\
  -\frac{\nu_{12}}{E_1} & \frac{1}{E_2} & -\frac{\nu_{32}}{E_3} & 0 & 0 & 0 \\
  -\frac{\nu_{13}}{E_1} & -\frac{\nu_{23}}{E_2} & \frac{1}{E_3} & 0 & 0 & 0 \\
  0 & 0 & 0 & \frac{1}{G_{23}} & 0 & 0 \\
  0 & 0 & 0 & 0 & \frac{1}{G_{31}} & 0 \\
  0 & 0 & 0 & 0 & 0 & \frac{1}{G_{12}}
  \end{array}\right]

with

.. math::

   E_1>0, E_2>0, E_3>0, G_{12}>0, G_{23}>0, G_{13}>0


Code Developed by: |mhs|

