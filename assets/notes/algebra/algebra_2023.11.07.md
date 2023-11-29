## Przestrzenie wektorowe

```{admonition} Przestrzeń Wektorowa
(K, +, C, $*$) jest grupą abelową, natomiast `V` zbiorem ($V \neq \emptyset$).
 
- (V, +) jest grupą abelową
- $\forall v, v \in V \quad \forall \alpha \in K \quad \alpha * (v + v) = (\alpha * v) + (\alpha * v)$ (występuje rozdzielność mnożenia względem dodawania w mnożeniu **sumy wektorów** przez **skalar**)
- $\forall v \in V \quad \forall \alpha, \beta \in K \quad (\alpha + \beta) * v = (\alpha * v) + (\beta * v)$ (występuje rozdzielność mnożenia względem dodawania w mnożenia **sumy skalarów** przez **wektor**)
- $\forall v \in V \quad \forall \alpha, \beta \in K \quad \alpha * (\beta * v) = (\alpha * \beta) * v$ (mnożenie wektora i skalarów jest łączne)
- $\forall v \in V \quad 1 * v = v$ (występuje element neutralny)
- możliwe jest mnożenie przez skalar
```

```{tip}
Elementy zbioru V nazywamy wektorami, a K - skalarami
```

```{note}
Zbiór $(\mathbb{R}^2, +, \mathbb{R}, *)$ to tradycyjny zbiór wektorów na płaszczyźnie dwuwymiarowej.
$V = \mathbb{R}^2$ określa dwa wymiary palszczyzny a $K = \mathbb{R}$ to ciało (zbiór) tzw. skalarów.
```

### Podprzestrzenie liniowe

Zbiór $U$ nazywamy podprzestrzenią przestrzeni V gdy działania zadeklarowane dla te podprzestrzeni są w niej wewnętrzne.

```{note}
Innymi słowy aby sprawdzić czy dany zbiór jest podprzestrzenią przestrzeni V dla dla dwuch wektorów $v_1 i v_2 \in V$ oraz skalara $\alpha$

$$
v_1 + v_2 \in V' \land \alpha v_1 \in V'
$$
```

```{important}
**0** musi należeć do podprzestrzeni

$$
niech~(\mathbb{R^3}, +, \mathbb{R}, *) \\
-1 * v_1 = -v_1 \in \mathbb{R}^3 \\
v_1 - v_1 = 0 \\
$$
```

```{tip}
Jeżeli w definicji przestrzeni występuje translacja (dodanie stałej) przestrzeń ta nie jest podprzestrzenią przestrzeni V.

$$
V = (\mathbb{R}^3, +, K, *) \\
U = \left\{(x + 1, y + x, z) : x, y, z \in \mathbb{R} \right\} \\
\\
x_1 + 1 + x_2 + 1 = (x_1 + x_2) + 2 \neq (x_1 + x_2) + 1
\\
\\
V = (\mathbb{R}^3, +, K, *) \\
U = \left\{(2x, y + x, z) : x, y, z \in \mathbb{R} \right\} \\
\\
2x_1 + 2x_2 = 2(x_1 + x_2) \\
\alpha 2 x_1 + \alpha 2 x_2 = \alpha 2 (x_1 + x_2)
$$

Analogicznie można postępować dla innych wyrazów.
```

### Liniowa zależność wektorów

```{admonition} liniowa zależność wektorów

Wektory są liniowo niezależne gdy żadnego z nich nie można przedstawić w formie kombinacji liniowej pozostałych.

Przykładowo $v = \alpha v_1 + \beta v_2 + \gamma v_3$ nie jest liniowo niezależny.

Biorąc pod uwagę inny przykład:

$$
v = (5, 4, -18) \\
v = 5 \hat{i} + 4 \hat{j} - 18 \hat{k} \\
gdzie:\\
\hat{i} = (1, 0, 0) \\
\hat{j} = (0, 1, 0) \\
\hat{k} = (0, 0, 1) \\
$$

:::{tip}
To tak jak w macierzach, gdzie jeden z rzędów można wyzerować za pomocą innych.
:::

:::{note}
Aby sprawdzić czy wektory są liniowo niezależne budujemy macierz
z wektorami wpisanymi w kolumny (tak aby poróœnywać x-owe współrzędne e.t.c.) i przyrównujemy do (0,0,...,0)
i obliczamy jej rząd.
:::
```

```{admonition} Generatory
Zbiór generatorów to zbiór wektorów pozwalających na zapisanie każdego
innego wektora w danej podprzestrzeni.

$$
v = \alpha w_1 + \beta w_2 + ... + \theta w_n
$$

- zbiór generatorów oznaczamy jako $W$
- natomiast generowaną przez nie podprzestrzeń $limW$
```

```{admonition} Twierdzenie o geneowaniu podprzestrzeni $\mathbb{R}^n$
Wektory $v_1, v_2, ..., v_k$ generują przestrzeń $\mathbb{R}^n$ (o n wymiarach) $\Leftrightarrow$ $rowA$ (rząd macierzy A) jest równy n.
Macierz A to taka macierz, która składa się w kolejno wpisanych w wierszach wektorach v.

:::{tip}
$k \geq n$ tzn. że generatorów może być więcej niż wymiarów przestrzeni, jednak jeżeli tak jest
oznacza to że kilka z nich ($k-n$) jest liniowo zależnych.
:::
```


