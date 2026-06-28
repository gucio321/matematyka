## Dygresja - wyprowadzenie transformacji lorentza

Transformacja typu:

$$
\left\{\begin{matrix}
x' = ax + bt \\
t' = Cx + dt
\end{matrix}\right.
$$

1. początek ukłądu współrzędnych $s'$ porusza się w ukłądzie odniesienia z prędkością $v$ czyli dla $x'=0$, $x=vtt$

$$
0 &= a v t + bt \\
0 &= t (av + b) \Leftrightarrow b = -a v \\
\\
\left\{\begin{matrix}
x' = ax - av t \\
t' = cx + dt
\end{matrix}\right.
$$


Niech $a = \gamma$

$$
\left\{\begin{matrix}
x' = \gamma x - \gamma v t \\
t' = Cx + dt
\end{matrix}\right.
$$

2. 1 postulat einstaina - zasada względności - transformacja do $s'$ musi mieć analogiczną transformacje z powrotem do $s$:

$$
x = \gamma x' + \gamma v t' \\
$$

3. 2 postulat Einsteina - prędkość światła w każdym układzie wynosi $c$. Zakładamy błysk światłą wyemitowany w chwili $t = t' = 0$, więc pzycja tych błyskóœ będzie opisana przez $x=ct$.

$$
\left\{\begin{matrix}
c t' = \gamma c t - \gamma v t \\
c t = \gamma c t' + \gamma v t' \\
\end{matrix}\right. \\
\\
c^2 t t' = \gamma^2 t t' (c - v)(c + v) \\
c^2 = \gamma^2 (c - v)(c+v) \\
\gamma^2 = \frac{c^2}{c^2 - v^2} \\
\gamma^2 = \frac{1}{1 - \frac{v^2}{c^2}} \\
\gamma = \sqrt \frac{1}{1 - \frac{v^2}{c^2}} \\
$$

mamy zatem postać $\gamma$

4. Należy znaleźć postać $t'$

$$
x = \gamma x' + \gamma v t' \\
t' = \frac{x - \gamma x'}{\gamma v} \\
t' = \frac{x - \gamma (\gamma x - \gamma v t)}{\gamma v} \\
t' = \frac{(1-\gamma^2) x + \gamma^2 v t}{\gamma v} \\
t' = \frac{(1-\gamma^2) x}{\gamma v} + \gamma t \\
\frac{1-\gamma^2}{\gamma} &= \frac{1 - \frac{1}{1-\frac{v^2}{c^2}}}{\gamma} \\
&= \frac{\frac{1 - \frac{v^2}{c^2} - 1}{1-\frac{v^2}{c^2}}}{\gamma} \\
&= \frac{\frac{- \frac{v^2}{c^2}}{1-\frac{v^2}{c^2}}}{\gamma} \\
&= \frac{- \frac{v^2}{c^2} \gamma^2}{\gamma} \\
&= - \frac{v^2}{c^2} \gamma \\
t' = -\frac{v}{c^2}\gamma x + \gamma t \\
$$

Więc:

$$
\left\{\begin{matrix}
C &= -\frac{v}{c^2}\gamma \\
d &= \gamma
\end{matrix}\right.
$$

Ostatecznie:

$$
\left\{\begin{matrix}
x' &=& \gamma x - \gamma v t \\
t' &=& \gamma t - \frac{v}{c^2} \gamma x \\
\end{matrix}\right.
$$

W jednostkach naturalnych ($c=1$)

$$
\left\{\begin{matrix}
x' &=& \gamma (x - v t) \\
t' &=& \gamma (t - v x) \\
\end{matrix}\right.
$$

## Wykład 5

Pęd uogulniony zapisuje się wzorem $p_i = \pfrac{\partial L}{\partial \dot q_I}*

Hamiltonian $H = \sum_i p_i \dot q_i - L$

Przestrzeń fazowa to przestrtzeń w któ©ej bazę stanowią wszystkie uogulnione położenia i pędy (czyli to co byłop na MOF v(x) to specyficzny przypadek)

Objętość punktów w przestrzeni fazowej jset zachowana (tw Liouville'a).

Nawiasy Poissona to antykomutator pochodnych po p i q działających na f i g.

Jeżeli nawias poissona z hamiltonem $\{f,H\} = 0$  to $f$ jest całką ruchu.

Równania Hamiltona

$$
\left\{\begin{matrix}
\dot q_i &=& \frac{\partial H}{\partial p_i} \\
\dot p_i &=& \frac{\partial H}{\partial q_i}
\end{matrix}\right.
$$

## Wykłąd 7

Konwencja sumacyjna:
- jeżeli wskaźnik pojawia się na gó©ze i na dole to jest to wskaźnik niemy i w domyśłe jest po nim suma
- jeżeli wskaźnik pojawia się po obu stronach wyrażenia to jest to wksaźnik wolny i determinuje wymiar wyjściowej macierzy


Iloczyn skalarny $g$:

$$
g(x,y) = x \cdot y = \braket{x|y} = g_{ij} x^i y^j = x_i y^i
$$


Dla ukłądu euklidesowego (czyli chyba tak normalnie) $g_ij \equiv \delta_{ij}$

Ale w OTW: $g \equiv g_{ij} (M, \vec{x})$ cokolwiek to znaczy.

Tensor metryczny (metryka) $g_{ij} g^{ij} = \delta_i^j$

Podnoszenie i opuszczanie wskaźników:

$$
v_i = g_{ij}v^j \\
v^i = g^{ij} v_j
$$

konstrukty:
- prosta: $x^i(t) = x_0^i + tv^i$
- hiperpłaszczyzna: $n_i(x^i-x_0^i)$

Operatory pochodnej dla 3d
- rotacja $\nabla \times \vec A \Rightarrow \epsilon^{ijk} \partial_j A_k$
- gradient $\nabla \phi \Rightarrow \partial_i \phi$
- dywergencja $\nabla \cdot \vec A \Rightarrow \partial_i A^i$
- laplasjan $\Delta \phi = g^{ij} \partial_i \partial_j \phi$

problem włąsny macierzy $\mathbb{A}x = \lambda x$:
- w mechanice kwantowej hamiltonian daje energie $\hat H x = E x$
- coś tam w ciastkach też sie robi.

## Wykłąd 8

STW:
1. prawa fizyki są takie same we wszystkich ukłądach odniesienia
2. prędkość światła to max prędkość i jest niezależna od ruchu układu

| STW | OTW |
|---|---|
| duże prędkośći | duże masy |
| 4-wektory | tensory $g_{ij}$ |
| metryka minkowskiego | krzywizna czasoprzestrzeni |
