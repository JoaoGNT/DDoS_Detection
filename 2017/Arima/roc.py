import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd

# conf_arr = np.array([[474183,287375], # (1,1,1)
#                     [209640, 256635]])


# conf_arr= np.array([[436865,310280], # (3,3,1)
#                     [187591,293979]])

conf_arr= np.array([[399447,324624], # (2,3,3)
                    [173247,331397]])

df_cm = pd.DataFrame(conf_arr,
                  index = ['Verdadeiro', 'Falso'],
                  columns = ['Positivo', 'Negativo'])
fig = plt.figure()

plt.clf()

ax = fig.add_subplot(111)

ax.set_aspect(1)

res = sn.heatmap(df_cm, cmap='mako',annot=True, vmin=0.0, vmax=1228715.0, fmt='.1f')

plt.yticks([0.5,1.5], ['Verdadeiro','Falso'],va='center')
# plt.title('Matriz de Contingência - (2,3,3)')
plt.savefig('confusion_table2,3,3.png', format='png', bbox_inches='tight')