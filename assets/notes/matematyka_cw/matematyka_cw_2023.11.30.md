## Przydatne własności

```{tip}
Przy wistępowaniu nioznaconości typu $[0 * \infty]$ wystarczy iloczyn zapisać
w postaci ilorazu na przykład

$$
\lim_{x \to 0} x * \left(\frac{1}{x}+1\right) = \frac{\frac{1}{x} + 1}{\frac{1}{x}}
$$

W ten sposób otrzymamy nieoznaczoność typu $\left[\frac{\infty}{\infty}\right]$ więc możemy skorzystać z reguły
de l'Hospital'a
```

## Przykładowa tabela przebiegu zmienności funkcji:

|          | $(-\infty, -1)$ | $-1$         | $\left(-1, -\frac{2}{5} \right)$ | $-\frac{2}{5}$                    | $\left(\frac{-2}{3}, 0\right)$ | 0 | $(0,2)$  | 2                | $(2, \infty)$ |
|----------|-----------------|--------------|----------------------------------|-----------------------------------|--------------------------------|---|----------|------------------|---------------|
|  $f'(x)$ | +               | 0            |  -                               | -                                 | -                              | X | -        | 0                | +             |
| $f''(x)$ | -               | -            | -                                | 0                                 | +                              | X | +        | +                | +             |
| $f(x)$   | rośnie          | max $e^{-1}$ | maleje                           | PP $\frac{8}{5}e^{-\frac{5}{2}}$  | maleje                         | X | maleje   | min $4 \sqrt{e}$ | rośnie        |
