# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:20:24 2020

@author: kshit
"""

import json, numpy
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data_df = pd.read_json('ark_bathroom_savings.json')
data_df = data_df.T

data_df.reset_index(level=0, inplace=True)
# plt.figure(figsize=(12,8), dpi= 200)
# ax = sns.lineplot(x="index", y="cost_savings",markers=True, dashes=True, data=data_df)
# data_df.drop(['current_energy_savings','current_cost_savings'], axis=1).plot()
# plt.xlabel('Date')
# plt.ylabel('Cost in $ and Energy in Watt')
# plt.savefig('living_room_savings.png')


plt.figure(figsize=(12,8), dpi= 200)
plt.title("Savings for Jackie bathroom")
plt.xlabel('Date')
plt.ylabel('Cost in $ and Energy in Watt')
plt.plot('index', 'cost_savings', data=data_df, color='tab:blue', label='Cost savings')
plt.plot('index', 'energy_savings', data=data_df, color='tab:red', label='Energy savings')
plt.savefig('ark_bathroom_savings.png')