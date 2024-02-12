## Ciągi

Zbierzność asymptotyczna $\frac{a_n}{b_n} \to 1$

```{admonition} wzór Sterlinga
$n! \~ n^n - e^{-n} \sqrt{2 \pi n}
```

### ważne granice
- 
$$
\lim_{x \to 0} \frac{sin(x)}{x} = 1 \\
$$
- 
$$
dla~a > 1\\
lim_{x \to 0} a^x = 1\\
\forall n \in \mathbb{N} ~a^{\frac{1}{n+1}} < a^x < a^{\frac{1}{n}}
$$

- 
$$
\lim_{h \to 0} \frac{a^h - 1}{h} = logn~a \\
$$

## Funkcje ciągłe

$$
niech~f: D \rightarrow \mathbb{R}
$$

f jest ciągła w punkcie $x_0 \in D$ jeśli $\exists \lim_{x \to x_0} = f(x_0)$

```{important}
funkcja $f(x) = \frac{1}{x} ~ x \neq 0$ jest ciągła, mimo, że w $x_0 = 0$ granica
nie istnieje, ponieważ $x_0 \notin D$
```

```{tip}
$f(x) = sin \frac{1}{x}$
<!--f(x) = sin 1/x-->
<iframe src="https://www.desmos.com/calculator/ikwyzx40pl" width="100%" style="min-height:200px"></iframe>
```

#### Własności funkcji ciągłych

```{admonition} Twierdzenie o lokalnym zachowaniu znaku
niech f ciągła. Dla dowolnego punktu $x_0 \land f(x_0) > 0 \Rightarrow \exists a = \left(x_0 - \epsilon, x_0 + \epsilon \right) taki~że \forall x_a \in a~ f(x_a) > 0$
```

```{tip}
jeżeli f jest ciągła oraz $\exists a, b ~ f(a) < 0 \land f(b) > 0 \Rightarrow \exists x_0 \in (a, b) ~ f(x_0) = 0$
```

```{admonition} Twierdzenie Bezuta
jeżeli $x_0$ jest pierwiastkiem wielomianu to wielomian $W(x)$ można
przedstawić jako $W(x) = (x - x_0)P(x)$
```

```{admonition} własoność Garbouta
własnność o przyjmowaniu wartościpośrednich

dla $f: I \to \mathbb{R}$
Jeżeli f(a) = m i f(b) = M $\land  m < M \land m < W < M$

$\bf{\forall W \in (m, M) \exists x \in (a, b)~f(x) = W}$
```
