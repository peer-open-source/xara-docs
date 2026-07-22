
.. _printA:

getTangent (``printA``)
***********************

The ``getTangent`` function, or ``printA`` in Tcl, is used to return system matrices like the stiffness or mass.

.. tabs::

   .. tab:: Python

      .. py:method:: Model.getTangent(m=0, c=0, k=1)

         Return the current tangent to the equilibrium residual.

         :param |float| m: factor with which to scale the inertial part of the tangent (default is ``0.0``).
         :param |float| c: factor with which to scale the damped part of the tangent (default is ``0.0``).
         :param |float| k: factor with which to scale the static part of the tangent (default is ``1.0``).
         :returns: A *numpy.array* representing the tangent matrix.

   .. tab:: Tcl

      .. function:: printA <-file $file> <-m $m> <-c $c> <-k $k>

      .. list-table:: 
         :widths: 10 10 40

         * - ``file``
           - *string*
           - file name to write tangent to.
         * - ``m``
           - |float|
           - factor with which to scale the inertial part of the tangent (default is ``0.0``; OpenSeesRT only).
         * - ``c``
           - |float|
           - factor with which to scale the damped part of the tangent (default is ``0.0``; OpenSeesRT only).
         * - ``k``
           - |float|
           - factor with which to scale the static part of the tangent (default is ``1.0``; OpenSeesRT only).


If using a static integrator, the resulting matrix is the *stiffness* matrix. If a
transient integrator, it will be some combination of mass and stiffness
matrices.


Examples
========

The following examples will return a matrix :math:`\mathbf{A}` that is given by a linear combination of 
the mass :math:`\mathbf{M}` and stiffness :math:`\mathbf{K}`:

.. math::

   \mathbf{A} = \frac{1}{2}\mathbf{M} + \frac{1}{10}\mathbf{K}


In Tcl:

.. code-block:: tcl

   printA -m 0.5 -k 0.1

and in Python with OpenSeesRT:

.. code-block:: python

   A = model.getTangent(m=0.5, k=0.1)



.. note::

   The full version of this command as documented above is supported from Python and Tcl
   through OpenSeesRT.
   In OpenSeesPy and older Tcl versions this command only works with the ``FullGeneral`` linear system,
   and the ``GimmeMCK`` integrator must be used to specify ``m`` ``c`` and ``k`` factors.
