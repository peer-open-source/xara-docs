
.. _HingeMidPoint-BeamIntegration:
   
===============
 HingeMidpoint
===============

.. py:method:: Model.beamIntegration('HingeMidpoint',tag,secI,lpI,secJ,lpJ,secE)
   :no-index:

   :param |integer| tag: Unique object tag.
   :param |integer| secI: A previous-defined :ref:`Section` for hinge at I.
   :param |float| lpI: The plastic hinge length at I.
   :param |integer| secJ: A previous-defined :ref:`Section` for hinge at J.
   :param |float| lpJ: The plastic hinge length at J.
   :param |integer| secE: A previous-defined :ref:`Section` for the element interior.

   Midpoint integration over each hinge region is the most accurate one-point integration rule;
   however, it does not place integration points at the element ends and there is a small integration
   error for linear curvature distributions along the element.

   The plastic hinge length at end I (J) is equal to ``lpI`` (``lpJ``) and the associated force deformation response is defined by the ``secI`` (``secJ``). The force deformation
   response of the element interior is defined by the ``secE``.
   Typically, the interior section is linear-elastic, but this is not necessary.


Example 
-------


.. code-block:: python

   lpI = 0.1
   lpJ = 0.2
   model.beamIntegration('HingeMidpoint',tag,secI,lpI,secJ,lpJ,secE)




