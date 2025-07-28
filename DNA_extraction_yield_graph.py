# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('C:/Users/willt/OneDrive/Desktop/work_stuff/SINC2_addedWater_extractions.csv')

# Ensure DNA_yield is numeric
df['DNA_yield'] = pd.to_numeric(df['DNA_yield'], errors='coerce')

# Assign sample group
def assign_group(name):
    if name.endswith('-r'):
        return 'r'
    elif name.endswith('-s'):
        return 's'
    elif name.endswith('-e'):
        return 'e'
    else:
        return 'x'

df['sample_group'] = df['sample_name'].apply(assign_group)

# Define color palette for groups
palette = {'r': '#e41a1c', 's': '#377eb5', 'e': '#4daf4a'}

# Plot for each group
for group in ['e', 's', 'r']:
    plt.figure(figsize=(8, 6))
    subset = df[df['sample_group'] == group]
    ax = sns.scatterplot(
        data=subset,
        x='sample_total_weight',
        y='DNA_yield',
        hue='water_add(ul)',
        palette='viridis',
        s=80
    )
    for i, row in subset.iterrows():
        ax.text(row['sample_total_weight'], row['DNA_yield'],
                str(row['sample_name']), fontsize=8, ha='right', va='bottom')
    plt.title(f'DNA yield vs sample weight (Group {group})')
    plt.xlabel('Sample total weight (g)')
    plt.ylabel('DNA yield (ng/ul)')
    plt.legend(title='Water added (ul)')
    plt.tight_layout()
    plt.show()
