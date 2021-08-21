#%%
import seaborn as sns # for data visualization
import pandas as pd # for data analysis
import matplotlib.pyplot as plt # for data visualization
import numpy as np

from compute_processes import process, process_1, madgraph_path, param_card_name, param_card_path, output_name

# %%
sns.set(style='darkgrid',)
sns.__version__

# %%
# df_mass1 = pd.read_csv('double_peak_data/'+process[0][1]+'.csv')
# print(process[0][1])
df_mass1 = pd.read_csv('double_peak_data/'+process_1[0][1]+'.csv')
print(process_1[0][1])

df_mass2 = pd.read_csv('double_peak_data/'+process[1][1]+'.csv')
print(process[1][1])

df_mass3 = pd.read_csv('double_peak_data/'+process[2][1]+'.csv')
print(process[2][1])

#%%
ppza4l = df_mass1.imass.to_numpy()
pph14l = df_mass2.imass.to_numpy()
pph24l = df_mass3.imass.to_numpy()

pph14l_vec = [r'$pp\rightarrow h1 \rightarrow ZZ \rightarrow 4l$']*len(pph14l)
pph24l_vec = [r'$pp \rightarrow h2 \rightarrow ZZ \rightarrow 4l$']*len(pph24l)
ppza4l_vec  = [r'$pp \rightarrow Z \rightarrow 2l\gamma * \rightarrow 4l$']*len(ppza4l)
df1 = pd.DataFrame(dict(m = pph14l, channel = pph14l_vec), columns=['m', 'channel'])
df2 = pd.DataFrame(dict(m = pph24l, channel = pph24l_vec), columns=['m', 'channel'])
df3 = pd.DataFrame(dict(m = ppza4l, channel = ppza4l_vec), columns=['m', 'channel'])

df = pd.concat([df1,df2,df3])
df
# %%
sns.histplot(
    df, x="m", hue="channel", element="step",
)

plt.xlim(0,200)
#plt.yscale('log')
#plt.xlabel(r'$M_{\mu^{+}\mu^{-}} $')
plt.xlabel(r'$M_{4ll} $')
plt.ylabel('Events')
plt.show()
# %%


# %%
