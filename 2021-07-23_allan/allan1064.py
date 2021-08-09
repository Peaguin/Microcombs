"""
Created on Tue Jul 27 16:21:05 2021.

@author: Confotec
"""
import allantools as allan
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("D:\\2021_07_cwlaser_test\\2021_07_27cwlaser_1064nm.csv")

time = data.iloc[:, 0].values
frequency = data.iloc[:, 1].values

time = pd.DatetimeIndex(time)
absolute_time = time.hour * 3600 + time.minute * 60 + time.second + time.microsecond * 1e-6
absolute_time = absolute_time - absolute_time[0]

frac_frequency = frequency / frequency.mean()
(taus2, ad, ade, ns) = allan.oadev(frac_frequency, data_type='freq', taus=absolute_time)
fig, ax = plt.subplots()
ax.errorbar(taus2, ad, yerr=ade, ecolor='black')
plt.yscale("log")
