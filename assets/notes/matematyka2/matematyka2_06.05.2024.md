<!--21.05.2024 - sala w łączniku A3-A4 -->

### Całka powierzchniowa niezorientowana

i$$
x = x(u,v)\\
y = y(u,v) \\
z = z(uxv \\
u,v, \in \Delta
$$)

```{admonition} wektor normalny

$$
\vec{V} = det \begin{bmatrix}
\vec{i} & \vec{j} & \vec{k} \\
\frac{\partial x}{\partial u} & \frac{\partial y}{\partial u} & \frac{\partial z}{\partial u} \\
\frac{\partial x}{\partial v} & \frac{\partial y}{\partial v} & \frac{\partial z}{\partial v} \\
\end{bmatrix}
$$

W szczegulnym  przypadku, kiedy obszar jest opisany wykresem funkcji

$$
u = x
v = y
z = f(x,y)
$$
```

$$
\iint_S f(x,y,z) ds = \iint_S f(x(u,v), y(u,v), z(u,v)) \sqrt{A^2 + B^2 + C^2} dudv
$$
