## Równania Różniczkowe

```{admonition} postać ogólna równania różniczkowego zwyczajnego I Rzędu
$$
F(x,y,y')
$$
```

Rząd róœnania zależy od najwyższego rzędu pochodnej z tego róœnania.

```{admonition} Krzywa całkowa
wykres całki szczególnej - rozwiązania róœnania różniczkowego
```

### Przykłąd 1

$$
y' = x^4 + 2x \\
\int y' dx = \int x^4 + 2x dx \\
y = \frac{1}{5}x^5 + x^2 + C
$$

### Przykład 2 

```{math}
y' = x^4 + 2x ~ y(0) = 1 \\
\int y' dx = \int x^4 + 2x dx \\
y = \frac{1}{5}x^5 + x^2 + C \\
1 = \frac{1}{5}0^5 + 0^2 + C \Rightarrow C = 1 \\
y = \frac{1}{5}x^5 + x^2 + 1 \\
```

### Przykłąd 3

$$
y' = 1+y^2 \\
\frac{y'}{1+y^2} = 1 \\
\int \frac{y'}{1+y^2} dx = \int dx \\
\int \frac{\frac{dy}{\cancel{dx}}}{1+y^2} \cancel{dx} = \int dx \\
arctg(y) = x \\
y = tg(x + C) ~ X \in \left(-\frac{\pi}{2} -C, \frac{\pi}{2}-C)\right)
$$

```{admonition} Twierdzenie o istnieniu rozwiązań równania różniczkowego
jeżeli prawa strona równania różniczkowego jest funkcją ciągłą w obszarze D,
to przez każdy punkt tego obszaru musi przechodzić **conajmniej jedna** krzywa całkowa.
```

```{admonition} warunek na jedyne rozwiązanie problemu początkowego
Oprócz ciągłości prawej strony zakłada się również ciągłość pochodnej cząstkowej $\frac{\partial y}{\partial x}$
```

### Przyład 4

$$
y' = \root{3}\of{y^2} \\
$$

Zauważmy, że $f(x)=0$ jest rozwiązaniem równania

$$
\frac{y'}{\root{3}\of{y^2}} = 1 \\
\int \frac{dy}{\root{3}\of{y^2}} = x \\
3 \root{3}\of{y} = x + C \\
$$

## Równania Różniczkowe o zmiennych rozdzielonych

```{admonition} Postać ogólna równania różniczkowego o zmienych rozdzielonych
$$
y' = \frac{f(x)}{g(x)}
$$
```

```{admonition} Rozwiązanie problemu coshiego
Jeżeli f jest ciągła w X i g jest ciągła i różna od 0 w Y, to $(x,y) \in X \cross Y$ przechodzi jedna krzywa całkowa
```

$$
\frac{dy}{dx} = \frac{f(x)}{g(y)}
dy * g(y) = dx * f(x)
\int dy * g(y) = \int dx * f(x)
$$
