podzbiorami przestrzeni wektorowych $\mathbb{R}^2$ i $\mathbb{R}^3$ są:
- proste
- płaszczyzny

```{admonition} kombinacja zerowa
$$
a_1 v_1 + a_2 v_2 + ... + a_n v_n = 0
$$
```

```{admonition} Powłoka liniowa
$$
\left\{v = a_1 v_1 + ... + a_k v_k~:~v_1...v_k \in V \quad a_1...a_k \in A\right\}
$$

Jest podprzestrzenią
```

### Baza

Układ wektorów (generatorów) można nazwać bazą, jeżeli:
- są niezależne liniowo
- generują przestrzeń wektorową

```{admonition} Baza 
Podsumowując: układ n wektorów-generatorów liniowo niezależnych w przestrzeni n-wymiarowej jest bazą

:::{important}
przestrzeń $\left\{\bf{0}\right\}$ nie posiada bazy.
:::

:::{tip}
Najprostszą bazą przestrzeni 3-wymiarowej jet układ wersorów $(\hat{j}, \hat{k}, \hat{l})$
:::

:::{admonition} Reper Bazowy (aka Baza uporządkowana)
To uporządkowany ciąg wektorów bazowych.
:::
```

```{admonition} Wymiar przestrzeni wektorowej V
To liczba eleentów bazy i oznaczamy $dimX$ gdzie X to przestrzeń.

:::{note}
$dim{0} = 0$
:::

:::{tip}
Wymiar podprzestrzeni jest mniejszy niż wymiar przestrzeni wyjściowej.
Jeżeli $dimV = dimW \Rightarrow W = V$
:::
```

```{tip}
Współrzędnymi wektora nazywamy skalary $v = \alpha_1 v_1 + \alpha_2 v_2 + ... + \alpha_n v_n$
i zapisujemy jako $v = [\alpha_1, \alpha_2, ..., \alpha_n]_B$
```

### Macierz Przejścia

```{note}
Oznaczenie: $P_{B \to B'}$
```

```{admonition} Macierz przejścia
Wektor v należy do przestrzeni liniowej V.

W bazie `B` można zapisać go jako $v = [x_1, x_2, ..., x_n]_B$ natomiast w bazie $B'$:
$v = [x_1', x_2', ..., x_n']_{B'}$

__W takim przypadku macierz przejścia można powiązać z wektorami w poszczególnych bazach jako:__ $\bf{X = P_{B \to B'} X'}$.

X to wypisane w jdenej kolumnie współrzędne w bazie B a $X'$ - w bazie $B'$.

$$
X = \begin{Bmatrix}
x_1 \\
x_2 \\
... \\
x_n
\end{Bmatrix}
\quad
X' = \begin{Bmatrix}
x_1' \\
x_2' \\
... \\
x_n'
\end{Bmatrix}
$$

$P_{B \to B'}$ to obraz azy $B'$ w bazie $B$

$$
P_{B \to B'} = \begin{Bmatrix}
b_{1_1} & b_{1_2} & ... & b_{1_n} \\
b_{2_1} & b_{2_2} & ... & b_{2_n} \\
... & ... & ... & ... \\
b_{n_1} & b_{n_2} & ... & b_{n_n} \\
\end{Bmatrix}
$$
```
