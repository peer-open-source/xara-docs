Interpreters
^^^^^^^^^^^^

.. toctree::
   :maxdepth: 3
   :hidden:

   python
   openseespy
   tcl
   parallel


There are several ways to use the `xara` package:

- The :ref:`standard way <xara-python>` to use `xara` is to import it into your Python script and create an instance of the :py:class:`xara.Model` class. 

- To execute Tcl procedures from a Python script, just create an instance
  of the :py:class:`xara.Model` class and call its :py:meth:`xara.Model.eval` method:

  .. code-block:: Python
     
     model = xara.Model()
     model.eval("model Basic -ndm 2")
     model.eval("node 1 0.0 0.0")


- To start an :ref:`interactive interpreter <tcl-shell>` run the shell command:

  .. code-block:: bash
     
     python -m xara



- The `xara` package exposes a compatibility layer that exactly reproduces
  the :ref:`OpenSeesPy <OpenSeesPy>` functions, but does so without mandating a single
  global program state. To run OpenSeesPy scripts, just change the import:

  .. code-block:: Python
     
     import openseespy.opensees

  to

  .. code-block:: Python
        
     import opensees.openseespy
