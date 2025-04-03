import pandas as pd
import numpy as np

# dictionary of lists
dict = {
    "id": [1, 8, np.nan, 9],
    "Age": [30, 45, np.nan, np.nan],
    "Score": [np.nan, 99, 180, 198],
}

# creating a DataFrame
df = pd.DataFrame(dict)


print(df.value_counts())
