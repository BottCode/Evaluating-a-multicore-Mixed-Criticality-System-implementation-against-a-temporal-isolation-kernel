import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd


def plot_cumulative_histogram (data, kind, number_of_bins, title, x_label, output, ticks, experiment_id, range = None):
  if kind != "by_migrability" and kind != "by_interfering_migrations":
      fig = plt.figure(figsize=(15, 8))
      plt.xticks (np.arange(min(data), max(data)+min(data), ticks), rotation=45)
  else:
      fig = plt.figure(figsize=(7, 7))

  ax = plt.axes()
  plt.ylabel("Frequency")
  plt.xlabel(x_label)
  plt.grid(axis="x")
  
  values, base, _ = plt.hist( data  , bins = number_of_bins, alpha = 0.5, color = "green", range = range, label = "Frequencies histogram")
  ax_bis = ax.twinx()
  values = np.append(values,0)
  ax_bis.plot( base, np.cumsum(values)/ np.cumsum(values)[-1], color='darkorange', marker='o', linestyle='-', markersize = 1, label = "Cumulative frequencies curve" )
      
  
  plt.ylabel("Proportion")
  plt.title(title)
  ax_bis.grid()
  ax_bis.legend();
  ax.legend();
  plt.yticks (np.arange(0, 1.01, 0.05))

  plt.savefig(output)

by_budget = [3087.0, 1497.0, 3210.0, 4803.0, 1378.0, 2874.0, 519.0, 3962.0, 2883.0, 3653.0, 3399.0, 2938.0, 10351.0, 1006.0, 2298.0, 4624.0, 1944.0, 2609.0, 5012.0, 32053.0, 4327.0, 1972.0, 3361.0, 684.0, 2298.0, 967.0, 1079.0, 2907.0, 2348.0, 2186.0, 830.0, 1250.0, 2598.0, 1718.0, 2745.0, 1408.0, 1279.0, 5767.0, 1777.0, 1550.0, 4070.0, 4240.0, 3254.0, 4631.0, 3107.0, 2447.0, 2134.0, 3421.0, 1710.0, 4570.0, 3633.0, 1528.0, 2641.0, 3990.0, 2839.0, 4902.0, 2474.0, 3364.0, 1201.0, 3051.0, 1115.0, 5282.0, 2293.0, 3305.0, 5294.0, 2873.0, 1809.0, 1203.0, 5481.0, 6734.0, 1282.0, 1069.0, 930.0, 857.0, 624.0, 2480.0, 5196.0, 4063.0, 1165.0, 3410.0, 4721.0, 6738.0, 16301.0, 1829.0, 1505.0, 819.0, 2367.0, 2302.0, 4316.0, 2287.0, 10266.0, 7961.0, 3016.0, 3407.0, 2435.0, 1754.0, 2548.0, 3141.0, 4792.0, 1571.0, 1283.0, 1066.0, 6036.0, 1540.0, 2005.0, 1556.0, 13858.0, 2546.0, 3987.0, 2054.0, 4609.0, 3290.0, 1165.0, 6321.0, 3308.0, 7832.0, 2539.0, 1879.0, 2186.0, 3469.0, 7468.0, 5499.0, 2052.0, 1517.0, 3160.0, 1915.0, 2260.0, 2965.0, 3482.0]
by_priority = [5, 5, 3, 5, 6, 5, 5, 5, 5, 5, 5, 5, 5, 6, 5, 7, 6, 5, 7, 2, 6, 5, 5, 5, 7, 6, 6, 6, 4, 8, 6, 3, 5, 6, 4, 5, 6, 5, 4, 5, 5, 5, 5, 5, 5, 4, 5, 4, 6, 6, 5, 5, 4, 6, 5, 5, 6, 5, 7, 3, 5, 4, 5, 5, 6, 7, 6, 5, 5, 5, 7, 5, 5, 6, 5, 4, 5, 5, 6, 5, 5, 3, 5, 5, 4, 5, 4, 4, 5, 5, 5, 4, 7, 5, 4, 4, 6, 2, 5, 5, 5, 8, 6, 7, 5, 5, 4, 6, 5, 6, 6, 4, 5, 5, 4, 5, 6, 4, 6, 5, 6, 5, 4, 5, 5, 5, 5, 6, 5]
by_interfering_migrations = ['No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'Migs interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences']
by_period = [18.9, 15.75, 18.9, 28.35, 26.25, 25.2, 10.0, 45.0, 25.2, 56.7, 47.25, 45.0, 35.0, 10.0, 20.0, 20.0, 15.75, 40.0, 40.0, 100.8, 39.375, 20.0, 15.75, 10.0, 26.25, 20.0, 15.75, 18.9, 20.0, 22.5, 15.75, 25.2, 50.4, 25.2, 28.35, 20.0, 26.25, 35.0, 22.5, 26.25, 26.25, 60.0, 26.25, 25.2, 25.2, 20.0, 40.0, 28.35, 30.24, 35.0, 65.625, 18.9, 45.36, 26.25, 18.9, 26.25, 33.75, 15.75, 10.0, 18.9, 18.9, 64.8, 45.36, 15.75, 26.25, 18.9, 18.9, 18.9, 20.0, 25.2, 20.0, 20.0, 15.75, 10.0, 10.0, 15.75, 45.36, 39.375, 15.75, 22.5, 26.25, 28.35, 63.0, 18.9, 25.2, 15.75, 42.0, 25.2, 25.2, 45.36, 35.0, 42.0, 18.9, 18.9, 20.0, 20.0, 45.36, 37.8, 35.0, 10.0, 15.75, 15.75, 37.8, 18.9, 40.0, 25.2, 129.6, 25.2, 18.9, 26.25, 45.36, 33.75, 20.0, 30.24, 47.25, 26.25, 42.0, 37.8, 28.35, 15.75, 63.0, 37.8, 28.35, 18.9, 22.5, 18.9, 20.0, 18.9, 15.75]
by_migrability = ['True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'False', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'False', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'False', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'False', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True']
by_utils = [17, 10, 17, 17, 6, 12, 6, 9, 12, 7, 8, 7, 30, 11, 12, 24, 13, 7, 13, 32, 11, 10, 22, 7, 9, 5, 7, 16, 12, 10, 6, 5, 6, 7, 10, 8, 5, 17, 8, 6, 16, 8, 13, 19, 13, 13, 6, 13, 6, 14, 6, 9, 6, 16, 16, 19, 8, 22, 13, 17, 6, 9, 6, 21, 21, 16, 10, 7, 28, 27, 7, 6, 6, 9, 7, 16, 12, 11, 8, 16, 18, 24, 26, 10, 6, 6, 6, 10, 18, 6, 30, 19, 16, 19, 13, 9, 6, 9, 14, 16, 9, 7, 16, 9, 6, 7, 11, 11, 22, 8, 11, 10, 6, 21, 8, 30, 7, 5, 8, 23, 12, 15, 8, 9, 15, 11, 12, 16, 23]
experiment_id = 2

number_of_bins = int(len(set(by_budget))*1.4)
title = "Experiment " + str(experiment_id) + "; BE tasks grouped by criticality-level budget"
plot_cumulative_histogram (data = by_budget, kind = "by_budget", number_of_bins = number_of_bins, title = title, x_label = "Microseconds", output = "./BE_by_budget.png", range = [min(by_budget), max(by_budget)], experiment_id = experiment_id, ticks = 1500)

number_of_bins = len(set(by_migrability))
title = "Experiment " + str(experiment_id) + "; BE tasks grouped by migrability"
plot_cumulative_histogram (data = by_migrability, kind = "by_migrability", number_of_bins = 2, title = title, x_label = "Is migrabile: True or False", output = "./BE_by_migrability.png", range = None, experiment_id = experiment_id, ticks = 1500)

for i in range(0, len(by_period)):
    by_period[i] *= 1000 # cast to microseconds
number_of_bins = len(set(by_period))
title = "Experiment " + str(experiment_id) + "; BE tasks grouped by period"
plot_cumulative_histogram (data = by_period, kind = "by_period", number_of_bins = number_of_bins, title = title, x_label = "Microseconds", output = "./BE_by_period.png", range = [min(by_period), max(by_period)], experiment_id = experiment_id, ticks = 3500)

print(by_priority)
number_of_bins = len(set(by_priority))
title = "Experiment " + str(experiment_id) + "; BE tasks grouped by priority level"
plot_cumulative_histogram (data = by_priority, kind = "by_priority", number_of_bins = number_of_bins, title = title, x_label = "Priority level", output = "./BE_by_priority.png", range = [min(by_priority), max(by_priority)], experiment_id = experiment_id, ticks = 1)

print(by_interfering_migrations)
number_of_bins = len(set(by_interfering_migrations))
title = "Experiment " + str(experiment_id) + "; BE tasks grouped by interfering migrations"
plot_cumulative_histogram (data = by_interfering_migrations, kind = "by_interfering_migrations", number_of_bins = 2, title = title, x_label = "Interference or not", output = "./BE_by_interfering_migrations.png", range = None, experiment_id = experiment_id, ticks = 1500)

print(by_util)
number_of_bins = len(set(by_util))
title = "Experiment " + str(experiment_id) + "; BE tasks grouped by task's utilization (WCET)"
plot_cumulative_histogram (data = by_util, kind = "by_util", number_of_bins = len(set(by_util)), title = title, x_label = "Utilization in [0, 100]", output = "./BE_by_util.png", range = [min(by_util), max(by_util)], experiment_id = experiment_id, ticks = 5)
