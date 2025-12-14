## Elementy obwodu

Obwóð skłąda się z m.in.:
- źródło napięcia
- źródło prąðu (natężenia prąðu)
- rezystory
- kondensatory
- cewki

z punktu widzenia topologii obwodu wyróżniamy:
- węzły
- oczka
- gałęzie

### Sygnały

- napięcie (różnica potencjałów) $U_AB = V_A - V_B$. Może być idealna albo rzeczywiste (zależy, czy jest opornik z oporem wewnętrznym)
wyróżniamy także źródło napięćia sterowana (na przykład $U = ax$)
- prąd $I = \frac{dq}{dt}$
Również można wyróżnić idealne lub realne, do którego wpina się rezystor równolegle.
Dzielnik prądu: TODO $I_1 = J \frac{G_1}{G_1 + G_2+...}$ gdzie G to konduktancja ($\frac{1}{R}$)

Źródło prąðu i źródło napięcia nazywamy elementami aktywnymi, natomiast pozostałe to elementy pasywne.

L i C to elementy zachowawcze (zachowują energię)
R to element dyscypatywny (rozprasza energię)

### Prawa

Prawo Ohma: $U = I*R$ (napięcie jest proporcjonalne do prądu ze wszpółczynnikiem R)

Kondensator charakteryzuje się pojemnością C a Cewka Idukcyjnośćią L

Prawa Kirhoffa:
1. algebraiczna suma prądów w węźle jest równa 0
2. algebraiczna suma napięć w oczku jest róœna 0

```{admonition} Ukłądy LTI
Linear Time Invariant - obwody liniowe niezależne w czasie
```

## Dzielniki prądu i napięcia

### Dzielnik Napięcia

Rozważmy szeregowo połączone m rezystorów o róznych napięciach ($R_1, R_2, ..., R_m$)

Rozważmy następujące wyrażenia

$$
U_0 = \sum_{i=1}^{m} U_i = \sum_{i=1}^{m} I * R_i = I \sum_{i=1}^{m} R_i \\
U_n = I * R_n \\
$$

Można wyliczyć sotsunek napięcia źródła $U_0$ do napięcia na n-tym oporniku:

$$
\frac{U_0}{U_n} = \frac{\sum_{i=1}^{m} R_i}{R_n}
$$

### Dzielnik Prądu

Rozważmy najpierw 2 równolegle połączone rezystory zasilane źróðłem prądowym.
Dla takiego układu, można zapisać następujące wyrażenia.

![dzielnik prądu](04kabelki/obwod1.svg)

$$
I_0 = I_1 + I_2 = \frac{U}{R_1} + \frac{U}{R_2}
I_2 = \frac{U}{R_2}
$$

Nastęþnie, znalogicznie do powyższego przypadku, można zapisać stosunek:

$$
\frac{I_0}{I_2} = R_2 \left( \frac{1}{R_1} + \frac{1}{R_2} \right) = \\
= \frac{R_2 + R_1}{R_1}
$$

Uogulnienie tego zagadnienia na m rezystorów nie da tak prostego wzoru jak powyżej.
Jego najprostsza postać przyjmie postać:

$$
\frac{I_0}{I_n} = R_n \sum_{i=1}^{m} \frac{1}{R_i}
$4
