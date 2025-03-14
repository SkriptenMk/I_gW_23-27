# %%

import pandas as pd
from unternehmen import Unternehmen

# %%

konti = pd.read_csv('konti.csv', index_col=0)

# %%

ug1 = Unternehmen(konti)

# %%

ug1.bilanz.get_ek()

# %%

ug1.save_data()
# %%
