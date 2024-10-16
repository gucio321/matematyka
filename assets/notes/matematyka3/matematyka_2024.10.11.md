- egzamin pisemny (część teoretyczna i obliczeniowa)
- kolokwium poprawkowe razem z egzaminem
- zbió© zadań Stańkiewicza (Witold Stańkiewicz) - Zadania z Matematyki dla wyższych uczelni technicznych (cz. 1 B) [link](http://www.wzim.interblock.pl/Matematyka/Literatura/W.Stankiewicz.-.Zadania.z.Matematyki.Dla.Wyzszych.Uczelni.Technicznych.czesc.B.pdf)
- Stańkiewicz + Wojtowicz (część 2)


## szeregi liczbowe (pojęcie zbierzności sz.l.)

dla ciąŋu $a_n$ definiujemy ciąŋ $s_n$ gdzie $s_1 = a_1$ i $s_{n+1} = s_n + a_n$

Mówimy, że szereg $a_n$ jest zbierzny jeżeli ciąg $s_n$ ma granicę właściwą $S$, wtedy $\sum a_n = S$.

```{admonition} twierdzenie
z: Szereg $a_n$ jest zbierzny

T: ciąg wyrazów z tego szeregu zmierza do 0

D:
$$
a_n = s_n - s_{n-1} \\
n \to \infty \\
a_n = S - S = 0
$$

przykładowo szereg $\frac{1}{n}$ nie jest zbierzny, bo
$\lim s_n - s_{2n} \to \frac{-1}{2}$
```

<!--bo, to jest skrót od ponieważ, jest mniej eleganckie ale 4 razy krótsze-->>


Szereg liczbowy jest bezwzględnie zbierzny jeżeli 
zbierzny jest szereg szereg wartości bezwszględnych

### szereg anharmoniczny

szereg $\frac{(-1)^n}{n}$ jest zbierzny (later), ale nie jest zbierzny bezwzględnie (szereg harmoniczny nie jest zbierzny).

### Kryteria zbierzności szeregu

- kryterium porównawcze $|a_n| < |b_n|$ i $b_n$ jest bezwzględnie zbierzny $\Rightarrow$ to znaczy że $a_n$ również


### Kryterium Cossiego

$\gamma = \lim \root{n}{|a_n|}
jeżeli $\gamma < 1$  to szereg $a_n$ jest bezwzględnie zbierzny.
jeżeli $\gamma > 1$ nie jest bezwzględnie zbierzny (jest można nawet powiedzieć rozbierzny).

### Kryterium d'Alamberta

$\gamma = \lim \frac{a_{n-1}}{a_n}$ dalej tak samo jak wyżej
