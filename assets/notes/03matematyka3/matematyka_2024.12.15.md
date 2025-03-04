## Szeregi Fouriera

Po pierwsze, przepraszam za długi brak update'ów strony - w tym semestrze wiekszość rzeczy
zamiast z wykładów ogarniam z youtube albo gotowych prezentacji ze stron prowadzących,
więc robienie notatek na bierząco przestało mieć sens.
Zapraszam do zerknięcia na ref'y na poszczegulnych podstronach.

Rozważamy funkcję $f(x)$ na przedziale $[-p, p]$. Wtedy szereg Fouriera tej funkcji to:

```{admonition} Warunki Dirichleta:
- funkcja jest przedziałami monotonicnza (czyli na przykład nie funkcja weierstrassa)
- funkcja ma skończoną liczbę punktów nieciągłości, z tym, że $f(x) = \frac{f(x^+) + f(x^-)}{2}$
- funkcja na granicach przedziału spełnia warunek $f(-p) = f(p) = \frac{f(p) + f(b)}{2}$
```

Definiujemy następujące ciągi:

$$
a_n = \frac{1}{p} \int_{-p}^{p} f(x) \cos\left(\frac{n\pi x}{p}\right) dx \\
b_n = \frac{1}{p} \int_{-p}^{p} f(x) \sin\left(\frac{n\pi x}{p}\right) dx
$$

```{tip}
w skrajnym przypadku $a_0$ przyjmuje postać:

$$
a_0 = \frac{1}{p} \int_{-p}^{p} f(x) dx
$$

```

Szereg Fouriera funkcji $f(X)$ przyjmuje następującą postać:

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left(a_n \cos\left(\frac{n\pi x}{p}\right) + b_n \sin\left(\frac{n\pi x}{p}\right)\right)
$$
