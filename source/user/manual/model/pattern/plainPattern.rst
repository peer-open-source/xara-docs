.. _plainPattern:

Plain Pattern
^^^^^^^^^^^^^

Each *plain* load pattern is associated with a TimeSeries and can contain multiple NodalLoads, ElementalLoads and SP_Constraints.

.. tabs::

   .. tab:: Python 

      .. py:method:: Model.pattern("Plain", tag, series, loads={})

         :param tag: integer tag identifying the load pattern
         :param series: a string indicating a type, or an integer tag identifying a time series. This time series is used to determine the load factor applied to the loads in the pattern. Two common values for ``series`` are:  ``"Linear"`` and ``"Constant"``.
         :param loads: dict of loads to be added to the pattern


   .. tab:: Tcl

      .. function:: pattern Plain $tag $series <-fact $cFactor> {load commands}

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $patternTag, |integer|,   unique tag among load patterns
         $series, |integer|, the tag of the time series to be used in the load pattern
         $cFactor, |float|, constant factor (optional: default=1.0)


.. toctree::
   :maxdepth: 1
   :caption: load commands:

   PlainPatternloadcommands/load
   PlainPatternloadcommands/eleLoad
   PlainPatternloadcommands/sp


The loads (element, nodal, constraints) in a ``Plain`` Load pattern are **reference** loads. 
The actual load applied to a node or element is the product of the reference load, and a **load factor**. 
The *load factor* is obtained from the associated :ref:`timeSeries` as a function of the **time** in the domain.

It is common to use ``series="Linear"``, which results in a linear variation of the load factor with time.
Similarly, ``series="Constant"`` results in a constant load factor.


Example
-------

The following example defines a ``Plain`` load pattern which contains reference loads at nodes **3** and **4** with magnitudes **(0,-50)** and **(50.0, -100)** respectively. 
Because the series is ``"Linear"``, at each analysis step the actual load applied to the nodes is the product of the reference load and the current time in the domain.

.. tabs::

   .. tab:: Python

      .. code-block:: python

         model.pattern("Plain", 1, "Linear", loads={
            3: [ 0.0,  -50.0, 0.0],
            4: [50.0, -100.0, 0.0]
         })

   .. tab:: Tcl

      .. code-block:: tcl

         timeSeries Linear 2
         pattern Plain 1 "Linear" {
               load  3   0.0  -50.0  0.0
               load  4   50.0  -100.0 0.0
         }


Code Developed by: |fmk|
