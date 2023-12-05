```{tip}
Aby obraz wektorów liniowo niezależnych był liniowo niezależny
odwzorowanie musi być injektywne.

_Na przykład rzutowanie $\mathbb{R}^3$ na płaszczyznę $OY$_
```

```{note}
macierz reprezentuje odwzorowanie liniowe
- dodawanie macierzy reprezentuje dodawanie odwzorowań
- natomiast mnożenie macierzy to składanie
```

``` {admonition} Reprezencacja macierzowa odwzorowań liniowych
Macierz której kolumny nsą **obrazami** wektorów bazowych nazywamy
reprezentacją macierzową odwzoorowania liniowego
```

```{admonition} Jądro
Przeciwobraz wszystkich elementów które przechodzą na 0.

Obliczamy Je następująco: $\phi(x) = 0$

Przykładowo

$$
\text{dla v w postaci}~v=(x,y,z) \\
\phi(v) = (2x, y, x+y) \\
\phi(v) = 0 \\
(2x, y, x+y) = 0 \Leftrightarrow x = 0 \land y = 0 \Rightarrow z \in \mathbb{R} \\
ker\phi = \left\{(0,0,z), z \in \mathbb{R}\right\} \\
dimKer\phi = 1
$$

**Przeciwobraz** - elementy które "podajemy" do odwzorowania (jak dziedzina funkcji)
:::{tip}
$$
\begin{matrix}
\text{przeciwobraz} &=& \text{Dziedzina} \\
\text{Obraz} &=& \text{Zbiór Wartości}
\end{matrix}
$$
:::
```

