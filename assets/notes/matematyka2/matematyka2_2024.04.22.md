### Całka potrójna

```{admonition} Obszar
obszar jest normalny do płąszczyzny jeżeli

$$
(x,y) \in D
z \in \left<\phi_1 (x,y), \phi_2(x,y)\right> \\
$$
```

```{admonition} całka potrójna 
$$
\iiint f(x,y,z) dx dy dz = \iint_D dx dy \int_{\phi_1}^{\phi_2} f(x,y,z) dz
$$
```

### Zastosowania całek

pole: obszar płąski $D = \iint y_D = \int 1 dx dy$

Objętość bryły $\iiint 1 dx dy dz$

Pole powierzchni  

$$
P_{ij} = r_{ij} * cos (\phi_{ij}) \\
cos (\phi_{ij}) = (f_x'^2 + f_y'^2 + 1)^{-\frac{1}{2}} \\
P = \iint_D \sqrt{1 + f_x'^2 + f_y'^2+1} dx dy \\
P = \iint_D ||\vec{N}|| dx dy
$$

```{tip}
krzywą $f(x)$ obracamy wogół osi $OX$.
```

środek Ciężkości:

Jeżeli środek ciężkości ma współżędne $\ksi, \eta$, to

$$
\xi = \frac{1}{|D|} \iint_D x dx dy \\
\eta = \frac{1}{|D|} \iint_D y dx dy \\
$$

<!-- po co jest nam środek ciężkoći? Żeby dawać zadania, bo tak to wygląda jak zwykłę liczenie całki a jak się powie "Oblicz środek ciężkości" to brzmi to bliżej zastosowania czyli bardziej Górniczo-Hutniczo-->

```{note}
Objętość bryły jest równa polu powierzchni obszaru zakreślającego bryłę pomnożonemu przez drogę jaką przebył środek masy.
```
