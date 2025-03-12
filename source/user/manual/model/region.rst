.. _region:

Region
------

The region command is used to label a group of nodes and elements.
This command is also used to assign rayleigh damping parameters to the
nodes and elements in this region. The region is specified by either
elements or nodes, not both. 
If elements are defined, the region
includes these elements and the all connected nodes, unless the ``-eleOnly``
option is used in which case only elements are included. If nodes are
specified, the region includes these nodes and all elements of which all
nodes are prescribed to be in the region, unless the ``-nodeOnly`` option is
used in which case only the nodes are included.

