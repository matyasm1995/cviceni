import json, csv


def zastavky_v_pasmu(zastavky, pasmo):
    jmena = []
    for z in zastavky:
        props = z["properties"]
        if props["ZAST_PASMO"] is None:
            continue
        if pasmo in props["ZAST_PASMO"]:
            jmena.append(props["ZAST_NAZEV"])
    return jmena


with open("zastavky.json", encoding="utf-8") as f:
    zastavky = json.load(f)

features = zastavky["features"]
zastavky_P = zastavky_v_pasmu(features, "P")


with open('zastavky_out.txt', mode='w', encoding='utf-8') as f: # vytvori novy format
    writer = csv.writer(f)
    for z in zastavky_P:
        #f.write(z)
        #f.write('\n')
        #print(z, file=f)
        writer.writerow([z])
with open('zastavku_out.json', mode='w') as f: # vytvori kopiii souboru
    json.dump(zastavky, f)


def uloz_nasobnosti(nas):
    with open('nasoubnosti_out.txt', mode='w') as f:
        writer = csv.writer(f)
        #for k, v in nas.items():
            #writer.writerow([k, v])
        writer.writerow(nas.items())

def spocti_nasobnosti(zastavky):
    nasobnosti = {}
    for k in zastavky:
        if k in nasobnosti:
            nasobnosti[k]+=1
        else:
            nasobnosti[k]=1
    print(nasobnosti)

nas={'andel':10, 'zvichov':2, 'lihovat':3}
#uloz_nasobnosti(nas)
spocti_nasobnosti(zastavky_P)

exit()
