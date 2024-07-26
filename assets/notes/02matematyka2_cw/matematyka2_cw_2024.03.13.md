## Metoda czynnika całkującego

$$
y' + p(x) = q(x) \\
y' \mu(x) + \mu(x)p(x)y = q(x) \mu(x) \\
(y*\mu(x))' = q(x) \mu(x) \\
\mu(x) = e^{\int p(x) dx}
$$

Rozwiązywanie róœnań liniowych II rzędu

- wielomian harakterystyczny

$$
y'' +y' - 2y = e^{-x} \\
\lambda^2 + \lambda - 2 = 0 \\
\lambda = 1 \lor \lambda = -2 \\
y = C_1 e^{x} + C_2 e^{-2x}
$$

- dla $\Delta < 0$ - suma sinus+cos, ignorujemy `i`
- dla $\Delta = 0$ - $Ce^x + Cxe^x$


$$
\left\{
    \begin{matrix}
    C_1' y_1 + c_2' y_2 = 0 \\
    C_1' y_1' + C_2' y_2' = f(x)
    \end{matrix}
\right.
$$
