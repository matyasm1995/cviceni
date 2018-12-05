import json
z = {'jmeno': 'Albertov', 'pasmo': 'P', 'seznam_linek':[7,18,14,24,93], 'prist': True , 'ID':493843}
print(z)
if 'ID' in z:
    print('id je {}'.format(z['ID']))
else:
    print('ID neni')

for k in z:
    print('{} = {}'.format(k, z[k]))

for k, v in z.items():
    print('{} = {}'.format(k, v))

k, v = ('jmeno', 'Albertov')

print(k, v)

znamky = {1: 'vyborne', 2: 'nic moc', 3: 'neprospel'}
print('hodnoceno {}'.format(znamky[2]))


druhy={1:"metro",2:"tramvaj",4:"autobus",6:"tramvaj a autobus",8:"lanovka",16:"vlak", 20:"vlak a autobus", 32:"ostatni"}
seznam = []

def filter(pasmo):
    with open("zastavky.json", encoding="utf-8") as f:
        zastavky = json.load(f)
    features = zastavky["features"]
    for f in features:
        props = f["properties"]
        if props['ZAST_PASMO'] is None:
            continue
        if pasmo in props['ZAST_PASMO']:
            if props["ZAST_DD"] in druhy:
                seznam.append(props['ZAST_NAZEV'])
                seznam.append(druhy[props["ZAST_DD"]])
    print(seznam)

filter("P")