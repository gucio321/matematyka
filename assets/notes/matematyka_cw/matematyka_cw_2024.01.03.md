## Całki - Istotne wzory / wyprowadzenia

- Wzór redukcyjny (na $sin^nx$)

$$
\int sin^n x = -\frac{sin^{n-1}x * cos~x}{n} + \frac{n-1}{n} \int sin^{n-2}x dx
$$

<details><summary>Wyprowadzenie</summary>

$$
\int sin^nx = \\
= \int sin^{n-1}x* sin~x = \\
\left|\begin{matrix}
u = sin^{n-1}x && v' = sin~x \\
u' = (n-1)sin^{n-2}x cos~x && v = -cos~x \\
\end{matrix}\right| = \\
= - sin^{n-1}x * cos~x + (n-1)\int sin^{n-2} cos^2x = \\
= - sin^{n-1}x * cos~x + (n-1)\int sin^{n-2}x (1- sin^2x) dx = \\
= - sin^{n-1}x * cos~x + (n-1)\int sin^{n-2}x - (n-1) \int sin^nx \\
\\
n \int sin^n x dx = - sin^{n-1}x * cos~x + (n-1)\int sin^{n-2}x dx \\
\int sin^n x dx = -\frac{ sin^{n-1}x * cos~x}{n} + \frac{n-1}{n}\int sin^{n-2}x dx \\
$$

</details>
