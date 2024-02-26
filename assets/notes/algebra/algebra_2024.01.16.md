## Przestrzenie euklidesowe

```{admonition} Macierze ortogonalne
TO takie macierze, które $A^T * A = I$.

::::{note}
$$
detA \neq 0 \land \left( detA^2 = 1 \Rightarrow detA = 1 \lor detA = -1 \right)
$$
:::
```

```{tip}
Jeżeli macierze A i B są ortogonalne, wtedy $A * B$ też jest ortogonalna.
```

Własności baz ortonormalnych. Niech $B_{\perp}$ i $B_{\perp}'$ będą dwiema bazami ortonormalnymi.
Niech $P_{B \to B'}$ będzie macierzą przejścia pomiędzy nimi. Wtedy $P$ również jest ortogonalna.

```{tip}
Zauważ, że $P_{B' \to B} = P_{B \to B'}^{-1} = P_{B \to B'}^T$
```

```{admonition} Izometrie liniowe
to przekształcenia które nie zmieniają odległości między wektorami.

$$
|| u - w || = || \phi(u) - \phi(w) ||
$$

Można wysnuć wniosek, że $\phi$ jest ortogonalne.

Możliwe typy Izormorfizmów **liniowych** to:
- obrót
- odbicie (względem prostej o równaniu $y = tg\left(\frac{\alpha}{2}\right)x$)
```
