#research
### Model Files
The Sarah file was taken from [B-L-SSM – Trac – Hepforge (sarah.hepforge.org)](https://sarah.hepforge.org/trac/wiki/B-L-SSM).  This model was created by L.Basso, F.Staub. The UFO and SPHENO files where created in Mathematica by SARAH by an `generate_model.m` through: 
```mathematica
Needs["SARAH`","/mainfs/home/mjad1g20/HEP/SARAH/SARAH-4.14.5/SARAH.m"]

Start["B-L-SSM"]
ModelOutput[EWSB]

MakeSPheno[]
MakeUFO[]
MakeCHep[]

Quit[];
```

### 
I generated the param_card.dat files with SPheno with the low energy limit of the Les Houches file. [LesHouches.in.blssm](Files/LesHouches.in.blssm). The input parametes are the ones in TABLE I in [2015. W. Abdallah. S. Khalil. S. Moretti](References/Files/2015.%20S.%20Moretti.%20Double%20Higgs%20peak%20in%20the%20minimal%20SUSY%20B%20−%20L%20model.pdf).

![inputs](Files/Pasted%20image%2020210331203159.png)

