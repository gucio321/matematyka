#### Zadania

```{note}
Z kwadratoweo arkusza blachy wycinamy 4 kwadratowe kawałki (na rogach).
Z czego powstaje nam "pudełko". Jaka największa objętość?

$$
0 < x < \frac{a}{2} \\
V(x) = (a-2x)^2 x \\
$$

szukamy największą wartość funkcji w przedziale $x \in \left<0, \frac{a}{2}\right>$

$$
V'(x) = (a-2x)^2 -4x(a-2x) \\
V'(x) = (a-2x)(a-2x -4x) \\
V'(x) = (a-2x)(a-6x) \\
x = \frac{a}{2} \lor x = \frac{a}{6} \\
$$

```

```{note}
$$
O(h) = C * sin \alpha * \frac{1}{r^2} \\
\frac{a}{r} = cos \alpha \\
O(h) = C * sin \alpha * \frac{cos^2 \alpha}{a^2} \\
O(h) = \frac{C}{a^2} * sin \alpha * cos^2 \alpha \\
f(x) = sin x * cos^2 x \\
x \in \left<0, \frac{\pi}{2}\right) \\
f'(x) = cos^3 x - 2sin^2 x cos x  \\
f'(x) = cos x (cos^2 x - 2sin^2 x) \\
x = \frac{\pi}{2} &\lor tg^2 x = \frac{1}{2} \\
&\lor tg x = \frac{1}{\sqrt{2}} \text{tg > 0 w przedziale} \\
&\lor x = arctg \frac{1}{\sqrt{2}} \\
$$
```

#### Wypukłość funkcji

`f` jest wypukłą ku górze jeśli w pewnym otoczeniu
wykres f jest poniżej wykresu stycznej.

Funkcja jest wypukła ku dołowi w punkcie $x_0$ jeżeli w tm punkcie wykres jest powyżej wykresu stycznej

```{admonition} Twierdzenie o wypukłości
`f` klasy $C^2$

Jeżeli `f` wypukła ku górze $\Rightarrow f''(x_0) \leq 0$
Jeśli $f''(x_0) < 0 \Rightarrow$ funkcja jest wypukła ku górze.
```

#### Asymptoty

Asymptoty to proste, do których wykres danej funkcji zbliża się dowolnie blisko.

```{tip}
Prosta o równaniu $y = ax+b$ jest asymptotą ukośną, jeśli
$f(x)-ax-b \to 0~dla~x\to \infty$
```

Prosta o równaniu $y=ax+b$ jest asymptotą ukośną funkcji f $Rightleftarrow$
$\exists lim_{x \to \infty} \frac{f(x)}{x} = a \land$
$\exists lim_{x \to \infty} f(x)-ax = b$
