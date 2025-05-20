.. _UniaxialElastic:

Elastic 
^^^^^^^


.. py:method:: Model.uniaxialMaterial("Elastic", 1, E, eta=0)
   :no-index:



.. py:class:: Elastic
   :noindex:


   .. math::

       \sigma = E \varepsilon + \eta \dot{\varepsilon}

   .. py:attribute:: E
      :type: float

      Stiffness :math:`E`. Analogous to :py:attr:`J2.E`. 
    
   .. py:attribute:: eta
      :value: 0.0
      :type: float

