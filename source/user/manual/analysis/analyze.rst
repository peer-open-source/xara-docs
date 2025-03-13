.. _analyze:


analyze
^^^^^^^

This command is used to perform the analysis. 
It returns a value indicating success or failure of the analysis. 

.. tabs::
   
   .. tab:: Python

      .. function:: model.analyze(n, **options)

         :param n: number of analysis steps to perform.
         :type n: |integer|
         :param dt: time-step increment. Required if transient or variable transient analysis
         :type dt: |float|
         :param dtMin: minimum time step. Required if a variable time step transient analysis was specified.
         :type dtMin: |float|
         :param dtMax: maximum time step. Required if a variable time step transient analysis was specified.
         :type dtMax: |float|
         :param Jd: number of iterations user would like performed at each step. The variable transient analysis will change current time step if last analysis step took more or less iterations than this to converge. Required if a variable time step transient analysis was specified.
         :type Jd: |integer|

   .. tab:: Tcl

      .. function:: analyze $n <$dt> <$dtMin $dtMax $Jd>


.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   ``n``, |integer|,	number of analysis steps to perform.
   ``dt``, |float|, time-step increment. Required if transient or variable transient analysis
   ``dtMin`` ``dtMax``, |float|, minimum and maximum time steps. Required if a variable time step transient analysis was specified.
   ``Jd``, |integer|, number of iterations user would like performed at each step. The variable transient analysis will change current time step if last analysis step took more or less iterations than this to converge. Required if a variable time step transient analysis was specified.


The function returns an integer value indicating the success or failure of the analysis:

* ``0`` if successful

* ``< 0`` if not successful


Examples
-------- 

The following example shows how to construct a Static analysis.

.. tabs::
   
   .. tab:: Python

      .. code:: python

         model.system("SuperLU")
         model.constraints("Transformation")
         model.numberer("RCM")
         model.test("NormDispIncr", 1.0e-12, 10, 3)
         model.algorithm("Newton")
         model.integrator("LoadControl", 0.1)
         model.analysis("Static")
         ok = model.analyze(10)

   .. tab:: Tcl

      .. code:: tcl

         system SuperLU
         constraints Transformation
         numberer RCM
         test NormDispIncr 1.0e-12  10 3
         algorithm Newton
         integrator LoadControl 0.1
         analysis Static
         set ok [analyze 10]


The following example shows how to construct a Transient analysis.

.. tabs::
   .. tab:: Python

      .. code:: python

         model.system("SuperLU")
         model.constraints("Transformation")
         model.numberer("RCM")
         model.test("NormDispIncr",1.0e-12, 10, 3)
         model.algorithm("Newton")
         model.integrator("Newmark", 0.5, 0.25)
         model.analysis("Transient")
         ok = model.analyze(2000, 0.02)

   .. tab:: Tcl

      .. code:: tcl

         system SuperLU
         constraints Transformation
         numberer RCM
         test NormDispIncr 1.0e-12  10 3
         algorithm Newton
         integrator Newmark 0.5 0.25
         analysis Transient -numSubLevels 3  -numSubSteps 10
         set ok [analyze 2000 0.02]



Code Developed by: |fmk|
