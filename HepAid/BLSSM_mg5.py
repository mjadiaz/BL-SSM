import HepRead
import HepTools
import os

model = 'BLSSM'
work_dir = '/scratch/mjad1g20/HEP/WorkArea/BLSSM_Work'
spheno_dir = '/scratch/mjad1g20/HEP/SPHENO/SPheno-3.3.8'
reference_lhs = '/scratch/mjad1g20/HEP/SPHENO/SPheno-3.3.8/BLSSM/Input_Files/LesHouches.in.BLSSM'
madgraph_dir = '/scratch/mjad1g20/HEP/MG5_aMC_v3_1_1'

# Initiating Madgraph
mg5 = HepTools.Madgraph(madgraph_dir, work_dir)

# Selected param_card.dat
param_card_path = os.path.join(work_dir,'SPhenoBLSSM_output/SPheno.spc.BLSSM_HEscan_770')

# UFO model name in madraph_dir
ufo_model = 'BLSSM-2'

# Creating the Madgraph script
script = HepRead.MG5Script(work_dir,ufo_model)

processes = [['p p > h1, h1 > a a', 'pph1aa'],
             ['p p > h2, h2 > a a', 'pph2aa'],
             ['p p > a a / h1 h2', 'ppaa_bg']]

for p in processes:
    process, syntax = p
    script.process(process)
    script.output(syntax)
    script.launch(syntax)
    script.param_card(param_card_path)
    script.delphes_card('/mainfs/scratch/mjad1g20/HEP/MG5_aMC_v3_1_1/Delphes/cards/delphes_card_CMS.tcl')
    script.write()
    mg5.run()
