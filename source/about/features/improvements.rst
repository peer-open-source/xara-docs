Features 
^^^^^^^^

Xara offers several advanced features that make it a powerful tool for nonlinear finite element analysis:

- **Mixed Formulations**: It supports mixed formulations for beams and solids, enabling accurate modeling of complex structural systems.
- **Extensive Material Models**: With over 200 material models, Xara provides flexibility for simulating various materials and their nonlinear behaviors.
- **Continuation Algorithms**: These algorithms are designed to solve highly nonlinear problems efficiently, making Xara suitable for challenging engineering scenarios.
- **Stateless Modeling**: Xara introduces a `Model` class for true stateless modeling, allowing users to work without relying on a single global program state.
- **Compatibility Layer**: It reproduces OpenSeesPy functions, ensuring seamless integration for users familiar with the OpenSees ecosystem.
- **Performance Optimization**: Built on the OpenSeesRT framework, Xara delivers substantial performance improvements over traditional interpreters.


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


