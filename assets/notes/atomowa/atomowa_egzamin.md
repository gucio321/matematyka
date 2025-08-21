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
