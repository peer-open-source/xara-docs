


.. py:method:: Model.uniaxialMaterial("FullBoucWen", tag, E, Fy, b [, beta, gamma, n] [, detla_v, delta_n, lamda, p, q, zeta, detla_p, po])
   :no-index:

   :param tag: unique integer tag for the material
   :type tag: |integer|
   :param E: initial stiffness, :math:`E`
   :type E: |float|
   :param Fy: yield force, :math:`F_y`
   :type Fy: |float|
   :param b: post-yield stiffness ratio, :math:`b`
   :type b: |float|
   :param beta: First hysteretic
   :type beta: |float|
   :param gamma: second hysteretic shape parameter, :math:`\gamma`
   :type gamma: |float|
   :param n: sharpness of yield, :math:`n`
   :type n: |float|
   :param delta_v: strength degradation rate, :math:`\delta_v`
   :type delta_v: |float|
   :param delta_n: stiffness degradation rate, :math:`\delta_n`
   :type delta_n: |float|
   :param lamda: pinching severity, :math:`\lambda`
   :type lamda: |float|
   :param p: pinching slope, :math:`p`
   :type p: |float|
   :param q: pinching initiation, :math:`q`
   :type q: |float|
   :param zeta: measure of total slip, :math:`\zeta`
   :type zeta: |float|
   :param delta_p: pinching rate, :math:`\delta_{\psi}`
   :type delta_p: |float|
   :param po: pinching magnitude, :math:`\psi_0`
   :type po: |float|
   

   
\begin{tabular}{|l|l|}
\hline $\alpha$ & Post-yield stiffness ratio \\
\hline $k_0$ & Initial stiffness \\
\hline $F_y$ & Yield force \\
\hline $\beta$ & Basic hysteretic shape control \\
\hline $n$ & Sharpness of yield \\
\hline $\delta_v$ & Strength degradation rate \\
\hline $\delta_\eta$ & Stiffness degradation rate \\
\hline $\zeta_0$ & Measure of total slip \\
\hline $p$ & Pinching slope \\
\hline $q$ & Pinching initiation \\
\hline $\psi$ & Pinching magnitude \\
\hline $\delta_\psi$ & Pinching rate \\
\hline $\lambda$ & Pinching severity \\
\hline $c_{\varepsilon}$ & Hysteretic energy amplification factor \\
\hline $c_h$ & Crack closure coefficient \\
\hline
\end{tabular}