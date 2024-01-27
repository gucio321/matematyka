## Granice: - Tricki

### Symbole Nieoznaczone czyli co z tym robić?

#### $0 * \infty$

$$
\left[0 * \infty\right] =
\left[\frac{0}{\frac{1}{\infty}}\right] =
\left[\frac{0}{0}\right]
$$

Teraz można użyć twierdzenia de l'Hospital.

Dowód: 

$$
\lim_{n \to \infty} n \frac{1}{n^2} \stackrel{\left[0 * \infty\right]}{=} 0 \\
\lim_{n \to \infty} n^2 \frac{1}{n} \stackrel{\left[0 * \infty\right]}{=} \infty \\
$$

#### $\infty - \infty$

Dowód:

$$
\lim_{n \to \infty} n - n^2 \stackrel{\left[\infty - \infty\right]}{=} \lim_{n\to \infty} n^2(\frac{1}{n} - 1) = - \infty \\
\lim_{n \to \infty} n^2 - n \stackrel{\left[\infty - \infty\right]}{=} \lim_{n\to \infty} n^2(1-\frac{1}{n}) = \infty \\
$$

#### $\frac{\infty}{\infty}$ i $\frac{0}{0}$

Dowód analogiczny jak powyżej. Aby rozwiązać korzystamy z twierdzenia de l'Hospital'a
