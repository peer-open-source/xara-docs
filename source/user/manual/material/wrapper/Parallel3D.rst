.. _Parallel3D:

Parallel3D
^^^^^^^^^^

This command is used to construct a Parallel3D material. 
It is a wrapper that imposes an iso-strain condition to an arbitrary number of previously-defined 3D nDMaterial objects. 
Therefore, in each sub-material the strains are equal, the parallel stress and tangent are equal to the (weighted) sum of those of the sub-materials.

.. tabs::
   .. tab:: Python

      .. py:class:: xara.MultiaxialMaterial("Parallel3D", tags, weights=None)
         :no-index:

         Construct a Parallel3D material wrapper.

         :param tag: integer tag identifying this parallel material wrapper
         :param tags: integer tags identifying previously defined nD materials
         :param weights: list of weight factors, optional. If not defined, they will be assumed all equal to 1
   
   .. tab:: Tcl

      .. function:: nDMaterial Parallel3D $tag    $tag1 $tag2 ... $tagN   <-weights $w1 $w2 ... $wN>


      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|, "unique tag identifying this series material wrapper"
         $tag1 $tag2 ... $tagN, N |integer|, "unique tags identifying previously defined nD materials"
         $w1 $w2 ... $wN, N |float|, "weight factors, optional. If not defined, they will be assumed all equal to 1"


Notes
"""""

.. admonition:: Responses

   * All responses available for the nDMaterial object: **stress** (or **stresses**), **strain** (or **strains**), **tangent** (or **Tangent**), **TempAndElong**.
   * **material** **$matId** ... : use the **material** keyword followed by the 1-based index of the sub-material (and followed by the desired response) to forward the request to the matId sub-material.
   * **homogenized** ... : use the **homogenized** keyword followed by the desired response to forward the request to all sub-materials, and to compute its weighted average.

Examples
""""""""

.. ref-gallery::

   examples/material/material-0031


Code Developed by: **Massimo Petracca** at ASDEA Software, Italy.
