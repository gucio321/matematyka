## Przestrzenie euklidesowe

```{admonition} Przestrzeń euklidesowa
to po prostu w dziwny sposób powiedziane "Iloczyn Skalarny".

To tak aprzestrzeń wektrowoa, nad któ©ą zdefiiowano iloczyn skalarny.

Oznaczenie: $\mathbb{E}^n$ to $\mathbb{R}^n$ ze zdefiniowanym standardowym iloczynem skalarnym.

:::{note}
standardowy iloczyn skalarny to funkcja zefiniwoana w następujący sposób

$$
u = (u_0, u_1, ... u_n) \\
w = (w_0, w_1, ... w_n) \\
s(u, w) = u \dot w = \Sigma_{i=0}^{n} u_i * w_i
$$
:::
```

```{admonition} Norma
Norma to dziwna nazwa na "długość wektora"

oznaczenie: $||v||$
:::{note}
- Norma spełnia zasadę liniowości
- $||v|| = 0 \Leftrightarrow v = \bf{0}$
- $||\alpha v|| = |\alpha| * ||v||$
:::

Przestrzeń wektorową ze zdefiniowaną normą nazywamy _Przestrzenią Unormowaną_
```

```{tip}
Jeżeli znamy iloczyn wektorowy możemy od razu zdefiniować normę.
Określamy ją następującym wzorem:

$$
||v|| = \sqrt{s(v, v)}
$$

Obrazowo:
- iloczynn skalarny $v \dot v$ lub $s(v, v)$ to po prostu z definicji
iloczynu skalarnego długość $v$ pomnożona przez rzut $v$ na $v$ czyli po prostu długość $v$
podniesiona do kwadratu
- gdy nałożymy na to pierwiastek otrzymamy długość $v$
```

```{admonition} Wektor unormowany
Również znany jako **wersor**.

Jesto to wektor w przestrzeni V którego norma wynosi `1`

:::{tip}
Każdy wektor z przestrzeni euklidesowej można unormować.

$$
\hat{v} = \frac{v}{||v||}
$$
:::
```

Znając powyższe zależności można określić
miarę kąta między wektorami.

$$
cso \angle (u, v) = \frac{u \dot v}{||u|| * ||v||}
$$

```{important}
To wszystko nie ma sensu dopuki togo nie zobaczysz, więc polecam
<iframe width="560" height="315" src="https://www.youtube.com/embed/LyGKycYT2v0?si=wuELwsKmKt-c6Mfc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{tip}
W przypadku ww. zależnośći warto rozważyć dwa skrajne przypadki:
- jeżeli wektory są współliniowe, to długość rzutu `u` na `v` ma długość całego `u`, więc $$\frac{\cancel{||u|| * ||v||}}{\cancel{||u||*||v||}} = 1 \Rightarrow cos \angle(u, v) = 0^o$
- jeżeli wektory są prostopadelk, długość rzutu `u` na `v` ma długość `0` z czego wynika, że $\frac{0 * ||v||}{||u||*||v||} = 0 \Rightarrow cos\angle(u,v) = 90^o$
```

```{admonition} Wektory ortogonalne
To inaczej wektory prostopadłe (aka $u \perp w$). Z tego również wynika, że
$u \dot w = 0$ (ofc w drugą stronę też to działa)
:::{important}
w tym przypadku jednak inna nazwa ma sens, ponieważ pojęcie wektoróœ ortogonalnych ma również
sens w większej liczbie wymiarów (np. 4)
:::
````
