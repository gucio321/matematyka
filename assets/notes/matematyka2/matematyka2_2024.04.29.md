$$
\psi = \frac{1}{|D|} \iint_D x dx dy
$$

```{note}
Przykłąd:

rozważmy pókole (fragment łuku)

$$
x = r cos \phi \\
y = r sin \phi \\
\phi \in [0, \pi] \\
{x'}^2 = r^2 sin^2 \phi \\
{y'}^2 = r^2 cos^2 \phi \\
\sqrt{{x'}^2 + {y'}^2} = r \\
\psi = \frac{1}{\pi r} \int_0^\pi r cos \phi r^2 d\phi = 0 
\etha = \frac{2r}{\pi}
$$
```

```{important}
:::{admonition} reguła guldina
Pole powierzchni otrzymanej przez obrót łuku `ł` dookoła
prostej `e` (łuk nie przecina prostej) wynosi długość łuku razy droga
przebyta przez środek ciężkości łuku.
:::`

:::{note}
objętość takiego obszaru jest równe pole tego co się obraca razy droga środka ciężkości
:::

$$
4 \pi r^2 = 2 \pi \etha  \pi r \\
2 r = \etha  \pi \\
\etha = \frac{2r}{\pi} \\
$$
```

<!--wyszło tak samo, oczywiście wyszło tak samo, dlatego że się nie pomyliłem, albo pomyliłem się dwa razy-->

## Całki Krzywoliniowe

### Całka krzywoliniowa nieskierowana

```{admonition} definicja
jeżeli dla każdego podziału krzywej `k` suma $\sum f(N_i) \Delta s$ dąży
przy średnicy podziału do zera dąży do tej samej liczby niezależnej od punktów podziału
e.t.c., to granicę tę nazywamy całką krzywolinią nieskierowaną i
oznaczamy $\int_k f(s) ds$
```

niech

$$
x = x(s) \\
y = y(s)
$$

gdzie $s$ to długość ktrzywej liczona od punktu a

### Całka krzywoliniowa skierowana

w obszarze pewnej krzywej rozważmy pole wektorowe.
 
 ```{admonition} def
 jeżeli ... granicę tę nazywamy całką krzywoliniową skierowaną z pola $\vec{R}$ wzdłuż krzywej `k` i oznaczamy $\int_k \vec{R} \cdot d\vec{s}$

$$
\int p(x(t))\frac{dx}{dt} + q(y(t)) \frac{dy}{dt}
$$
 ```
