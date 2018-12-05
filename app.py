strana = input ("rekni ahoj")
pocet_a = 0
pocet_b = 0
pocet_c = 0
pocet_d = 0

while strana != "konec":
    strana = input("zadej stranu nebo konec")
    if strana == "konec":
        break
    hlas = int(input ("zadej pocet hlasu"))
    if strana == "a":
        pocet_a = pocet_a + hlas
    if strana == "b":
       pocet_b = pocet_b + hlas
    if strana == "c":
       pocet_c = pocet_c + hlas
    if strana == "d":
        pocet_d = pocet_d + hlas
print("a=", pocet_a, "b=", pocet_b, "c=", pocet_c, "d=", pocet_d)