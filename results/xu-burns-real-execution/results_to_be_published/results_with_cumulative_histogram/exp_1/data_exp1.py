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

by_budget = [1926.0, 1837.0, 1279.0, 13205.0, 2220.0, 9063.0, 4487.0, 2737.0, 778.0, 1469.0, 1489.0, 7487.0, 2831.0, 2154.0, 4992.0, 2086.0, 1391.0, 2707.0, 1604.0, 886.0, 592.0, 8549.0, 4332.0, 1460.0, 3420.0, 980.0, 1722.0, 1350.0, 10411.0, 4131.0, 1882.0, 965.0, 7850.0, 3324.0, 2154.0, 1212.0, 2358.0, 2332.0, 3373.0, 5013.0, 57359.0, 3250.0, 2199.0, 7511.0, 1085.0, 3841.0, 2426.0, 1432.0, 1615.0, 2437.0, 2617.0, 3477.0, 1746.0, 6263.0, 3426.0, 2924.0, 5340.0, 1866.0]
by_priority = [4, 6, 6, 3, 7, 5, 4, 5, 7, 6, 6, 5, 5, 6, 5, 5, 5, 4, 5, 4, 6, 7, 5, 6, 4, 4, 5, 5, 1, 6, 6, 7, 6, 8, 5, 5, 6, 6, 7, 6, 2, 3, 5, 5, 8, 6, 6, 5, 5, 6, 6, 4, 5, 6, 6, 6, 6, 6]
by_interfering_migrations = ['No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences']
by_period = [39.375, 26.25, 22.5, 40.0, 26.25, 47.25, 18.9, 18.9, 15.75, 10.0, 25.2, 30.24, 25.2, 35.0, 78.75, 18.9, 18.9, 10.0, 18.9, 15.75, 10.0, 56.25, 28.35, 15.75, 22.5, 18.9, 28.35, 10.0, 64.8, 50.0, 33.75, 10.0, 52.5, 40.0, 15.75, 15.75, 25.2, 25.2, 30.24, 30.24, 180.0, 26.25, 15.75, 40.0, 15.75, 18.9, 18.9, 15.75, 26.25, 15.75, 15.75, 52.5, 15.75, 42.0, 37.8, 37.8, 33.75, 15.75]
by_migrability = ['True', 'True', 'True', 'False', 'True', 'False', 'False', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'False', 'True', 'True', 'True', 'False', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'False', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'False', 'False', 'True', 'True', 'True', 'False', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True']
by_util = [5, 7, 6, 34, 9, 20, 24, 15, 5, 15, 6, 25, 12, 7, 7, 12, 8, 28, 9, 6, 6, 16, 16, 10, 16, 6, 7, 14, 17, 9, 6, 10, 15, 9, 14, 8, 10, 10, 12, 17, 32, 13, 14, 19, 7, 21, 13, 10, 7, 16, 17, 7, 12, 15, 10, 8, 16, 12]
experiment_id = 1

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
