Overview
===============

*xara* is a free and open source tool for simulating the nonlinear response of structural and geotechnical systems. 
*xara* is developed by PEER as an alternative front-end to the simulation framework proposed by :ref:`McKenna (1997) <references>`.
The design of the interface was guided by the demands of the |BRACE2| project, for which a suitably *reliable* and *performant* solution was not available.


.. toctree::
   :hidden:

   self

.. _user-manual:

The :ref:`Model <modelClass>` class encapsulates a finite element analysis with *xara*. 
The simplest way to create a model is by using its constructor:

.. code:: Python
   
   import xara
   model = xara.Model(ndm=2, ndf=3)


Once a Model has been created, its `methods` are used to perform various operations. 
Documentation of these methods is organized as follows:

* :ref:`Modeling <modeling>` methods are used to add components to the finite element model.
* :ref:`Analysis <lblAnalysisCommands>` methods are used to move the state of the model from one converged state to another via a number of trial steps.
* :ref:`Output <output>` methods allow one to obtain output from a finite element analysis, e.g. to record the node displacement history.


.. toctree::
   :caption: Documentation
   :maxdepth: 1
   :hidden:

   user/manual/modeling
   user/manual/meshing/index
   user/manual/analysis/index
   user/manual/output/index
   user/manual/misc/index
   user/manual/modules/index
   Examples <https://gallery.stairlab.io/examples/>



.. toctree::
   :caption: About
   :maxdepth: 1
   :hidden:

   user/guides/index
   about/compatibility/index
   about/license
   about/references
   cite

