## Całki dla przeciałów nieskończonych

$$
\int_a^\infty f(x) dx = \lim_{b \to \infty} \int_a^b f(x)dx \\
$$

Całka jest zbierzna, jeżeli 

$$
\int_a^\infty f(x) dx < \infty
$$

```{admonition} Przykład
$$
\int_1^\infty \frac{1}{x} dx \\
\int_1^b \frac{1}{x} dx = \left|ln(x)\right|_1^b \\
\lim_{b \to \infty} ln(b) - ln(1) \to \infty
$$

Ta całka **nie** jest zbierzna.
```

## Całki funkcji nieskończonych

Jeżeli $f(x) \to \infty ~ x \to b$, to mówimy, że $\int_a^b f(x) dx$ jest zbierzna, jeśli
$\exists \lim_{\psi \to b} \int_a^\psi f(x) dx$.

$$
\int_0^1 \frac{1}{x} dx = \lim_{\psi \to \infty} ln(1) - ln(\psi)  = -\infty \Rightarrow \text{Całka jest rozbierzna}
$$

### Szczególne przypadki całek na przedziałach nieograniczonych

- Kiedy całka $\int_1^\infty \frac{1}{x^\alpha} dx$ jest zbierzna?

$$
\int_1^\infty \frac{1}{x^\alpha} dx = \left| \frac{x^{1-\alpha}}{1-\alpha} \right |_ 1^\infty = \\
= \lim_{b \to \infty} \frac{b^{1-\alpha}}{1-\alpha} - \frac{1}{1-\alpha}
$$

Całka jest zbierzna dla $1-\alpha < 0


$$
\int_0^1 \frac{1}{x^\alpha} dx = \psi^1 - \frac{x^{1-\alpha}}{1-\alpha} 
$$

### Kryteria porównawcze

- jeżeli $$f(x) > 0 \land f(x) < g(x) \in \left(a,b\right)$ i $\int_a^b g(x) dx$ jest zbierzna
to $\int_a^b f(x) dx$ też jest zbierzna.
- jeżeli $f(x)$ jest asymptotycznie zbierzne z $g(x)$ to $\int_a^b f(x)$ i $\int_a^b g(x)$ są obie równocześnie
zbierzne lub rozbierzne.

<!-- rzecz troszeczke nielegalna -->>
### Szeregi

```{seealso}
Szerzej rozważane w MATEMATYKA 3
```

$$
\Sum_i^1^\infty a_n = a_1 + a_2 + a_3 + ... + a_\infty$ \\
$$
Jeżeli ciąg $a_n$ jest zbierzny, wtedy mówimy, że szereg jest zbierzny.

Rozważmy tzw. szereg harmoniczny:

$$
\Sum_n=1^\infty \frac{1}{n} \\
$$

```{admonition} bezwzględna zbierzność
jeżeli $\int_a^b f(x) dx$ jest zbierzna, to t acałka jest bezwzględnie zbierzna jeżeli $\int_a^b |f(x)| dx$
```

```{note}
Jeżeli całka $\int_a^b f(x)dx$ jest bezwzględnie zbierzna, to jest również zbierzna
```
