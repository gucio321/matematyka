## Obwody elektryczne

### Elementy obwodu

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
