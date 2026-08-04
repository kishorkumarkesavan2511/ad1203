import numpy as np
import pandas as pd

replaceFrame = pd.DataFrame({'column 1': [200., 3000., -786.,3000., 234., 444., -786., 332., 3332. ], 'column 2': range(9)})
print(replaceFrame)
print(replaceFrame.replace(to_replace =-786, value= np.nan))