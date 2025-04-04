Additions
^^^^^^^^^



- Unlike other Python packages which merely wrap the broken OpenSeesPy package, *xara* employs a completely new interface layer that is implemented in C++.

- The *xara* package is designed to be a drop-in replacement for the OpenSeesPy package.
- improved `printA`:
  - does not require `FullGen` solver; now all one needs
    to do is call `model.getTangent()`. This is possible due to the
    new consolidated memory ownership model.
  - `-mck` options


- improved `print` command
  - new `-registry` option.
  - more reliable JSON printing
  - includes `MP_Constraint` information

- add `-det` option to static integrators:
  - ArcLength, ...

- add `-det` capability to solvers:
  - `FullGenLapack`, `Umfpack`, `BandGenLapack`

- Verbosity control

- new `export` command in Python and Tcl, when run through Python
- new `getTangent()` method in Python
- new `invoke` Tcl command and Python constructs
- new `progress` command in Tcl
- new `=` command, fixes vexing operator precedence in `expr`

- Minimized use of ``exit()`` syscalls.


Quality of Life
---------------

*xara* features several small "quality of life" improvements. These include

* Improved error messages and tracebacks. Error messages have been extensively reworked to allow for colorful and informative error tracebacks. 
  For example, instead of:

  ... code-block::

      Bad

  one now has:

  ... code-block::

      Better

* Improved log messages (TODO: Example 5)


