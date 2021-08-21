import os
import subprocess
import gzip
import shutil

#from compute_processes  import process, output_name, madgraph_path

process=    [['p p > z > l+ l- a $a , a > l+ l-', 'ppza4l'],
             ['p p > h1 > z z, (z > l+ l-, z > l+ l-)', 'pph14l'],
             ['p p > h2 > z z, (z > l+ l-, z > l+ l-)', 'pph24l'],
             ['p p > h1 > a a','pph1aa'],
             ['p p > h2 > a a','pph2aa']]

madgraph_path = '/home/mjad1g20/HEP/MG5/MG5_aMC_v3_1_1'  
output_name = '/double_peak/'

delphes_path = '/home/mjad1g20/HEP/DELPHES/Delphes-3.5.0'
delphes_card = '/mainfs/home/mjad1g20/HEP/DELPHES/Delphes-3.5.0/cards/delphes_card_CMS.tcl'
DelphesHepMC2 = '/mainfs/home/mjad1g20/HEP/DELPHES/Delphes-3.5.0/DelphesHepMC2'


#print(DelphesHepMC2)

if not os.path.exists(delphes_path+output_name):
    print('Create directory for Delphes output: {}'.format(output_name))
    os.makedirs(delphes_path+output_name)

def gunzip(gzfile, gunzipfile):
    with gzip.open(gzfile, 'rb') as f_in:
        with open(gunzipfile, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

for p in process:
    _, p_name = p

    hepmc_path = madgraph_path+output_name+p_name+'/Events/run_01/tag_1_pythia8_events.hepmc'
    delphes_output = delphes_path+output_name+p_name+'.root'

    print(hepmc_path)
    
    if os.path.exists(delphes_output):
        print('Removing existing .root output for the process')
        os.remove(delphes_output)
    
    if not os.path.exists(hepmc_path):
        print('Unzip hepmc.gz for DelphesHepMC2')
        gunzip(hepmc_path+'.gz',hepmc_path)
    
    print('Running DelphesHepMC2')
    #run_delphes = subprocess.run([DelphesHepMC2, delphes_card, delphes_output, hepmc_path], capture_output=True, text=True)
    subprocess.run([DelphesHepMC2, delphes_card, delphes_output, hepmc_path])


    # if os.path.exists(delphes_path+output_name+p_name+'_output.txt'):
    #     os.remove(delphes_path+output_name+p_name+'_output.txt')
    # with open(delphes_path+output_name+p_name+'_output.txt','w') as f:
    #     f.write(run_delphes.stdout)
    #     f.write(run_delphes.stderr)
    
    print('Removing hepmc file ... t0o heavy')
    os.remove(hepmc_path)



    

    