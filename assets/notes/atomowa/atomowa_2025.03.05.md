## Wstęp

- [strona](https://home.agh.edu.pl/~czapli)

## Jednostki

```{seealso}
pierwszy punkt ze strony
```

## Układ 2 ciał punktowych oddziaływujących siłą centralną

rozważmy 2 punkty położone względem punktu obserwacyjnego O

Zapisujemy 2 zas. dynamiki.

$$
\left\lbrace\begin{matrix}
m_1 r_1'' = -F(r) \\
m_2 r_2'' = F(r)
\end{matrix}\right. \\

F(r) = -\nabla V(r)
$$

```{tip}
$$
P_{tot} = p_1 + p_2 \\
\vec{L_{tot}} = L_1 + L_2 \\
E_{tot} = \frac{m_1 v_1^2}{2} + \frac{m_2 v_2^2}{2} + V(r)
$$

Pokazać, ze powyższe wielkości są zachowane w trakcie ruchu ciała w czasie (są całkami ruchu) - policzyć pochodne i pokazać ze są równe 0
```

### Zmienne względem środka masy

zmieniamy zmienne opisujące układ (do tej pory zmienne położenia) na zimenneśrodka masy
oznaczone jako $(\vec(r_1), \vec{r_2}) \to (\vec{R}, \vec{r})$ gdzie R jes takie, że
$\vec{R} = \frac{m_1 \vec{r_1} + m_2 \vec{r_2}}{m_1 + m_2}$ natoimiast
$\vec{r} = \vec{r_2} - \vec{r_1}$

### Równania ruchu w zmiennych $\vec{R} \vec{r}$

```{tip}
odwracamy przekształcenie:
$$
\vec{r_1} = \vec{R} - \frac{m_2}{m_1+m_2} \vec{r} \\
\vec{r_2} = \vec{R} - \frac{m_1}{m_1+m_2} \vec{r}
$$
```

Otrzymujemy, że:

$$
\left\lbrace\begin{matrix}
m_{tot} \vec{R}'' = 0 \\
r \frac{m_1 m_2}{m_1 m_2} = F(r)
\end{matrix}\right.
$$

```{note}
- równanie 1 ma proste rozwiązanie: $\vec{R}(t) = R_0 + v_{cm}*t$
- rozwiązanie równania 2 zależy od postaci siły $F(r)$
```

### Rozwiązanie dla siły culombowskiej

Załóżmy, $F(r) = \frac{D}{r^2} \hat{r}$ gdzie $D \neq 0$

```{note}
TODO: Wyrazić całki ruchu $p_{tot}$, $L_{tot}$ i $E_{tot}$ wyrazić w nowych zmiennych

$$
p_{tot} = m_{tot} * v_{tot} \\
L_{tot} = R \times P_{tot} + \mu r \times v \\
E_{tot} = \frac{P_{cm}^2}{m_{tot}} + \frac{\mu v^2}{2} + V(r)
$$
```

```{note}
TODO: Wykaż, że P,L,E są całkami ruchu
```

### Potencjał efektywny w problemie 2 ciał

Definicja pędu względnego

$$
p^2 = (\mu v)^2 = p_r^2 + p_\perp^2 \\
L^2 = (r\times p)^2 = (r \times p_\perp)^2 = r^2 p^2 - (\vec{r} \times \vec{p})^2 = r^2 p^2
$$

TODO: czemu ten iloczyn się tak rozbija?

$$
E = E_r + V_{ef}(r)
$$

w opisie klasycznym eneriga raidalna jest zwsze większa lub równa 0

$$
V_{ef} = \frac{L^2}{2 \mu r^2} + \frac{D}{r}
$$

TODO: Przeprowadź analogiczne rozważania dla D > 0
