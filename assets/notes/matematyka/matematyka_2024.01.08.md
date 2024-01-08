## Całka Oznaczona (Rimana)

Podzielmy przedział $(a, b)$ na `n` części, w taki sposób.

$$
\Delta x_i  = |X_i - X_{i-1}| \\
\delta_n = max(\Delta x) \\
\\
s_n = \Sigma_{i} n_i * \Delta x_i \\
c_n = \Sigma_i \psi(i) \Delta x_i \\
S_n = \Sigma_i M \Delta x_i \\
$$

- $n_i$ to infinum funkcji w danym przedziale (najmniejsza wartość)
- $M$ to supremum funckji w danym przedziale (czyli mnożenie przez największą wartość funkcji w przedziale)

```{tip}
$s_n$ reprezentuje sumę wszystkich prostokątów w zaokrągleniu pod wykresem, natomiast $S_n$ - wszystkich
kawałkóœ zaokrąglonych do maksymalnej wartości
```

```{admonition} definicja całki oznaczonej
Jeżeli suma $\sigma_n$ przy dowolnym coraz róœniejszym podziale
(tzn. przy $\sigma_n \to 0$) dąży do tej samej granicy niezależnie
od wyboru punktóœ podziału ani od wyboru od wyboru punktów $\psi_i$ to 
granicę tę nazywamy **Całką Oznaczoną** z funkcji `f` w przedziale $\left<a, b\right>$
(tzw. całka Rimmana)

Oznaczenia:

$$
\int_a^b f(x)dx = \int_{\left<a, b\right>} f
$$
```

Całka nie zawsze istnieje.

Całka $\exists \int_a^b  \Leftrightarrow s_n = S_n$


```{tip}
:::{admonition} funkcja jednostajnie ciągła
f jest jednostajnie ciągła, $\forall \epsilon > 0, \exists \delta > 0$
że jeżeli $|x-x'| < \delta \Rightarrow f(x) - f(x') < \epsilon$
:::

$\epsilon > 0$ i f jednostajnie ciągła, $x-x' < \epsilon \Rightarrow f(x)-f(x')<\delta$

$$
S_n - s_n = \Sigma_i x_i (M-m ) <= \epsilon \Sigma_i x_i = \epsilon (a-b)
$$
```

### Własności całki Rimmana

- spełnia zasadę liniowości (rozdzielność względem dodawania oraz mnożenia przez skalar)
- addytywność względem przedziału - jeżeli $c \in \left<a,b\right>$ to
$\int_a^b f = \int_a^c f + \int_c^b f$
- $m(b-a)\leq \int_a^b \leq M(b-a)$
- twierdzenie o wartośći średniej dla całęk (jeżeli f ciągła) $\exists \psi \in \left<a,b\right> ~ \frac{1}{b-a} \int_a^b f = f(\psi)$
