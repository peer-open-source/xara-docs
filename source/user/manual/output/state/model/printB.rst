.. _getResidual:

getResidual
^^^^^^^^^^^

.. tabs::
   
   .. tab:: Python

      .. py:method:: Model.getResidual()
      
         Return the residual vector from the last iteration.

         :returns: A list containing the residual vector.

   .. tab:: Tcl

      .. function:: printB;

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40
       
         $residual, |list|,  the residual vector


.. note::

   The specific form of the residual is documented in the pages for :ref:`Static <StaticAnalysis>` and
   :ref:`Transient <TransientAnalysis>`, respectively.


Example
-------

The following example is used to set the variable **residual** equal to the residual vector from the last iteration.

.. tabs::
   
   .. tab:: Python 

      .. code-block:: python

         residual = model.getResidual()

   .. tab:: Tcl
    
      .. code-block:: tcl

         set residual [getResidual]
