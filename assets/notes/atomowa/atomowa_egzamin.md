## Egzamin 2 termin

### Tabelka

| zadanie z Kartek z Grupy | Wykrzyknik                                      |
|--------------------------|-------------------------------------------------|
| 1                        | (wsm to nie mam tego ale podobne do 4.2)        |
| 2                        | 4.2                                             |
| 3                        | nie ma w ! ale jest w wykładzie 4               |
| 4                        | 4.5                                             |
| 5                        |                                                 |
| 6                        |                                                 |
| 7                        | okolice 6.3                                     |
| 8                        | nie wiem i TODO                                 |
| 9                        | 5.3 i 6.1                                       |
| 10                       | 5.5                                             |
| 11                       | 6.2                                             |
| 12                       | 7.2                                             |
| 13                       | 8.1                                             |
| 14                       | 9.1                                             |
| 15                       | 9.3                                             |
| 16                       | trochę na pewno jest 9.5                        |

![Strona 1](./atomowa/egzamin_s1.jpg)

### Zadanie 1
1. $\psi = Y R$
2. $\hat{H} = \frac{p^2}{2m} - \frac{ke^2}{r}$
3. $\hat{H}\psi = E \psi$
4. $R'' + \frac{2}{r} R' + \frac{2m}{\hbar^2} \left( E + \frac{ke^2}{r} + \frac{\hbar^2 l(l+1)}{2mr^2} \right) R = 0$
5. $L^2 Y = \hbar^2 l(l+1)Y$
6. $\nabla^2 = \frac{1}{r^2} \frac{\partial}{\partial r} \left( r^2 \frac{\partial}{\partial r} \right) - \frac{1}{r^2 \hbar^2} \hat{L}^2$
7. $p = -i \hbar \nabla$

Musimy udowodnić 4. Podstawiamy kolejno:
3 <- 1 <- 2 <- 7 <- 6, <- 5. Upraszczamy i wychodzi 4.

### Zadanie 2

```{important}
Trzeba pamiętać, że $\frac{d}{dr}\chi = \frac{d}{d\rho}\chi \frac{d}{dr}\rho$ (czyli innymi słowy, że różniczkowanie $\chi$ po $r$ wypluwa nam jeszcze $\rho'$)
```

Cała trudność polega na policzeniu 2 pochodnej $\chi$ po $r$. Potem wstawiamy do równania które jest w zadaniu i wychodzi.

### zadanie 3
#### A
po prostu podstawiamy pod $\rho$ 0 albo $\infty$.
```{tip}
dla 0 zostaje tylko skłądnik z $\rho^2$ w mianowniku. Potem pdostawiamy $\chi = \rho^\alpha$ i wychodzi.
```

### B
przy rozwiązywaniu równań należy pamiętać, że $\chi(\rho \to 0) = 0 \land \chi(\rho \to \infty) = 0$.
Powinno wyjść $\chi(\rho \to 0) = C \rho^{l+1}$ i $\chi(\rho \to \infty) = e^{-\frac{1}{2}\rho}$

Potem trzeba policzyć 2 pochodną tego nowego $\chi$ ale to jest tortura więc jak to wyciągnę to będę liczył.

### C

Aby policzyć energię trzeba wyliczyć E (podstawiająć $\alpha = -n$)

### Zadanie 4

Sferyczne liczby kwantowe:
- Główna liczba kwantowa $n = 1, 2, 3, \ldots$
- Orbitalna liczba kwantowa $l \in \{0, 1, \ldots, n-1\}$
- magnetyczna liczba kwantowa $m \left< -l, l \right> \cap \mathbb{Z}$
- spinowa liczba kwantowa $s = \pm \frac{1}{2}$

Energia zdegenorwana oznacza, że dla jednej wartości energii możliwe jest więcej niż jedna kombinacja liczb kwantowych.
Aby udowodnić, że liczba takich deformacji wynosi $n^2$ należy obliczyć sumę po wszystkich możliwych wartościach, czyli $\sum_{l=0}^{n-1}\sum_{m=-l}^{l} 1$.

### Zadanie 5

W tym zadaniu są 2 (a nawet 3) kluczowe rzeczy:
- definicja sferycznego ukłądu współrzędnych. Wtedy wiemy, że $\hat{r} = (\phi, \theta) \Rightarrow -\hat{r} = (\phi \pm \pi, \pi - \theta)$ (pamiętamy, że $\theta$ liczymy od osi OZ).
- rozkminienie co to jest $\cos(\pi - \theta) = - \cos\theta \Rightarrow \cos^2(\pi - \theta) = \cos^2 \theta$. Wtedy cosinusy w wielomianie Laguerre'a zjadają minusa tylko dół pochodnej wypluwa $(-1)^{l+m}$.
- $exp(im\pi) = (-1)^m$ natomiast $(-1)^{l+m+m} = (-1)^{l+2m} = (-1)^l$, ponieważ $m \in \mathbb{Z}$.

![Strona 2](./atomowa/egzamin_s2.jpg)

### Zadanie 6
#### A

Cała filozofia polega na rozpisaniu $\psi_{nlm} = R_{nl}(r) Y_{lm}(\hat{r})$. Wyciągamy funkcję niezależną od $\theta \phi$.
#### B
Podstawiamy z tablic (które są dołączone do zestawu) i wychodzi. P'stwo w r=0 jest zawsze 0.
#### C
Bierzemy rozwiązanie z punktu B i liczymy dla niego coś takiego: $\left<r\right> = \int_0^\infty r P_{10}(r) dr$. Powinno wyjśc $\frac{3}{2}$.

```{tip}
$$
\lim_{x \to -\infty} x^n e^x = 0 \quad \text{dla } n \in \mathbb{N}_+
$$
```

### Zadanie 7

Zacznijmy od ostatniej części:
dowód na uproszczenie do delty Diraca jest prosty. Wystarczy powiedzieć, że dla $\epsilon_0$ widać dlete, bo $\epsilon_0 \perp \epsilon_{\pm 1}$.
Natomiast dla $m = \pm 1$ definiujemy $\epsilon_m = \frac{-m}{\sqrt{2}} \left( \hat{e_1} + i m \hat{e_2} \right)$ i jawnie wyliczamy $\epsilon_m \cdot \epsilon *_{m'}$.
```{tip}
$$
\hat{e_1} \perp \hat{e_2} \Rightarrow \hat{e_1} \cdot \hat{e_2} = 0 \\
\hat{e_m}^2 = 1
$$
```

W 1 części zadania, należy z tablic rozpisać harmonike sferyczną dla $l=1$ i $m=0, \pm 1$. Następnie podstawiamy i wychodzi definicja cylindrycznego ukłądu współrzędnych. (Potem liczymy sumę ale to już nie jest trudne).

### Zadanie 9
#### A
Wyliczamy $E'$ i dochodzimy do $E$ od razu. przy $B$ trzeba wyprowadzić $\nabla \times (\nabla f) = 0$.

```{tip}
niech $G = \nabla \times \nabla f$.

$$
G_i = \epsilon_{ijk} \partial_j \partial_k f
$$

ponieważ $\partial_j$ komutuje z $\partial_k$, to symbol antysymetryczny okazuje się być symetryczny :smile: i wychodzi 0.
```

#### B
najpierw rozpisujemy równanie do jawnej postaci.
po obu stronach pojawi się wtedy wyraz typu $\gamma q \chi' \psi$.
Powinniśmy wtedy dojść do momentu, w którym należy udowodnić, że $D^2(A')\gamma \psi = \gamma D^2(A) \psi$.
Robi się to w 2 etapach
1. udowadniamy, że $D(A')\gamma \psi = \gamma D(A)\psi$. 
2. mnożymy powyższy wynik przez siebie samego i otrzymujemy wersję kwadratową.

### Zadanie 10
#### A

Tutaj trudna część to pamiętanie definicji dalambercianu $\square = -\nabla^2 + \frac{1}{c^2} \frac{\partial^2}{\partial t^2}$.
polaryzacja jest liniowa jeśli $A_0 = const$

#### B
Bierzemy warunek z cechowania czyli $\nabla A = 0$ i wychodzi, że $k \perp A_0$.

#### C
no wstawiamy.

### Zadanie 11

Trzeba się trochę pobawić. Wygodnie jest zrobić następujące podstawienia:
- zakładamy, że $\Im a = 0$ co znacznie uprości obliczenia.
- $\Theta = \omega t - \vec{k}\cdot\vec{r}+\Phi$

plan działania jest taki:
1. liczymy pochodną $E_m = - \frac{\partial A_m}{\partial t}$
2. Wyciągamy co się da
3. Stosujemy sprytny trick
4. rozpisujemy jako wektor i wychodzą współrzędne walcowe.

```{admonition} sprytny trick
Niech $Z$ dowolna liczba urojona

$$
Z - Z* = (Z_x + i Z_y) - (Z_x - i Z_y) = 2 i Z_y = 2 i \Im Z
$$
```

![Strona 3](./atomowa/egzamin_s3.jpg)

### Zadanie 12

1. zakładamy, że $\vec{A_0}\perp\vec{k}$
2. korzystamy z relacji $k = \frac{\omega}{c}$ oraz $\frac{1}{\mu_0} = \epsilon_0 c^2$

### Zadanie 13

Rozpisuje się $H_at = \frac{\hat{\vec{p}}^2}{2m} - \frac{ke^2}{r}$ (ta 2 część od razu wypada bo komutuje z definicji do 0).
Rozpisujemy komutator $\left[\nabla^2, r\right]$

```{tip}
Należy pamiętać, że $\nabla r = \delta_{ij} \partial_i x_j = 1$ oraz, że $\nabla^2 r = \delta_{ij} \partial^2_i x_j = 0$.
```

### Zadanie 14
#### Część pierwsza
1. zakłądamy, że bierzemy bazę funkcji ortogonalnych (bo czemu nie). Wtedy $\braket{\psi_i|\psi_j} = \delta_{ij}$.
2. Norma z def to $\braket{\psi|\psi} = \int \psi^* \psi d^3r = 1$.

#### Część druga
```{tip}
jak to wylosujesz, to możesz się poddać.
Jak to wylosujesz, to twoje szczęście jest porównywalne z... wyobraź sobie, że próbujesz otworzyć drzwi ale zamiast tego nie trafiasz w klamkę, odbijasz się od nich, przewracasz się i łamiesz rękę.
```

A tak serio, to da się to zrobić, ale trzeba używać jakichś dzikich przekształceń.
1. wychodzisz z R. Schrödingera (w formie ketowej najlepiej) $H \ket{\psi} = i \hbar \ket{\psi}$
2. rozpisujesz kety.
3. prawa strona: Pamiętaj o tym że C zależą od czasu więc trzeba je też różniczkować i mamy po kolei:
   - $\braket{\psi_i|\psi_j'} = \braket{\psi_1|\frac{-i E_j}{\hbar} \psi_j} = -\frac{i E_j}{\hbar} \delta_{ij}$ 
   - $\bra{\psi_i} H \ket{\psi_j} = \bra{\psi_i} H_{at} \ket{\psi_j} + \bra{\psi_i} V \ket{\psi_j}$
   - $\bra{\psi_i} H \ket{\psi_j} = exp\left(i\frac{E_i - E_j}{\hbar}t \right) E_j \delta_{ij}$
   - $\bra{\psi_i} V \ket{\psi_j} = exp\left(i\frac{E_i - E_j}{\hbar}t \right) \cos\left(\omega t\right) W_{ij}$
   - zakłądamy, że $W_{ii} = 0$

### Zadanie 15

(Protip z [zadania 14](#zadanie-14) nadal obowiązuje)
To jest to zadanie z evil-trickami w całkach.

Definiujemy sobie:
- $\omega_0 = \frac{E_2 - E_1}{\hbar}$
- $\omega_\pm = \left|\omega \pm \omega_0\right|$
- $T_\pm = \frac{2\pi}{\omega_\pm}$

```{note}
$\omega_- \to 0$
```

```{important}
$$
cos x = \frac{1}{2} \left(e^{ix} + e^{-ix}\right) \\
$$
```

Wiedząc to wszystko walczymy z całką:

$$
I_\pm = \int_t^{t+T_+} e^{i\omega_\pm t} C_2 dt
$$

Całkę liczymy oczywiście przez części (no bo czemu nie?).

Rozpisujemy wszystko no i ogólnie jest problem. Na pewno jak się wyciągnie $\frac{1}{i\omega_-}$, to $I_+$ się całe wyzeruje (bo $\frac{\omega_-}{\omega_+}$ ma się zerować).
No i z tego co zostaje robimy jakieś ugabuga z Taylorem i wychodzi... a przynajmniej powinno.

```{note}
tam w jednym miejscu coś się wyciąga przed całkę mimo tego, że jest zależne od zmiennej całkowania
```

### Zadanie 16
#### A
z jednego z równań liczymy $C_1$ a następnie $C_1'$ i podstawiamy do 2. jak się nie pomylimy to wychodzi.
#### B
Warunki początkowe:
- $C_2(0) = 0$, bo tak.
- $C_1(0) = 1$ z normalizacji.
- $C_2'(0) = -\frac{iW_{21}}{2\hbar}$ z pierwszego równania.

Podstawiamy równanie charakterystyczne $C_2(t) = \exp(\lambda t)$
W $\Delta$ powinien już sięp okazać $\omega_R$ potem liczyby współczynniki no i coś wychodzi.

#### C
$P_{12} = |C_2(t)|^2$ bo to kwadrat amplitudy funkcji falowej.

![Strona 4](./atomowa/egzamin_s4.jpg)
#### Zadanie 17
