******
Manual
******

The :ref:`Model <modelClass>` class encapsulates a finite element analysis in OpenSees. 
The simplest way to create a model is by using its constructor:

.. code:: Python
   
   model = ops.Model(ndm=2, ndf=3)


Once a Model has been created, its `methods` are used to perform various operations. 
These are organized as follows:

1. :ref:`Modeling <modeling>` methods are used to add components to the finite element model.

2. :ref:`Analysis <lblAnalysisCommands>` methods are used to move the state of the model from one converged state to another via a number of trial steps.

3. The **Domain**, code that holds the current state and the last committed state of the finite element model.

4. :ref:`Output <output>` methods allow the user to obtain output from a finite element analysis, e.g. to record the node displacement history.


.. _command-manual:

.. toctree::
   :hidden:
   :maxdepth: 1   

   manual/modeling
   manual/analysisCommands
   manual/outputCommands
   manual/miscCommands



