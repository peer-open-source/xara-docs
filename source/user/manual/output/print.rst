.. _print:

print
^^^^^


.. tabs::

   .. tab:: Python
      
      .. py:method:: Model.print([file, node, ele])
         
         Print information about a :class:`Model` to *stdout*, or a file.

         :param file: The name of the file to which data will be sent. Overwrites existing file. Default is to print to *stdout*.
         :param node: :ref:`Node` tags to print. Default is to print all nodes.
         :type node: |integerTuple|
         :param ele: :ref:`Element` tags to print. Default is to print all elements.
         :type ele: |integerTuple|

   
   .. tab:: Tcl
      
      .. function:: print <-file $fileName> [-node|-ele] <-flag $flag > {*}$tags
  
         fileName    (optional) name of file to which data will be sent. overwrites existing file. default is to print to stderr)
         flag	     integer flag to be sent to the print() method, depending on the node and element type (optional)
         tags  (optional) integer tags of nodes or elements to be printed. default is to print all.




Examples
--------

.. code:: tcl

   print -ele; # print all elements

   print -node 1 2 3; # print data for nodes 1,2 & 3

.. code:: Python

   model.print(ele=True)  # print all elements

   model.print(node=(1, 2, 3))  # print data for nodes 1,2 & 3

