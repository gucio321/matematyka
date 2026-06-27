```{admonition} działanie
to funkcjonał (czyli przyjmuje funkcje i zwraca liczbe) opisujący zmiane lagranżjanu (czyli bilansu energii) wzdłuż trajektorii

$$
S \equiv \int_{t_1}^{t_2} L dt
$$

```

Zasada najmniejszego działania mówi, że wszechświat jest leniwy: $\frac{\delta S}{\delta q(t)}

Równanie Eulera-Lagrange'a:

$$
\delta S = S[q(t) + \delta q(t)] - S[q(t)]
$$

Korzystająć z rozwinięcia Teylora $f(x + \delta x,y + \delta y) = f(x,y) + \frac{\partial f}{\partial x} \delta x + \frac {\partial f}{\partial y} \delta y$:

$$
\delta S &= \int_{t_1}^{t_2} dt \left(L + \frac{\partial L}{\partial q} \delta q + \frac{\partial L}{\partial \dot{q}} \delta \dot q \right) - \int_{t_1}^{t_2} dt L \\
\delta S &= \int_{t_1}^{t_2} dt \left(\cancel L + \frac{\partial L}{\partial q} \delta q + \frac{\partial L}{\partial \dot{q}} \delta \dot q \right) - \cancel{\int_{t_1}^{t_2} dt L} \\
\frac{d}{dt} \left(\frac{\partial L}{\partial \dot q} \delta q\right) &= \delta q \frac{d}{dt} \frac{\partial L}{\partial \dot q} + \frac{\partial L}{\partial \dot q} \frac{d}{dt} \delta q \\
\delta S &= \int_{t_1}^{t_2} dt \left(\frac{\partial L}{\partial q} \delta q + \frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}} \delta q\right) - \delta q \frac{d}{dt} \frac{\partial L}{\partial \dot q} \right) \\
\delta S &= \int_{t_1}^{t_2} dt \delta q \left(\frac{\partial L}{\partial q} \delta q - \delta q \frac{d}{dt} \frac{\partial L}{\partial \dot q} \right) + \left. \frac{\partial L}{\partial \dot q} \delta q \right|_{t_1}^{t_2} \\
$$

Zakłada się, że na krańcach trajektorii, system jest w stanie ustalonym, więc warjacja $q$ zmierza do zera, dlatego:

$$
\delta S = \int_{t_1}^{t_2} dt \delta q \left(\frac{\partial L}{\partial q} - \frac{d}{dt} \frac{\partial L}{\partial \dot q} \right) \\
$$

Zgodnie z zasadą najmniejszego działąnia, $\delta S$ musi znikać. Ponieważ $\delta q$ nie może zanikać:

$$
\delta S = 0 \Leftrightarrow \frac{\partial L}{\partial q} - \frac{d}{dt} \frac{\partial L}{\partial \dot q} = 0 \\
$$

Własnośći lagranżjanu:
- Można bezkarnie doać pochodną dowolnej funkcji po czasie $L + \frac{d f(q, \dot q, t)}{dt} \Leftrightarrow L$
- Operator eulera-lagrange'a jest liniowy dla lagranżjanu ($\alpha E(L_1) + \beta E(L_2) = E(\alpha L_1 + \beta L_2))$ 

## Wykład 2

```{admoniton} Ukłąd inercjalny
Ukłąd w którym ruch swobodny odbywa się ze stałą prędkością (czyli nie ma przyspieszenia).

::::{tip}
Funfact: spytałem chatGPT czy pociąg jadący po ziemii jest układem inercjalnym, skoro przecież na ziemii mamy przyspieszenie grawitacyjne.
Okazuje się, że w mechanice newtonowskiej traktuje się przyspieszenie grawitacyjne jako rzeczywistą siłę - czyli to tak na prawde nie jest przyspieszenie.
::::

Przestrzeń jest jednorodna i izotropowa a czas jest izotropowy, to znaczy nie ma w nich dziur ($dt \to 0$, definicja przestrzeni liniowej) a dodatkowo w przestrzeni nie ma kierunków (czyli obrót o kont nie zmienia fizyki).
```

Układ odniesienia porusza się z prędkością $\vec{v}$ (stałą) i jest układem inercjalnymm.

zarówno w **układzie inercjalnym** jak i we wszystkich **układach odniesienia** obowiązują te same prawa fizyki.

Transformacja galileusza:

Niech $\vec r^*$ oznacza położenie układu odniesienia względem ukłądu inercjalnego (obserwatora)

$$
\vec r^*(t) &=  \vec r(t) + \vec R_0 \vec v t \\
\dot{\vec r^*}(t) &= \dot{\vec r}(t) + \vec v
$$

```{important}
czas płynie tak samo we wszystkich układach odniesienia (jest uniwersalny)

Nie no to tak na prawde scam bo potem jest Einstain ale na razie nie ma.
```

Całka ruchu oznacza, że dana wielkość nie zmienia się w czasie.

$f(q, \dot q)$ nazywamy całką ruchu, jeżeli $\frac{\df }{dt} = 0$.

```{admonition} Twierdzenie Noether
Jeżeli występuje symetria to coś jest zachowane.
Formalnie:

$$
\delta L(q(t, \epsilon), \dot q(t, \epsilon), t)|_{\epsilon \to 0} = \frac{d}{dt} f(q, t)
$$

Chodzi o to, że czasem nie da się znaleźć takiego $F$ żeby spełniało równanie.
```

Jeżeli ukłąd spełnia równanie E-L, to istnieje całka ruchu:

$$
I = \sum_i \frac{\partial L}{\partial \dot q_I} \frac{\partial q_i}{\partial \epsilon} |_{\epsilon \to 0} - f(q,t) = const
$$

Prawo zachowania energii: $\frac{d}{dt} \left(\sum_i \dot q_i \frac{\partial L}{\partial \dot q_i} - L\right) = 0$

Translacja lagrangianu o wektor w przestrzeni nie zmienia praw fizyki.

No i tak można iść dalej (pęd, obrót o kąt)
