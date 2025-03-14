.. _timeSeries:

Time Series
***********

A TimeSeries represents the relationship between the time in the domain, :math:`t`, and the load factor applied to the loads, :math:`\lambda`, in the load pattern with which the TimeSeries object is associated, i.e. :math:`\lambda = F(t)`.

.. tabs::

   .. tab:: Python

      .. py:method:: Model.timeSeries(type, tag, *args)
         
         :param type: type of time series
         :type type: |string|
         :param tag: unique time series tag.
         :type tag: |integer|
         :param args: a sequence of arguments that depend on type
   
   .. tab:: Tcl

      .. function:: timeSeries $type $tag $args ...

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $type, |string|,      type of time series
         $tag,  |integer|,     unique time series tag.
         $args, |list|,        a list of arguments with args depending on type


A TimeSeries may be one of the following types:

.. toctree::
   :maxdepth: 1

   timeseries/constantTimeSeries
   timeseries/linearTimeSeries
   timeseries/pathTimeSeries

..
   timeseries/trigTimeSeries
   timeseries/RampTimeSeries
   timeseries/triangleTimeSeries
   timeseries/rectangularTimeSeries
   timeseries/pulseTimeSeries
   timeseries/peerMotion
   timeseries/PeerNGAMotion
