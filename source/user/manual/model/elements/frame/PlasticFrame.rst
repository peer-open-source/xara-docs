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
