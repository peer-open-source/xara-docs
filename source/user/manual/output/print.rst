.. print_

``print``
^^^^^^^^^


.. tabs::

   .. tab:: Python
      
      .. py:method:: Model.print([node, ele])
         
         Print information about a :class:`Model` to *stdout*, or a file.
   
   .. tab:: Tcl
      
      .. function:: print <-file $fileName> [-node|-ele] <-flag $flag > {*}$tags
  
         $fileName    (optional) name of file to which data will be sent. overwrites existing file. default is to print to stderr)
         $flag	     integer flag to be sent to the print() method, depending on the node and element type (optional)
         $node1 $node2 ..     (optional) integer tags of nodes to be printed. default is to print all.
         $ele1 $ele2 ..	     (optional) integer tags of elements to be printed. default is to print all.




Examples
--------

.. code:: tcl

   print -ele; # print all elements

   print -node 1 2 3; # print data for nodes 1,2 & 3

.. code:: Python

   model.print(ele=True)  # print all elements

   model.print(node=(1, 2, 3))  # print data for nodes 1,2 & 3

