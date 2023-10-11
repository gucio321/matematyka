## Ciało liczb zespolonych
- w przeciwieństwie do liczb rzeczywistych nie można ich przedstawić
w postaci linearnej
- dlatego też nie można powiedzieć że dana liczba jest ujemna/dodatnia
- liczba zespolona to para
- $i^2 = -1$

### Dzielenie

Przy dzieleniu liczb zespolonych należy pomnożyć przez czynnik sprzężony
(tak jak usuwanie niewymierności z mianownika)

### moduł liczby zespolonej

Utożsamiany z długością wektora będącego interpretacją liczby urojonej.
niech $z = (x, yi)$

$$
|z| = \sqrt{x^2 + y^2}
$$

### Postać trygonometryczna liczyb zespolonej
$$
niech~z = x + yi \neq 0 \\
z = |z|(\frac{x}{|z|}+\frac{y}{|z|})\\
\exists \phi ~ cos \phi = \frac{x}{|z|} \land sin \phi = \frac{y}{|z|}
z = |z|(cos \phi + i * sin \phi)
$$

$arg z$ to tzw. argument główny gdzie $argz \in [0, 2 \pi]$

#### potęgowanie liczby zespolonej w postaci trygonometrycznej
Wzór de Moivre'a
$$
\frac{z_1}{z_2} = \frac{|z_1|}{|z_2|} (cos(\alpha - \beta) + i sin(\alpha - \beta)) \\
z^n = |z|^n (cos n \phi + i * sin n \phi)
$$

### postać wykładnicza

$$
e^{i \phi} = cos \phi + i sin \phi
$$$

$$
z_k = \root{n} \of{r}(cos \frac{\phi + 2k \pi}{n} + i ~ sin\frac{\phi + 2k \pi}{n} ~~ k = 0 , 1 ... n
$$

```{important}
Pierwiastek `n` stopnia **ma `n` rozwiązań**
```

### zasadnicze twierdzenie algebry

Każdy wielomian dodatniego stopnia ma rozwiązania w $\mathbb{C}$
