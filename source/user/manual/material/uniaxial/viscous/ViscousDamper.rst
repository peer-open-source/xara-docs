

F = K*u_s = C*pow(V_d,alpha)


Variables:
$K: Elastic stiffness of linear spring (to model the axial flexibility of a viscous damper (brace and damper portion)
$C: Viscous damping coefficient of the damper
$Alpha: Viscous damper exponent
$LGap: gap length to simulate the gap length due to the pin tolerance
$NM:	Employed adaptive numerical algorithm (default value NM = 1; 1 = Dormand-Prince54, 2=6th order Adams-Bashforth-Moulton, 3=modified Rosenbrock Triple)
$RelTol:	Tolerance for absolute relative error control of the adaptive iterative algorithm (default value 10^-6)
$AbsTol:	Tolerance for absolute error control of adaptive iterative algorithm (default value 10^-6)
$MaxHalf: Maximum number of sub-step iterations within an integration step, h=dt*(0.5)^MaxHalf (default value 15)




References
----------

* Akcelyan, S., and Lignos, D.G. (2015), “Adaptive Numerical Method Algorithms for Nonlinear Viscous and Bilinear Oil Damper Models Under Random Vibrations”, ASCE Journal of Engineering Mechanics, (under review)
* Kasai K, Oohara K. (2001). “Algorithm and Computer Code To Simulate Response of Nonlinear Viscous Damper”. Proceedings Passively Controlled Structure Symposium 2001, Yokohama, Japan.