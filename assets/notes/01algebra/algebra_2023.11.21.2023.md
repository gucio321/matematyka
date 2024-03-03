- **baza** - zbiór wekorów liniowo niezależnych generujących przestrzeń
- **wymiar** - liczność bazy

aby przedstawić wektor w bazie _kanonicznej_ w innej bazie
należy rozwiązać układ równań ($b_1' = \alpha~b_2' = \beta$)

#### Macierz Przejścia

niech $b_1, b_2...$ - stara baza i $b_1', b_2' ....$ nowa baza.

Wektory ze starej bazy można przedstawić jako kombinacje współrzędnych z nowej bazy oraz
wypisac w macierzy w kolumnach.
Następnie należy znaleźć macierz odwrotną.

- $P_{B\to B'} = (P_{B'\to B})^{-1}$
- $P_{B \to B'} * P_{B' \to B''} = B_{P \to B''}$

### Odwzorowania Liniowe

- Załóżmy dwie przestrzenie liniowe **nad tym samym ciałem**
- morfizm przestrzeni liniowych (odwzorowanie liniowe) zachodzi jeżeli
zachodzi odwzorowanie działań w tych przestrzeniach

$$
\phi(\alpha x) = \alpha \phi(x) \\
\phi(x_1 + x_2) = \phi(x_1) + \phi(x_2)
$$

```{important}
Jeżeli występuje translacja (dodanie stałęj) odwzorowanie nie jest liniowe (nie spełnia warunku addytywności).
```

```{tip}
operator różniczkowania $\frac{dy}{dx}$ jest odwzorowaniem liniowym
```

```{note}
Przy odwzorowaniu liniowym $0 \to 0$
```

- odwzorowanie może być surjekcją (tożsamość obu zbiorów) (**epimorfizm**)
- aby sprawdzić czy odwzorowanie jest injekcją można sprawdzić czy $0 \to 0$

```{tip}
Zbiór wszystkich odwzorowań liniowych V w W oznaczamy przez $Hom_k(V, W)$
```

```{important}
Jezeli w liniowym występuje translacja nie jest ono liniowe.

$$
\phi : \mathbb{R} \to \mathbb{R},~\phi(x) = ax + b \\
$$

Niech $x_1 = 1 \land x_2 = 2$ wtedy:

$$
\begin{matrix}
\phi(1+2) = a(1 + 2) + b  = 3a + b \\
\phi(1) + \phi(2) = a + b + 2a + b = 3a + 2b
\end{matrix} \Rightarrow \phi(1+2) \neq \phi(1) + \phi(2)
$$
```
