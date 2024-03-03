## Funkcja Gamma Eulera

$$
\Gamma(x) = \int_0^\infty t^{x-1} e^{-t} dt
$$

- W otoczeniu 0

$$
\Gamma ~ \int_0^\infty t^{x-1} dt
$$

Funkcja jest zbierzna jeżeli $1 - x < 1 \Leftrightarrow x > 0$

W "otoczeniu" $\infty$

$$
\text{dla } t \to \infty \\
t^{x-1} \leq e^t \\
$$

### Własnośći
- $\Gamma(x+1) = x * \Gamma(x)$

_dowóð z obliczenia całki $\Gamma(x+1)$ przez części_

- $\Gamma(1) = \left. -e^{-t} \right|_ 0^\infty = 1$ 

- Definicja silni

$$
\Gamma(2) = 1 * \Gamma(1) = 1 \\
\Gamma(3) = \Gamma(2 + 1) = 2 * \Gamma(2) = 2 \\
\Gamma(4) = 3 * \Gamma(3) = 6 \\
\\
\Gamma(n+1) = n! \\
$$

- $\Gamma(\alpha) * \Gamma(1-\alpha) = \frac{\pi}{sin(\pi \alpha)}$

$n! ~ n^n * e^{-n} * \sqrt{2\pi n}$


## Funkcja $\beta$

$$
\beta(\alpha, \beta) = \frac{\Gamma(\alpha) * \Gamma(\beta) }{\Gamma(\alpha + \beta)} = \int_0^1 x^{\alpha-1}(1-x)^{\beta-x} \\
\\
\int_{-\infty}^{\infty} e^{-t^{2}} = \sqrt{\pi}
$$
