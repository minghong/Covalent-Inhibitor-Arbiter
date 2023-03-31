
import csv
from rdkit.Chem import BRICS
from rdkit import Chem
a=open('d:\\2.txt',mode='w')
f = csv.reader(open('e:\\b.csv','r'))
for i in f:
    flag=0
    m = Chem.MolFromSmiles(i[2])
    z=BRICS.BRICSDecompose(m)
    for r in z:
        if(i[3] not in r):
            flag=1
            a.writelines(r+";")      
    if(flag==0):
        a.writelines("0"+" ") 
    a.write("\n")
a.close()
