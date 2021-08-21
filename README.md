# BLSSM-Double-Peak


## The analisys of the MadGraph runs are explained in [Double-Higgs-Production.md](Double-Higgs-Production.md)

* [Codes](Codes) folder contains the script to calculate the processes in MadGraph.
    1) [compute_processes.py](Codes/compute_processes.py): Creates a txt file with the commands to copute each process.
    2) [read_lhe.py](Codes/read_lhe.py): Uses the **Pylhe** library to read the output (lhe file) of MadGraph and save the invariant mass of each event in the [double_peak_data](Codes/double_peak_data) folder. 
    3) [events_invariant_mass_plot.py](Codes/events_invariant_mass_plot.py): Creates the histograms with the data.
