.. _tcl-format:

Tcl
^^^

The Tcl scripting language is natively supported in |xara|. 
This page describes the built-in Tcl interpreter that can be executed from the command line to run ``.tcl`` scripts written for `OpenSees.exe`.
Other Tcl-related capabilities included with |xara| are documented here:

- Export Python simulations to Tcl using the :ref:`echo-file` feature.
- Import/Execute tcl scripts in Python using the :py:meth:`xara.Model.eval` method.



Command Line Options
--------------------

.. function:: python -m xara <file>

.. option:: <file>

   Specify the input file path for processing.

.. option:: -i, --interactive

   Enable interactive mode.


