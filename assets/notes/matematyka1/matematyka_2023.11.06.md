$$
f(x) = \left\{\begin{matrix}
x^2~,~x\in \mathbb{Q} \\
0~,~x \in \mathbb{R} \setminus \mathbb{Q}
\end{matrix}\right.
$$

Funkcja jest różniczkowalna w punkcie `x=0` ($\frac{h^2}{h} \to 0$)

### Zastosowanie pochodnych

```{admonition} Maksimum lokalne
$$
f : I \to \mathbb{R} \quad I = \left(a,b\right) \\
\exists \delta \quad x_0 \in \left(x_0 - \delta, x_0 + \delta \right) \\
f(x) \leq f(x_0)
$$
```

```{admonition} Twierdzenie o zerowaniu się pochodnych w maksimum lokalnym
Jeżeli funkcja `f` jest różniczkowalna i ma w punkcie $x_0$ maksimum
lokalne $\Leftrightarrow f'(x_0) = 0$

$$
R = \frac{f(x)-f(x_0)}{x-x_0} \\
dla~x_0 > x \land x \to x_0 \\
f(x) - f(x_0) \leq 0 \land x-x_0 \geq 0 \Rightarrow R < 0 \\
dla~x_0 > x \land x \to x_0 \\
f(x) - f(x_0) \leq 0 \land x-x_0 \leq 0 \Rightarrow R > 0 \\
R \leq 0 \geq R \Rightarrow R = 0 \\
$$
```

```{note}
jeżeli f jest ciągła i różniczkowalna

$$
f : I \to \mathbb{R} \quad I = \left(a, b\right) \\
jeżeli~f(a) = f(b) \\
\exists~c \in I ,~ f'(c) = 0
$$
```

```{admonition} Twierdzenie Lagrange'a o wartości średniej
- `f` jest ciągła
- `f` jest różniczkowalna

$$
\exists c \in \left(a, b\right) \\
f'(c) = \frac{f(a) - f(b)}{a-b}
$$

```

```{admonition} Twierdzenie Coushy'ego
- `f`, `g`, są ciągłe $\in \left[a, b\right]
- `f`, `g`, są różniczkowalne
- $g' \neq 0 \in \left(a,b\right)$

wtedy:

$$
\exists c \in \left(a,b\right) \\
\frac{f'(c)}{g'(c)} = \frac{f(b)-f(a)}{g(b)-g(a)}
$$

:::{tip}
$g(a) \neq g(b)$ ponieważ `g` jest różniczkowalna $\Rightarrow~g(b)-g(a) \neq 0$
:::

```
