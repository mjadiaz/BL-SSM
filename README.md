

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


- There is an option to [create the CalcHep](https://gitlab.in2p3.fr/goodsell/sarah/-/wikis/CalcHep/CompHep) file to run it with spheno, that might be helpful. 
	- `RunSPhenoViaCalcHep`: writes C code to run SPhenofrom the graphical interface of CalcHepto calculate the spectrum on the fly.

- There are more options that should be looked.

#### Useful links

- [Running Jupyter Notebook on a remote server](https://docs.anaconda.com/anaconda/user-guide/tasks/remote-jupyter-notebook/)


