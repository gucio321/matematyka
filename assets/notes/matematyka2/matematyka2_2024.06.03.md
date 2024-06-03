kryterium sylfwstra (aka kryterium sylwestera)

- jeżeli oba wyznaczniki są dodatnie, to w punkcie znajduje się minimum
- jeżeli oba wyznaczniki są ujemne, to w punkcie znajduje się maksimum
- jeżeli wyznacznik jest dodatni, a drugi ujemny, to punkt jest punktem siodłowym

```{note}
Przykłąd

obszar D: $x \in \left(0, 2 \pi\right) \land y \in \left(0, 2 \pi\right) \land x + y = 2 \pi$
$u(x,y) = \sin x + \sin y - \sin(x+y)$

Etap 1
poszukać punktóœ podejżanych

$$
u'_x = \cos x - \cos(x+y) = 0 \\
u'_y = \cos y - \cos(x+y) = 0 \\

P = \left(\frac{2}{3} \pi, \frac{2}{3} \pi \right) \\

u''_{x} = -\sin x + \sin(x+y) \\
u''_{y} = -\sin y + \sin(x+y) \\
u''_{xy} = \cos(x+y) - \cos(x+y) = 0 \\

\begin{bmatrix}
u''_{xx} & u''_{xy} \\
u''_{yx} & u''_{yy}
\end{bmatrix}
$$

ogólnie wychodzi na to że jest maksimum lokalne ponieważ $W_1$ i $W_2$ są ujemne.

etap 2
sprawdzić co się dzieje na brzegu

$y = 0, x \in (0, 2 \pi)$

$u(x) = sin(x) - sin(x) = 0$

$$
x = 0, y \in (0, 2 \pi) \\
u(y) = 0 + sin(y) - sin(y) = 0
$$

$$
x \in \left(0, 2\pi\right) \land x + y = 2 \pi \Rightarrow y = 2\pi - x \\

u(x,y) = sin(x) + sin(2 \pi - x) - sin(2 \pi) = sin(x) - sin(x) = 0
$$

wnioski: największa wartość jest w punkcie P, natomiast najmniejsza jest na brzegu (0).
```

### Metoda lagrange'a

załużmy, że mamy funkcję $f(x,y)$ oraz ograniczenie $g(x,y) = 0$

wtedy tworzymy funkcję $\Phi(x,y,\lambda) = f(x,y) + \lambda g(x,y)$

następnie liczymy pochodne cząstkowe $\Phi$ po $x$, $y$ i $\lambda$ i rozwiązujemy układ równań

