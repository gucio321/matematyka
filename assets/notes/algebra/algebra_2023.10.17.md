## Macierze

Oznaczenie: $M_{m \times n} (K)$ gdzie
- m, n - wymiary macierzy
- K - ciało na którym określamy macierz

```{note}
Dwie macierze są równe gdy ich wymiary są równe oraz wszystkie wartości są równe
```

```{tip}
**Macierzą kwadratową** nazywamy macierz, w której $m=n$
```

```{admonition} Macierz zerowa
to taka macierz $0_{m \times n}$ gdzie wszystkie elementy są równe 0
```

```{admonition} Macierz diagonalna
Macierz, w której niezerowe elementy leżą jedynie na przekątnych
```

### Działania na macierzach

- Dodawanie (i odejmowanie) macierzy których wyrazy są równe wykonujemy poprzez dodawanie odpowiednich wyrazów
- Mnożenie przez liczbę - każdy wyraz macierzy mnożymy przez liczbę
- transponowanie - wiersze zmieniają się na kolumny
- mnożenie macierzy przez macierz macierz A musi mieć tyle samo kolumn co wierszy

### Własności działań

```{note}
działania są dziedziczone ze zbioru $\mathbb{R}$
```

- składanie odwzorowań jest łączne, ale **nie** przemienne
Macierz diagonalna jednostkowa jest elementem neutralnym.
Na przykład
$$
\begin{bmatrix}
1&0 \\
0&1
\end{bmatrix}
$$

- transponowanie:
$$
(A^T)^T = A
$$

```{important}
$$
(AB)^T = B^T A^T
$$
```

### Suma elementów na przekątnych

$$
tr \begin{vmatrix}
\bf{1}&0&0 \\
2&\bf{-7}&2 \\
0&1&\bf{3}
\end{vmatrix} = 1-7+3 = -3
$$

`tr` to ślad macierzy - suma elementów na przekątnej

### Macierze symetryczne i antysymetryczne


```{admonition} Twierdzenie
każdą macierz kwadratową można rozbić na dwie macierze,
z których jedna jest symetryczna, a druga antysymetryczna
```

### Wyznacznik macierzy

```{admonition} Definicja
wyznacznik to liczba $detA$ taka, że:
- dla n = 1 $detA = a_11$
- dla $n \geq 2$ $\sum_{j=1}^n (-1)^{i+j} * a_ij * detA_ij
gdzie $detA_ij$ to wyznacznik (tzw. minor) macierzy powstałej po skreśleniu i-ego wiersza i j-tej kolumny
```

$detA = detA^T$

```{tip}
dla macierzy trujkątnych górnych i dolnych detA to iloczyn elementów na przekątnej
```

#### zmiany na macierzy nie zmieniające wyznacznika

- $detA = detA^T$
- jeżeli w jednej kolumnie są same 0, detA = 0
- $det(nA) = n * detA~ n\in \mathbb{R}$
- dla $A = B+C$ $detA = detB + detC
- po zmianie kolumn miejscami wyznacznik zmieni znak
- jeżeli dwie kolumny są proporcjonalne detA = 0
- jeżeli kolumna jest kombinacją liniową pozostałych detA = 0
- do kolumny można dodać kombinację liniową pozostałych co nie zmieni wyznacznika

### Macierz odwrotna
macierze kwadraowe

$$
\exists A^{-1} ~ A * A^{-1} = I \\
$$

```{note}
macierz osobliwa jeżeli detA = -
```

```{note}
Macierz jest odwracalna jeżeli jest niosobliwa
```

#### Obliczanie macierzy odwrotnej

- Macierz odwrotna to taka macierz, która składa się z odpowiednich dopełnień arytmetycznych
wszystkich elementów macierzy początkowej.
- dopełnienie arytmetyczne elementu `a_ij` to wyznacznik macierzyz z wykreślon `i`tym rzędem i `j`otą kolumną pomnożony przez $\fra{1}{detA}$
