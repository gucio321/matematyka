## Notatki do egzaminu (break it down)

### Momenty
ogólnie moment `n`tego rzędu to wartość oczekiwana x podniesionego do `n`:

$$
m_n = \left\langle x^n \right\rangle
$$

Moment pierwszego rzędu jest popularnie zwany średnią.

Moment centralny, to... Moment zwykły tylko że wokół środka (czyli od każdego x odejmujemy średnie x aka jego wartośc oczekiwaną - serio tu nie ma różnicy chyba).

Moment centralny oznacza się przez $\mu$ i definuje jako:

$$
\mu_n = \left\langle (x - \left\langle x \right\rangle)^n \right\rangle
$$

```{important}
moment centralny 1 rzędu byłby równy zero:

$$
\mu_{hipotetycznie 1} = \left\langle (x - \left\langle x \right\rangle)^1 \right\rangle = \\
\left\langle x \right\rangle - \left\langle\left\langle x \right\rangle\right\rangle = 
\left\langle x \right\rangle - \left\langle x \right\rangle = 0
$$

Można to udowodnić (szczególnie cześć z $\left\langle\left\langle x \right\rangle\right\rangle = \left\langle x \right\rangle$ z faktu, że $\left\langle x \right\rangle$ jest liczbą więc można
wyciągnąć przed całkę i mieć całkę z `f` która jest oczywiście `1` (zachęcam do policzenia. ja to mam w zeszycie i mi się nie chce przepisywać).

Dlatego też moment centralny 1 rzędu to... moment zwykły 1 rzędu czyli po prostu średnia.
```

```{important}
Spoiler alert! tak na prawdę to "śrdnia" $\neq$ $\left\langle x \right\rangle$,
bo średnia to estymator wartości oczekiwanej, a wartość oczekiwana to wartość oczekiwana.

To jest tak, że średnią aka estymator liczysz z **DANYCH**, natomiast wartość oczekiwaną z **ROZKŁADU**.
Więc hipootetycznie to te same rzeczy ale no jednak nie.
```

Moment mieszany $\mu_{m, n}$ to moment centralny dla 2 rzeczy

$$
\mu_{m, n} = \left\langle (x - \left\langle x \right\rangle)^m (y - \left\langle y \right\rangle)^n \right\rangle
$$

### ważne momenty

- wariancja: $\sigma^2 = \mu_2 = \left\langle x^2 \right\rangle - \left\langle x \right\rangle^2$
- kowariancja to moment mieszany 1 rzędu $\mu_{1, 1} = \left\langle xy \right\rangle - \left\langle x \right\rangle \left\langle y \right\rangle$
Jeżeli zmienne są statystycznie niezależne $\Rightarrow$ kowariancja równa 0


### Współczynnik korelacji (Pearsona)

$$
p = \frac{cov[x,y]}{\sqrt{v[x]v[y]}}
$$
