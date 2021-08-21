#%%
import os
import subprocess
import random
#%%
############################
# Paths and processes info #
############################

# MadGraph process syntax and launch/output name
#process=    [['p p > h1 > z z, z  > l+ l-,z > l+ l-', 'pph12z4l']]
#process=    [['p p > h2 > a a', 'pph2aa']]
process=    [['p p > h1 > a a','pph1aa'],
             ['p p > h2 > a a','pph2aa'],
             ['p p > h1 > z z, (z > l+ l-, z > l+ l-)', 'pph14l'],
             ['p p > h2 > z z, (z > l+ l-, z > l+ l-)', 'pph24l'],
             ['p p > z > l+ l- a $a , a > l+ l-', 'ppza4l']]
# wget https://launchpad.net/mg5amcnlo/3.0/3.1.x/+download/MG5_aMC_v3.1.1.tar.gz

madgraph_path = '/scratch/mjad1g20/HEP/MG5_aMC_v3_1_1'  


param_card_name_2 = '/SPheno.spc.BLSSM'
param_card_path_2 = '/home/mjad1g20/HEP/SPHENO/SPheno-3.3.8'
param_card_name = '/param_card.dat'
param_card_path = '/home/mjad1g20/HEP/WorkArea/BLSSM-Double-Peak/Codes/Cards'

delphes_card = '/mainfs/home/mjad1g20/HEP/WorkArea/BLSSM-Double-Peak/Codes/Cards/delphes_card_CMS.dat'

output_name = '/double_peak/'

#################################
# Compute processes in Madgraph #
#################################
if __name__ == '__main__':

    #for p in range(len(process)):
    for p in process:
        mg5_syntax, p_name = p

        

        f = open(madgraph_path+'/compute_process.txt',"w+")
        f.write('import model BLSSM-2 --modelname\n')
        f.write('define p = g d1 d2  u1 u2  d1bar d2bar u1bar u2bar\n')
        f.write('define l+ = e1bar e2bar\n')
        f.write('define l- = e1 e2\n')
        f.write('generate '+mg5_syntax+'\n')

        while os.path.exists(madgraph_path+output_name+p_name):
            p_name = p_name+'_'+str(random.randint(1,100))

        f.write('output '+madgraph_path+output_name+p_name+'\n')
        f.write('launch '+madgraph_path+output_name+p_name+'\n')
        f.write('shower=Pythia8\n')
        f.write('detector=Delphes\n')
        f.write('0\n')
        f.write(param_card_path_2+param_card_name_2+'\n')
        f.write(delphes_card+'\n')
        f.write('set mh1 = 125\n')
        f.write('set mh2 = 136\n')
        f.write('set ebeam1 = 4000.0\n')
        f.write('set ebeam2 = 4000.0\n')
        f.write('0\n')
        f.close()

        subprocess.call([madgraph_path+'/bin/mg5_aMC', madgraph_path+'/compute_process.txt'])
        break
    
    os.remove(madgraph_path+'/compute_process.txt')
    
