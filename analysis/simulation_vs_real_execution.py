import config_sim_vs_real

import copy

import os

import xml.etree.ElementTree as ET
import xml.dom.minidom
import sys

from shutil import copyfile, rmtree

import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def plot_data (results, output):
  fig, ax = plt.subplots(figsize=(12,9))

  for approach in results:
    ax.plot([results[approach][i][0] for i in range(len(results[approach]))], [results[approach][i][1] for i in range(len(results[approach]))], label=approach)

  ax.set(xlabel='Utilization levels', ylabel='Percentage of actually schedulable tasksets')
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

def organize_executions():
    clean_XML_experiments()
    experiment_id = 0
    try:
        tree_source = ET.parse (config_sim_vs_real.PATH_TO_LOG)
    except:
        # it means that log file has no root => Add it!
        print("no root!")
        with open(config_sim_vs_real.PATH_TO_LOG, "a") as logfile:
            logfile.write("\n</executions>")
            logfile.close()
        with open(config_sim_vs_real.PATH_TO_LOG, 'r+') as logfile:
            content = logfile.read()
            logfile.seek(0, 0)
            logfile.write('<executions>\n' + content)
            logfile.close()

        tree_source = ET.parse (config_sim_vs_real.PATH_TO_LOG)
    
    beautify_XML_log()
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

    beautify_XML_experiments()


    '''if config_sim_vs_real.RUN_FIRST_TEST:
        experiment_id = 1
        clean_XML_Files (experiment_id)

        for approach in config_sim_vs_real.XML_Files[experiment_id]:
            tree_target = ET.parse(config_sim_vs_real.XML_Files[experiment_id][approach])
            root = tree.getroot()

            execution_XML = ET.SubElement (root, 'execution')'''

def produce_results_experiment_1():
    experiment_id = 1
    utilizations_levels = {}
    number_of_exec_for_util_lv = {}
    results_to_plot = {}

    for approach in config_sim_vs_real.XML_Files[experiment_id]:
        results_to_plot[approach] = []
        utilizations_levels[approach] = {}
        number_of_exec_for_util_lv[approach] = {}
        tree = ET.parse(config_sim_vs_real.XML_Files[experiment_id][approach])
        root = tree.getroot()
        
        for execution_XML in root.findall('execution'):
            if str(execution_XML.find('experimentisnotvalid').text).upper() == 'FALSE' and str(execution_XML.find('safeboundaryexceeded').text).upper() == 'FALSE':
                util_lv = execution_XML.find('tasksetutilization').text
                
                if util_lv not in number_of_exec_for_util_lv[approach]:
                    number_of_exec_for_util_lv[approach][util_lv] = 1
                    utilizations_levels[approach][util_lv] = 0
                else:
                    number_of_exec_for_util_lv[approach][util_lv] += 1

                if str(execution_XML.find('tasksetisschedulable').text).upper() == 'TRUE':
                    utilizations_levels[approach][util_lv] += 1
        
        for u in utilizations_levels[approach]:
            # compute percentage of taskset schedulable / total taskset
            if utilizations_levels[approach][u] == 0:
                perc = 0
            else:
                perc = (utilizations_levels[approach][u] / utilizations_levels[approach][u]) * 100

            results_to_plot[approach].append([float(u), perc])

    # print(number_of_exec_for_util_lv)            
    # print(utilizations_levels)
    # print(results_to_plot)
    output_path = './result1.png'
    plot_data(results_to_plot, output_path)


def produce_results():
    organize_executions()

    produce_results_experiment_1()

produce_results()
