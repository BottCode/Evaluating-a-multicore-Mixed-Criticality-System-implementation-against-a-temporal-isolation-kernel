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

by_budget = [2684.0, 1644.0, 3665.0, 7603.0, 1858.0, 992.0, 2718.0, 2002.0, 2124.0, 7510.0, 9057.0, 1981.0, 1583.0, 2044.0, 5370.0, 1236.0, 2307.0, 3830.0, 3113.0, 3799.0, 958.0, 992.0, 3763.0, 5921.0, 1651.0, 3777.0, 2140.0, 11673.0, 3853.0, 4089.0, 3113.0, 1319.0, 4714.0, 1496.0, 1426.0, 1363.0, 4569.0, 962.0, 1261.0, 2166.0, 1846.0, 2424.0, 1084.0, 4268.0, 2235.0, 1826.0, 1995.0, 2339.0, 2280.0, 4176.0, 4610.0, 5709.0, 1050.0, 1002.0, 2151.0, 2271.0, 1527.0, 2819.0, 1249.0, 2800.0, 6077.0, 2699.0, 702.0, 4249.0, 2082.0, 22377.0, 1472.0, 839.0, 2858.0, 12832.0, 4061.0, 1024.0, 4060.0, 3700.0, 2236.0, 2508.0]
by_priority = [5, 5, 5, 5, 6, 5, 5, 5, 5, 5, 5, 6, 5, 5, 6, 7, 6, 5, 5, 5, 5, 5, 4, 5, 6, 4, 5, 4, 6, 5, 5, 6, 6, 6, 4, 4, 5, 7, 6, 6, 5, 7, 5, 7, 6, 6, 6, 6, 6, 6, 7, 5, 5, 5, 5, 6, 5, 6, 6, 8, 6, 5, 5, 5, 6, 3, 5, 5, 5, 4, 4, 5, 5, 5, 4, 4]
by_interfering_migrations = ['No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'Migs interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences']
by_period = [18.9, 26.25, 22.5, 81.0, 18.9, 15.75, 37.8, 39.375, 28.35, 28.35, 35.0, 15.75, 15.75, 33.75, 30.24, 15.75, 18.9, 39.375, 15.75, 22.5, 15.75, 15.75, 65.625, 37.8, 20.0, 47.25, 15.75, 75.0, 22.5, 18.9, 22.5, 25.2, 30.24, 20.0, 18.9, 25.2, 54.0, 18.9, 10.0, 22.5, 26.25, 28.35, 18.9, 28.35, 15.75, 26.25, 20.0, 18.9, 30.24, 37.8, 25.2, 33.75, 18.9, 20.0, 18.9, 37.8, 26.25, 28.35, 10.0, 25.2, 33.75, 18.9, 10.0, 30.24, 15.75, 120.0, 25.2, 15.75, 25.2, 35.0, 25.2, 15.75, 20.0, 28.35, 25.2, 15.75]
by_migrability = ['True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'False', 'True', 'True', 'True', 'False', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'False', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'False', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'False', 'True', 'True', 'True']
by_util = [15, 7, 17, 10, 10, 7, 8, 6, 8, 27, 26, 13, 11, 7, 18, 8, 13, 10, 20, 17, 7, 7, 6, 16, 9, 8, 14, 16, 18, 22, 14, 6, 16, 8, 8, 6, 9, 6, 13, 10, 8, 9, 6, 16, 15, 7, 10, 13, 8, 12, 19, 17, 6, 6, 12, 7, 6, 10, 13, 12, 19, 15, 8, 15, 14, 19, 6, 6, 12, 37, 17, 7, 21, 14, 9, 16]
experiment_id = 3

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
