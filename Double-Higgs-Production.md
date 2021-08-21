#research
## Double peak Higgs Production
We want to recreate the higgs production plots from [2015. W. Abdallah. S. Khalil. S. Moretti](References/Files/2015.%20S.%20Moretti.%20Double%20Higgs%20peak%20in%20the%20minimal%20SUSY%20B%20−%20L%20model.pdf). I used UFO and Sarah files from the model from [B-L-SSM – Trac – Hepforge (sarah.hepforge.org)](https://sarah.hepforge.org/trac/wiki/B-L-SSM).  This model was created by L.Basso, F.Staub. 

I generated the param_card.dat files with SPheno with the low energy limit of the Les Houches file. [LesHouches.in.blssm](Files/LesHouches.in.blssm). The input parametes are the ones in TABLE I in [2015. W. Abdallah. S. Khalil. S. Moretti](References/Files/2015.%20S.%20Moretti.%20Double%20Higgs%20peak%20in%20the%20minimal%20SUSY%20B%20−%20L%20model.pdf).

![inputs](Files/Pasted%20image%2020210331203159.png)

- One issue was that in the Les Houches File I have to give also values to the Td, Te, Tx, Tu, Tv, MBBp, MBp and M1, M2, M3. 

To run Madgraph I got the SPC file from SPheno and modified by hand the masses of $h_{SM}$, $h_1$ and $h_2$.

## Plots

### All events
- generate p p > z,( z > l+ l- a $a, a > l+ l-)

- generate p p > h1, (h1 > z z,(z > l+ l-, z > l+ l-))

- generate p p > h2, (h2 > z z,(z > l+ l-, z > l+ l-))
- 
![inputs](Files/Pasted%20image%2020210331122545.png)

* param_card.dat: [param_card_modified.dat](Files/param_card_modified.dat)


I tried also with:
- generate p p > z, z > l+ l- l+ l-

![inputs](Files/Pasted%20image%2020210331194822.png)

Finally this worked better:
-generate p p > z,( z > l+ l- a $a,( a > l+ l-))

![inputs](Files/Pasted%20image%2020210331201848.png)

### With $p_T$ cut of 5 GeV on the four leptons
- generate p p > z,( z > l+ l- a $a, a > l+ l-)
 ![inputs](Files/Pasted%20image%2020210331131018.png)
 
- generate p p > z,( z > l+ l- a $a,( a > l+ l-))
![inputs](Files/Pasted%20image%2020210331202710.png)
 ### Error for $\gamma \gamma$ channel
 WARNING: The optimizer detects that you have coupling evaluated to zero:
GC_5031
This will slow down the computation. Please consider using restricted model:
https://answers.launchpad.net/mg5amcnlo/+faq/2312
INFO: Compiling for process 2/8.
INFO:     P1_d1d2bar_h1_h1_aa
INFO: Compiling for process 3/8.
INFO:     P1_d2d1bar_h1_h1_aa
INFO: Compiling for process 4/8.
INFO:     P1_d2d2bar_h1_h1_aa
INFO: Compiling for process 5/8.
INFO:     P1_u1u1bar_h1_h1_aa
INFO: Compiling for process 6/8.
INFO:     P1_u1u2bar_h1_h1_aa
INFO: Compiling for process 7/8.
INFO:     P1_u2u1bar_h1_h1_aa
INFO: Compiling for process 8/8.
INFO:     P1_u2u2bar_h1_h1_aa
INFO:     P1_d1d1bar_h1_h1_aa
INFO:     P1_d1d2bar_h1_h1_aa
INFO:     P1_d2d1bar_h1_h1_aa
INFO:     P1_d2d2bar_h1_h1_aa
INFO:     P1_u1u1bar_h1_h1_aa
INFO:     P1_u1u2bar_h1_h1_aa
INFO:     P1_u2u1bar_h1_h1_aa
INFO:     P1_u2u2bar_h1_h1_aa
INFO:  Idle: 1,  Running: 0,  Completed: 7 [ current time: 13h30 ]
INFO:  Idle: 0,  Running: 1,  Completed: 7 [  0.043s  ]
INFO:  Idle: 0,  Running: 0,  Completed: 8 [  0.42s  ]
INFO: End survey
refine 10000
Creating Jobs
INFO: Refine results to 10000
INFO: Generating 10000.0 unweighted events.
sum of cpu time of last step: 3 seconds
INFO: Effective Luminosity 1.2e+103 pb^-1
INFO: need to improve 0 channels
Survey return zero cross section.
   Typical reasons are the following:
   1) A massive s-channel particle has a width set to zero.
   2) The pdf are zero for at least one of the initial state particles
      or you are using maxjetflavor=4 for initial state b:s.
   3) The cuts are too strong.
   Please check/correct your param_card and/or your run_card.
Zero result detected: See https://cp3.irmp.ucl.ac.be/projects/madgraph/wiki/FAQ-General-14
INFO:
quit
INFO:
more information in /mnt/d/projects/PhD/WorkArea/mg5/MG5_aMC_v2_9_2/double_peak/pph1aa/index.html
quit
