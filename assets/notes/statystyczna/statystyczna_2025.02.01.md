### Rozkłady

1. Poissona $P_k(\mu) = \frac{\mu^k}{k!}e^{-\mu}$, gdzie $\mu > 0$.
Wartość oczekiwana: $E(X) = \mu$ (jedyne dziwne przejście to z Teylora mamy $\sum_{i=1}^{\infty} \frac{\mu^i}{i!} = e^{\mu}$).
2. Geometryczny $G(p) = p* (1-p)^{k-1}$, gdzie $k \in \mathbb{N}$.
Wartość oczekiwana: $E(X) = \frac{1}{p}$ (w obliczeniu robimy pochodna z $\sum_k^\infty q^k = \frac{1}{1-q}$ - suma ciągu geometrycznego)

### Populacja a Próba

Prawdę mówiąc te pojęcia są często używane praktycznie wszędzie w wykładach ale... jest to  trochę mylące.

```{admonition} Populacja
zbiór **WSZYSTKICH** obiektów, które nas interesują.

Na przykład - badając wzrost ludzi na świecie populację stanowią... wszyscy ludzie na świecie.
Inny przykład - badamy czy cegły danego producenta są wadliwe. Populacje stanowią wszystkie cegły tego kolesia ever.
```

```{admonition} Próba
jak widać z powyższej definicji badanie całej populacji jest średnio wykonalne/praktyczne.

**Próba** to __Element__ populacji co do którego mamy dane.

W przykładach powyżej:
- 1000 losowo wybranych osób
- n losowych cegieł.
```

| Nazwa          | Populacja | Próba    |
|----------------|-----------|----------|
| średnia        | $\mu$     | $\bar{x} |
| wariancja      | $\sigma^2$| $s^2$    |


```{admonition} Centralne Twierdzenie Graniczne
mamy n niezależnych zmiennych losowych $X_1, X_2, ..., X_n$ pochodzących z tego samego rozkładu.

Niech: $S_n = X_1 + X_2 + ... + X_n$ oraz $\bar{X} = \frac{S_n}{n}$

wtedy dzieje się fajna rzecz, otóż:

$$
\lim_{n \to \infty} \frac{S_n - n\mu}{\sigma \sqrt{n}} = \frac{\bar{x} - \mu}{\frac{\sigma}{\sqrt{n}}} = N(0,1)
$$
```

Polecam poniższy kod:

```python
import numpy as np
import matplotlib.pyplot as plt

def central_limit_theorem_demo(sample_size=1000, num_samples=10000): # ode mnie: można ustawić sample size na 1 i za dużo to nie zmieni - dalej działa
    means = []
    for _ in range(num_samples):
        sample = np.random.uniform(0, 1, sample_size)  # Losujemy próbkę z rozkładu jednostajnego
        means.append(np.mean(sample))  # Obliczamy średnią próbki

    # Rysowanie histogramu średnich
    plt.hist(means, bins=50, density=True, alpha=0.6, color='b')

    # Teoretyczna krzywa normalna
    mu = 0.5  # Średnia rozkładu jednostajnego U(0,1)
    sigma = np.sqrt(1/12) / np.sqrt(sample_size)  # Wariancja U(0,1) wynosi 1/12
    x = np.linspace(min(means), max(means), 100)
    plt.plot(x, (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(- (x - mu) ** 2 / (2 * sigma ** 2)), 'r', linewidth=2)

    plt.title(f'CTG: Średnie {num_samples} próbek (rozmiar próbki={sample_size})')
    plt.xlabel('Średnia próbek')
    plt.ylabel('Gęstość prawdopodobieństwa')
    plt.show()

# Uruchamiamy demonstrację
central_limit_theorem_demo(sample_size=30, num_samples=10000)
```
