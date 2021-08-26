import os 
import re
import subprocess

import time




class pySpheno:
    def __init__(self, spheno_dir):
        self._dir=spheno_dir
        self.models = pySpheno._models_in_dir(self)
    
    def _models_in_dir(self):
        models = []
        for f in os.listdir(self._dir+'/bin'):
            if not (re.search(r'SPheno\w+',f)==None):
                m = re.search('(?<=SPheno).*','SPhenoBLSSM')[0]
                models.append(m)
        return models

    def run(self, model, in_file, out_file):
        #subprocess.call([self._dir+'/bin'+'/SPheno'+model, in_file])
       
        run = subprocess.run([self._dir+'/bin'+'/SPheno'+model, in_file, out_file], capture_output=True, text=True)        
        if 'Finished' in run.stdout:
            print(run.stdout)                
        else:
            print('Error')
            

       
        


spheno_dir = '/home/mjad1g20/HEP/SPHENO/SPheno-3.3.8'
in_file = '/mainfs/home/mjad1g20/HEP/SPHENO/SPheno-3.3.8/LesHouches.in.BLSSM_low'
out_file = '/mainfs/home/mjad1g20/HEP/WorkArea/BLSSM-Double-Peak/Codes/spheno_cards/param_card.dat'


spheno = pySpheno(spheno_dir)
spheno.run(model='BLSSM', in_file=in_file, out_file=out_file)


