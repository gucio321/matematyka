```{tip}
gradient równy $1$ pokazuje kierunek największego wzrostu funkcji
```

### Funkcje uwikłane

```{admonition} tw. o funkcji uwikłanej
niech funkcja $f(x,y)$ będzie klasy $C^1$ w obszarze $D$.
- $f(x_0, y_0) = 0$
- $\frac{\partial f}{\partial y} \neq 0$ w punkcie $(x_0, y_0)$
- istnieje prostokąt postaci $P=(x_0-\delta, x_0 + \delta) \times (y_0 - \varepsilon, y_0 + \varepsilon)$, taki że $f(x, y) = 0$ ma jednoznaczne rozwiązanie $y = \varphi(x)$ taki, że $F(x, f(x)) = 0$
```

```{admonition} tw. o funkcji uwikłanej w przestrzeni $\mathbb{R}^3$
Jeżeli $F$ jest klasy $C_1$ w obszarze $D$
- $F(x_0, y_0, z_0) = 0$
- $\frac{\partial F}{\partial z} \neq 0$ w punkcie $(x_0, y_0, z_0)$
- istnieje funkcja $z = z(x,y)$ taka, że $F(x, y, z(x,y)) = 0$
```

### płaszczyzna styczna

```{note}
Ogólne róœnanie płaszczyzny to $Ax + By + Cz + D = 0$
```

Szukana płaszczyzna ma równanie $A(x-x_0) + B(y-y_0) + C(z-z_0) = 0$

<!-- jeśli się o kimś powie że nie jest zbyt prostopadły to raczej nie zrozumie-->

Równanie płaszczyzny ma postać $\frac{\partial f}{\partial x}(x- x_0) + \frac{\partial f}{\partial y}(y - y_0) + \frac{\partial f}{\partial z}(z - z_0) = 0$
