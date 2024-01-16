## Zastosowania całek
### Pole pod wykresem

Jeżeli funkcja jest całkowalna, to pole pomiędzy prostymi $a$ i $b$ wynosi $\int_a^b f(x)dx$.

```{note}
całka to **nie** jest pole. (e.g. $\int_0^{\frac{\pi}{2}} sin~x~dx = 0$)
```

```{admonition} pole elipsy
$$
\frac{x^2}{A^2} + \frac{y^2}{B^2} = 1 \\
y = +- \frac{B}{A} * \sqrt{A^2 - x^2} \\
\\
P = 4 \int_0^a \frac{B}{A} \sqrt{A^2-x^2} = \pi * A * B \\
$$
```

###4 Obliczanie długości krzywej

$$
l = \Sigma_i \sart{(\phi(t_i) - \phi(t_i - 1))^2 + (\psi(t_i) - \psi(t_i - 1))^2} = \\
= \Delta t_i \Sigma_i \sqrt{\phi'(u_i)^2 + \psi(\dzeta_i)^2 } \\
\int_\alpha^\beta \sqrt{\phi'^2 + \psi'^2 } dt \\

$$

```{admonition} Twierdzenie
$$
\gamma = \int_\alpha^\beta \sqrt{\phi'^2 + \psi'^2} dt
$$
jeżeli krzywa jest opisana równaniem

$$
\gamma = \int_a^b \sqrt{1+f'(x)^2} dx
$$

```
