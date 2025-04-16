Steel
^^^^^

.. tabs::

   .. tab:: Python 
          
        .. py:method:: Model.uniaxialMaterial('Steel', tag, E, Y, Hiso, Hkin, eta=None)
            :no-index:
    
            :param |integer| tag: unique tag identifying material
            :param |float| E: elastic modulus
            :param |float| Y: yield stress
            :param |float| Hiso: isotropic hardening modulus
            :param |float| Hkin: kinematic hardening modulus
            :param |float| eta: optional parameter 

Examples 
--------


.. tabs::

   .. tab:: Python
      
      .. code-block:: Python

         import xara
         model = xara.Model(ndm=3)

         Y  = 50
         E  = 29e3
         G  = 11.2e3
         K  = 3
         nu = 0.24

         Hiso = 20e3
         Hkin = 10e3

         # All positional arguments
         model.uniaxialMaterial("Steel", 1, E, Y, Hiso, Hkin)

         # Mix keywords and positional arguments
         model.uniaxialMaterial("Steel", 2, E, Y, Hiso=Hiso, Hkin=Hkin)

         # All keyword arguments
         model.uniaxialMaterial("Steel", 4, Y=Y, E=E, Hkin=Hkin, Hiso=Hiso)
         model.uniaxialMaterial("Steel", 5, Y=Y, G=G, nu=nu, Hkin=Hkin, Hiso=Hiso)

         # Legacy
         model.uniaxialMaterial("Hardening", 9, E, Y, Hiso, Hkin)

         model.print(json=True)


   .. tab:: Tcl 
      
      .. code-block:: Tcl 

        model BasicBuilder -ndm 3 -ndf 6

        set Y 50
        set E 29e3
        set G 11.2e3
        set nu 0.24

        set Hiso 20e3
        set Hkin 10e3

        # All positional arguments
        uniaxialMaterial Steel 1 $E $Y $Hiso $Hkin

        # Mix keywords and positional arguments
        uniaxialMaterial Steel 2 $E $Y -Hiso $Hiso -Hkin $Hkin
        uniaxialMaterial Steel 3 -Hiso $Hiso -Hkin $Hkin $E $Y

        # All keyword arguments
        uniaxialMaterial Steel 4 -Y $Y -E $E -Hkin $Hkin -Hiso $Hiso
        uniaxialMaterial Steel 5 -Y $Y -G $G -nu $nu -Hkin $Hkin -Hiso $Hiso

        # Legacy
        uniaxialMaterial Hardening 9 $E $Y $Hiso $Hkin

        print -json
