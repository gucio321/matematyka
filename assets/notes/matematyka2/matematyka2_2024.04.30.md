$$
\int_{k (a\to b)} \vec{F} \cdot d\vec{r} = - \int_{k (b\to a)} \vec{F} \cdot d\vec{r}
$$

<!--statujemy NAJNOWSZE techniki audio-wizualne, tzw. Animację Multichromatyczną *animacja skłąda się ze dwóch okręgów i strzałki-->

```{admonition} def: Obszar Jednospójny
$D \in \mathbb{R^2}$ nazywamy obszarem jednospójnym, jeżeli
brzeg tego obszaru jednego kawałka
```

```{admonition} tw. Greena
$D$ jest obszarem jednospójnym.
Krzywa $k=\partial D$ jest zorientowana dodatnio, wtedy

$$
\int_{k} \vec{F} \cdot d\vec{r} = \iint_{D} \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dxdy
$$
```

Można sforumować następująće twierdzenia:
Pole jest ptencjalne (gradientowe) jeżeli
1. $\oint_{k} \vec{F} \cdot d\vec{r} = 0 \Leftrightarrow \vec{F}$ jest polem gradientowym
2. $\int \vec{F} \cdot d\vec{r}$ nie zależy od drogi, tylko od punktów początkowego i końcowego
3. $\frac{\partial Q}{\partial X}$ i $\frac{\partial P}{\partial y}$ są ciągłe na $D$

