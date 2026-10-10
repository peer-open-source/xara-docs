.. _PlasticFrame:

PlasticFrame
^^^^^^^^^^^^

Two-node frame finite element with plastic hinge behavior.



The N-Mz-My interaction surface is described by a polynomial

.. math::

   f(n,mz,my) = \sum_i d_i \; n^{a_i} \; m_z^{b_i} \; m_y^{c_i}

where n = N/Np, mz = Mz/Mpz and my = My/Mpy

a,b,c,d = polynomial coefficients in array GPYSC according to the scheme

.. math::

    GPYSC = \begin{bmatrix}
                 d1 & a1 & b1 & c1 \\
                 d2 & a2 & b2 & c2 \\
                 d3 & a3 & b3 & c3 \\
               ...         \\
    \end{bmatrix}

e.g. if 

.. math::

    GPYSC = \begin{bmatrix}
                 1  & 2 &  0 &  0 \\
                 1  & 0 &  2 &  0 \\
                3.5 & 2 &  2 &  0 \\
                 3  & 0 &  2 &  2 \\
                -1  & 0 &  0 &  0 \\ 
    \end{bmatrix}

the yield surface is 

.. math::

    f(n,m_z,m_y) = n^2 + m_z^2 + 3.5 n^2 \; m_z^2 + 3 m_z^2 m_y^2 - 1


References
----------

.. [1] T. Do Ngoc, "Damage Assessment and Collapse Simulations of Structures under Extreme Loading Conditions," UC Berkeley, 2017. Available: https://escholarship.org/uc/item/3sn707kd

.. [2] J. E. D. Cohen, "A Flexible Framework for the Damage-Based Modeling of Frame Elements With Applications to Steel Structures," Ph.D., UC Berkeley, 2022. Available: https://www.proquest.com/docview/2884075481/abstract/4371F56A2326476APQ/1


.. code-block:: bibtex

   @thesis{dongoc2017damage,
      title = {Damage {{Assessment}} and {{Collapse Simulations}} of {{Structures}} under {{Extreme Loading Conditions}}},
      author = {Do Ngoc, Thanh},
      date = {2017},
      institution = {UC Berkeley},
      url = {https://escholarship.org/uc/item/3sn707kd},
      abstract = {This dissertation presents a family of new beam-column element models which are based on damage-plasticity and are suitable for the damage assessment and the collapse simulation of structures.First, a new 1d hysteretic damage model based on damage mechanics is developed that relates any two work-conjugate response variables such as force-displacement, moment-rotation or stress-strain. The strength and stiffness deterioration is described by a damage variable with continuous evolution. The formulation uses a criterion based on the hysteretic energy and the maximum absolute deformation value for the damage initiation with a cumulative probability distribution function for the damage evolution.The damage evolution function is extended to accommodate the sudden strength and stiffness degradation of the force-deformation relation due to brittle fracture. The model shows excellent agreement with the hysteretic response of an extensive set of reinforced concrete, steel, plywood, and masonry specimens. In this context, it is possible to relate the model's damage variable to the Park-Ang damage index so as to benefit from the extensive calibration of the latter against experimental evidence.The 1d damage model is then extended to the development of beam-column elements based on damage-plasticity. In these models, the non-degrading force-deformation relation in the effective space is described by a linear elastic element in series with two rigid-plastic springs with linear kinematic and isotropic hardening behavior. The first model, the series beam element, assumes that the axial response is linear elastic and uncoupled from the flexural response. The second model, the NMYS column element, uses an axial-flexure interaction surface for the springs to account for the inelastic axial response and capture the effect of a variable axial load on the flexural response. A novel aspect of the beam-column formulation is that the inelastic response is monitored at two locations that are offset from the element ends to account for the spread of inelasticity for hardening response and the size of the damage zones for softening response. The plastic hinge offsets account for the response coupling between the two element ends.The implementation of the damage-plasticity elements with the return-mapping algorithm ensures excellent convergence characteristics for the state determination. The proposed elements compare favorably in terms of computational efficiency with more sophisticated models with fiber discretization of the cross section while achieving excellent agreement in the response description for homogeneous metallic structural components. The excellent accuracy is also confirmed by the agreement with experimental results from more than 50 steel specimens under monotonic and cyclic loading. The models are able to describe accurately the main characteristics of steel members, including the accumulation of plastic deformations, the cyclic strength hardening in early cycles, the low-cycle fatigue behavior, and the different deterioration rates in primary and follower half cycles. With the plastic axial energy dissipation accounted for in the damage loading function, the damage-plasticity column model captures the effect of a variable axial force on the strength and stiffness deterioration in flexure, the severe deterioration under high axial compression, the nonsymmetric response under a variable axial force, and the very large plastic axial and flexural deformations before column failure. The validation studies point out the dependence of the strength and stiffness deterioration on the section compactness, the element slenderness, the axial force history, and the axial shortening of the columns. A regression analysis is then used to establish guidelines for the damage parameter selection in relation to the geometry and the boundary conditions of the structural member.The proposed damage-plasticity frame elements are deployed in an analysis framework for the large-scale simulation and collapse assessment of structural systems. The capabilities of the modeling approach are demonstrated with thecase study of an 8-story 3-bay special moment-resisting steel frame that investigates various aspects of the structural collapse behavior, including the global and local response under strength and stiffness deterioration, the magnitude and distribution of the local damage variables, and the different types of collapse mechanism. The study proposes new local and global damage indices, which are better suited for the collapse assessment of structures than existing engineering demand parameters like the maximum story drift. The incremental dynamic analysis of the 8-story moment frame under a suite of earthquake ground motions confirms the benefits of the proposed damage indices for the collapse assessment of structures. The study shows that an aftershock as strong as the main shock increases the collapse margin ratio by as much as 30\textbackslash\% and requires more stringent design criteria for protecting the building from collapse that currently specified.The study compares different modeling aspects for the archetype building to assess the benefits of the proposed beam-column elements, such as the ability to account for the member damage, the offset location of the plastic hinges, the inelastic axial response, the axial-flexure interaction, and the sudden strength and stiffness deterioration due to brittle fracture of the structural member.The study concludes that the proposed family of beam-column elements holds great promise for the large scale seismic response simulation of structural systems with strength and stiffness deterioration, because of their computational efficiency and excellent accuracy. Consequently, the proposed models should prove very useful for the damage assessment and the collapse simulation of structures under extreme loading conditions.},
      langid = {english}
   }

   @thesis{cohen2022flexible,
      type = {phdthesis},
      title = {A {{Flexible Framework}} for the {{Damage-Based Modeling}} of {{Frame Elements With Applications}} to {{Steel Structures}}},
      author = {Cohen, Jade E. D.},
      date = {2022},
      institution = {University of California, Berkeley},
      url = {https://www.proquest.com/docview/2884075481/abstract/4371F56A2326476APQ/1},
      abstract = {The objective of this study is the development of analytical capabilities for the simulation of the inelastic response of structures under the strength and stiffness deterioration they experience when subjected to extreme events. The study addresses the development of such an analytical capability for steel frames. To this end, a family of 2d and 3d frame element models is proposed based on damage-plasticity. The strength and stiffness of these models degrade continuously as a function of one or more damage indices making them suitable for the damage assessment of steel frames up to incipient collapse. The study extends an existing damage model to cover the damage evolution of the constitutive relation of the frame element under multiple, interacting stresses or stress resultants. The formulation uses several damage indices that evolve continuously with the weighted sum of the plastic energy dissipation of the stress resultants with the work-conjugate deformation variables. The damage evolution function accounts for low-cycle fatigue and the different rate of damage accumulation in primary and follower deformation cycles. The function also accounts for the fact that the behavior in one loading direction may be affected by the damage accumulated in the opposite direction. The damage model operates as an independent wrapper of the effective force-deformation relation of the element, section or material and returns the true forces or stress resultants and the true tangent stiffness of the force-deformation relation under damage. With this modular formulation it is possible to use the damage wrapper with a material stress-strain relation, with a section force-deformation relation, or with the constitutive relation between the element basic forces and the work-conjugate deformations. Consequently, the study investigates the following three modelling alternatives for steel frame members without damage: a plasticity-based frame element with the basic forces and the work-conjugate deformations in the role of stress resultants and generalized strains, and a frame element that integrates the section force-deformation relation over the element length, with the section model based on plasticity theory for stress-resultants and generalized strains, or on the integration of the material stress-strain relation over the cross-section, a model commonly referred to as fiber section model. With the introduction of the damage wrapper at the element, or at the section, or at the material level, six modeling alternatives for steel frame members under damage result. Before embarking on the evaluation of the damage plasticity formulations, this study assesses the accuracy of the section model for stress-resultants by comparing its response with the response of the section model that integrates the material stress-strain relation over the cross section. To this end, an existing formulation is extended to accommodate the kinematic and isotropic hardening of the stress-resultants and the numerical implementation is enhanced with the scaling of the state determination variables to minimize the risk for an ill-conditioning of the Jacobian for the return-mapping algorithm of the section state determination. The same process is repeated for two existing stress-resultant frame elements: a 2d beam-element with linear elastic axial response, and a 3d beam-column element with axial force-biaxial flexure interaction of the basic forces in the role of stress-resultants with linear elastic torsional response. The former is suitable for steel girders experiencing small to negligible axial forces, while the latter is suitable for steel columns under any level of axial force, including variable axial forces due to the overturning effect of steel frames under lateral loads. The existing elements are extended to accommodate the kinematic and isotropic hardening of the stress-resultants and the numerical implementation is again enhanced with the scaling of the state determination variables to minimize the risk for an ill-conditioning of the Jacobian for the return-mapping algorithm of the element state determination. To account for the spread of inelasticity at the ends of steel beams and columns under strain hardening, both elements allow for the plastic hinges to be offset from the element ends. This feature requires the careful determination of the equivalent kinematic and isotropic hardening ratio for the element to match the moment-rotation relation of steel members under symmetric or anti-symmetric flexure. The study derives the necessary analytical expressions for this calibration, which are exact for beams and approximate for columns under axial force-flexure interaction. Correlation studies are conducted to assess the quality of the approximation for typical load-deformation scenarios of a steel member. After completing the evaluation of the resultant plasticity formulations, the study compares the response of four alternatives for a frame element under damage against available experimental data from the hysteretic uniaxial and biaxial bending response of steel columns under constant and variable axial force. These comparisons lead to recommendations on a consistent set of damage parameter values for typical steel members. The study concludes with the seismic response analysis of an irregular six-story steel frame under a strong ground acceleration in both principal directions at the base. The inelastic response history evaluates the effect of the damage evolution on the collapse risk of the frame and assesses the effect of nonlinear geometry and ground motion intensity on its global and local response.},
      isbn = {979-8-3806-2277-6},
      langid = {english},
      pagetotal = {286},
      keywords = {Beam-column element,Civil engineering,Collapse simulation,Damage assessment,Damage plasticity,Materials science,Stress resultants}
   }
