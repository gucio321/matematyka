#### Przez podstawienie

```{admonition} Podstawienie
Niech $G(y)$ będzie funkcją pierwotną funkcji $g(y)$ a $f(x)$ będzie klasy $C^1$.
Wtedy $\int g(y)dy |_{y = f(x)} = \int g(y) f'(x) dx

:::{tip}
$$
\int \sqrt{1-x^2} dx \\
x = sin t \\
dx = cos t dt \\
\int \sqrt{1-sin^2t} cos t*dt = \\
= \int cos^2(t) dt = \frac{1}{2} \int 2 cos^2{t} dt = \\
= \frac{1}{2} \int 1 + cos(2t) dt = \\
= \frac{1}{2} (t + \frac{1}{2} sin(2t)) = \\
\frac{1}{2} arcsin(x) + \frac{1}{2}x \sqrt{1-x^2}

$$
:::
```

$$
I_n = \int \frac{1}{(1+x^2)^n} \\
I_1 = arctg(x) \\
I_n = \int \frac{1+x^2 - x^2}{1+x^2} dx = \int \frac{dx}{(1+x^2)^n} - \int \frac{x^2}{(1+x^2)^n}dx = \\
= I_{n-1} - \int \frac{x^2}{(1+x^2)^n}
I_n = \frac{1}{2n-2} \frac{x}{(1+x^2)^{n-1}} + \frac{2n-3}{2n-2} I_{n-1}
$$

#### Całki funkcji wymiernych
$$
\int \frac{P(x)}{Q(x)}  = ?
$$

Należy znaleźć rozkład funkcji na ułamki proste:
| f(x) | $\int f(x) dx$ |
|---|---|
| $\frac{A}{x-A}$ | $ln(x-A) |
| $\frac{A}{(x-A)^k}$ | $\frac{-1}{x-1} ....$ |
- $\frac{Cx - B}{(x-p)^2 + q^2}$
- $\frac{Cx - B}{((x-p)^2 + q^2)^k}$
