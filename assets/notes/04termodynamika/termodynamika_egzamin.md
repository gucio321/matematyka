## Przed Egzaminem (Powtórzenie)

### 1 zasada termodynamiki

Istnieje funkcja stanu taka, że:

$$
\Delta U = Q + W
$$

Gdzie:
- U - zmiana energii wewnętrznej
- Q - ciepło dostarczone do układu ($Q > 0 \Rightarrow$ dostarczono ciepło)
- W - praca wykonana **nad** układem ($W > 0 \Rightarrow$ dostarcono energię)

W formie różniczkowej: $dU = \delta Q + \delta W$

### 2 zasada termodynamiki
Gdy dojdzie kontaktu cieplnego między dwoma układami o różnych temperaturach, nastąpi przepływ ciepła między nimi co spowoduje
wyrównanie się ich temperatur. Rozdzielenie układow nie wpłynie na ich temperatury.

### Praa wykonana przez układ

$$
W = pV \\
dW = p dV
W = \int dW = \int_{V_1}^{V_2} p dV
$$

### Cykl Carnota

1. Gaz **otrymuje ciepło** więć pozostaje w temperaturze cpiełej $T_h$ i radośnie się rozpręża (bo 1 zas termodynamiki, trochę ciepła idzie na $\Delta U$ a trochę na pracę, czyli rozprężanie).
2. gaz nie otrzymuje ciepła, ale nadal rozpręża się **adiabatycznei** więc jego temperatura (energia wewnętrzna) spada do $T_c$.
3. **Ciepło** jest aktywnie **odprowadzane** z układu, więc znowu trochę idzie na obniżenie $\Delta U$ a trochę na antypracę.
4. układ dalej się kurczy **adiabatycznie** więc jego temperatura rośnie do $T_h$

| krok | ciepło | praca | temperatura ($\Delta U$) |
|------|--------|-------|--------------------------|
| 1    | otrzymuje | wykonuje | $T_h$ |
| 2    | brak   | wykonuje kosztem $\Delta U$ | $T_h \to T_c$ |
| 3    | oddaje | antypracuje (kurczy się) | $T_c$ |
| 4    | brak   | antypracuje kosztem $\Delta U$ które rośnie | $T_c \to T_h$ |


Sprawność: $\eta = \frac{W}{Q} = 1 - \frac{Q_{12}}{Q_{34}}

### Skala Kelwina

$$
\frac{T}{T_0} = \lim_{p \to 0} \frac{(p V)_\Theta}{(p V)_{\Theta_0}}
$$

Gdzie:
- p - ciśnienie
- V - objetość
- $\Theta$ i $\Theta_0$ - stany
- $\Theta_0$ to punkt potrójny wody ($0 ^\circ C$).

### Sformuowanie Clausiusa

```{tip}
**NIE** istnieje proces termodynamiczny, którego **jedynym** wynikiem jest przekazanie
ciepła ze zbiornika o niższej do zbiornika o wyższej temperaturze.
```

### Sformuowanie Kelvina

```{tip}
Nie istnnieje proces termodynamiczny, którego jedynym skutkiem jest pobranie ciepła ze zbiornika
i całkowite przekształcenie go w pracę.
```

### Prawo Hessa

Zmiana Entalpii układu $\Delta H$ (podczas reakcji) jest niezależna od drogi jaką zachodzi ta rakcja.

```{admonition} Entalpia
Całkowita energia układu.

$$
H = U + pV
$$ (entalpia)
```

**Dowód:** Załóżmy, że reakcja z A do B zachodzi na 2  sposoby:

$A \to B$ (droga 1) i $A \to C \to B$ (droga 2).

Wtedy:

$$
\Delta H_1 = H_B - H_A
\Delta H_2 = \Delta H_{A \to C} + \Delta H_{C \to B} = H_C - H_A + H_B - H_C = H_B - H_A = \Delta H_1
$$

W ogólnym prypadku $\Delta H = \sum_{i=1}^n \Delta H_{i \to i+1}$.


### Doświadczenie Joul'a (rozprężanie w próżni)

```{important}
zakładamy gaz doskonały i idealne warunki (idealna próżnia)
```

- Dwa pojemniki w izolacji termicznej (nie wymieniają ciepła z otoczeniem).
- w jednym z nich jest gaz doskonały w stanie 1.
- dwa pojemniki łączymy i gaz rozpręża się do drugiego pojemnika (próżnia).

Jak można sobie wyobrazić, z powodu izolacji termicznej żadne ciepło nie jest dostarczane do układu. 
Gaz nie wykonał również żadnej pracy, ponieważ rozpręża się do próżni więc nie ma żadnych oporów.
Temperatura jest stała, więc $\Delta U = 0$.
