#### Pojęcie Różniczki
Jeżeli `f` jest różniczkowalna

$$
\frac{f(x+h)-f(x)}{h} \to f'(x) \\
\frac{f(x+h)-f(x)}{h} - f'(x) \to 0 \\
\frac{f(x+h)-f(x)-f'(x) * h}{h} \to 0 \\
f(x+h)-f(x)-f'(x_0) * h= o(h) \\
\Delta y-f'(x_0) * h= o(h) \\
\Delta y = f'(x_0) * \Delta x + o(\Delta x)
$$

```{note}
Odwzorowanie liniowe $h \to f'(x_0) * h$ nazywamy różniczką funkcji `f`
w punkcie $x_0$.

Jest to odwzorowanie takie, że $f(x_0+h) - f(x_0)  = f'(x_0) * h + o(h)$
```

#### Oznaczenia

| $f$ | pochodna | |
|---|---|---|
| $f$ | $f'$     | $\frac{df}{dx}$ |
| $f'$ | $f''$ | $\frac{d^2 f}{dx^2}$ |

```{admonition} Definicja
Funkcję nazywamy **funkcją klasy $C^k$** jeżeli ma pochodne do rzędu `k` i `k`ta pochodna jest ciągła.
```

#### Wzór Taylora

$$
F: I \to \mathbb{R}~\land ~ "f klasy" C^1 \\
\text{tw. lagrange'a dla przedziału}
\left(x_0, x_0+h\right) \\
f(x_0+h)-f(x_0) = f'(\psi) * h \\
f(x_0+h)=f(x_0) + f'(\psi) * h \\
\exists \psi \in (x_0, x_0+h) \\
\psi = x_0 + \theta h \quad \theta \in \left<0,1\right> \\
$$

$$
Niche~f~będzie~klasy~C^n \\
\exists \psi~f(x_0+h) = f(x_0) + \frac{h}{1!} f'(x_0) + \frac{h}{2!} f''(x_0) + ... + \frac{h}{n!} f^{(n)}(\psi)
$$

Ostatnie równanie nazywamy Równaniem Taylora z resztą Lagrange'a


```{admonition} Wzór Maclaurina
$$
f(x) = f(0) + x * f'(0) + \frac{x^2}{2!} f''(0) + ... + \frac{x^n}{n!} * f^(n) (\theta x)
$$
```

| $f(x)$ | Rozwinięcie |
|---|---|
| $e^x$ | $1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + ... + \frac{x^n}{n!} * e^{\theta x}$ |
| $sin(x)$ | $x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + ... + R_n$ |
| $cos(x)$ | $1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + ... + R_n$ |
| $ln(1+x)$ | $0 + x - x^2 + \frac{x^3}{3} - \frac{x^4}{4} + \frac{x^5}{5} + ... + R_n = \left(\Sigma_{i=1}^n (-1)^{n+1} * \frac{x^n}{n}\right)+R_n$ |
| $(x+1)^\alpha$ | $1 + {\alpha \choose 1} x + {\alpha \choose 2} \frac{x^2}{2!} + {\alpha \choose 3}* \frac{x^3}{3!} + ... + R_n$ |

```{important}
$$
{\alpha \choose k} = \frac{\alpha (\alpha-1)(alpha-2) * ... * (\alpha-k)}{k!}
$$
```

```{tip}
Zastosowanie wzoru Taylora do obliczeń przybliżonych:

dla x = 1, n = 6

$$
e = 1 + 1 + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} + \frac{1}{120} + \frac{1}{720} * e^\theta \\
0 \leq \theta \leq 1 \\
e \approx 1 + 1 + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} + \frac{1}{120} \\
$$
```
