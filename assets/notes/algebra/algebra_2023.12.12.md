### Własności spektrum

- spec(A) = spec(A^T)
- spec(A^n) = spec(A)^n
- \frac{1}{\lambda} = spec(A^{-1})

```{admonition} Kiedy można dokonać diagonalizacji macierzy odwzorowania?
Jeżeli wszystkie pierwiastki wielomianu (z któ©ego szukamy wartości włąsnych)
są krotności 1.

Inaczej musi istnieć baza z wektoróœ własnych.
```

```{note}
macierze reprezentujące to samo odwzorowanie **w różnych bazach** są do siebie podobne
```

### Schemat rozwiązywania zadań:

- załóżmy, że mamy dane odwzorowanie.
:::{tip}
Jeżeli odwzorowanie mamy zadane w następujący sposób:

$$
\phi(1, 0, 0) = (1, 0, 0) \\
\phi(0, 1, 1) = (0, 2, 2) = 2 * (0, 1, 1) \\
e.t.c.
$$

Oznacza to że mamy zadane już wektory/wartości własne w tym przypadku:

$$
\begin{matrix}
\lambda_1 = 1 && v_1 = (1, 0, 0) \\
\lambda_2 = 2 && v_2 = (0, 1, 1)
\end{matrix}
$$
:::

- Najpierw należy skonstruować macierz odwzorowania
- teraz od wszystkich elementów na diagonali macierzy odejmujemy $t$ (bądź $\lambda$ - ja przyjmuję tutaj $t$ dla kompatybilności z panią dr)
```{tip}
Jeżeli macierz ma postać trujkątną, można pominąć ten i następny krok
przyjmując za $\lambda$ elementy na diagonali.
```
- Obliczamy wyznacznik z którego później wyliczamy wartości $t$.
```{important}
Należy pamiętać o możliwych wartościach $t$ ($\mathbb{R}$ czy $\mathbb{C}$)
```

```{important}
Jeśli wyszło nam w sumie (licząc krotności) mniej $\lambda$ nniż wynika z wymiaru przestrzeni
(na przykład część rozwiązań wyszła urojona i nie było to dopuszczone)
macierz **NIE** jest diagonalizowalna.
```

```{admonition} Spektrum
Otrzymane wyniki nazywamy **spektrum** odwzorowania.
```

``` {admonition} Spektrum proste
Jeżeli wszystkie $t$ są jednokrotnymi rozwiązaniami równania, i jest ich dokładnie tyle
co wymiar przestrzeni, to mamy do czynienia ze spektrum prostym - pomiń następny krok (jeżeli zadanie tego nie wymaga)
```

- Obliczanie wektorów Własnych. Aby to zrobić rozwiązujemy następujące równanie:

$$
\phi(v) = \lambda v \\
A * v = \lambda * I *  v \\
(A - \lambda * I) * v = 0
$$

Gdzie: $A$ to macierz odwzorowania, $\lambda$ to dana wartość $t$ a $v$ to szukany wektor własny

```{important}
jeśli $\lambda$ jest n-krotna należy sprawdzić następujący warunek:
$n = dim E_{\lambda} = dim A - Row(A-\lambda I)$
Jeżeli warunek nie jest spełniony - macierz nie jest diagonalizowalna.
```

- Teraz nowa macierz tego przekształcenia to

$$
\begin{Bmatrix}
\lambda_1 && 0 && ... && 0 \\
0 && \lambda_2 && ... && 0 \\
... && ... && ... && ... \\
0 && 0 && ... && \lambda_n
\end{Bmatrix}
$$

A więc macierz ze współczynnikami $\lambda$ na diagonali.

```{note}
Nowa macierz odwzorowania zapisana jest dla bazy złożonej z wektorów własnych!
```

```{tip}
załużmy wektor $v$ w bazie kanonicznej. Aby przekształcić go taką macierzą diagonalną należy:
- Pomnożyć lewostronnie wektor przez macierz przejścia (złożoną z wektorów nowej bazy - wektorów własnych)

$$
P_{B_k \to B} * v
$$

- Pomnożyć lewostronnie przez nową macierz diagonalną $D$

$$
D * P_{B_k \to B} * v
$$

- na koniec można powrócić do bazy kanonicznej

$$
P_{B_k \to B}^{-1} * D * P_{B_k \to B} * v
$$

```

```{tip}
Wizualizacja graficzna!

<iframe width="560" height="315" src="https://www.youtube.com/embed/PFDu9oVAE-g?si=QySpNWEbMN5QoFL6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

```
