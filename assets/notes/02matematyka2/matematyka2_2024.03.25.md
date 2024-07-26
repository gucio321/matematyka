### Pochodne cząstkowe

Granicę $\lim_{h \to 0} \frac{f(x+h,y,z)-f(x,y,z)}{h}$ o ile istnieje nazywamy pochodną cząstkową 
względem zmiennej $x$ i oznaczamy $\frac{\partial f}{\partial x}$.

```{admonition} Tw. Schwartza
Jeżeli pochodne mieszane są ciągłe, to są równe.
```

Funkcja 2 zmiennych jest klasy $C^1$ jeżeli $\frac{\partial f}{\partial x}$ i $\frac{\partial f}{\partial y}$ są ciągłe.

Funkcja jest klasy $C^2$ jeżeli $\frac{\partial^2 f}{\partial x^2}$, $\frac{\partial^2 f}{\partial y^2}$, $\frac{\partial^2 f}{\partial x \partial y}$, $\frac{\partial^2 f}{\partial y \partial x}$ są ciągłe.

### Pojęcie różniczkowalności

$$
f(\vec{x}-\vec{h}) - f(\vec{x}) = L_{\vec{x}}(\vec{h}) + o(||h||)
$$

<!--ja nie wiem czy oni nie sprowadzają tej kredy z wydziału fizyki. Taka jest... nienajlepsza-->

```{admonition}
$f$ jest klasy $C^1$, $\Rightarrow$ $f$ jest różniczkowalna i różniczka ma postać

$$
L_{\vec{x}}(\vec{h}) = \frac{\partial f}{\partial x_1} + \frac{\partial f}{\partial x_2} + ... + \frac{\partial f}{\partial x_n} + o(||h||0

$$
```

### Pochodna funkcji złożonych

niech $f(x,y,z) \land x=x(t)~y=y(t)~z=z(t)$. Wtedy
$F(t) = f(x(t),y(t),z(t))$ Wtedy $\frac{dF}{dt} = \frac{\partial f}{\partial x } * \frac{d x}{d t} + \frac{\partial f}{\partial y} \frac{dy}{dt} + \frac{\partial f}{\partial z} \frac{dz}{dt}$

### Pochodna kierunkowa

Niech $\omega=(cos \alpha, cos \beta, cos \gamma)$ będzie wektorem jednostkowym.

Granica

$$
\lim_{t \to 0} \frac{f(x+t cos\alpha, y+t*cos \beta, z+t*cos \gamma)}{t}
$$

o ile istnieje nazywana jest pochodną $f$ w kierunku $\omega$ i oznaczamy $\frac{\partial f}{\partial \omega}$
