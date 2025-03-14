.. _wipe:

``wipe``
^^^^^^^^

This command is used to clear the domain objects, the recorders, and any analysis objects. 
It resets the time in the **Domain** to **0.0**.

.. tabs::

   .. tab:: Python 
      .. py:method:: Model.wipe()

         Remove all objects in the model.
   
   .. tab:: Tcl

      .. function:: wipe;

         Remove all objects in the model.

This command is used to start over without having to exit and restart the interpreter. This is useful for example if you want to subject the model to multiple ground motions or subject different models to the same ground motion! It causes all elements, nodes, constraints, loads to be removed from the domain. In addition it deletes all recorders, analysis objects and all material objects created by the model builder. 

.. deprecated:: 3.0.3

   The `wipe` method is deprecated for Python and may be removed in future versions.


Examples
--------

The following example demonstrates the use of the wipe command.

   1. **Tcl Code**

   .. code-block:: none

      wipe

   2. **Python Code**

   .. code-block:: python

      model.wipe()


Code Developed by: |fmk|
