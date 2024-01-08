##### Całkowanie ułamków prostych

$$
\frac{Ax+B}{((x-p)^2 +q)^k}
$$

```{tip}
$$
\frac{x+3}{((x-2)^2+5)^2} \\
y=(x-2)^2+5 \\
dy = 2(x-2)dx \\
\frac{2(x-2)-2(x-2) + x+3}{((x-2)^2+5)^2} \\
$$
```

```{note}
Rozkładanie na ułamki proste

$$
\frac{1}{(x-1)(x+2)} = \frac{A}{x-1} + \frac{B}{x+2} \\
1 = A(x+2) + B(x-1) \\
1 = Ax + 2A + Bx - B \\
\left\{\begin{matrix}
A + B = 0 \\
2A - B = 1 \\
\end{matrix}\right. \Rightarrow A = -B = \frac{1}{3} \\
$$
```

#### Całkowanie Funkcji typu $R(cos(x), sin(x))$

Metoda: Podstawienie $t=tg\frac{x}{2}$

$$
sin(x) = 2 * sin(\frac{x}{2})cos(\frac{x}{2}) = \frac{2tg\frac{x}{2}}{1+tg^2\frac{x}{2}} \\
cos(x) = \frac{1-t^2}{1+t^2} \\
tg(x) = \frac{2t}{1+t} \\
dt = 2 \frac{1}{1+t^2}dt
$$

#### Całki z pierwiastkiem

$$
\int \sqrt{1-x^2}dx \\
x = sin(t) \\
dx = cos(t) \\
\int \sqrt{1-sin^2(t)} cos(t) dt \\
\int cos^2(t) dt \\
\\
\\
\int \sqrt{1+x^2}dx \\
x= sinh(t) \\

$$
