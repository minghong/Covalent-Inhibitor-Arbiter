from multiprocessing import freeze_support
import csv
from rdkit import Chem
from mordred import Calculator, descriptors
import warnings

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    freeze_support()
    calc = Calculator(descriptors,ignore_3D=True)
    f = csv.reader(open('e:\\b.csv','r'))
    mols = []
    for i in f:
        m = Chem.MolFromSmiles(i[0])
        mols.append(m)
    

    h=calc.pandas(mols)
    h.to_csv(r'D:/2.csv')
