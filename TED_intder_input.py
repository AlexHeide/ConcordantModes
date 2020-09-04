import numpy as np
import os
import shutil
import re


class intder_100(object):
    def __init__(self,zmat):
        self.zmat = zmat

    def run(self):
        root = os.getcwd()
        packagepath = os.path.realpath(__file__)
        packagepath = packagepath[:-len('/100_intder_input.py')]
        
        # Do some directory tomfoolery here to get all the necessary files
        os.chdir(packagepath + '/templates')
        with open('intder_100_template.dat','r') as file:
            template = file.readlines()
        os.chdir(root)
        
        with open('SymAdaptInts.dat','r') as file:
            SymAdaptInts = file.readlines()
        
        # Now we can build the intder.inp file
        template[-1] = '{:5d}'.format(len(self.zmat.atomList)*3 - 6) + template[-1][15:]
        template[-1] = '{:5d}'.format(len(self.zmat.atomList)*3 - 6) + template[-1]
        template[-1] = '{:5d}'.format(len(self.zmat.atomList)) + template[-1]
        
        # Write the bond internal coords
        if len(self.zmat.bondIndices) > 0:
            for i in self.zmat.bondIndices:
                buffString = ''
                buffString += 'STRE '
                for j in i:
                    buffString += '{:5d}'.format(int(j))
                buffString += '\n'
                template.append(buffString)
        
        # Write the angle internal coords
        if len(self.zmat.angleIndices) > 0:
            for i in self.zmat.angleIndices:
                buffString = ''
                buffString += 'BEND '
                for j in i:
                    buffString += '{:5d}'.format(int(j))
                buffString += '\n'
                template.append(buffString)
        
        # Write the torsion internal coords
        if len(self.zmat.torsionIndices) > 0:
            for i in self.zmat.torsionIndices:
                buffString = ''
                buffString += 'TORS '
                for j in i:
                    buffString += '{:5d}'.format(int(j))
                buffString += '\n'
                template.append(buffString)
        
        # Write the symmetry adapted internal coordinates
        if len(SymAdaptInts) > 0:
            for i in SymAdaptInts:
                template.append(i)
        template.append('{:5d}'.format(0) + '\n')
        
        # Now we can write in the cartesian coordinates
        if len(self.zmat.Cartesians) > 0:
            for i in self.zmat.Cartesians:
                buffString = ''
                buffString += '{:19.10f}'.format(float(i[0]))
                buffString += '{:21.10f}'.format(float(i[1]))
                buffString += '{:20.10f}'.format(float(i[2]))
                buffString += '\n'
                template.append(buffString)
        
        # And finally, print out the atoms
        if len(self.zmat.atomList) > 0:
            buffString = ''
            for i in self.zmat.atomList:
                buffString += '{:>12s}'.format(i)
                if len(buffString) > 70:
                    buffString += '\n'
                    template.append(buffString)
                    buffString = ''
            if len(buffString) > 0:
                template.append(buffString)
            # This statement ensures there is no extra line break at the end of the file if the atom
            # number is a multiple of 6.
            else:
                template[-1] = template[-1][:-1]
        
        with open('intder.inp','w') as file:
            file.writelines(template)



