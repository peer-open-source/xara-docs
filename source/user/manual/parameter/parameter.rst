.. _parameter:

parameter
^^^^^^^^^

.. py:method:: Model.parameter(tag, <specific parameter args>)

   define a paramemter in the model.

   ==============================   ===========================================================================
   ``tag`` |int|                    integer tag identifying the parameter.
   ``<specific parameter args>``    depend on the object in the FE model encapsulating the desired parameters.
   ==============================   ===========================================================================


.. note::

   Each parameter must be unique, and all parameter tags must be numbered sequentially starting from 1.



The format of the *<specific object arguments>* is different for each considered element/section/material. 


Examples
---------

#. To identify the elastic modulus, E, of the material 1 at section 3 of element 4, the <specific object arguments> string becomes::
   
     model.parameter(1, 'element', 4, 'section', 3, 'material', 1, 'E')
   
#. To identify the elastic modulus, E, of elastic section 3 of element 4 (for elastic section, no specific material need to be defined), the <specific object arguments> string becomes::
   
     model.parameter(1, 'element', 4, 'section', 3, 'E')
   
#. To parameterize E for element 4 with material 1 (no section need to be defined), the <specific object arguments> string simplifies as::

     model.parameter(1, 'element', 4, 'material', 1, 'E')


