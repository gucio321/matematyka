## Forma kwadratowa -- przykłąd

niech $X = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$, 
$A = \begin{bmatrix} a_{11} && a_{12} && a_{13} \\ a_{21} && a_{22} && a_{23} \\ a_{31} && a_{32} && a_{33} \end{bmatrix}$

$$
f(x_1, x_2, x_3) = X^{T} * A * X = a_11 x_1^2 + a_22 x_2^2 + a_33 x_3^2 + 2 a_12 x_1 x_2 + 2 a_13 x_1 x_3 + 2 a_23 x_2 x_3
$$

szukamy najmniejszej wartośći tej funkcji na sferze jednostkowej $1-x_1^2 - x_2^2 - x_3^2 = 0$

$$
\Phi(x_1, x_2, x_3) = f(x_1, x_2, x_3) + \lambda * g(x_1, x_2, x_3) = a_11 x_1^2 + a_22 x_2^2 + a_33 x_3^2 + 2 a_12 x_1 x_2 + 2 a_13 x_1 x_3 + 2 a_23 x_2 x_3 + \lambda (x_1, x_2, x_3)

\left\{ \begin{matrix}
\frac{\partial \Phi}{\partial x_1} = 2 a_11 x_1 + 2 a_12 x_2 + 2 a_13 x_3 - 2 \lambda x_1 = 0 \\
\frac{\partial \Phi}{\partial x_2} = 2 a_22 x_2 + 2 a_12 x_1 + 2 a_23 x_3 - 2 \lambda x_2 = 0 \\
\frac{\partial \Phi}{\partial x_3} = 2 a_33 x_3 + 2 a_13 x_1 + 2 a_23 x_2 - 2 \lambda x_3 = 0 \\
g(x_1, x_2, x_3) = 0 \\
\end{matrix} \right.
\\
\\
\left\{ \begin{matrix}
2 * A * X - 2 \begin{bmatrix} 1 && 0 && 0 \\ 0 && 1 && 0 \\ 0 && 0 && 1 \end{bmatrix} \lambda X = 0 \\
g(x_1, x_2, x_3) = 0 \\
\end{matrix} \right. = 

\left\{ \begin{matrix}
A * X - \lambda X = 0 \\
g(x_1, x_2, x_3) = 0 \\
\end{matrix} \right. = 

$$

```{admonition} twierdzenie
Jeżeli szukamy najmniejszej i największej wartośći funkcji $f(x_1, x_2, x_3) = X^T A X$ na sferze jednostkowej, to
punkty podejrzane to wektory własne macierzy $A - Z* \lambda$
```


```{important}
Podsumowanie wykłądu
- $\Gamma$ euler'a
- funkcje wielu zmiennych, różniczkowalność e.t.c. (analogicznie jak dla 1 zmiennej)
- pojęcie ciąŋłości (tw. Darbou)
- funkcje z $\mathbb{R}^n \to \mathbb{R}^m$ ciągłość, granice)
- różniczkowanie fcji wielu zmiennych; pochodne cząstkowe; różniczka $df = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{bmatrix}$
- ekstrema fcji wielu zmiennych (forma kwadratowa, tw. La'grange'a)
- całki (podwójne, potrójne, krzywoliniowe, powierzchniowe, objętościowe, zorientowane, niezorientowane, tw. Stokes'a, tw. Green'a, tw. Gauss'a-Ostrogradskiego, tw. o polu bezźródłowym)
- zadania typu oblicz objętość/ppowierzchnię
- **Reguły GULDINA** $\leftarrow$ przypadkiem zawsze się pojawiają na egzaminie...
```
