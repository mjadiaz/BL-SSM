import numpy as np

import HepRead
import HepTools
import os

from HepTools import Scanner as sc

model = 'BLSSM'
work_dir = '/scratch/mjad1g20/HEP/WorkArea/BLSSM_DoublePeak'
spheno_dir = '/scratch/mjad1g20/HEP/SPHENO/SPheno-3.3.8'
reference_lhs = '/scratch/mjad1g20/HEP/SPHENO/SPheno-3.3.8/BLSSM/Input_Files/LesHouches.in.BLSSM'
madgraph_dir = '/scratch/mjad1g20/HEP/MG5_aMC_v3_1_1'


SPhenoBLSSM = HepTools.Spheno(spheno_dir, work_dir ,model)
lhs  = HepRead.LesHouches(reference_lhs, work_dir, model)


# Fixed parameters
option, value = [8,7,3], [1700,1.15,5]
for i,j in zip(option, value):
    lhs.block('MINPAR').set(i,j)

[lhs.block('EXTPAR').set(i,0) for i in [11,12,13,14]]
option, value = [3,10,1,2], [1700,1.15,0.55,-0.12]
for i,j in zip(option, value):
    lhs.block('EXTPAR').set(i,j)

# Spheno options to run with Madgraph
option = [13, 16,78,520,67,60] 
value  = [3,0,1,0,1,1]
for i,j in zip(option, value):
    lhs.block('sphenoinput').set(i,j)

# Turning off loop decay options because they are already defined
option = [1,2,3,4,5,6,7,8,9,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013] 
value  = np.zeros(len(option),dtype = int)
for i,j in zip(option, value):
    lhs.block('decayoptions').set(i,int(j))
                                  



# Scanned parameters 
m0 = lambda low, high: sc.runiform_float(low,high)
m12 = lambda low, high: sc.runiform_float(low,high)
a0 = lambda low, high: sc.runiform_float(low,high)
N_POINTS = 1000

points = 0
index = []
for i in range(N_POINTS):
    
    lhs.block('MINPAR').set(1,m0(100,1000))
    lhs.block('MINPAR').set(2,m12(2000,4500))
    lhs.block('MINPAR').set(5,- a0(1000,4000))
    new_lhs_name = 'LesHouches.in.BLSSM_HEscan_'+str(i)
    out_spheno_name = 'SPheno.spc.BLSSM_HEscan_'+str(i)
    # Creating the new LesHouches file, and runing Spheno.
    lhs.new_file(new_lhs_name)
    param_card_path = SPhenoBLSSM.run(new_lhs_name,out_spheno_name)
    # Reading spheno output
    if not(param_card_path==None):
        points = points + 1
        index.append(i)
        
        
        
with open('number_of_points.txt','w+') as f:
    f.write(f'{points} \n')
    for i in index:
        f.write(f'{i} \n')
    
        





