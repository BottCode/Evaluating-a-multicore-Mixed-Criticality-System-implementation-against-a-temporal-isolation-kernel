import config_sim_vs_real

import copy

import os

import xml.etree.ElementTree as ET
import xml.dom.minidom
import sys

from shutil import copyfile, rmtree

import time

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

def add_root_to_XML(file_name=config_sim_vs_real.PATH_TO_LOG, line='<executions>\n'):

    with open(config_sim_vs_real.PATH_TO_LOG, "a") as logfile:
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
    experiment_id = 0
    try:
        tree_source = ET.parse (config_sim_vs_real.PATH_TO_LOG)
    except:
        # it means that log file has no root => Add it!
        # print("no root!")
        #add_root_to_XML()
        '''with open(config_sim_vs_real.PATH_TO_LOG, 'r+') as logfile:
            content = logfile.read()
            logfile.seek(0, 0)
            logfile.write('<executions>\n' + content)
            logfile.close()
            # This sleep seems necessary because file writing is asynchronous. 
            # Since the files are quite large, it may happen that the next parsing
            # starts before the previous writing is complete.
            time.sleep(3)'''

        tree_source = ET.parse (config_sim_vs_real.PATH_TO_LOG)
        #beautify_XML_log()

    root_source = tree_source.getroot()

    for execution_XML in root_source.findall('execution'):
        execution_id = execution_XML.find('executionid').text

        if execution_id != '-1':
            experiment_id = int(execution_XML.find('experimentid').text)
            approach = execution_XML.find('approach').text

            if experiment_id == 1 and config_sim_vs_real.RUN_FIRST_TEST:
                tree_target = ET.parse(config_sim_vs_real.XML_Files[experiment_id][approach])
                root_target = tree_target.getroot()
                root_target.append(execution_XML)

                tree_target.write(config_sim_vs_real.XML_Files[experiment_id][approach])

            elif experiment_id == 2 and config_sim_vs_real.RUN_SECOND_TEST:
                tree_target = ET.parse(config_sim_vs_real.XML_Files[experiment_id][approach])
                root_target = tree_target.getroot()
                root_target.append(execution_XML)

                tree_target.write(config_sim_vs_real.XML_Files[experiment_id][approach])

            elif experiment_id == 3 and config_sim_vs_real.RUN_THIRD_TEST:
                tree_target = ET.parse(config_sim_vs_real.XML_Files[experiment_id][approach])
                root_target = tree_target.getroot()
                root_target.append(execution_XML)

                tree_target.write(config_sim_vs_real.XML_Files[experiment_id][approach])

            elif experiment_id == 4 and config_sim_vs_real.RUN_FOURTH_TEST:
                tree_target = ET.parse(config_sim_vs_real.XML_Files[experiment_id][approach])
                root_target = tree_target.getroot()
                root_target.append(execution_XML)

                tree_target.write(config_sim_vs_real.XML_Files[experiment_id][approach])

    # beautify_XML_experiments()


    '''if config_sim_vs_real.RUN_FIRST_TEST:
        experiment_id = 1
        clean_XML_Files (experiment_id)

        for approach in config_sim_vs_real.XML_Files[experiment_id]:
            tree_target = ET.parse(config_sim_vs_real.XML_Files[experiment_id][approach])
            root = tree.getroot()

            execution_XML = ET.SubElement (root, 'execution')'''

def produce_results_experiment(experiment_id):
    xml_level_to_analyze = ""
    if experiment_id == 1:
        xml_level_to_analyze = 'tasksetutilization'
        x_lab = 'Utilization level'
    elif experiment_id == 2:
        xml_level_to_analyze = 'criticalityfactor'
        x_lab = 'Criticality Factor'
    elif experiment_id == 3:
        # hi-crit proportion
        xml_level_to_analyze = 'perc'
        x_lab = 'HI-CRIT task proportion'
    elif experiment_id == 4:
        xml_level_to_analyze = 'tasksetsize'
        x_lab = 'Taskset size'
    x_axis_levels = {}
    number_of_exec_for_each_level = {}
    results_to_plot = {}

    for approach in config_sim_vs_real.XML_Files[experiment_id]:
        results_to_plot[approach] = []
        x_axis_levels[approach] = {}
        number_of_exec_for_each_level[approach] = {}
        tree = ET.parse(config_sim_vs_real.XML_Files[experiment_id][approach])
        root = tree.getroot()
        
        for execution_XML in root.findall('execution'):
            if str(execution_XML.find('experimentisnotvalid').text).upper() == 'FALSE' and str(execution_XML.find('safeboundaryexceeded').text).upper() == 'FALSE':
                single_level = execution_XML.find(xml_level_to_analyze).text
                
                if single_level not in number_of_exec_for_each_level[approach]:
                    number_of_exec_for_each_level[approach][single_level] = 1
                    x_axis_levels[approach][single_level] = 0
                else:
                    number_of_exec_for_each_level[approach][single_level] += 1

                if str(execution_XML.find('tasksetisschedulable').text).upper() == 'TRUE':
                    x_axis_levels[approach][single_level] += 1

        for level in x_axis_levels[approach]:
            # compute percentage of taskset schedulable / total taskset
            if x_axis_levels[approach][level] == 0:
                perc = 0
            else:
                perc = (x_axis_levels[approach][level] / number_of_exec_for_each_level[approach][level]) * 100

            results_to_plot[approach].append([float(level), perc])

    output_path = './result' + str(experiment_id) + '.png'
    plot_data(results_to_plot, output_path, x_lab)


def produce_results():
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
