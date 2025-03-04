## Efekt comptona

ref:
- https://www.youtube.com/watch?v=oTNiJVdEyCc&list=PLRN3HroZGu2mCtdalEmZAM2nr1xBWAtUn&index=9

Gdy swiatło pada na materię, czasami wybija z niej elektrony,
przekazując im część swojej energii. Powoduje to zmianę długości fali
(dowód z zasady zachowania pędu i zasaday zachowania energii $E = \sqrt{m^2 c^4 + p^2 c^2}$)

Końcowe przesunięcie fali $\Delta \lambda = \frac{h}{m_e c}\left(1 - cos \Theta\right) = \lambda_C (1 - cos \Theta)$

W doświadczeniu z rozpraszaniem wiązki lasera na materii powoduje to dwa "piki" na wykresie odbieranych długości fali.
Pik dalszy (przesunięty w prawo o dłuższych falach to właśnie efekt Coptona). Drugi (pierwszy o niższej dł. Fali)
powstaje w wyniku interakcji fotonów z całym atomem (nie udało im się wybić elektronu a atom jest większy)

## Kreacja i anichilacja
ref:
- http://website.fis.agh.edu.pl/~Wolny/Wc680ac88c02ae.htm
- https://www.youtube.com/watch?v=AfQj5ISTU3s&list=PLRN3HroZGu2mCtdalEmZAM2nr1xBWAtUn&index=10

Gdy materia bombardowana jest wysokoenergetycznym promieniowaniem (światłem) ($E = h \nu \approx N meV ~ ~ N > 1$) dochodzi do stworzenia
nowej pary cząstek (elektronu i pozytonu) z energią kinetyczną $E_k = E - 2 m_e c^2$.

$$
E = h \nu = m_{e^-} c^2 + E_{e^-} + m_{e^+} c^2 + E_{e^+} = 2 m_e c^2 + E_k
$$

```{note}
Odwrotny proces wydarza się gdy elektron spotyka pozyton.
```

```{tip}
Minimalna długość fali tworzącej elektrony wynosi $\lambda = 1.2 pm$ - fotony gamma.
```

```{important}
Zjawisko to nie zachodzi (nie powinno zachodzić) w próżni.
Porces ten wymaga obecności nukleonów

Dowód:

Z ZZE mamy:

$$
E = 2 \gamma m_0 c^2 
$$

Natomiast z ZZP:

$$
2 p_x = \frac{E}{c} = \frac{h \nu}{c} = 2 p cos \theta \\
h \nu &= 2 p c cos \theta \\
&= 2 \gamma m_0 v c cos \theta \\
&= 2 \gamma m_0 c^2 \frac{v}{c} cos \theta \\
$$

- z założenia $\frac{v}{c} < 1$
- z definicji $cos \theta \leq 1$

Więc mamy:
$$
\frac{v}{c} < 0 ~ \land ~ cos \theta \leq 1 \Rightarrow \frac{v}{c} cos \theta < 1 \Rightarrow h \nu < 2 m_0 c^2
$$

Ostatnie spostrzeżenie nie zgadza się z ZZE.
```

```{admonition} Cciekawostka
W zależności od energii fotonów obserwujemy różne efekty kwantowe:
- niska energia - efekt fotoelektryczny
- średnia energia - przesunięcie Comptona
- Bardzo duża energia - kreacja par elektron/pozyton
```
