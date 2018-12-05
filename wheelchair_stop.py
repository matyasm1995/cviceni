import sys
from csv import reader,writer

if len(sys.argv) < 2:
    print('Usage: {} <filename>'.format(sys.argv[0]))
    exit(1)

filename = sys.argv[1]
print(filename)

yesl = []
nol = []
with open (filename,'r', encoding="utf-8") as f:
    # wheelchair  je 6. nebo -1. sloupec
    zast_reader = reader(f)
    for row in zast_reader:
        if row[-1]  == '0':
            continue
        if row [-1] == '1':
            yesl.append(row)
        elif row[-1] == '2':
            nol.append(row)

print('Existuje {} bezbarierovych zastavek a {} barierovych zastavek'.format(len(yesl),len(nol)))

suffix = filename[-4:] #.txt
preffix = filename[:-4] # stop

yes_filename = preffix + '_yes' + suffix
no_filename = preffix + '_no' + suffix

with open (yes_filename,'w',encoding="utf-8") as f:
    zast_writer = writer(f)
    zast_writer.writerows(yesl)

with open (no_filename,'w', encoding="utf-8") as f:
    zast_writer = writer(f)
    zast_writer.writerows(nol)

