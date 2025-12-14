## Notatki z wykładu na youtube

`https://www.youtube.com/watch?v=yQDfVJzEymI&list=PLyYrySVqmyVPzvVlPW-TTzHhNWg1J_0LU`

### Półprzewodniki

Istnieją 2 sposoby przenoszenia ładunków w półprzewodniku:
- elektrony
- dziury

```{important}
Przenoszenie poprzez dziury jest wolniejsze niż poprzez elektrony gdyż technicznie wymaga ono uwolnienia elektronu z jednego wiązania i wychwyt przez wiązanie "z dziurom"
```

```{admonition} Definicja eV
Elektroo-volt, to ilość energii potrzebnej, aby przetransportować jeden elektron przez różnicę potencjałów jednego volta.
```

Wzór na ilość wolnych elektronów w półprzewodniku:

$$
n_i = 5.2 \cdot 10^{15} T^{\frac{3}{2}} \exp\left(-\frac{E_g}{2kT}\right)
$$

Gdzie:
- $T$ - temperatura bezwzględna
- $E_g$ - przerwa energetyczna


| $E_g$ [eV]  | Atom    |
|-------------|---------|
| 0.67        | German  |
| 1.12        | Krzem   |
| 2.5         | Diament |

```{note}
Wiemy, że diament jest izolatorem, dlatego jego energia jest tak duża.
```

```{tip}
Wiemy, że dla krzemu $n_i \approx 10^{10}$

Oznaczmy:
- $n$ - koncentracja (liczba / gęstość) wolnych elektronów
- $p$ - koncentracja dziur

```{tip}
Dla krzemu niedomieszkowanego (czystego) $n = p = n_i$
```


Domieszkowanie pozwala nam zwiększyć liczbę elektronów/dziur w półprzewodniku.
Domieszkujemy atomy z 5 lub 3 elektronami walencyjnymi.

Przykładowo, gdy chcemy zwiększyć liczbę elektronów, dodajemy atomy fosforu w liczbie $N_D$ (donorów) (zazwyczaj między $10^{15}$ a $10^{17} \frac{atom}{cm^3}$ atomów).
Jak widać, liczba domieszkowanych atomów znacząco przeayższa liczbę wolnych elektronów natywnie w krzemie $\Rightarrow n \approx N_D$.
Można także stwierdzić, że:

$$
n\cdot p = n_i^2
$$

### Domieszkowanie

`https://www.youtube.com/watch?v=NWolpDgi6_Y&list=PLyYrySVqmyVPzvVlPW-TTzHhNWg1J_0LU&index=2`

Gdy dodajemy $N_D$ atomów donorowych (np. fosforu) na $cm^3$, przyjmójemy że w materiale będziemy mieć $N_D$ wolnych nośników (tu elektronów).

```{tip}
Zakładamy, że $N_D \gg n_i$
```

Wyróżniamy 2 typy domieszkowania:
- materiał typu n (donor) - więcej elektronów
- materiał typu p (akceptor) - więcej dziur

### Przepływ nośników

**Dryf** to przepływ ładunków spowodowany różnicą potencjałów (polem elektrycznym).

Taki przepływ określa prawo Ohma $U = I\cdot R$. Jednak jak znaleźć R?
