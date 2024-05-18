# unverified ssl 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
## importar la librería -> solo hay que hacerlo una vez
import seaborn as sns
## cargar el set de datos -> solo hay que hacerlo una vez por "rectangulo"
penguins = sns.load_dataset("penguins")
### ejecutar el gráfico
sns.histplot(data=penguins, x="flipper_length_mm")