## Egzamin 2 termin

### Tabelka

| zadanie z Kartek z Grupy | Wykrzyknik                                      |
|--------------------------|-------------------------------------------------|
| 1                        | (wsm to nie mam tego ale podobne do 4.2)        |
| 2                        | 4.2                                             |
| 3.a                      | nie ma w ! ale jest w wykładzie                 |

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
Trzeba pamiętać, że $\frac{d}{dr}\Chi = \frac{d}{d\rho}\Chi \frac{d}{dr}\rho$ (czyli innymi słowy, że różniczkowanie $\Chi$ po $r$ wypluwa nam jeszcze $\rho'$)
```

Cała trudność polega na policzeniu 2 pochodnej $\Chi$ po $r$. Potem wstawiamy do równania które jest w zadaniu i wychodzi.

### zadanie 3
#### A
po prostu podstawiamy pod $\rho$ 0 albo $\infty$.
```{tip}
dla 0 zostaje tylko skłądnik z $\rho^2$ w mianowniku. Potem pdostawiamy $\Chi = \rho^\alpha$ i wychodzi.
```

### B
przy rozwiązywaniu równań należy pamiętać, że $\Chi(\rho \to 0) = 0 \and \Chi(\rho \to \infty) = 0$.
Powinno wyjść $\Chi(\rho \to 0) = C \rho^{l+1}$ i $\Chi(\rho \to \infty) = e^{-\frac{1}{2}\rho}$
