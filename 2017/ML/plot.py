import csvReader
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame(csvReader.data)
df.columns = csvReader.columns
dataInteresse = df.drop(csvReader.flow[0][4:80], axis=1)
dataInteresse.insert(0, 'Label',csvReader.label, True)
print(dataInteresse)
sns.pairplot(dataInteresse,hue='Label', height =2.5 )

plt.show()