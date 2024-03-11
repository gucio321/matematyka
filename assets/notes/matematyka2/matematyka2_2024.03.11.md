## Równania liniowe

### Równania liniowe 1 rzędu

$$
y' + p(x) * y = f(x) \\
niech~
L(y) = y' + p(x) * y  \\
L(y_1 + y_2) = L(y_1) + L(y_2) \\
L(\alpha y) = \alpha L(y) \\
$$

Mówi się, że równanie jest liniowe, jeżeli _lewa strona_ jest liniowa
ze względu na `y`.

```{note}
jeżeli $f(x) = 0$, mówimy o równaniu jednorodnym.
```

```{tip}
niech $y^{*}$ i $y$ będą rozwiązaniami równania liniowego niejednorodnego, wtedy

$$
L(y^{*}) - L(y) = f(x) - f(x) = 0 \\
L(y^{*} - y) = 0
$$

Z tego wynika, że różnica $y^{*} - y$ jest rozwiązaniem równania jednorodnego
```

```{admonition} tw. kukurydzy

$$
CORN = CSRN + CORJ
$$

- CORN = całka ogólna równania niejednorodnego
- CSRN = Całka szczególna równania jednorodnego
- CORJ = Całka ogólna równania jednorodnego
```

$$
y' + p(x) y = 0 \\
\frac{dy}{y} = -p(x) dx \\
\int \frac{dy}{y} = \int -p(x) dx \\
ln(y) = \int p(x) dx + C \\
|y| = e^{\int p(x) dx} + C \\
CORJ: \quad y = Ce^{\int p(x) dx} \\
$$

#### Metoda Uzmienniania stałej:

Szuikamy CSRN W postaci $y(x) = C(x) * e^{-\int p(x) dx}$

$$
C'(x) * e^{-\int p(x) dx} + \cancel{C(x) * (-p(x)) e^{-\int p(x) dx}} + \cancel{p(x)* C(x)e^{-\int p(x) dx}} = f(x) \\
C'(x) * e^{-\int p(x) dx} = f(x) \\
C'(x) = f(x) e^{\int p(x) dx}
C(x) = \int f(x) e^{\int p(x) dx}
$$

#### Metoda Przewidywania

Jeżeli $p(x) = const$

$$
\frac{dy}{dx} + 3y = x^2 \\
$$

Pomińmy COFJ, CSRN:
Rozwiązaniem Najprawodopodobniej będzie wielomian stopnia 2

$$
y=Ax^2 + Bx + C \\
y' = 2Ax + b \\
2Ax + B + 3Ax^2 + 3Bx + 3C = x^2 \\
\left\{\begin{matrix}
3A = 1 \\
2A + 3B = 0 \\
B + 3C = 0 \\
\end{matrix}\right. \Rightarrow
\left\{\begin{matrix}
A = \frac{1}{3} \\
B = \frac{-2}{9} \\
3C = \frac{2}{27} \\
\end{matrix}\right.
$$

Jeżeli f(x) jest w postaci funkcji trygonometrycznych, zakładamy
rozwiązanie w postaci $Asin(x) + Bcos(x)$
