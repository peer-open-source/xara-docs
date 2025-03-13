
===========
 UserHinge
===========

.. py:function:: model.beamIntegration("UserHinge",tag,secETag,npL, secsLTags, locsL, wtsL,npR, secsRTags, locsR, wtsR)
   :noindex:

   Create a UserHinge beamIntegration.

   ========================   ============================================================================
   ``tag`` |integer|              tag of the beam integration
   ``secE`` |integer|             A previous-defined section tags for element interior
   ``npI`` |integer|              number of integration points along the hinge at end I
   ``secsI`` |integerList|          A list of previous-defined section tags for hinge at end I
   ``locsI`` |floatList|          A list of locations of integration points for hinge at end I
   ``wtsI`` |floatList|           A list of weights of integration points for hinge at end I
   ``npJ`` |integer|              number of integration points along the hinge at end J
   ``secsJ`` |integerList|          A list of previous-defined section tags for hinge at end J
   ``locsJ`` |floatList|          A list of locations of integration points for hinge at end J
   ``wtsJ`` |floatList|           A list of weights of integration points for hinge at end J
   ========================   ============================================================================

Examples
--------

 .. code-block:: Python

    tag = 1
    secE = 5

    npI = 2
    secsI = [1,2]
    locsI = [0.1,0.2]
    wtsI = [0.1,0.05]

    npJ = 2
    secsJ = [3,4]
    locsJ = [0.8,0.9]
    wtsJ = [0.05,0.1]

    model.beamIntegration("UserHinge",tag,secE,npI, secsI, locsI, wtsI,npJ, secsJ, locsJ, wtsJ)





