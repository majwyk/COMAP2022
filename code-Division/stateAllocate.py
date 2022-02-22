import numpy as np
import pandas as pd

wateruse = pd.read_excel('./2010美国各州用水细分.xlsx')
wateruse.index = wateruse['State'].values.tolist()
wateruse = wateruse.iloc[:, [3,6,9,10]]
print(wateruse)

