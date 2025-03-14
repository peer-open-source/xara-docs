.. _linearTimeSeries:

Linear TimeSeries
^^^^^^^^^^^^^^^^^

This command is used to construct a TimeSeries object in which the load factor applied is linearly proportional to the time in the domain, i.e. :math:`\lambda = f(t) = \alpha t`.

.. figure:: figures/LinearTimeSeries.gif
	:align: center
	:figclass: align-center

	Linear Time Series

.. tabs::

   .. tab:: Python 

      .. py:method:: Model.timeSeries("Linear", tag, factor=1.0)
         :no-index:

         :param |integer| tag: unique tag among TimeSeries objects
         :param |float| factor: the linear factor (optional: default=1.0)

   .. tab:: Tcl

      .. function:: timeSeries Linear $tag <-factor $cFactor>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

            $tag, |integer|,	unique tag among TimeSeries objects
            $cFactor, |float|, the linear factor (optional: default=1.0)


Examples
--------

The following code demonstrates how user would create two linear time series, the first with tag **1** has a **1.0** factor, the second **2** has a constant load factor of **20.0**.

   1. **Tcl Code**

   .. code-block:: none

      timeSeries Linear 1
      timeSeries Linear 2 -factor 20.0


   2. **Python Code**

   .. code-block:: python

      model.timeSeries('Linear',  1)
      model.timeSeries('Linear',  2, factor=20.0)


Code Developed by: **fmk**

