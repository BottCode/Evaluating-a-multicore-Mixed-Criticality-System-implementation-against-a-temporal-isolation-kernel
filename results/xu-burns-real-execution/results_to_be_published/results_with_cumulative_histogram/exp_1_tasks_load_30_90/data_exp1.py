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

by_budget = [1303.0, 3181.0, 1463.0, 2425.0, 4627.0, 11026.0, 821.0, 1169.0, 4199.0, 3113.0, 1013.0, 1763.0]
by_priority = [5, 7, 5, 5, 5, 4, 6, 6, 5, 5, 5, 8]
by_interfering_migrations = ['No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'Migs interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences', 'No interferences']
by_period = [25.2, 15.75, 25.2, 30.24, 42.0, 87.5, 15.75, 15.75, 25.2, 18.9, 18.9, 33.75]
by_migrability = ['True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True']
by_util = [6, 21, 6, 9, 12, 13, 6, 8, 17, 17, 6, 6]
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
