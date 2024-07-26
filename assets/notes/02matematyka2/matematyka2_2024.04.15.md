## Rachunek całkowy wielu zmiennych

### Całka podwójna

Niech $f = f(x,y)$

- $F: P \to \mathbb{R} ~ P = [a,b] \times [c,d]$

Przypuśćmy, że mamy prostokąt (płąszczyznę) nad którą znajduje się wykres $f$.

Załużmy, że musimy obliczyć objętość pod wykresem $f$.

Tworzymy 3 sumy (jakd dla całek) dla prostopadłościanów skłądających się na wykres funkcji.
($s_n$ dla najmniejszej wartości, $S_n$ dla największej oraz $\sigma$)

```{admonition} Definicja
Jeżeli przy każdym, coraz drobniejszym, podziale prostokąta $P$ ciąg $\sigma_n$ dąży do tej samej granicy niezależnej od podziału, ani od wyboru punktów pośrednich, to granicę tę nazywamy
całką podwójną funkcji $f$ po prostokącie $P$ i oznaczamy $\iint_P f(x,y) dxdy$.
```

```{note}
Całka $\iint_P f(x,y) dxdy$ nie zawsze istnieje
```

### Całka podwójna nie dla prostokąta

jeżeli nie mamy prostokąßa, rozszeżamy naszą funkcję żeby była na prostokącie
Przykłądowo: $f = \sqrt{1 - x^2 - y^2}$

```{admonition} zbiór miary 0
Jeżeli zbiór $A$ jest zbiorem miary 0, to całka podwójna po $A$ jest równa 0.

przykładowo:
- punkt jest miary 0 ponieważ można go pokryć prostokątem o dowolnie małym polu
```

```{admonition} podstawowe twierdzenie
Jeśli $F:P \to \mathbb{R}$ i zbiór punktów nieciągłości $F$ ma miarę 0,
to $F$ jest całkowalna na $P$.
```

Aby rozpoznać czy brzeg jest miary 0, można posłużyć się następującym
twierdzeniem:

```{admonition} Twierdzenie
jeżeli $f: \mathbb{R} \to \mathbb{R}$ jest całkowalna, to jej wykres
(krzywa) ma miarę 0.
```

Wniosek:
> Jeżeli $f: [a,b] \to \mathbb{R}$ jest ciągła $\Rightarrow$ jej wykres ma miarę 0.

Na przykłądzie wykresu koła:
- brzeg to okrąg
- okrąg można traktować jako wykres funkcji
- wykres jest ciągły
- wykres jest miary 0
- funkcja jest całkowalna

<!--skoro jesteśmy już uspokojeni, to można iść... możecie iść gdzie kto chce, ja idę na obiad.-->
