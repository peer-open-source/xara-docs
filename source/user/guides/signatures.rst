Guide to Docs
^^^^^^^^^^^^^


.. _kwd-star:

Keyword-Only Arguments
----------------------

In the documentation of a function, a ``*`` separator indicates that all arguments following it must be supplied in keyword form.
For example, 


.. py:method:: Model.element("ForceFrame", tag, nodes, *, section, transform)
    :no-index:

This indicates that the arguments ``section`` and ``transform`` must be supplied as keyword arguments.
For example:

.. code-block:: python

    # Correct
    Model.element("ForceFrame", 1, (1, 2), section=section, transform=transform)
    # Incorrect
    Model.element("ForceFrame", 1, (1, 2), section, transform)



.. _kwds:

Keyword Arguments
-----------------

It is common to see the argument ``**kwds`` in Python function signatures.
This is a way to pass a variable number of keyword arguments to a function.

