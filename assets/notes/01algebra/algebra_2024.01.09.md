```{note}
Przykłądem bazy ortonormalnej jest baza kanoniczna w $\mathbb{R}^3$.
```

Aby wyliczyć współrzędne wektora w bazie ortogonalnej?:

$$
\alpha_a = \frac{\left<v, b_1\right>}{||b_1||^2}
$$

```{note}
$\left<v, b_1\right>$ to $||v_{b_1}|| * ||b_1|$ po podzieleniu zostaje
$\frac{||v_{b_1}||}{||b_1||}$

gdzie $v_{B_1}$ to długość rzutu $v$ na $b_k$
```

### Metoda ortogonalizacji Gramma-Schmidta

Jeżeli istnieje basa generujaca jakąś podprzestrzeń to istnieje
też inna **ortogonalna** baza która generuje tą podprzestrzeń.

0. najpierw warto sprawdzić, czy zadana baza nie jest już przypadkiem ortogonalna ;-)
1. $c_1 = b_1$
2. aby $c_2$ generował tą samą przestrzeć co $lin\left\{c_1, b_2\right\}$ musi on być kombinacją liniową tych wektorów $c_2 = b_2 + \alpha c_1$.
3. to samo należy zrobić dla 3 wektora.  Również $c_2 = \left<c_2, b_2\right> = 0$

### Rzut Ortogonalny

```{tip}
również znany jako rzut prostokątny w $\mathbb{r}^2$
```
