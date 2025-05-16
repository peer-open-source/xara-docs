.. _parameter:

parameter
^^^^^^^^^

.. py:method:: Model.parameter(tag, *args)

   define a paramemter in the model.

   :param tag: integer tag identifying the parameter.
   :type tag: |integer|
   :param args: arguments that idendify objects in the model which should bind to the parameter.


.. note::

   Each parameter tag must be unique, and all parameter tags must be numbered sequentially starting from 1.



Examples
---------

#. To identify the elastic modulus, E, of the material 1 at section 3 of element 4, the <specific object arguments> string becomes::
   
     model.parameter(1, 'element', 4, 'section', 3, 'material', 1, 'E')
   
#. To identify the elastic modulus, E, of elastic section 3 of element 4 (for elastic section, no specific material need to be defined), the <specific object arguments> string becomes::
   
     model.parameter(1, 'element', 4, 'section', 3, 'E')
   
#. To parameterize E for element 4 with material 1 (no section need to be defined), the <specific object arguments> string simplifies as::

     model.parameter(1, 'element', 4, 'material', 1, 'E')


