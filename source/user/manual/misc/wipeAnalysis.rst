.. _wipeAnalysis:

wipeAnalysis
************


.. tabs::

   .. tab:: Python

      .. py:method:: Model.wipeAnalysis()
         
         Remove all the analysis objects. 

   .. tab:: Tcl

      .. function:: wipeAnalsyis;
         
         Remove all the analysis objects. 


This method is needed when the user wishes to switch from a static analysis to a transient analysis, e.g. when switching from the initial gravity load analysis to an analysis of the subsequent response due to earthquake loading.


.. note::

   * The time in the domain is not reset as in the :ref:`wipe`.
   * The state of the model does not change, i.e. the loads remain active and will change with subsequent analyze commands unless a :ref:`loadConst` is issued.



Examples
--------

The following demonstrates the use of the *wipeAnalysis* command.

1. **Tcl Code**

   .. code-block:: Tcl

      wipeAnalysis

2. **Python Code**

   .. code-block:: python

      model.wipeAnalysis()


Code Developed by: |fmk|

