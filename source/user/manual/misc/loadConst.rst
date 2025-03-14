.. _loadConst:

loadConst
*********

.. tabs::

   .. tab:: Python 

      .. py:method:: Model.loadConst([time])
         
         Set the loads constant in the domain and also set the time in the domain.

         :param time: Time domain is to be set to (optional)
         :type time: |float|

   .. tab:: Tcl
         
      .. function::  loadConst <-time $time>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $time, |float|, Time domain is to be set to (optional)


This command is used to set the loads constant in the domain and to also set the time in the domain. 

.. note::
   
   Load Patterns added afer this command is invoked are not set to constant.


Example
-------

The following examples demonstrate the command to set the loads constant and to also rest the time to 0.0, which is the most common use of the command.

1. **Tcl Code**

   .. code-block:: tcl

      loadConst -time 0.0

2. **Python Code**

   .. code-block:: python

      model.loadConst(time=0.0)

Code Developed by: |fmk|
