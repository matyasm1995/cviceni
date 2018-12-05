import random
reseni = random.randint(1,100)
def osloveni (jmeno):
    if jmeno in ("Jiri","Samo"):
        return jmeno
    if jmeno in ("Jural", "Daniel"):
        return jmeno + 'i'
    if jmeno in ("Michal", "David"):
        return jmeno + 'e'
    if jmeno in ("Honza","Katka"):
        return jmeno[0:(len(jmeno)-1)] + 'o'

max_pokusu = 7
pokus = max_pokusu
vyhral = False

jmeno = input("zadej jmeno")
print("vitej " + osloveni(jmeno))

while pokus>0:
    cislo = int(input("zadej cislo"))
    if cislo == reseni:
        print('jsi borec')
        vyhral = True
        break
    if cislo < 1 or cislo >100:
        print('to asi ne')
        continue
    if reseni>cislo:
        print('resei je vetsi')
    if reseni<cislo:
        print('reseni je mensi')

    pokus -=1

print('konec hry')
if vyhral:
    print('vyhral jsi')
else:
    print('jsi looser')