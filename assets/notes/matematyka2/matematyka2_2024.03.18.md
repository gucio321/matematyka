<!--nie przerywam pańśtwu, bo przecież nie wolno stresować młodzierzy-->

### Równania II liniowe rzędu

$$
y'' = x^2 \\
y' = \frac{x^3}{3} + C \\
y = \frac{x^4}{12} + C x + C_1 \\
$$

```{tip}
rodzina funkcji wyjściowych zeleży od 2 parametrów
```

$$
y'' + p(x) y' + q(x) y = f(x)
$$

```{note}
liniowe, ponieważ $L(y_1 + y_2) = L(y_1) + L(y_2) \land L(\alpha y) = \alpha L(y)$
```

```{note}
twierdzenie CORN nadal zachodzi
```


Rozważmy nastęþujące równanie:

$$
y'' + py' + qy = 0 \\
$$

```{admonition} Macierz Wrońskiego
Dwa rzowiażania rówania jednordnego stanowią tzw. **układ fundamentalny**
jeżeli następujący wyznacznik $\left|\begin{matrix}y_1 (x) & y_2 (x) \\ y_1'(x) & y_2'(x)\end{matrix}\right| \neq 0$

Jeżeli $y_1(x)$ oraz $y_2(x)$ stanowią ukłąd fundamentalny dla RJ, to
$y = C_1 y_1 + C_1 y_2$ to CORJ.

Ponadto zagadnienie Coshiego tj. $\left\{\begin{matrix}y(x_0) = a \\ y'(x_0) = b\end{matrix}\right.$ ma dokładnie
jedno rozwiązanie.
```

ROzwiązania szukamy w postaci $y = e^{r * x}$. Udowadniamy z dowodu nie-wprost.
<!--Muszę trochę energiczniej pisać, bo nie uda mi się rozwalic tej tablicy do końca semestru i znowu będę się z n nią musiał...-->

$$
r^2 + pr + q = 0
$$

- jeżeli $\Delta > 0$
istnieją 2 pierwiastki.

$$
y = e^{r_1 x} + e^{r_2 x}
$$

<!---skoro już jestem przy ogłoszeniach, to jutro mamy.... wykład. i jeśli się okaże, że to jest dobre rozwiązanie, to w przyszłym tygodniu też tak zrobimy.-->
- $\Delta = 0$

$$
r = \frac{-p}{2} \\
\\
y_1 = e^{rx} \\
y_2 = x * e^{rx} 
$$

- $\Delta < 0$

załóżmy, że rozważamy róœnanie w dziedzinie $\mathbb{C}$

$$
r_1 = \alpha + \beta i \\
y_1 = e^{\alpha x} cos \beta x \\
y_2 = e^{\alpha x} sin \beta x
$$
