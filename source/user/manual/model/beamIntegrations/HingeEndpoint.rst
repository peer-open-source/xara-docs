

HingeEndpoint
^^^^^^^^^^^^^

.. py:method:: Model.beamIntegration("HingeEndpoint",tag,secI,lpI,secJ,lpJ,secE)
   :noindex:

   :param |integer| tag: Unique object tag.
   :param |integer| secI: A previous-defined :ref:`Section` for hinge at I.
   :param |float| lpI: The plastic hinge length at I.
   :param |integer| secJ: A previous-defined :ref:`Section` for hinge at J.
   :param |float| lpJ: The plastic hinge length at J.
   :param |integer| secE: A previous-defined :ref:`Section` for the element interior.

   Endpoint integration over each hinge region moves the integration points to the element ends;
   however, there is a large integration error for linear curvature distributions along the element.

   Arguments and examples see :ref:`HingeMidPoint-BeamIntegration`.

