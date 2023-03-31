import csv
from rdkit.Chem import BRICS
from rdkit import Chem
import random
from rdkit.Chem import RDConfig
import os

def cor(i):
    m=Chem.MolFromSmiles(i)
    z=BRICS.BRICSDecompose(m)
    file=csv.reader(open('e:\\covalent.csv','r'))
    for k in file:
        for r in z:
            if(k[0] in r):
                return True
    return False

if __name__ == '__main__':
    f=csv.reader(open('e:\\b.csv','r'))
    a=open('d:\\2.txt',mode='w')
    allfrags=set()
    for m in f:
        allfrags.update(m)
    fragms = [Chem.MolFromSmiles(x) for x in sorted(allfrags)]
    
    ms = BRICS.BRICSBuild(fragms)
    new=[next(ms) for x in range(100)]
    
    for i in new:
        i.UpdatePropertyCache(strict=False)
    for i in range(100):
        h=Chem.MolToSmiles(new[i],True)
        if(cor(h)):
            a.write(h+'\n')
    a.close()
                
