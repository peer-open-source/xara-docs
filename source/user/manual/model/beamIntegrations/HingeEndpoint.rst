
===============
 HingeEndpoint
===============

.. function:: beamIntegration('HingeEndpoint',tag,secI,lpI,secJ,lpJ,secE)
   :noindex:

   Endpoint integration over each hinge region moves the integration points to the element ends;
   however, there is a large integration error for linear curvature distributions along the element.

   ========================   ============================================================================
   ``tag`` |integer|              tag of the beam integration.
   ``secI`` |integer|             A previous-defined section object for hinge at I.
   ``lpI`` |float|            The plastic hinge length at I.
   ``secJ`` |integer|             A previous-defined section object for hinge at J.
   ``lpJ`` |float|            The plastic hinge length at J.
   ``secE`` |integer|             A previous-defined section object for the element interior.
   ========================   ============================================================================

   Arguments and examples see :ref:`HingeMidPoint-BeamIntegration`.

