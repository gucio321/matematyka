## Dobra, po kolei:

ref;
- https://www.youtube.com/watch?v=OvTEhNL96v0
- https://home.agh.edu.pl/~mariuszp/wfiis_stat/wyklad_stat_4.pdf

### Wartość Oczekiwana

Wartość oczekiwana to teoretyczna (bo liczymy prawdopodobieństwo) wartość
średniej pomiarów/danych.

$$
E(X) = \sum_{i=1}^{n} x_i * p(x_i)
$$

```{tip}
Dlaczeog średnia?

Rozważmy taką tabelkę:

| $x_i$    | 1 | 2 | 3 |
|----------|---|---|---|
| $p(x_i)$ | 0.2 | 0.5 | 0.3 |

To przecież oznacza, że gdybyśmy zrobili 10 pomiarów, to 
2 z nich to byłoby 1, 5 - 2 i 3 3.
Prawdopodobieństwo $p(x_i) oznacza procentowy udział $x_i$ w docelowych pomiarach.

$$
\bar{x} = \frac{1 + 1 + 5 * 2 + 3 * 3}{10} = (1 * 0.2) + (2 * 0.5) + (3 * 0.3) = \sum_{i = 1}^{3} x_i * p(x_i)
$$

hehe, mam nadzieję że to jasne.
```

```{note}
Oznaczenia:
na wartość oczekiwaną X mamy następujące oznaczenia
- $E(x)$ (z youtube) również $\mu$
- profesor oznacza jako $\epsilon\left[x\right] = \left<x\right>$
```

```{note}
Wartość Oczekiwana Funkcji Zmiennej losowej $E(g(x)) = \sum_{i} g(x_i) * p(x_i)$
```
