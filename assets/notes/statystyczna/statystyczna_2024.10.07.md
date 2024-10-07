[https://home.agh.edu.pl/mariuszp](https://home.agh.edu.pl/mariuszp)

## Wstęp / pojęcia podstawowe

**populacja** - zbiór wszystkich przedstawicieli przedstawiających daną cechę

**próbka losowa** - reprezentatywna próbka całej populacji

**prób prosta** - ma miejsce gdy prawdopodobieństwo jednego wyboru nie ma wpływu na kolejne/inne wybory (białe/czarne kule, losowanie z/bez zwracania)

zachowanie ukłądu któ©ego nie jesteśmy w stanie przewidzieć nazywamy przypadkowym a miarą przypadkowośći jest prawdopodobieńśtwo.

**zdarzenie losowe** - dowolny podzbiór przestrzeni zdarzeń elementarnych

zdarzenie elementarne musi być **ekskluzywne** (nie zawiera innych zdarzeń elementarnych)

**Prawdopodobieńśtwo**: Każdemu zdarzeniu losowemu z PZA przypisujemy liczbę określająćą prawdoopodbieńśtwo tego zdarzenia (0, 1).
zdarzenie pewne = 1
prawdopodobieńśtwo Sumay ekskluzywnych zdarzeń jest równe sumie prawdopodobieńśtw.

```{admonition} prawdopodobieństwo subiektywne
gdy nie wiemy czy dane są prawdziwe (np. czy istnieje życie pod powierzchnią oceanu jednego z księżyców saturna).

albo, czy wolisz dostać 100 czy wziąć udział w loterii o 1000
```


### Prawa De Morgana

$$
\bar{A \cup B} = \bar{A} \cap \bar{B} \\
\bar{A \cap B} = \bar{A} \cup \bar{B}
$$

## Prawo rozdzielności dodawania i mnożenia

$$
A \cap (B \cup C) = (A \cap B) \cup (A \cap C) \\
A \cup (B \cap C) = (A \cup B) \cap (A \cup C)
$$

Wnioski:

$$
A \cup B = A \cup (B - A \cap B) \\
$$

```{tip}
Prawdopodobieńśtwo zdarzenia przeciwnego jes trówne $P(\bar{A}) = 1-P(A)$
```

## Wiele sdarzeń

$$
P(U_{i=1}^{n} A_i) = \sum_{i=1}^{n} P(A_i) - \sum_{i=1}^{n} \sum_{j=i+1}^{n} P(A_i \cap A_j) + \sum_{i=1}^{n} \sum_{j=i+1}^{n} \sum_{k=j+1}^{n} P(A_i \cap A_j \cap A_k) - \ldots
$$

```{admonition} przykłąd
A_i = i-ta ścianka nie wypadła ani raz
$P(A_i) = \frac{5}{t}^n$
$A_j$ = dowolne 2 śicanki nie wypadły ani raz
$P(A_j) = \frac{2}{3}^n$
itd.

formuła wł/wył

$$

```

## rozszerzenie pojęć kombinatorycznych

dwa typy losowań:
- bez powtórzeń - raz wylosowany element nie wraca do populcji
- z powtórzeniami - element wraca do populacji
<!--w tym momencie skończył się prąd w laptopie profesora-->

Jeżeli kolejność jest istotna to **warjacja**, jeśli nie to **kiombinacja**

-  Warjacja z powtórzeniami $W(n, k) = n^k$ (np. rozkłąd n rozróżnialnych cząstek w k komórkach)
- warjacja bez powtórzeń $V(n, k) = \frac{n!}{(n-k)!}$ (k rozróżnialnych kól w n komórkach gdy w komórce może być tylko jedna kula) (winda)
- Permutacja $P(n) = n!$ (Boltzman: k kul w k komórkach)
- Kombinacja bez powtórzeń $C(n, k) = \frac{n!}{k!(n-k)!}$ 
- kombinacje z powtó©zniami $C(n+k-1, k)$
