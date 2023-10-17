# ALGEBRA

## Zestaw 1 zadanie 5
Korzystając z zas. indukcji udowodnij że:
dla dowolnego $n \in \mathbb{N}, n >= 4$ liczba diagonalnych
w n-koncie wypukłym jest niewiększa niż $\frac{1}{2} n(n-3)$

- utworzenie wzoru na liczbę diagonalnych
    * dla 4-kątu jest to  `1`
    * dla 5-kątu - `2`
    * dla 6-kątu - `3`

z tego wniosek, że liczba diagonalnych $d = n-3$

- sprawdzenie warunku dla ~ n = 4

$$
n-3 <= \frac{1}{2} n (n - 3)\\
dla ~ n = 4\\
1 <= 2 * 1
$$

- krok indukcyjny

$$
załóżmy, że: \\
\frac{1}{2}n (n-3) >= n-3 \\
n (n-3) >= 2n-6 \\
n^2 - 3n >= 2n-6 \\
n^2 - 5n + 6 >= 0 \\
wtedy~dla~n+1:\\
\frac{1}{2}(n+1)(n-2) >= n-2 \\
n^2-n-2 >= 2n-4 \\
n^2-3n+2 >= 0 \\
(n^2-5n+2) + (2n - 4) >= 0\\
\begin{matrix}
(n^2-5n+2) &  + & (2n - 4) & >= 0\\
z~ind~mat. &    & \forall n >= 4 2n - 4 >=0 &
\end{matrix}
$$
