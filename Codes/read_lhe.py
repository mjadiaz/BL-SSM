    #%%
import pylhe
import math
import numpy as np
import pandas as pd
import os
import subprocess
import gzip
import shutil


from compute_processes import process, madgraph_path, param_card_name, param_card_path, output_name
#%%

#process = [['p p > z,( z > l+ l- a $a,( a > l+ l-))', 'ppza4l_test_2']]
def invariant_mass(p1, p2, p3, p4):
    return math.sqrt(
        sum(
            (1 if mu == "e" else -1) * (getattr(p1, mu) + getattr(p2, mu) + getattr(p3, mu) + getattr(p4, mu)) ** 2
            for mu in ["e", "px", "py", "pz"]
        )
    )


def PT(p1):
    return math.sqrt(
        sum((getattr(p1, mu)) ** 2 for mu in ["px", "py"])
    )
# %%


if __name__ == '__main__':

    cut_pt = 5
    cut = True

    # Create directory for store the data
    if not os.path.exists('double_peak_data'):
        os.makedirs('double_peak_data')

    
        

    for p in range(3):

        lhe_path = madgraph_path+output_name+process[p][1]+'/Events/run_01'
        lhe_file  = lhe_path+'/unweighted_events.lhe'

        # Unzip the LHE.gz files 
        with gzip.open(lhe_path+'/unweighted_events.lhe.gz', 'rb') as f_in:
            with open(lhe_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        # Get the invariant mass data for each process
        invariant_mass_vec = np.array([])       #  Vector to store the invariant mass
        for e in pylhe.readLHE(lhe_file):
            # block raising an exception
            m = invariant_mass(e.particles[-1], e.particles[-2],  e.particles[-3], e.particles[-4])
            
            PT_event_list = [PT(e.particles[-1]),PT(e.particles[-2]),PT(e.particles[-3]),PT(e.particles[-4])]
            above_cut_test =  all(x > cut_pt for x in PT_event_list)
            if cut == True:
                if above_cut_test == True:
                    print('all above cut in: ', PT_event_list)
                    invariant_mass_vec=np.append(invariant_mass_vec,m)
                # print('at least one bellow cut in: ', PT_event_list)
                # print(invariant_mass_vec)
            else:
                invariant_mass_vec=np.append(invariant_mass_vec,m)

        df = pd.DataFrame(invariant_mass_vec,columns=['imass'])
        print(df.head(), len(df))
        df.to_csv('double_peak_data/'+process[p][1]+'.csv')
        print(lhe_path, ' Done')


