## Prawa Kirhoffa i prawa wynikające

### Zasada superpozycji

> Odpowiedź ukłądu na sume wymuszeń jest róœna sumie odpowiedzi na poszczególne wymuszenia.

$$
I_L = I_L(E) + I_L(J)
$$

### Tw. Thévenina

> Każdy liniowy dwójnik aktywny możemy zastąpić obwodem równoważnym w postaci rzeczywistego źródła napięcia. Rezystancja tego źródła jest rezystancją dwójnika, po wyłączeniu w nim wszystkich realnych źródeł napięcia i prądu. Wartość napięcia tego źródła wyliczamy jako napięcie na rozwartych końcówkach dwojnika.

```{admonition} dwójnik
obwód z któ©ego można wyprowadzi 2 "nóżki"
```

### Tw. Nortona

 Każdy liniowy dwójnik aktywny możemy zastąpić obwodem równoważnym w postaci rzeczywistego źródła prądu. Rezystancja tego źródła jest rezystancją dwójnika, po wyłączeniu w nim wszystkich realnych źródeł napięcia i prądu. Wartość prądu tego źródła wyliczamy jako prąd dwójnika przy jego końcówkach zwartych.

### Metoda macierzowa prądów oczkowych

```{important}
w obwodzie nie mogą występować źródła prądu
```

Zapisujemy równania dla oczek (gałężie - węzły + 1 równań) i zapisujemy macierz

$$
[U] = [R] \cdot [I]
$$

```{note}
I w macierzy to tzw. prżdy oczkowe, natomiast prądy rzecywiste w układzie trzeba dopiero wyliczyć
```

Macierz [R] mamy:
- na diagonali sumaryczne opory oczek
- w pozostałych miejscach wzajemne ich opory (jak prąð przechodzi w 2 różnych kierunkach ,dajemy -)

### Metoda macierzowa potencjałów węzłowych

$G * V = I$ (macierz konduktancji razy wektor nieznanych potencjałów jest równy wektorowi znanych prądów)

```{important}
w obwodzie nie może być źródeł napięciowych
```

1. ustalamy rząd problemu (węzły - 1)
2. ustalamy węzeł referencyjny (w dla którego wszystkie potencjały będą liczone)
3. 
