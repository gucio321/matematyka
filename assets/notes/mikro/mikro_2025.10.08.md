## Logika cyfrowa

Wyróżniamy 2 stany logiczne: 0 (napięcie GND) oraz 1 (napięcie zasilania).

### Algebra Boole'a

Operacje elementarne:
- negacja $\bar{x}$
- $a + b$ (OR)
- $a \cdot b$ (AND)

podstawowe własności:
- $a*b = b*a$ (przemienność) [dualizm] $\Leftrightarrow a + b = b + a$
- $(a*b)*c = a*(b*c)$ (łączność)


Do opisu ukłądów logicznych używa się "tablicy prawdy" lub funkcji logicznych.

### Minimalizacja funkcji logicznych - Tablice Karnough

| $x_2 ~ x_1 x_0$ | 00 | 01 | 11 | 10 |
|------------------|----|----|----|----|
| 0                | 0  | 1  | 1  | 1  |
| 1                | 0  | 0  | 1  | 0  |

```{tip}
w pierwszym wierszu jest tzw. kod Gray'a
```

Teraz szukamy prostokątów o bogu $2^n$ (tabelka się loopuje). i zapisujemy sumę iloczynów albo i9loczyn sum

![Bramki](mikro/gates.png)
