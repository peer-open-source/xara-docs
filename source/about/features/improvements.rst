Additions
^^^^^^^^^

Unlike other Python packages which merely wrap the broken OpenSeesPy package, *xara* employs a completely new interface layer that is implemented in C++.

- Improved :ref:`<printA>` for obtaining structural matrices:

  - does not require `FullGen` solver; now all one needs
    to do is call `model.getTangent()`. This is possible due to the
    new consolidated memory ownership model.

  - `-mck` options


- Improved `print` command

  - new `-registry` option.
  - more reliable JSON printing
  - includes `MP_Constraint` information

- Add `-det` option to static integrators:

  - :ref:`ArcLength`

- add `-det` capability to solvers:

  - `FullGenLapack`, `Umfpack`, `BandGenLapack`

- Verbosity control

- new `export` command in Python and Tcl, when run through Python
- new `invoke` Tcl command and Python constructs
- new `progress` command in Tcl
- new `=` command, fixes vexing operator precedence in `expr`

- Minimized use of ``exit()`` syscalls.


Quality of Life
---------------

*xara* features several small "quality of life" improvements. These include

* Improved error messages and tracebacks. Error messages have been extensively reworked to allow for colorful and informative error tracebacks. 
  For example, instead of:

  .. figure:: figures/upstream-output.png
     :width: 100%
     :align: center

  one now has:

  .. figure:: figures/xara-output.png
     :width: 100%
     :align: center

..
  * Improved log messages (TODO: Example 5)


