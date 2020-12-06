import config_sim_vs_real

import copy

import os

import xml.etree.ElementTree as ET
import xml.dom.minidom
import sys

from shutil import copyfile, rmtree

import time
import optparse

import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def plot_data (results, output, x_lab):
  fig, ax = plt.subplots(figsize=(12,9))

  for approach in results:
    ax.plot([results[approach][i][0] for i in range(len(results[approach]))], [results[approach][i][1] for i in range(len(results[approach]))], label=approach)

  ax.set(xlabel=x_lab, ylabel='Percentage of actually schedulable tasksets')
  ax.grid()
  plt.xticks()
  plt.legend()
  plt.savefig(output)
  print('Result saved: ' + output)

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
    elif experiment_id == 4:
        xml_level_to_analyze = 'tasksetsize'
        x_lab = 'Taskset size'
        level_list = config_sim_vs_real.TASKSETS_SIZE

    x_axis_levels = {}
    number_of_exec_for_each_level = {}
    # for each level => number of tasksets that exceed their budget
    BE_for_each_level = {}
    # for each level => number of NOT schedulable tasksets
    NS_for_each_level = {}
    # for each level => number of tasksets that exceed their safe boundary
    SBE_for_each_level = {}
    results_to_plot = {}

    report_on_bad_tasksets = '# Report on Experiment ' + str(experiment_id)+ '\n\n## Bad tasksets\n\n'
    bad_tasksets_safe_boundary = '\n### **Safe Boundary Exceeded**\n\nOvvero quando un taskset ha troppi core (2 nel contesto dual-core) eseguenti in HI-crit mode.\n\n'
    # BE stands for budget exceeded
    bad_tasksets_BE = '\n### **Criticality Level Budget Exceeded**\n\nOvvero quando un task di un taskset ha ecceduto il suo criticality-level budget, cioè un LO-crit task che eccede il suo LO-crit budget, oppure un HI-crit task che eccede il suo HI-crit budget.\n\n'
    not_schedulable_tasksets = '\n### **Not schedulable tasksets**\n\nOvvero quando almeno un task non completa entra almeno una sua deadline.\n\n'
    results_for_each_level = '\n## Focus for each ' + x_lab + ' level.\n\n'

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
                'utilization' : execution_XML.find('tasksetutilization').text,
                'criticality_factor': execution_XML.find('criticalityfactor').text,
                'hicrit_proportion': execution_XML.find('perc').text
            }
            
            cores_info = '   <details> <summary markdown="span">Click here to see the CPUs log.</summary>\n\n   Idle time is expressed as **seconds**.\n\n'
            guilty_tasks = '   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>\n\n   Time values are expressed as **micro-seconds**.\n\n'
            list_of_tasks = []

            single_level = execution_XML.find(xml_level_to_analyze).text
            if experiment_id == 4:
                single_level = int(single_level)
            
            number_of_exec_for_each_level[approach][single_level] += 1
            tasks_XML = execution_XML.find('tasks')
            cores_XML = execution_XML.find('cores')
            collapse_menu_containing_tasks = '   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>\n\n   Time values are expressed as **micro-seconds**.\n\n'
            
            for core_XML in cores_XML.findall('cpu'):
                curr_core = {}
                curr_core['id'] = core_XML.find('id').text
                curr_core['lowtohigh'] = core_XML.find('lowtohigh').text
                curr_core['hightolow'] = core_XML.find('hightolow').text
                curr_core['idletime'] = core_XML.find('idletime').text
                cores_info += '\n\n   CPU: ' + curr_core['id'] + '\n\n    ' + str(curr_core) + '\n\n'
            cores_info += '\n   </details>\n\n'

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
                    curr_task['budgetexceeded'] = task_XML.find('budgetexceeded').text
                    curr_task['timesmigrated'] = task_XML.find('timesmigrated').text
                    curr_task['timesrestored'] = task_XML.find('timesrestored').text
                    curr_task['timesonc1'] = task_XML.find('timesonc1').text
                    curr_task['timesonc2'] = task_XML.find('timesonc2').text
                    curr_task['lockedtime'] = task_XML.find('lockedtime').text
                    list_of_tasks.append(copy.deepcopy(curr_task))
                    # Write on markdown report
                    collapse_menu_containing_tasks += '\n\n   Task: ' + curr_task['id'] + '\n\n    ' + str(curr_task) + '\n\n'
                    if int(task_XML.find('taskid').text) == int(execution_XML.find('guiltytask').text) or int(curr_task['deadlinesmissed']) > 0:
                        guilty_tasks += 'Task: ' +  curr_task['id'] + '\n\n    ' + str(curr_task) + '\n\n'
            
            guilty_tasks += '\n   </details>\n\n'
            collapse_menu_containing_tasks += '\n   </details>\n\n'

            if str(execution_XML.find('experimentisnotvalid').text).upper() == 'FALSE' and str(execution_XML.find('safeboundaryexceeded').text).upper() == 'FALSE':

                if str(execution_XML.find('tasksetisschedulable').text).upper() == 'TRUE':
                    x_axis_levels[approach][single_level] += 1
                else:
                    not_schedulable_tasksets += '  ' + str(numbered_list_index_NS) +'. Taskset **' + str(execution_XML.find('executionid').text) + '**\n'
                    not_schedulable_tasksets += '\n    Taskset execution params: ' + str(execution_info) + '\n\n' + guilty_tasks + '\n\n'
                    not_schedulable_tasksets += cores_info + collapse_menu_containing_tasks
                    NS_for_each_level[approach][single_level] += 1
                    numbered_list_index_NS += 1

            elif str(execution_XML.find('safeboundaryexceeded').text).upper() == 'TRUE':
                bad_tasksets_safe_boundary += '  ' + str(numbered_list_index_safe_boundary) + '. Taskset **' + str(execution_XML.find('executionid').text) + '**\n'
                bad_tasksets_safe_boundary += '\n    Taskset execution params: ' + str(execution_info) + '\n\n'
                bad_tasksets_safe_boundary += cores_info + collapse_menu_containing_tasks
                SBE_for_each_level[approach][single_level] += 1
                numbered_list_index_safe_boundary += 1
            elif str(execution_XML.find('experimentisnotvalid').text).upper() == 'TRUE':
                bad_tasksets_BE += '  ' + str(numbered_list_index_BE) + '. Taskset **' + str(execution_XML.find('executionid').text) + '**\n'
                BE_for_each_level[approach][single_level] += 1
                numbered_list_index_BE += 1
                bad_tasksets_BE += '\n    Taskset execution params: ' + str(execution_info) + '\n\n' + guilty_tasks + '\n\n'
                bad_tasksets_BE += cores_info + collapse_menu_containing_tasks
    
        total_executions = 0
        for level in x_axis_levels[approach]:
            # compute percentage of taskset schedulable / total taskset
            if number_of_exec_for_each_level[approach][level] == 0:
                perc = 0
                perc_NS = 0
                perc_BE = 0
                perc_SBE = 0
            else:
                total_executions += number_of_exec_for_each_level[approach][level]
                perc = (x_axis_levels[approach][level] / number_of_exec_for_each_level[approach][level]) * 100
                perc_NS = (NS_for_each_level[approach][level] / number_of_exec_for_each_level[approach][level]) * 100
                perc_BE = (BE_for_each_level[approach][level] / number_of_exec_for_each_level[approach][level]) * 100
                perc_SBE = (SBE_for_each_level[approach][level] / number_of_exec_for_each_level[approach][level]) * 100

            results_for_each_level += '### Level ' + str(level) + '\n\n   Tasksets executed: ' + str(number_of_exec_for_each_level[approach][level]) + '\n\n   - Tasksets actually schedulable: ' + str(x_axis_levels[approach][level]) + '/' + str(number_of_exec_for_each_level[approach][level]) + ' = ' + str(perc) + ' %\n\n'
            results_for_each_level += '   - Tasksets **not** schedulable: ' + str(NS_for_each_level[approach][level]) + '/' + str(number_of_exec_for_each_level[approach][level]) + ' = ' + str(perc_NS) + ' %\n\n'
            results_for_each_level += '   - Tasksets exceeding level-criticality budget: ' + str(BE_for_each_level[approach][level]) + '/' + str(number_of_exec_for_each_level[approach][level]) + ' = ' + str(perc_BE) + ' %\n\n'
            results_for_each_level += '   - Tasksets exceeding safe boundary: ' + str(SBE_for_each_level[approach][level]) + '/' + str(number_of_exec_for_each_level[approach][level]) + ' = ' + str(perc_SBE) + ' %\n\n'

            results_to_plot[approach].append([float(level), perc])
    
    report_on_bad_tasksets += not_schedulable_tasksets + bad_tasksets_BE + bad_tasksets_safe_boundary + results_for_each_level + '\n\n   ## Number of executions: **' + str(total_executions) + '**\n\n'
    f = open('report_bad_tasksets_e' + str(experiment_id) + '.md', 'w')
    f.write(report_on_bad_tasksets)
    f.close()
    #print(results_to_plot)
    output_path = './result' + str(experiment_id) + '.png'
    plot_data(results_to_plot, output_path, x_lab)

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
