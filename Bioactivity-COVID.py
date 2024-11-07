# Import necessary libraries

import pandas as pd
from chembl_webresource_client.new_client import new_client

# Target search for coronavirus

target = new_client.target
target_query = target.search('coronavirus')
targets = pd.DataFrame.from_dict(target_query)
targets

## Select and retrieve bioactivity data for Severe acute respiratory syndrome coronavirus 2 Replicase polyprotein 1ab (nineth entry)

selected_target = targets.target_chembl_id[9]
selected_target

# Retrieving only bioactivity data for for Severe acute respiratory syndrome coronavirus 2 Replicase polyprotein 1ab that are reported as IC 50  values in nM (nanomolar) unit.

activity = new_client.activity
res = activity.filter(target_chembl_id=selected_target).filter(standard_type="IC50")

# Transforming into dataframe

df = pd.DataFrame.from_dict(res)
df.head(2)

# Checking for missing values 

df.describe()
df
df[df.standard_value.notna()]

# There are 75 missing values, creating a dataframe without missing values

df2 = df[df.standard_value.notna()]
df2
df2.info()

# Labeling compounds as either being active, inactive or intermediate The bioactivity data is in the IC50 unit. 
# Compounds having values of less than 1000 nM will be considered to be active while those greater than 10,000 nM will be considered to be inactive. 
# As for those values in between 1,000 and 10,000 nM will be referred to as intermediate.

bioactive_class = []
for i in df2.standard_value:
    if float(i) <= 1000:
        bioactive_class.append("Acitve")
    elif float(i) >= 10000:
        bioactive_class.append("Inactive")

bioactive_class = pd.Series(bioactive_class, name = 'Bioactivity_class')
bioactive_class

# Creating the final da dataframe with prefered columns and bioativity classes.

selec = ['molecule_chembl_id', 'canonical_smiles', 'standard_value']
df3 = df2[selec]
df3

df4 = pd.concat([df3, bioactive_class], axis=1)
df4

# # Checking for missing values in the new dataframe

df4[df4.standard_value.notna()]
df5 = df4[df4.standard_value.notna() & df4.Bioactivity_class.notna()]
df5.info()

# Saving file as csv

df5.to_csv('bioactivity_data_preprocessed.csv', index=False)