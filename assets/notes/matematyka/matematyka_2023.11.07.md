#### Wnioski Tw. Lagrange'a

```{important}
funkcja $f: I \to \mathbb{R}$ jest różniczkowalna
```

- jeżeli $f' \equiv 0 \Rightarrow f \equiv const$
- jeżeli $f' \geq 0 \Rightarrow$ f jest niemalejąca
- jeżeli $f' \leq 0 \Rightarrow$ f jest nierosnąca

```{admonition} Twierdzenie AGH
$$
\forall x \geq 0 \quad \sqrt{x} \leq \frac{1}{2} x + \frac{1}{2} \\
a, b > 0 \\
A = \frac{a + b}{2} \\
G = \sqrt{a * b} \\
\\
x = \frac{a}{b} \\
\sqrt{\frac{a}{b}} \leq \frac{1}{2} \frac{a}{b} + \frac{1}{2} \\
b * \sqrt{\frac{a}{b}} \leq \frac{1}{2} a + \frac{1}{2} b \\
G \leq A \\
\frac{1}{H} = \frac{\frac{1}{a} + \frac{1}{b}}{2} \\
\bf{\color{red}{A} \color{white}{\geq} \color{green}{G} \color{white}{\geq} \color{black}{H}}
$$
```

#### Reguła de l'Hospitala

```{admonition} Reguła de l'Hospitala
`f`, `g` to funkcje różniczkowalne.

$$
jeżeli~\lim_{x\to a}\frac{f}{g} = \frac{0}{0} \\
jeżeli \quad \exists \lim_{x\to a} \frac{f'(x)}{g'(x)} = G \Rightarrow \exists \lim_{x \to a} \frac{f(x)}{g(x)} = G
$$
```

```{tip}
$$
\lim_{x \to 0} \frac{sin(x)}{x} \\
\lim_{x \to 0} \frac{(sin(x))'}{x'} \\
\lim_{x \to 0} \frac{cos(x)}{1} = 1 \Rightarrow \exists \lim_{x \to 0} \frac{sin(x)}{x} = 1 \\
$$
```

```{note}
- `f` jest niższego rzędu (niż `g`) gdy $\frac{f}{g} \to 0$
- `f` i `g` są równego rzędu gdy $\frac{f}{g} \to const \neq 0$
- jeżeli $\frac{f}{g} \to 1$, to `f` i `g` są **asymptotycznie równoważne**
```
