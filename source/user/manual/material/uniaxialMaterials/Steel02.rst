.. _steel02:

Steel02
^^^^^^^

*Steel02* is a uniaxial material based on the Giuffre-Menegotto-Pinto formulation with added isotropic strain hardening by [FilippouEtAl1983]_.

.. tabs::
   
   .. tab:: Python 

      .. py:method:: Model.uniaxialMaterial("Steel02", tag, fy, E0, b, R0, cR1, cR2, [a1, a2, a3, a4, sigInit])
         :no-index:

         Add a *Steel02* material to *model* identified by *tag*.


   .. tab:: Tcl

      .. function:: uniaxialMaterial Steel02 $tag $Fy $E $b $R0 $cR1 $cR2 <$a1 $a2 $a3 $a4 $sigInit>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   tag, |integer|,	    integer tag identifying material
   fy, |float|, yield strength
   E0, |float|, initial elastic tangent
   b, |float|, strain-hardening ratio (ratio between post-yield tangent and initial elastic tangent)
   R0 CR1 CR2, 3 |float|, parameters to control the transition from elastic to plastic branches.
   a1, |float|, isotropic hardening parameter. (optional: default = 0.0). see note. 
   a2, |float|, isotropic hardening parameter (optional: default = 1.0). see note.
   a3, |float|, isotropic hardening parameter. (optional: default = 0.0). see note.
   a4, |float|, isotropic hardening parameter. (optional: default = 1.0). see note.
   sigInit, |float|, Initial Stress Value (optional: default = 0.0) 



The hardening formulation was developed by [FilippouEtAl1983]_.
The parameters ``a1`` and ``a2`` increase of compression yield envelope as proportion of yield strength after a plastic strain of :math:`a_2 f_y/E_0`. 

The parameters ``a3`` and ``a4`` increase of tension yield envelope as proportion of yield strength after a plastic strain of $a4*($Fy/E0). 

Recommended values: ``R0`` between 10 and 20, ``cR1=0.925``, ``cR2=0.15``

If ``siginit`` is specified, strain is calculated from epsP=$sigInit/$E

.. code:: c++

  if (sigInit!= 0.0)
     this->eps = trialStrain + sigInit/E; 
  else
     this->eps = trialStrain;


.. _fig-steel02:

.. figure:: figures/Steel02/Steel02Monotonic.jpg
	:align: center
	:figclass: align-center

	Steel02 Material -- Material Parameters of Monotonic Envelope


.. figure:: figures/Steel02/Steel02HystereticA.jpg
	:align: center
	:figclass: align-center

	Steel02 Material -- Default Hysteretic Behavior (NO isotropic hardening)


Example 
-------

The following is used to construct a Steel02 mataerial with a tag of ``1``, a yield strength of **60.0** and an initial tangent stiffness of **30000,0**.

.. tabs::

   .. tab:: Python

      .. code:: python

         model.uniaxialMaterial('Steel02',1, 60.0, 30000.0, 0.1, 20.0, .925, .15)
   
   .. tab:: Tcl
      
      .. code:: tcl

         uniaxialMaterial Steel02 1 60.0 30000.0 0.1 20.0 .925 .15


References
----------

.. [FilippouEtAl1983] Filippou, F. C., Popov, E. P., Bertero, V. V. (1983). "Effects of Bond Deterioration on Hysteretic Behavior of Reinforced Concrete Joints". Report EERC 83-19, Earthquake Engineering Research Center, University of California, Berkeley.


Code Developed by: |mhs|, |fcf|

