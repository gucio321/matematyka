## Różniczkowanie

Niech $y = f(x) = a * x$ wtedy dla $x = 1~y = a \Rightarrow a = tg \alpha$

```{note}
**podejście geometryczne:** \
Spróbujmy znaleźć wykres stycznej do wykresu funkcji $f(x)

**Sieczna** - prosta przechodząca przez dowolne dwa punkty należące
do wykresu funkcji $f(x)$

$y-y_0 = \frac{f(x)-f(x_0)}{x-x_0}(x-x_0)$ - równanie siecznej przechodzącej przez $x$ i $x_0$
```

```{admonition} Definicja pochodnej
granicę $lim_{x \to x_0} \frac{f(x)-f(x_0)}{x-x_0}$ o ile istnieje
nazywamy **pochodną** funkcji `f` w punkcie $x_0$ i oznaczymy $f'(x_0)$ lub $\frac{df}{dx}$
```

```{important}
**Interpretacja geometryczna** \
$f'(x_0)$ to $tg$ kąta nachylenia stycznej do fykresu funkcji `f` w punkcie $x_0$
```

$f: I \to \mathbb{R}$ 
jeżeli $\forall x in I \exists f'(x)\quad f' : X \to \mathbb{R}$

### Przykłady funkcji pochodnych

| $f(x)$ | $f'(x)$ |
|---|---|
| $f(x) = a$ | $f'(x) = 0$ |
| $y = ax + b$ | $\frac{a(x+h) + b - (ax + b)}{h} = a$ |
| $y = ax^2$ | $\frac{(x+h)^2-x^2}{h} = x+h ~ dla~h\to0 \quad f'(x) = 2x$
| $y = \sqrt{x}$ | $\frac{f(x+h) - f(x)}{h} = \frac{x + h - x}{h(\sqrt{x+h} + \sqrt{x})} \to \frac{1}{2 \sqrt{x}}$ |
| $y = x^n$ | $\frac{f(x+h) - f(x)}{h} =\frac{(x+h)^n - x^n}{h} = n * x^{n-1}$ |
| $y = sin(x)$ [więcej](#pochodne-funkcji-trygonometrycznych) | $y' = cos(x)$ |
| $y = arctg(x)$ | $\frac{1}{x^2+1}$ |

**[Zaawansowany Kalkulator Pochodnych](https://mathdf.com/der/pl/)**

### Przykłady funkcji, które nie mają pochodnych

$$
f(x) = |x| \\
f'(0) = \frac{f(0+h) - f(0)}{h} = \frac{|h|}{h} \\
Dla~h < 0\quad f'(0) \to -1 \land dla~h>0\quad f'(0) \to 1
$$


```{admonition} Twierdzenie o ciągłości funkcji różniczkowalnej
Jeżeli `f` jest różnniczkowalna, to `f` jest ciągła

$$
f(x_0 + h) = f(x_0+h)-f(x)+f(x) = \frac{f(x+h)-f(x)}{h} * h + f(x) = \\
= 0 + f(x)
$$
```

### Działania na pochodnych

```{admonition} Twierdzenie o różniczkowalności złożeń funkcji różniczkowalnych
Jeżeli funkcje `f` i `g` sa różniczkowalne, to funkcje $f+g$ oraz $c*g$ są różniczkowalne
i zachodzą następujące wzory

$$
(f+g)' = f' + g' \\
(c*g)' = c * g'
$$
```

```{tip}
Nie jest prawdą stwierdzenie, że "suma pochodnych jest pochodną sumy".
prawdą jest, że "suma pochodnych jest pochodną sumy **Przy stosownych założeniach**".
```

```{tip}
$f(x) = ax + b$ **nie** jest operacją liniową, ponieważ
$f(x_1+x_2) \neq ax_1 + b + ax_2 + b$
```

### Pochodne funkcji trygonometrycznych

$$
y = sin(x) \\
y' = \frac{sin(x+h) - sin(x)}{h} \\
y' = \frac{sin x* cos h + cos x * sin h - sin x }{h} = \frac{2sin x (cos h - 1}{h}) = cos x \\
$$

### Pochodna funkcji wykładniczej

$$
(a^x)' = \frac{a^x a^h - a^x}{h} = a^x \frac{a^h-1}{h} =
= logn a * a^x \\
\\
(e^x)' = logn~e * e^x = e^x
$$
