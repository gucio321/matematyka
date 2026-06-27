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
