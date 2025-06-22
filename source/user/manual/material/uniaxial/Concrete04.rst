.. _Concrete04:

Concrete04 -- (Popovics)
^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a uniaxial Popovics concrete material with degraded linear unloading/reloading stiffness according to the work of Karsan-Jirsa and tensile strength with exponential decay. 

.. function:: uniaxialMaterial Concrete04 $tag $fc $ec $ecu $Ec <$fct $et> <$beta>  

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $tag, |integer|, integer tag identifying material.
   $fc, |float|,  concrete compressive strength at 28 days (compression is negative)*.
   $ec, |float|, concrete strain at maximum strength*.
   $ecu, |float|, concrete crushing strength*.
   $Ec, |float|, initial stifness**.
   $fct, |float|, maximum tensile strength of concrete.
   $et, |float|, ultimate tensile strain of concrete.
   $beta, |float|, exponential curve parameter to define the residual stress (as a factor of $ft) at $etu. 



The envelope of the compressive stress-strain response is defined using the model proposed by [Popovic1973]_. 

.. math::

   \sigma(\varepsilon) &= f_{cp}\frac{(\varepsilon/\varepsilon_{cp})r}{r-1+(\varepsilon/\varepsilon_{cp})^r},

where :math:`r` is a parameter often computed from:

.. math::
   
   r =\frac{E_{c}}{E_{c}-\left(f_{c p} / \epsilon_{c p}\right)},


and :math:`E_c` is the Young's modulus of the concrete material. 

.. math::
   
   f_{c i}=f_c^{\prime}\left(\frac{\varepsilon_{c i}}{\varepsilon_c}\right) \frac{n}{n-1+\left(\frac{\varepsilon_{c i}}{\varepsilon_c}\right)^n}

If the user defines :math:`E_c = 57000 \sqrt(f_{cc})` (in units of *psi*) then the envelope curve is identical to that proposed by [Mander1988]_.
For loading in compression, the envelope to the stress-strain curve follows the model proposed by [Popovic1973]_ until the concrete crushing strength is achieved and also for strains beyond that corresponding to the crushing strength. 
For unloading and reloading in compression, the [Karsan1969]_ is used to determine the slope of the curve. 
For tensile loading, an exponential curve is used to define the envelope to the stress-strain curve. 

.. math::

   \sigma_{\dot{i}}=f_t\left(\frac{\beta f_t}{f_t}\right)^{\frac{\varepsilon_i-\frac{f_i}{E_s}}{\varepsilon_i-\frac{f_i}{E_e}}}

For unloading and reloading in tensile, the secant stiffness is used to define the path.


.. figure:: figures/Concrete04/Concrete04A.png
  :align: center
  :figclass: align-center


.. figure:: figures/Concrete04/Concrete04B.png
  :align: center
  :figclass: align-center


References 
----------


.. [Mander1988]  Mander, J. B., Priestley, M. J. N., and Park, R. (1988). "Theoretical stress-strain model for confined concrete." Journal of Structural Engineering ASCE, 114(8), 1804-1825.
.. [Popovic1973] Popovics, S. (1973). " A numerical approach to the complete stress strain curve for concrete." Cement and concrete research, 3(5), 583-599.
.. [Karsan1969]  Karsan, I. D., and Jirsa, J. O. (1969). "Behavior of concrete under compressive loading." Journal of Structural Division ASCE, 95(ST12).
.. [Eurocode2] EN 1992-1-1 2004. Eurocode 2: Design of Concrete Structures - Part 1-1: General rules and rules for buildings

Code Developed by: Laura Lowes, University of Washington and Michael Berry, University of Washington
Images Developed by Silvia Mazzoni
