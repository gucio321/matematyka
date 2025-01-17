# Laboratorium Fizyczne - Kartkówka

## Tranzystor (125)

- Tranzystor to element półprzewodnikowy
- Budowa: Emiter (wytwarzane są z niej łądunki), Baza (steruje przepływem łądunków), Kolektor (zbiera ładunki)
- Podział [ref](https://pl.wikipedia.org/wiki/Tranzystor):
    * Bipolarne i Uniplorane
    * pnp i npn (dla bipolarnych) - ze względu na warstwy przewodzenia
    * materiał wykonania (krzem, german, e.t.c.)
    * {małej, dużej} mocy {małej, wielkiej} częstotliwości e.t.c.
- Prąd dyfuzyjny - mechanizm transportu ładunków w tranzystorze - związany z przemieszczaniem nośników (elektronów lub dziur) wzdłuż gradientu stężeń.
    * $J_n = q * \frac{\partial n}{\partial x}$ (dla elektronów. analogicznie dla dziur) gdzie n i p to koncentracja nośników (odpowiednio).
- Polaryzacje złącza Baza-Emiter (EB):
    * w kierunku przewodzenia: nośniki przepływają z emitera do bazy (odpowiedni potencjał emitera względem bazy)
    * w kierunku zaporowym: odwrotna polaryzacja niż ww. Blokuje przepływ prądu.
- $\frac{e}{k}$ oznacza stosunek ładunku elektrycznego do stałej Boltzmanna
- Stała Boltzmana łączy energię kinetyczną cząstek z temperaturą.
- Zastosowania: Silnik Cieplny (cykl Carnot'a), Rozkład Boltzmana
- dlaczego tranzystor bipolarny a nie dioda? W tranzystorze bipolarnym łątwo da się zbadać charakterystykę prądową (prąd kolektora $I_c$ zależy od $U_{EB}$. zależność t ajest znana $I_C = A*exp(\frac{U_{EB}}{kT})$)

## Halotron (43)

- Napięcie Halla - Napięcie powstałe w przewodniku z prądem umieszczonym w polu magnetycznym.
    * ładunki płyną przez halotron
    * po "włączeniu" B, ładunki pod wpływem siły lorentza zostają przeciągnięte na jdeną stronę przewodnika
    * ponieważ jednoimienne ładunki sią na jednej stronie przewodnika powstaje napięcie zwane napięciem Hala.
- Stała Halotronu zależy od materiału wykonania urządzenia. Określa intensywoność zjawiska $R_H = \frac{I* d}{U * B}$.
- Kalibracja: Przy znanym B dokonujemy pomiarów napięcia halla.
- Zastosowania:
    * pomiar prędkości kątowej
    * bezkontaktowy pomiar prądu
    * kompas (w smartfonach)
- Halotron wykorzystuje siłę Lorentza
- Pomiar: B ~ c*U

## Dozymetria (96)

- Radioaktywne izotopy używane w labie to m.in. Cez (Cs) bądź Kobalt (Co)
- Izotopy promieniotwórcze to materiały niestabilne ulegające rozpadowi po określonym czasie (określany probabilistycznie).
- Aktywność:
    * Miara liczby rozpadów w czasie $\frac{dN}{dt}$
    * Zależy od:
        - Liczby jąder
        - Okresu połowicznego rozpadu $T_{\frac{1}{2}}$
        - rodzaju promieniotwórczości (alfa, beta, gamma)
    * Zmienia się w czasie jak $e^{-\lambda t}$ gdzie $\lambda = \frac{ln(2)}{T_{\frac{1}{2}}}$
- Zależnośc mocy dawki od odległości wynika z zasady kwadratu odległości $P \sim \frac{1}{r^2}$
- Rodzaje promieniowania:
    * $\alpha$ (duża energia, niska penetracja),
    * $\beta$ (średnia energia, średnia penetracja),
    * $\gamma$ (niska energia, duża penetracja)
- prawo osłabienia $I(x) = I_0 * e^{-\mu x}$ gdzie $\mu$ to współczynnik osłabienia - zależy od energii promieniowania i od materiału.
- Czas połowicznego rozpadu wiąże się ze stałą rozpadu jak $T_{\frac{1}{2}} = \frac{ln(2)}{\lambda}$

## Kriogenika (113)

- Ciekły azot z uwagi na swą "ciekłość" utrzymuje stałą temperaturę $-209^oC$ (tak jak lód dopuki jest lodem ma najwyżej $0^oC$)
