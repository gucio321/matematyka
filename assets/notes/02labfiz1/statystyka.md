# Kolokwim ze statystyki (statystycznych metod poracowania danych pomiarowych)
1. umiejętności rozstrzygania jakiego rodzaju szacowanie niepewności

przeprowadzić - A czy B czy złożone czy z prawa przenoszenia
niepewności

Niepewność typu A: estymato odchylenia średniej
$S_{\bar{x}} = \sqrt{\frac{1}{n(n-1)} \sum_{i=1}^{n} (x_i - \bar{x})^2}$

Niepewność typu B: "Naukowa ocena eksperymentatora":
- dla prostych przyżądów mechanicznych równa najmniejszej podziałce
- dla urządzeń elektronicznych podawana przez producenta $\Delta x = C_1 x + C_2 * zakres$
- dla przyrządów wskazówkowych $U(x) = \frac{\text{klasa przyrządu}}{100} * zakres$ $U(x) = \frac{\Delta x}{\sqrt{x}}$

2. jak ustalać istotny zakres w zapisie otrzymanych wyników

3. jak zapisywać wynik końcowy wraz z niepewnością (dobrze zaokrągloną).

4. Jak porównywać dwie wielkości ze sobą.

5. Jak wydobyć potrzebne informacje z dopasowania prostej metodą

najmniejszych kwadratów - i na czym ta metoda polega i jak się ma do
linii trendu i czy ewentualnie można by to zrobić jakoś po swojemu ?

```{tip}
Linia trędu jest zastosowaniem metody najmniejszych kwadratów.

metoda najmniejszych kwadratów polega na minimalizacji odległości punktów od prostej,
czyli $min \sum_{i=1}^{n} (y_i - b - ax_i)^2$.

w MS Excel'u można użyć funkcji `linest` aby uzyskać wykaz parametrów dopasowania linii
metodą najmniejszych kwadratów. 

Tabela ta wygląda jak następuje:

| współczynnik a | współczynnik b |
|----------------|----------------|
| niepewność A   | niepewność B   |
| wartość $R^2$  | odchylenie standardowe estymatora y |
|                | stopnie swobody |
| suma kwadratów | suma kwadratów reszt |
```


6. Jakieś alternatywne reguły sobie wymyślić na najlepsze dopasowanie

prostej - co sprawdzać?

7. jak stosować zdrowy rozsądek w tych szacowaniach

8. Jak sprawić, żeby pomiar był precyzyjny lub dokładny lub jedno i
drugie?

9. Jaką informację niosą ze sobą niepewności względne?

10. Co właściwie robią pochodne cząstkowe w prawie przenoszenie niepewności?

11. I do tego wszystko o rozkładzie Gaussa i teście, testowaniu chi kwadrat.

Np. czy ma sens użycie k=4 w niepewności rozszerzonej i dlaczego
zazwyczaj k=2?

