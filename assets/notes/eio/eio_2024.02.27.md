## Ruch Falowy

### Uwagi wstępne

- Rozważamy fale sprężyste

```{admonition} fala
Falą nazywamy zaburzenie ośrodka rozchodzące się w przestrzeni
```

```{admonition} Ośrodek sprężysty
To taki ośrodek, który spełnia założenia prawa Hook'a
```

```{admonition} Fale sprężyste
to fale rozchodzące się w ośrodku sprężystym
```

### Podział fal ze względu na kierunek propagacji

| Fale poprzeczne                                                           | Fale Podłużne                                                 |
|---------------------------------------------------------------------------|---------------------------------------------------------------|
| ruch cząsteczek następuje w kierunku prostopadłym do kierunku propagacji  | wszystkie cząsteczki drgają równolegle do kierunku propagacji |
| występuje tylko w ciałach stałych                                         | mogą się rozchodzić w gazach cieczach i ciałąch stałych       |
|                                                                           | przykład: sprężyna, pręt w imadle                             |

| Fale Płaskie                                                    | Fale Kuliste                                                            |
|-----------------------------------------------------------------|-------------------------------------------------------------------------|
| czoło fali jest odcinkiem prostej (lub fragmentem płaszczyzny)  | powierzchnie falowe rozchodzą się symetrycznie we wszystkich kierunkach |

```{admonition} Fala okresowa (periodyczna)
Fukncja opisująca kształt fali jest funkcją periodyczną.
```

```{admonition} Fala o stałym kształcie
taka fala, która nie zmienia kształtu podczas rozchodzenia się w przestrzeni
```

#### Przykład

Rozważmy pojedynczy impuls falowy fali o stałym kształćie. kształt odkształćenia można opisać w postaci funkcji
$\psi(x, t)$ Można zapisać jako $\psi(x +- v * t)$.

Rozważmy falę sinusoidalną:

<!--TODO: check this-->
$$
\psi(x,t) = A * sin(x+- v * t) = A sin(2 \pi (\frac{x}{\lambda} +- \frac{t}{T})) = A sin(kx +- \omega t) \\
k = \frac{2\pi}{\lambda} \\
k * v = \omega \\
k = lambda * f \\
\psi(\vec{r}, t) = A sin(\vec{r}* k - \omega t) = \hat{A} * e^{i * (k * \vec{r} - \omega t)}
$$

```{admonition} wektor falowy
ma tki kierunek i zwrot jak propagacja fali w przestrzeni
```


#### Równanie D'Aramberta
Każda fala o stałym kształcie spełnia poniższe równanie

$$
\frac{\partial^2 \psi}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 \psi}{\partial t^2} \\
$$

$$
\psi(x,y,z,t) \\
\frac{\partial^2 \psi()}{\partial t^2} = v^2 * \Delta \psi
$$
