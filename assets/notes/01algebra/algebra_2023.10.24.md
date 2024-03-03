```{important}
Macierze odwracalne tworzą grupę (tzw. grupę liniową)
```

#### Obliczanie macierzy odwrotnej

- metoda dopełnień algebaicznych
    * możemy ją obliczyć tylko gdy $detA \neq 0$
    * $a_ij = (-1)^{i+j} * m_{ij}$
    * tak powstałą macierz transponujemy i kążdy element mnożymy przez $\frac{1}{detA}$

- metoda operacji elementarnych (bezwyznacznikiowa)
    * zestawienie macierzy blokowej z macierzy A i macierzy jednostkowej
    * jeżeli macierz A uda się sprowadzić do macierzy jednostkowej, to druga część bloku
    będzie macierzą odwrotną $A^{-1}$

```{admonition} Algorytm gausa
- korzystając z operacji elementarnych uzyskać macierz trujkątną górną
przemieszczając się od lewego górnego rogu macierzy
- zerowanie od prawej na lewą stronę

```


#### Własności macierzy odwrotnej

- $detA = \frac{1}{detA^{-1}}$
- $(A^{-1})^{-1} = A$
- $(A^{-1})^T = (A^T)^{-1}$
- $(\alpha A)^{-1} = \frac{1}{\alpha} A^{-1}$
- (AB)^-1 = B^{-1} A^{-1}$

## Układy równań liniowych

Układ równań liniowych można zapisać jako $A * X = B$

### Układ równań

```{admonition} układy crammerowskie
są to takie układy, w których liczba niewiadomych jest równa liczbie równań
```

- Macierz A jest kwadratowa
- $x = \frac{W}{W_x}$ ...
- jeśli W = 0 układ **nie** jest oznaczony
- jeśli macierz **nie** jest kwadratowa należy wykorzystać rząd macierzy
    * rząd to **największy stopień niezerowego minora**

### Wyznaczanie rzędu

- sprowadzanie macierzy do postaci schodkowej
- rząd macierzy to ilość "schodów"

### Rozwiązywanie układów równań $m \neq n$

- układ jest sprzeczny jeżei rząd macierzy jest rożny od rzędu macierzy uzupełnionej

