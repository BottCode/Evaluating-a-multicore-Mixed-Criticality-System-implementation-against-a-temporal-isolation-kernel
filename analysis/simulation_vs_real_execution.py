import config_sim_vs_real

import copy

import os

import xml.etree.ElementTree as ET
import xml.dom.minidom
import sys

from shutil import copyfile, rmtree

import time
import optparse
import math

import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import json

def beautify_dict (task):
    s = json.dumps(task, indent=4)
    return s[0+1 : len(s)-1]


def plot_two_or_more_functions(results, output, x_lab, experiment_id):

    if experiment_id == 1:
        base_loc_x = config_sim_vs_real.UTIL_STEP * 2
    elif experiment_id == 2:
        base_loc_x = config_sim_vs_real.CRITICALITY_STEP
    elif experiment_id == 3:
        base_loc_x = config_sim_vs_real.PROPORTION_STEP
    else:
        base_loc_x = 5

    fig, ax = plt.subplots(figsize=(20,9))
    for function in results:
        ax.plot([results[function]['values'][i][0] for i in range(len(results[function]['values']))], [results[function]['values'][i][1] for i in range(len(results[function]['values']))], label=function, alpha=0.7, linewidth=5)

    ax.set(xlabel=x_lab, ylabel='Percentage')
    loc_x = ticker.MultipleLocator(base=base_loc_x) # this locator puts ticks at regular intervals
    ax.xaxis.set_major_locator(loc_x)
    loc_y = ticker.MultipleLocator(base=5) # this locator puts ticks at regular intervals
    ax.yaxis.set_major_locator(loc_y)
    ax.grid()
    plt.xticks()
    plt.legend()
    plt.savefig(output)
    plt.close()


def draw_overall_histogram (schedulable_histogram, NS_histogram, BE_histogram, output_histogram):
    plt.hist (schedulable_histogram, color = 'blue', alpha = 0.8, bins = 52, label = 'Schedulable tasksets')
    plt.hist (BE_histogram, color = 'green', alpha = 0.8, bins = 52, label = 'BE tasksets')
    plt.hist (NS_histogram, color = 'orange', alpha = 0.8, bins = 52, label = 'NS tasksets')
    plt.savefig(output_histogram)
    plt.close()
    # print('Result saved: ' + output_histogram)

def draw_utilizations_histogram (nominal_utilizations_schedulable_tasksets, real_utilizations_schedulable_tasksets, output_histogram):
    df = pd.DataFrame({'Nominal utilizations distribution for schedulable tasksets' : nominal_utilizations_schedulable_tasksets, 'Real utilizations distribution for schedulable tasksets' : real_utilizations_schedulable_tasksets})
    
    fig, axes = plt.subplots(ncols=len(df.columns), figsize=(16,6))
    for col, ax in zip(df, axes):
        df[col].value_counts().sort_index().plot.bar(ax=ax, title=col)

    plt.tight_layout()    
    plt.savefig(output_histogram)
    plt.close()

def plot_data (results, output, x_lab):
  fig, ax = plt.subplots(figsize=(12,9))

  for approach in results:
    ax.plot([results[approach][i][0] for i in range(len(results[approach]))], [results[approach][i][1] for i in range(len(results[approach]))], label=approach)

  ax.set(xlabel=x_lab, ylabel='Percentage of actually schedulable tasksets')
  ax.grid()
  plt.xticks()
  plt.legend()
  plt.savefig(output)
  plt.close()
  # print('Result saved: ' + output)

def plot_BE_data (by_budget, by_migrability, by_period, by_priority, by_interfering_migrations, output):
    df = pd.DataFrame({'Tasks BE by budget (microseconds)' : by_budget, 'Tasks BE by period (milliseconds)' : by_period, 'Tasks BE by migrability': by_migrability, 'Tasks BE by priority': by_priority, 'Tasks BE by interfering migrations': by_interfering_migrations})

    fig, axes = plt.subplots(ncols=len(df.columns), figsize=(16,6))
    for col, ax in zip(df, axes):
        df[col].value_counts().sort_index().plot.bar(ax=ax, title=col)

    plt.tight_layout()    
    plt.savefig(output)
    plt.close()

def plot_NS_data (by_period, by_migrability, by_util, by_priority, by_interfering_migrations, schedulable_histogram, output):
    df = pd.DataFrame({'Tasks NS by period (milliseconds)' : by_period, 'Tasks NS by migrability': by_migrability, 'Tasks NS by utilization (percentage %)': by_util, 'Tasks NS by priority': by_priority, 'Tasks NS by interfering migrations': by_interfering_migrations})

    fig, axes = plt.subplots(ncols=len(df.columns), figsize=(16,6))
    for col, ax in zip(df, axes):
        df[col].value_counts().sort_index().plot.bar(ax=ax, title=col)

    plt.tight_layout()    
    plt.savefig(output)
    plt.close()

def CLEAN_ALL():
  for i in range(4):
    clean_XML_Files(i+1)

def clean_XML_experiments():
    if config_sim_vs_real.RUN_FIRST_TEST:
        clean_XML_Files(1)
    if config_sim_vs_real.RUN_SECOND_TEST:
        clean_XML_Files(2)
    if config_sim_vs_real.RUN_THIRD_TEST:
        clean_XML_Files(3)
    if config_sim_vs_real.RUN_FOURTH_TEST:
        clean_XML_Files(4)

def clean_XML_Files(experiment_id):
  xml_template = '../results/xu-burns-real-execution/XML_results/template.xml'

  for path in config_sim_vs_real.XML_Files[experiment_id]:
    copyfile(xml_template, config_sim_vs_real.XML_Files[experiment_id][path])

def beautify_XML_experiments():
    if config_sim_vs_real.RUN_FIRST_TEST:
        beautify_XML_Files(1)
    if config_sim_vs_real.RUN_SECOND_TEST:
        beautify_XML_Files(2)
    if config_sim_vs_real.RUN_THIRD_TEST:
        beautify_XML_Files(3)
    if config_sim_vs_real.RUN_FOURTH_TEST:
        beautify_XML_Files(4)

def beautify_XML_Files(experiment_id):
  for path in config_sim_vs_real.XML_Files[experiment_id]:
    with open(config_sim_vs_real.XML_Files[experiment_id][path], "r") as xmldata:
      parsing = xml.dom.minidom.parseString(xmldata.read())  # or xml.dom.minidom.parseString(xml_string)
      xml_pretty_str = parsing.toprettyxml()
      xmldata.close()

    with open(config_sim_vs_real.XML_Files[experiment_id][path], "w") as xmldata:
      xmldata.write(xml_pretty_str)
      xmldata.close()

def beautify_XML_log():
    with open(config_sim_vs_real.PATH_TO_LOG, "r") as xmldata:
      parsing = xml.dom.minidom.parseString(xmldata.read())  # or xml.dom.minidom.parseString(xml_string)
      xml_pretty_str = parsing.toprettyxml()
      xmldata.close()

    with open(config_sim_vs_real.PATH_TO_LOG, "w") as xmldata:
      xmldata.write(xml_pretty_str)
      xmldata.close()

def add_root_to_XML(file_name, line='<executions>\n'):

    with open(file_name, "a") as logfile:
        logfile.write("\n</executions>")
        logfile.close()

    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)

def organize_executions():
    clean_XML_experiments()
    # experiment_id = 0
    for experiment_id in config_sim_vs_real.XML_Files:
        try:
            tree_source = ET.parse (config_sim_vs_real.MAIN_LOG)
        except:
            # it means that log file has no root => Add it!
            # print("no root!")
            add_root_to_XML(config_sim_vs_real.MAIN_LOG)

            tree_source = ET.parse (config_sim_vs_real.MAIN_LOG)
            # beautify_XML_log()
    
        root_source = tree_source.getroot()

        for execution_XML in root_source.findall('execution'):
            execution_id = execution_XML.find('executionid').text

            if execution_id != '-1':
                current_experiment_id = int(execution_XML.find('experimentid').text)
                approach = execution_XML.find('approach').text

                if experiment_id == current_experiment_id and config_sim_vs_real.RUN_FIRST_TEST:
                    tree_target = ET.parse(config_sim_vs_real.XML_Files[experiment_id][approach])
                    root_target = tree_target.getroot()
                    root_target.append(execution_XML)
                    tree_target.write(config_sim_vs_real.XML_Files[experiment_id][approach])

                    continue

                if experiment_id == current_experiment_id and config_sim_vs_real.RUN_SECOND_TEST:
                    tree_target = ET.parse(config_sim_vs_real.XML_Files[experiment_id][approach])
                    root_target = tree_target.getroot()
                    root_target.append(execution_XML)
                    tree_target.write(config_sim_vs_real.XML_Files[experiment_id][approach])
                    
                    continue
                    
                if experiment_id == current_experiment_id and config_sim_vs_real.RUN_THIRD_TEST:
                    tree_target = ET.parse(config_sim_vs_real.XML_Files[experiment_id][approach])
                    root_target = tree_target.getroot()
                    root_target.append(execution_XML)
                    tree_target.write(config_sim_vs_real.XML_Files[experiment_id][approach])

                    continue

                if experiment_id == current_experiment_id and config_sim_vs_real.RUN_FOURTH_TEST:
                    tree_target = ET.parse(config_sim_vs_real.XML_Files[experiment_id][approach])
                    root_target = tree_target.getroot()
                    root_target.append(execution_XML)
                    tree_target.write(config_sim_vs_real.XML_Files[experiment_id][approach])

                    continue

def produce_results_experiment(experiment_id):
    xml_level_to_analyze = ""
    # They are the x-axis values
    level_list = []
    if experiment_id == 1:
        xml_level_to_analyze = 'tasksetutilization'
        x_lab = 'Utilization'
        lb = config_sim_vs_real.UTIL_LOWER_BOUND
        ub = config_sim_vs_real.UTIL_HIGHER_BOUND
        stp = config_sim_vs_real.UTIL_STEP
        v = lb
        while v <= ub:
            level_list.append(str(v))
            v += stp
    elif experiment_id == 2:
        xml_level_to_analyze = 'criticalityfactor'
        x_lab = 'Criticality Factor'
        lb = config_sim_vs_real.CRITICALITY_LOWER_BOUND
        ub = config_sim_vs_real.CRITICALITY_HIGHER_BOUND
        stp = config_sim_vs_real.CRITICALITY_STEP
        v = lb
        while v <= ub:
            level_list.append(str(v))
            v += stp
    elif experiment_id == 3:
        # hi-crit proportion
        xml_level_to_analyze = 'perc'
        x_lab = 'HI-CRIT task proportion'
        lb = config_sim_vs_real.PROPORTION_LOWER_BOUND
        ub = config_sim_vs_real.PROPORTION_HIGHER_BOUND
        stp = config_sim_vs_real.PROPORTION_STEP
        v = lb
        while v <= ub:
            level_list.append(str(v))
            v += stp
            if v > 0.7 and v < 0.8:
                v = 0.8
            elif v > 0.8 and v < 0.9:
                v = 0.9
    elif experiment_id == 4:
        xml_level_to_analyze = 'tasksetsize'
        x_lab = 'Taskset size'
        level_list = config_sim_vs_real.TASKSETS_SIZE

    x_axis_levels = {}
    schedulable_histogram = []
    nominal_utilizations_schedulable_tasksets = []
    real_utilizations_schedulable_tasksets = []
    number_of_exec_for_each_level = {}
    # for each level => number of tasksets that exceed their budget
    BE_for_each_level = {}
    BE_histogram = []
    # for each level => number of NOT schedulable tasksets
    NS_for_each_level = {}
    NS_histogram = []
    # for each level => number of tasksets that exceed their safe boundary
    SBE_for_each_level = {}
    SBE_histogram = []
    results_to_plot = {}
    # for each period value => number of BE tasks
    BE_tasks_group_by_period = []
    # for each budget value => number of BE tasks
    BE_tasks_group_by_budget = []
    # for each "migrable" ('True' or 'False') value => number of BE tasks
    BE_tasks_group_by_migrability = []
    BE_tasks_group_by_priority = []
    BE_tasks_group_by_interfering_migrations = []

    # for each period value => number of NS tasks
    NS_tasks_group_by_period = []
    # for each "migrable" ('True' or 'False') value => number of NS tasks
    NS_tasks_group_by_migrability = []
    # for each utilisation value => number of NS tasks
    NS_tasks_group_by_util = []
    NS_tasks_group_by_priority = []
    NS_tasks_group_by_interfering_migrations = []

    report_on_bad_tasksets = '# Report on Experiment ' + str(experiment_id) + '\n\n'
    bad_tasksets_section = '## Bad tasksets\n\n<details><summary markdown="span">Click here to expand this section.</summary>\n\n'
    bad_tasksets_safe_boundary = '\n### **Safe Boundary Exceeded**\n\n<details><summary markdown="span">Click here to expand this section.</summary>\n\nOvvero quando un taskset ha troppi core (2 nel contesto dual-core) eseguenti in HI-crit mode.\n\n'
    # BE stands for budget exceeded
    bad_tasksets_BE = '\n### **Criticality Level Budget Exceeded**\n\n<details><summary markdown="span">Click here to expand this section.</summary>\n\nOvvero quando un task di un taskset ha ecceduto il suo criticality-level budget, cioè un LO-crit task che eccede il suo LO-crit budget, oppure un HI-crit task che eccede il suo HI-crit budget.\n\n'
    not_schedulable_tasksets = '\n### **Not schedulable tasksets**\n\n<details><summary markdown="span">Click here to expand this section.</summary>\n\nOvvero quando almeno un task non completa entra almeno una sua deadline.\n\n'
    results_for_each_level = '\n## Focus for each ' + x_lab + ' level.\n\n<details><summary markdown="span">Click here to expand this section.</summary>\n\n'

    for approach in config_sim_vs_real.XML_Files[experiment_id]:
        results_to_plot[approach] = []
        x_axis_levels[approach] = {}
        BE_for_each_level[approach] = {}
        NS_for_each_level[approach] = {}
        SBE_for_each_level[approach] = {}
        number_of_exec_for_each_level[approach] = {}

        for single_level in level_list:
            x_axis_levels[approach][single_level] = 0
            number_of_exec_for_each_level[approach][single_level] = 0
            BE_for_each_level[approach][single_level] = 0
            NS_for_each_level[approach][single_level] = 0
            SBE_for_each_level[approach][single_level] = 0

        tree = ET.parse(config_sim_vs_real.XML_Files[experiment_id][approach])
        root = tree.getroot()

        numbered_list_index_safe_boundary = 1
        numbered_list_index_BE = 1
        # NS stands for not schedulable
        numbered_list_index_NS = 1

        for execution_XML in root.findall('execution'):
            
            if execution_XML.find('executionid').text == '-1':
                continue

            execution_info = {
                'id': execution_XML.find('executionid').text,
                'size': execution_XML.find('tasksetsize').text,
                'utilization' : format (float (execution_XML.find('tasksetutilization').text), '.3f'),
                'realutilization' : 0,
                'criticality_factor': execution_XML.find('criticalityfactor').text,
                'hicrit_proportion': execution_XML.find('perc').text
            }
            
            cores_info = '   <details> <summary markdown="span">Click here to see the CPUs log.</summary>\n\n   Idle time is expressed as **seconds**.\n\n   Util values are expressed as **percentage** %.\n\n'
            guilty_tasks = '   <details> <summary markdown="span">Click here to see the guilty task.</summary>\n\n   Time values are expressed as **micro-seconds**.\n\n'
            dm_tasks = '   <details> <summary markdown="span">Click here to see the deadlines missed tasks list.</summary>\n\n   Time values are expressed as **micro-seconds**.\n\n'
            list_of_tasks = []

            single_level = execution_XML.find(xml_level_to_analyze).text
            if experiment_id == 4:
                single_level = int(single_level)
            
            number_of_exec_for_each_level[approach][single_level] += 1
            tasks_XML = execution_XML.find('tasks')
            cores_XML = execution_XML.find('cores')
            collapse_menu_containing_tasks = '   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>\n\n   Time values are expressed as **micro-seconds**.\n\n'
            
            biggest_hyperperiod = max (int(execution_XML.find('hyperperiodc1').text), int(execution_XML.find('hyperperiodc2').text))

            # it is the measured utilization.
            real_taskset_utilization = 0

            for core_XML in cores_XML.findall('cpu'):
                curr_core = {}
                curr_core['id'] = int(core_XML.find('id').text)
                curr_core['hyperperiod'] = int(execution_XML.find('hyperperiodc1').text) if curr_core['id'] == 1 else int(execution_XML.find('hyperperiodc2').text)

                curr_core['lowtohigh'] = core_XML.find('lowtohigh').text
                curr_core['hightolow'] = core_XML.find('hightolow').text
                curr_core['idletime'] = int(float(core_XML.find('idletime').text) * 1000000)
                curr_core['util'] = 100 - ((curr_core['idletime'] / biggest_hyperperiod) * 100)

                real_taskset_utilization += float (format (curr_core['util'] / 100, '.2f'))

                cores_info += '\n\n   CPU: ' + str(curr_core['id']) + '\n\n    ' + beautify_dict(curr_core) + '\n\n'
            
            execution_info['realutilization'] = float (format (real_taskset_utilization, '.2f'))
            cores_info += '\n\n   Real Utilization: ' + str(real_taskset_utilization) + '\n   </details>\n\n'

            for task_XML in tasks_XML.findall('task'):
                    curr_task = {}
                    curr_task['id'] = task_XML.find('taskid').text
                    curr_task['basecpu'] = task_XML.find('basecpu').text
                    curr_task['priority'] = task_XML.find('priority').text
                    curr_task['period'] = (float(task_XML.find('period').text)) * 1000000 # to microseconds conversion
                    curr_task['C(LO)'] = (float(task_XML.find('locritbudget').text)) * 1000000 # to microseconds conversion
                    curr_task['C(HI)'] = (float(task_XML.find('hicritbudget').text)) * 1000000 # to microseconds conversion
                    curr_task['criticality'] = task_XML.find('criticality').text
                    curr_task['migrable'] = task_XML.find('migrable').text
                    curr_task['completedruns'] = task_XML.find('completedruns').text
                    curr_task['preemptions'] = task_XML.find('preemptions').text
                    curr_task['minresponsejitter'] = task_XML.find('minresponsejitter').text
                    curr_task['maxresponsejitter'] = task_XML.find('maxresponsejitter').text
                    curr_task['minreleasejitter'] = task_XML.find('minreleasejitter').text
                    curr_task['maxreleasejitter'] = task_XML.find('maxreleasejitter').text
                    curr_task['avgresponsejitter'] = task_XML.find('avgresponsejitter').text
                    curr_task['deadlinesmissed'] = task_XML.find('deadlinesmissed').text
                    curr_task['deadlinemissedtargetcore'] = task_XML.find('deadlinemissedtargetcore').text if task_XML.find('deadlinemissedtargetcore') is not None else "Not monitored"
                    curr_task['deadlinemissedaftermigration'] = task_XML.find('deadlinemissedaftermigration').text if task_XML.find('deadlinemissedaftermigration') is not None else "Not monitored"
                    curr_task['budgetexceeded'] = task_XML.find('budgetexceeded').text 
                    curr_task['budgetexceededtargetcore'] = task_XML.find('budgetexceededtargetcore').text if task_XML.find('budgetexceededtargetcore') is not None else "Not monitored"
                    curr_task['budgetexceededaftermigration'] = task_XML.find('budgetexceededaftermigration').text if task_XML.find('budgetexceededaftermigration') is not None else "Not monitored"
                    curr_task['timesmigrated'] = task_XML.find('timesmigrated').text
                    curr_task['timesrestored'] = task_XML.find('timesrestored').text
                    curr_task['timesonc1'] = task_XML.find('timesonc1').text
                    curr_task['timesonc2'] = task_XML.find('timesonc2').text
                    curr_task['lockedtime'] = task_XML.find('lockedtime').text
                    curr_task_string = beautify_dict (curr_task)
                    list_of_tasks.append(copy.deepcopy(curr_task))
                    # Write on markdown report
                    collapse_menu_containing_tasks += '\n\n   Task: ' + curr_task['id'] + '\n\n    ' + curr_task_string + '\n\n'

                    if int(task_XML.find('taskid').text) == int(execution_XML.find('guiltytask').text):
                        guilty_tasks += 'Task: ' +  curr_task['id'] + '\n\n    ' + curr_task_string + '\n\n'
                        if int(task_XML.find('taskid').text) == int(execution_XML.find('guiltytask').text):
                            p = float (task_XML.find('period').text) * 1000
                            budget = float (task_XML.find('locritbudget').text) * 1000000  if task_XML.find('criticality') == 'LOW' else float (task_XML.find('hicritbudget').text) * 1000000
                            
                            if experiment_id == 2:
                                # print("yes")
                                # sum-up periods values for sake of the readability
                                step = 15
                                i = 0
                                while i <= p:
                                    if p in range(0+i+1, step+i):
                                        p = math.trunc ((((0+i) + (step+i)) / 2))
                                        break
                                    i += step

                            # sum-up budgets values for sake of the readability
                            step = 21
                            if experiment_id == 2:
                                step = 82
                            i = 0
                            while i <= budget:
                                if budget in range(0+i+1, step+i):
                                    budget = math.trunc ((((0+i) + (step+i)) / 2))
                                    break
                                i += step
                            
                            mig = str (task_XML.find('migrable').text)
                            have_migrations_interfered = "Migs interferences" if (int (task_XML.find('budgetexceededaftermigration').text)) > 0 else "No interferences"
                            BE_tasks_group_by_period.append (p)
                            BE_tasks_group_by_budget.append (budget)
                            BE_tasks_group_by_migrability.append (mig)
                            BE_tasks_group_by_priority.append (str(task_XML.find('priority').text))
                            BE_tasks_group_by_interfering_migrations.append (have_migrations_interfered)
                    elif int(curr_task['deadlinesmissed']) > 0 and str(execution_XML.find('experimentisnotvalid').text).upper() == 'FALSE':
                        dm_tasks += 'Task: ' +  curr_task['id'] + '\n\n    ' + curr_task_string + '\n\n'
                        p = float (task_XML.find('period').text) * 1000
                        budget = (float (task_XML.find('locritbudget').text) * 1000000) if task_XML.find('criticality') == 'LOW' else (float (task_XML.find('hicritbudget').text) * 1000000)
                        u = float (task_XML.find('period').text)
                        mig = str (task_XML.find('migrable').text)
                        have_migrations_interfered = "Migs interferences" if (int (task_XML.find('deadlinemissedaftermigration').text)) > 0 else "No interferences"
                        NS_tasks_group_by_period.append (p)
                        NS_tasks_group_by_migrability.append (mig)
                        NS_tasks_group_by_util.append (math.ceil ((budget / (p*1000)) * 100))
                        NS_tasks_group_by_priority.append (str(task_XML.find('priority').text))
                        NS_tasks_group_by_interfering_migrations.append (have_migrations_interfered)

                        '''if int(curr_task['deadlinemissedtargetcore']) > 0:
                            NS_tasks_group_by_migrability.append ('DM on target core.')'''
                                   
            guilty_tasks += '\n   </details>\n\n'
            dm_tasks += '\n   </details>\n\n'

            collapse_menu_containing_tasks += '\n   </details>\n\n'

            if str(execution_XML.find('experimentisnotvalid').text).upper() == 'FALSE' and str(execution_XML.find('safeboundaryexceeded').text).upper() == 'FALSE':

                if str(execution_XML.find('tasksetisschedulable').text).upper() == 'TRUE':
                    x_axis_levels[approach][single_level] += 1
                    schedulable_histogram.append (float(single_level))
                    nominal_utilizations_schedulable_tasksets.append (execution_info['utilization'])
                    real_utilizations_schedulable_tasksets.append (execution_info['realutilization'])
                else:
                    not_schedulable_tasksets += '\n\n  ' + str(numbered_list_index_NS) +'. Taskset **' + str(execution_XML.find('executionid').text) + '**\n'
                    not_schedulable_tasksets += '\n    Taskset execution params:\n\t ' + beautify_dict (execution_info) + '\n\n' + dm_tasks + '\n\n'
                    not_schedulable_tasksets += cores_info + collapse_menu_containing_tasks
                    NS_for_each_level[approach][single_level] += 1
                    NS_histogram.append (float(single_level))
                    numbered_list_index_NS += 1

            elif str(execution_XML.find('safeboundaryexceeded').text).upper() == 'TRUE':
                bad_tasksets_safe_boundary += '\n\n  ' + str(numbered_list_index_safe_boundary) + '. Taskset **' + str(execution_XML.find('executionid').text) + '**\n'
                bad_tasksets_safe_boundary += '\n    Taskset execution params:\n\t ' + beautify_dict (execution_info) + '\n\n'
                bad_tasksets_safe_boundary += cores_info + collapse_menu_containing_tasks
                SBE_for_each_level[approach][single_level] += 1
                SBE_histogram.append (single_level)
                numbered_list_index_safe_boundary += 1
            elif str(execution_XML.find('experimentisnotvalid').text).upper() == 'TRUE':
                BE_for_each_level[approach][single_level] += 1
                BE_histogram.append (float(single_level))
                numbered_list_index_BE += 1
                bad_tasksets_BE += '\n\n  ' + str(numbered_list_index_BE) + '. Taskset **' + str(execution_XML.find('executionid').text) + '**\n'
                bad_tasksets_BE += '\n    Taskset execution params:\n\t ' + beautify_dict (execution_info) + '\n\n' + guilty_tasks + '\n\n'
                bad_tasksets_BE += cores_info + collapse_menu_containing_tasks

        overall_results = {'Actually Schedulable': {'values': [], 'legend': 'AS'}, 'Deadline Missed': {'values': [], 'legend': 'DM'}, 'Budget Exceeded': {'values': [], 'legend': 'BE'}} #, 'Safe Boundary Exceeded': {'values': [], 'legend': 'SBE'}, 'DM and BE': {'values': [], 'legend': 'DM+BE'}}
        
        total_executions = 0
        total_schedulable = 0
        total_NS = 0
        total_BE = 0
        total_SBE = 0
        
        for level in x_axis_levels[approach]:
            # compute percentage of taskset schedulable / total taskset
            if number_of_exec_for_each_level[approach][level] == 0:
                perc = 0
                perc_NS = 0
                perc_BE = 0
                perc_SBE = 0
            else:
                total_executions += number_of_exec_for_each_level[approach][level]
                total_schedulable += x_axis_levels[approach][level]
                total_NS += NS_for_each_level[approach][level]
                total_BE += BE_for_each_level[approach][level]
                total_SBE += SBE_for_each_level[approach][level]

                perc = (x_axis_levels[approach][level] / number_of_exec_for_each_level[approach][level]) * 100
                perc_NS = (NS_for_each_level[approach][level] / number_of_exec_for_each_level[approach][level]) * 100
                perc_BE = (BE_for_each_level[approach][level] / number_of_exec_for_each_level[approach][level]) * 100
                perc_SBE = (SBE_for_each_level[approach][level] / number_of_exec_for_each_level[approach][level]) * 100
            
            perc_BE_and_NS = perc_BE + perc_NS

            results_for_each_level += '### Level ' + str(level) + '\n\n   Tasksets executed: ' + str(number_of_exec_for_each_level[approach][level]) + '\n\n   - Tasksets actually schedulable: ' + str(x_axis_levels[approach][level]) + '/' + str(number_of_exec_for_each_level[approach][level]) + ' = ' + str(perc) + ' %\n\n'
            results_for_each_level += '   - Tasksets **not** schedulable: ' + str(NS_for_each_level[approach][level]) + '/' + str(number_of_exec_for_each_level[approach][level]) + ' = ' + str(perc_NS) + ' %\n\n'
            results_for_each_level += '   - Tasksets exceeding level-criticality budget: ' + str(BE_for_each_level[approach][level]) + '/' + str(number_of_exec_for_each_level[approach][level]) + ' = ' + str(perc_BE) + ' %\n\n'
            results_for_each_level += '   - Tasksets exceeding safe boundary: ' + str(SBE_for_each_level[approach][level]) + '/' + str(number_of_exec_for_each_level[approach][level]) + ' = ' + str(perc_SBE) + ' %\n\n'

            overall_results['Actually Schedulable']['values'].append ([float(level), perc])
            overall_results['Deadline Missed']['values'].append ([float(level), perc_NS])
            overall_results['Budget Exceeded']['values'].append ([float(level), perc_BE])
            if experiment_id == 4:
                if 'Safe Boundary Exceeded' not in overall_results:
                    overall_results['Safe Boundary Exceeded'] = {'values': [], 'legend': 'SBE'}

                overall_results['Safe Boundary Exceeded']['values'].append ([float(level), perc_SBE])
            # overall_results['DM and BE']['values'].append ([float(level), perc_BE_and_NS])
            results_to_plot[approach].append([float(level), perc])

    mean_real_util = format (sum (real_utilizations_schedulable_tasksets) / len (real_utilizations_schedulable_tasksets), '.3f')
    var_real_util = format (sum ((x-float(mean_real_util))**2 for x in real_utilizations_schedulable_tasksets) / len(real_utilizations_schedulable_tasksets), '.3f')

    exp_param = '   Utilization range = [' + str(config_sim_vs_real.UTIL_LOWER_BOUND) + ', ' + str(config_sim_vs_real.UTIL_HIGHER_BOUND) + '] with step = ' + str(config_sim_vs_real.UTIL_STEP) + '\n\n'
    
    if experiment_id == 2:
        exp_param += '   Criticality factor range = [' + str(config_sim_vs_real.CRITICALITY_LOWER_BOUND) + ', ' + str(config_sim_vs_real.CRITICALITY_HIGHER_BOUND) + '] with step = ' + str(config_sim_vs_real.CRITICALITY_STEP) + '\n\n'
    elif experiment_id == 3:
        exp_param += '   HI-CRIT proportion range = [' + str(config_sim_vs_real.PROPORTION_LOWER_BOUND) + ', ' + str(config_sim_vs_real.PROPORTION_HIGHER_BOUND) + '] with step = ' + str(config_sim_vs_real.PROPORTION_STEP) + '\n\n'
    elif experiment_id == 4:
        exp_param += ' Taskset sizes = ' + str(config_sim_vs_real.TASKSETS_SIZE) + '\n\n'
 
    overall_data_section_markdown_table = '| Schedulable | Not schedulable | Budget Exceeded | Safe Boundary Exceeded |\n| ------ | ------ | ------ | ------ |\n'
    overall_data_section_markdown_table += '| ' + format((total_schedulable/total_executions)*100, '.2f') + '% | ' + format((total_NS/total_executions)*100, '.2f') + '% | ' + format((total_BE/total_executions)*100, '.2f') + '% | ' + format((total_SBE/total_executions)*100, '.2f') + '% |\n\n'

    overall_data_section = '\n\n## Overall data\n\n' + exp_param
    overall_data_section += overall_data_section_markdown_table
    overall_data_section += 'Number of executions: ' + str(total_executions) + '\n\n'
    overall_data_section += 'Schedulable executions: ' + str(total_schedulable) + '/' + str(total_executions) + ' = ' + str((total_schedulable/total_executions)*100) + ' %\n\n'
    overall_data_section += '_Not_ schedulable executions: ' + str(total_NS) + '/' + str(total_executions) + ' = ' + str((total_NS/total_executions)*100) + ' %\n\n'
    overall_data_section += 'Budget Exceeded executions: ' + str(total_BE) + '/' + str(total_executions) + ' = '  + str((total_BE/total_executions)*100) + ' %\n\n'
    overall_data_section += 'Safe Boundary Exceeded executions: ' + str(total_SBE) + '/' + str(total_executions) + ' = '  + str((total_SBE/total_executions)*100) + ' %\n\n'
    overall_data_section += 'NS + BE executions: ' + str(total_BE+total_NS) + '/' + str(total_executions) + ' = '  + str(((total_BE+total_NS)/total_executions)*100) + ' %\n\n'
    overall_data_section += '### **Simulations**\n\n#### **Weighted schedulability experiment ' + str(experiment_id) + ' according to simulations.**\n\n![ALT](result_' + str(experiment_id) + '.png)\n\n'
    overall_data_section += '#### **Percentage of (schedulable tasksets with at least one migrating tasks / number of schedulable tasksets) of experiment ' + str(experiment_id) + ' according to simulations.** \n\n![ALT](result_taskset_sched_' + str(experiment_id) + '.png) \n\n'
    overall_data_section += '\n### **Real Executions**\n\n#### **Schedulability for each level**\n\n![ALT](./overall_' + str(experiment_id) + '.png)\n\n'
    overall_data_section += '\n#### **Tasksets, grouped by differents parameters, with a Budget_Exceeded task.**\n\n![ALT](./BE_' + str(experiment_id) + '.png)\n\n'
    overall_data_section += '\n#### **Tasksets, grouped by differents parameters, with at least one task missing one (or more) of its deadlines.**\n\n![ALT](./NS_' + str(experiment_id) + '.png)\n\n'
    overall_data_section += '\n### **Nominal utilizations VS Real utilizations about schedulable tasksets**\n\n![ALT](./utilizations_histogram_' + str(experiment_id) + '.png)\n\n'

    overall_data_section += '| Average real utilizations | Variance real utilizations | Min | Max |\n| ------ | ------ | ------ | ------ |\n| ' + mean_real_util + ' | ' + var_real_util + ' | ' + format (min(real_utilizations_schedulable_tasksets), '.3f') + ' | '  + format (max(real_utilizations_schedulable_tasksets), '.3f') + ' |\n' 


    copyfile (config_sim_vs_real.MAIN_LOG, config_sim_vs_real.OUTPUT_DIR_PATH + 'exp_' + str(experiment_id) + '/log_e' + str(experiment_id) + '.xml')
    copyfile(config_sim_vs_real.SIMULATIONS_RESULTS + 'result_' + str(experiment_id) + '.png', config_sim_vs_real.OUTPUT_DIR_PATH + 'exp_' + str(experiment_id) + '/result_' + str(experiment_id) + '.png')
    copyfile(config_sim_vs_real.SIMULATIONS_RESULTS + 'result_taskset_sched_' + str(experiment_id) + '.png', config_sim_vs_real.OUTPUT_DIR_PATH + 'exp_' + str(experiment_id) + '/result_taskset_sched_' + str(experiment_id) + '.png')
    
    # Markdown generation
    report_on_bad_tasksets += overall_data_section + bad_tasksets_section +  not_schedulable_tasksets + '</details>\n\n\n' + bad_tasksets_BE + '</details>\n\n\n' + bad_tasksets_safe_boundary + '</details></details>\n\n\n' + results_for_each_level + '</details>\n\n\n'

    f = open(config_sim_vs_real.OUTPUT_DIR_PATH + 'exp_' + str(experiment_id) + '/report_executions_e' + str(experiment_id) + '.md', 'w')
    f.write(report_on_bad_tasksets)
    f.close()
    #print(results_to_plot)
    
    # plot_data(results_to_plot, output_path, x_lab)
    plot_two_or_more_functions(overall_results, config_sim_vs_real.OUTPUT_DIR_PATH  + 'exp_' + str(experiment_id) + '/overall_' + str(experiment_id) + '.png', x_lab, experiment_id)
    draw_overall_histogram (schedulable_histogram, NS_histogram, BE_histogram, config_sim_vs_real.OUTPUT_DIR_PATH  + 'exp_' + str(experiment_id) + '/overall_histogram_' + str(experiment_id) + '.png')
    draw_utilizations_histogram (nominal_utilizations_schedulable_tasksets, real_utilizations_schedulable_tasksets, config_sim_vs_real.OUTPUT_DIR_PATH  + 'exp_' + str(experiment_id) + '/utilizations_histogram_' + str(experiment_id) + '.png')
    plot_BE_data (BE_tasks_group_by_budget, BE_tasks_group_by_migrability, BE_tasks_group_by_period, BE_tasks_group_by_priority, BE_tasks_group_by_interfering_migrations, config_sim_vs_real.OUTPUT_DIR_PATH  + 'exp_' + str(experiment_id) + '/BE_' + str(experiment_id) + '.png')
    #plot_NS_data (NS_tasks_group_by_period, NS_tasks_group_by_migrability, NS_tasks_group_by_util, NS_tasks_group_by_priority, NS_tasks_group_by_interfering_migrations, schedulable_histogram, config_sim_vs_real.OUTPUT_DIR_PATH  + 'exp_' + str(experiment_id) + '/NS_' + str(experiment_id) + '.png')

    print ('Generated report about experiment ' + str(experiment_id) + ' at ' + config_sim_vs_real.OUTPUT_DIR_PATH + 'exp_' + str(experiment_id) + '/report_executions_e' + str(experiment_id) + '.md\n')

def parse_options():
  parser = optparse.OptionParser()

  parser.add_option('--util-low',
      action="store", dest="utillow",
      help="query string", default="1.6")

  parser.add_option('--util-high',
      action="store", dest="utilhigh",
      help="query string", default="1.2")

  parser.add_option('--util-step',
      action="store", dest="utilstep",
      help="query string", default="0.012")

  parser.add_option('--criticality-low',
      action="store", dest="criticalitylow",
      help="query string", default="1.5")

  parser.add_option('--criticality-high',
      action="store", dest="criticalityhigh",
      help="query string", default="4")

  parser.add_option('--criticality-step',
      action="store", dest="criticalitystep",
      help="query string", default="0.25")

  parser.add_option('--proportion-low',
      action="store", dest="proportionlow",
      help="query string", default="0.1")

  parser.add_option('--proportion-high',
      action="store", dest="proportionhigh",
      help="query string", default="0.9")

  parser.add_option('--proportion-step',
      action="store", dest="proportionstep",
      help="query string", default="0.1")

  parser.add_option('--exp-1',
      action="store", dest="exp1",
      help="query string", default="False")

  parser.add_option('--exp-2',
      action="store", dest="exp2",
      help="query string", default="False")

  parser.add_option('--exp-3',
      action="store", dest="exp3",
      help="query string", default="False")

  parser.add_option('--exp-4',
      action="store", dest="exp4",
      help="query string", default="False")
  
  parser.add_option('--numb-tests',
      action="store", dest="numbtests",
      help="query string", default="100")
      
  options, args = parser.parse_args()
  # print(options, args)

  config_sim_vs_real.UTIL_STEP = float(options.utilstep)
  config_sim_vs_real.UTIL_LOWER_BOUND = float(options.utillow)
  config_sim_vs_real.UTIL_HIGHER_BOUND = float(options.utilhigh)
  config_sim_vs_real.CRITICALITY_STEP = float(options.criticalitystep)
  config_sim_vs_real.CRITICALITY_LOWER_BOUND =float (options.criticalitylow)
  config_sim_vs_real.CRITICALITY_HIGHER_BOUND = float(options.criticalityhigh)
  config_sim_vs_real.PROPORTION_STEP = float(options.proportionstep)
  config_sim_vs_real.PROPORTION_LOWER_BOUND = float(options.proportionlow)
  config_sim_vs_real.PROPORTION_HIGHER_BOUND = float(options.proportionhigh)
  config_sim_vs_real.RUN_FIRST_TEST = True if (str(options.exp1) == 'True') else False
  config_sim_vs_real.RUN_SECOND_TEST = True if (str(options.exp2) == 'True') else False
  config_sim_vs_real.RUN_THIRD_TEST = True if (str(options.exp3) == 'True') else False
  config_sim_vs_real.RUN_FOURTH_TEST = True if (str(options.exp4) == 'True') else False
  config_sim_vs_real.NUMBER_OF_TESTS = int(options.numbtests)
  #config_sim_vs_real.TASKSETS_SIZE = 

def produce_results():
    parse_options()
    organize_executions()

    #produce_results_experiment_1()
    #produce_results_experiment_2()

    if config_sim_vs_real.RUN_FIRST_TEST:
        produce_results_experiment(1)
    if config_sim_vs_real.RUN_SECOND_TEST:
        produce_results_experiment(2)
    if config_sim_vs_real.RUN_THIRD_TEST:
        produce_results_experiment(3)
    if config_sim_vs_real.RUN_FOURTH_TEST:
        produce_results_experiment(4)

produce_results()
