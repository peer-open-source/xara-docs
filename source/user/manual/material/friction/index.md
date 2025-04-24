# Friction

The `frictionModel` command is used to construct a friction model
object, which specifies the behavior of the coefficient of friction in
terms of the absolute sliding velocity and the pressure on the contact
area. The command has at least one argument, the friction model type.
Each type is outlined below.

```tcl
frictionModel frnMdlType? arg1? ...
```

<hr />
The type of friction model created and the additional arguments
required depend on the <strong>frnMdlType?</strong> provided in the
command.

The following contain information about `type` and the args
required for each of the available friction model types:

```{eval-rst}
.. toctree::
   :maxdepth: 1

   108-Coulomb Friction
   401-Multi-Linear Velocity Dependent Friction
   744-Velocity Dependent Friction
   745-Velocity and Normal Force Dependent Friction
   746-Velocity and Pressure Dependent Friction
```

<hr />

The following friction model response quantities can be recorded
through the ElementRecorder object, as long as the element has a
friction model associated with it:

- `normalForce`,
- `velocity`, 
- `frictionForce`,
- **COF**

## Examples

```tcl
recorder Element -file Elmt.out -time -ele 1 frictionModel normalForce
```


## Used In

<ul>
<li><a
href="http://opensees.berkeley.edu/wiki/index.php/Flat_Slider_Bearing_Element">Flat
Slider Bearing Element</a></li>
<li><a
href="http://opensees.berkeley.edu/wiki/index.php/Single_Friction_Pendulum_Bearing_Element">Single
Friction Pendulum Bearing Element</a></li>
<li><a
href="http://opensees.berkeley.edu/wiki/index.php/Triple_Friction_Pendulum_Element">Triple
Friction Pendulum Bearing Element</a></li>
</ul>
