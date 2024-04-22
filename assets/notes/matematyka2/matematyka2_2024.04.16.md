### obliczanie całki podwójnej
$$
\iint_P f(x,y)dxdy = \int_a^b \left[\int_c^d f dy\right]dx
$$

```{admonition} Obszar normalny
D jest **obszarem normalnym** względem osi $X$ jeżeli jet opisany w następujący
sposób:

$$
x \in \left<a,b\right>
y \int \left<\phi_1, \phi_2\right>
$$

gdzie $\phi_1, \phi_2$ są są klasy $C^1$.
```

zmiana zmiennych:

$$
\iint_D f(x,y)dxdy \\
x = x(u,v) \\
y = y(u,v) \\
\iint_\Delta f(x(u,v),y(u,v)) j(u,v)dudv
$$

gdzie $j(u,v)$ to jakobian przekształcenia.

$$
j(u,v) = \begin{vmatrix}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v}
\end{vmatrix}
$$

```{admonition} Przykład
```
