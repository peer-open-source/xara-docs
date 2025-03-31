.. _RambergOsgoodSteel:

Ramberg Osgood
^^^^^^^^^^^^^^

A popular envelope model for metalic materials was developed by \citep{ramberg1943description} who proposed the following equation:
\begin{equation}
\varepsilon=\frac{\sigma}{E}+a\left(\frac{\sigma}{\sigma_y}\right)^n,
\label{eq:RO}
\end{equation}
where $E$ is the elastic modulus, $\sigma_y$ is the yield stress, assumed to be at the 0.2\% offset strain, $n$ is a parameter controlling the transition to yield, and $a$ is a yield offset parameter, typically taken as 0.002. Note that the stress \(\sigma\) is defined implicitly in terms of strain \(\varepsilon\) in this model and must be solved for numerically.

