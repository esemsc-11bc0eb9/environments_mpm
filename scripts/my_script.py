import sys

import numpy as np
sys.path.append("/Users/jl3124/Desktop/environments_mpm")
from  envtest import shape_df
import pandas as pd
df = pd.DataFrame(np.random.rand(4, 2), columns=['a', 'b'])
print(shape_df(df))
