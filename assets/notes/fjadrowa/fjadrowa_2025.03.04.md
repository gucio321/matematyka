## Wstęp

- 30 pkt z aktywności
- 40 pkt ze sprawdzianu pisemnego na koniec cwa
- egzamin ustny (30 pkt)
- [strona](http://website.fis.agh.edu.pl/~Bozek/)
- pokój 119 D-11
- [Particle Data Group](https://pdg.lbl.gov/)
- Isotope browser (aplikacja)

## Jednostki

Wartości energii są rzędu elektronowoltów (eV), natomiast odległości to kilka Angstromów (1 Angstrom = $10^{-10}$ m).

Masę można zapisać w postaci $m c^2 = [MeV]$

Masę protonu możńa zapisać jako $m_p = 938.3 \frac{MeV}{c^2}$

MOżna powiedzieć, że ustalamy #c = 1$, wtedy masa ma jednostkę energii, odległości mierzymy w metrach,
natomiast czas w $\frac{m}{c}$

### masy i wymiary atomóœ

Rozmiar atomów jest rzędu $1 A$.

Wymiary jądra są rzędu $1 fm = 10^{-15} m = 1 fermi$

| nazwa wielkości | jednostka |
|-----------------|-----------|
| Energia | MeV |
| Odległość | fermi |
| Masa    | $\frac{MeV}{c^2} $ |
| Pęd    | $\frac{MeV}{c}$ |

```{admonition} jednostka pędu

z niezmiennika $E = \sqrt{m^2 c^4 + p^2 c^2}$

$[MeV] = [mc^2] = [pc]$
```

### Notacja, przestrzeń minkowskiego

Rozważamy czterowektor $(ct, x, y, z)$

```{note}
iloczyn skalarny

$\vec{a}^T M \vec{b}$

dla zwykłęj przestrzeni M jest macierzą jednostkową.

W przestrzeni Minkowskiego macierz

$$
M = G = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0 \\
0 & 0 & -1 & 0 \\
0 & 0 & 0 & -1
\end{bmatrix}
$$
```

```{admonition} Interwał czassoprzestrzenny
tak nazywamy iloczyn wektorowy w przestrzeni minkowskiego wektora z samym sobą
```

```{important}
Iloczyn skalarny w przestrzeni Minkowskiego jest **niezmienniczy** przy transformacji lorentza
```

```{tip}
zastosujmy tranformacje lorentza o v wzdłuż osi z o prędkość $\beta$ (ewentualnie beta to część c) (tzw "boost")

$$
\begin{bmatrix}
\gamma 0 0 -\beta \gamma \\
0 1 0 0 \\
0 0 1 0 \\
-\beta \gamma 0 0 \gamma
\end{bmatrix} \begin{bmatrix}
t \\
x \\
y \\
z \end{bmatrix} = \begin{bmatrix}
$$

TODO: policzyć to i zobaczyć czy wyjdzie
```

```{note}
x nazywamy czterowektorem ko**ntra**wariantnym
G x nazywamy czterowektorem kowariantnym
```

## czterowektro energii pędu


$P = (E, \vec{p}) = (E, p_x, p_y, p_z)$

```{note}
$\mathbb{p}$ to trójwektor a $p$ to czterowektor
```

```{admonition} kwadrat długości czterowektora
wyjdzie $m^2$ (TODO)
```

## Energia

$E = \sqrt{m^2 + p^2} = \frac{m}{\sqrt{1 - \beta^2}}$

### CzteroPęd cząstek/ukłądu

$p = (E_1 + E_2, \vec{p}_1 + \vec{p}_2)$

Można zapisać analogiczną zasadę:  Prawo zachowania czteropędu

```{admonition} dygresja światopogląðowa
cząstko mogą ulegać anichilacji, zmieniać się w inne cząstki, ale zasada zachowania czteropędu zawsze będzie zachowana
```

## ukłąd środka masy

czteropęd środka masy to suma energii i pęd środka masy.

### Niezmiennik s

$sqrt{s}$ to energia w środku masy
s = (E_1 + E_2 + E_3)^2 - (p_1 + p_2 + p_3)^2

### Przykłąd

$p + p = p + p + p - \bar{p}$ (nie można z 2 protonów zrobić 3 protonów bo ładunek)

Jaka jest minimalna energia w środku masy żeby zaszla reakcja?
okazuje się że 2 początkowe protony muszą mieć energie kinetyczną 2 dodatkowych "protonów".

$$
\sqrt{s} = E_1 + E_2 >= 4 m_p \\

\gamma >= 2 \\
\frac{1}{1-\beta^2} >= 4 \\
\beta^2 <= \frac{3}{4} \\
\beta <= \frac{\sqrt{3}}{2}
$$
