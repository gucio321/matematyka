## Rachunek Całkowy

[Kalkulator Całek](https://mathdf.com/int/pl/)

```{admonition} definicja całki
f to funkcja określona na przedziale otwartym

jeżeli F na tym samym przedziale ma pochodną i $F'(x) = f(x)$
funkcję `F` nazywamy **funkcją pierwotną** `f` lub **całką nieoznaczoną funkcji `f`**
i oznaczamy $\int f(x) dx$
```

```{admonition} Twierdzenie o stałej całkowania
Jeżeli `F` jest funkcją pierwotną `f`, to $F + C$ róœnież jest
pierwotną funkcji `f`$

$\int f(x) dx$ to rodzina funkcji. Funkcja pierwotna jest określona z dokładnością
do stałej.
$$

```

### Metody obliczania całek

#### Zgadywanie

|  f(x)                    | $\int f(x) dx$                                    |
|--------------------------|---------------------------------------------------|
| $0$                      | const                                             |
| $C$                      | $C x$                                             |
| $x^2$                    | $\frac{1}{2} x^2$                                 |
| $x^\alpha$               | $\frac{1}{\alpha+1}x^{\alpha+1} ~ \alpha \neq -1$ |
| $\frac{1}{x}$            | $ln(|x|)                                          |
| $cos(x)$                 | $sin(x)$                                          |
| $sin(x)$                 | $-cos(x)$                                         |
| $ctg(x)$                 | $ln(|sin(x)|)$                                    |
| $tg(x)$                  | $-ln(\abs\|cos(x)})$                                   |
| $\frac{1}{cos^2(x)}$     | $tg(x)$                                           |
| $\frac{-1}{sin^2(x)}$    | $ctg(x$)$                                         |
| $e^x$                    | $e^x$                                             |
| $e^{-x}$                 | $-e^{-x}$                                         |
| $\frac{1}{1+x^2}$        | $arctg(x)$                                        |
| $cosh(x)$                | $sinh(x)$                                         |
| $sinh(x)$                | $cosh(x)$                                         |
| $\frac{1}{\sqrt{1-x^2}}$ | $arcsin(x)$                                       |
| $\frac{1}{\sqrt{x^2+a}}$ | $ln(x+\sqrt{x^2+a})$                              |


```{admonition} _Liniowość*_
Jeśli `f` i `g` mają funkcje pierwotne $f+g$ oraz $c*f$ też mają
funkcje pierwotne oraz $\int f+g = \int f + \int g$ natomiast $\int c*f = c * \int f$.

:::{important}
Operacja całkowania nie jest liniowa, ponieważ wystęþuje translacja o stałą
:::
```

```{important}
niech $f(x) \neq 0$

$$
\int \frac{f'(x)}{f(x)} dx = ln(f(x))
$$

:::{note}
$$
\int \frac{x}{1+x^2} dx = \frac{1}{2} \int \frac{2x}{1+x^2} dx = \\
= \frac{1}{2} ln (1+x^2) + C \\
\\
\int ctg(x) dx = \int \frac{cos(x)}{sin(x)} dx = ln(sin(x)) + C \\
\\
\int tg(x) dx = \int \frac{sin(x)}{cos(x)} dx = \\
= - \int \frac{-sin(x)}{cos(x)} dx = -ln(|cos(x)|) + C
$$
:::
```

#### przez części

$$
f * g = \int f' * g + \int f * g' \\
\int f' * g = f * g - \int f g' 
$$

:::{note}

$$
\int x * e^x = \int x * (e^x)' = x * e^x - \int e^x = x * e^x - e^x \\
\cancel{\int x * e^x = \int (\frac{x^2}{2})' * e^x = \frac{x^2}{2} e^x - \int(\frac{x^2}{2}e^x)}
\\
\\
\int ln(x) = \int 1 * ln(x) = \int (x)' ln(x) = x ln(x) - \int x * \frac{1}{x} = x * ln(x) - x \\
$$
:::

```{warning}
# EGZAMIN Z ANALIZY
- Czas trwania: 90 min
- 1 termin na początku sesji
- 4 zadania (3 zadania-zadania + 1 teoria).
- _Zadania klasyczne_
```
