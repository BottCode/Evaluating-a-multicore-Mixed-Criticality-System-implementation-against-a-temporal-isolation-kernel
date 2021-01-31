import config_sim_vs_real
import optparse
import pandas as pd
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Python program to convert a list to string 
	
# Function to convert 
def listToString(s): 
	
	# initialize an empty string 
	str1 = "" 
	
	# traverse in the string 
	for ele in s: 
		str1 += ele 
	
	# return string 
	return str1 

def draw_util_for_each_system (utilizations, output):
    plt.hist (utilizations, color = 'blue', alpha = 0.8, bins = 52, label = 'Schedulable tasksets')
    plt.savefig(output)
    plt.close()

    print ("TSP result saved in " + output)

def draw_util_for_each_core (utilizations, output):
    plt.hist (utilizations, color = 'blue', alpha = 0.8, bins = 52, label = 'Schedulable tasksets')
    plt.savefig(output)
    plt.close()

    print ("TSP result saved in " + output)

def produce_results_TSP_experiment(experiment_id):
    with open(config_sim_vs_real.TSP_MAIN_LOG,'r') as f:
        line = f.readline()
        idle_time = []

        # execution means the idle time of both core. i.e. the overall system
        executions_idle_time = []
        execution_idle_percentage = 0

        while line:
            # A new execution must be parsed.
            
            if 'New Execution' in line:
                partition_checked = 0

                execution_idle_percentage = 0
                line = f.readline()
                while (line and 'New Execution' not in line):
                    if 'IDLE' in line:
                        idle_percentage = []
                        # print(line)
                        # print ("REVERSE")
                        for n in range(len(line) - 1, -1, -1):
                            if line[n] == '|':
                                idle_percentage = float(listToString(idle_percentage))
                                # print(idle_percentage)
                                idle_time.append(idle_percentage)
                                execution_idle_percentage += idle_percentage
                                partition_checked += 1

                                if partition_checked == 2:
                                    # the overall system has been analyzed
                                    executions_idle_time.append(execution_idle_percentage)
                                    
                                
                                break
    
                            if line[n] != ' ' and line[n] != '\n':
                                idle_percentage = [line[n]] + idle_percentage
                        
                    line = f.readline()

            line = f.readline()
    
        utils_each_core = []
        utils_each_system = []

        for t in idle_time:
            utils_each_core.append (float (format (1-(t/100),'.3f')))
        for t in executions_idle_time:
            utils_each_system.append (float (format (2-(t/100),'.3f')))
        
        AVG_util = float (format ((sum(utils_each_core) / len(utils_each_core)), '.3f'))
        AVG_util_system = float (format ((sum(utils_each_system) / len(utils_each_system)), '.4f'))
        
        variance_each_core = float (format (sum ((x-float(AVG_util))**2 for x in utils_each_core) / len(utils_each_core), '.3f'))
        variance_each_system = float (format (sum ((x-float(AVG_util_system))**2 for x in utils_each_system) / len(utils_each_system), '.3f'))

        draw_util_for_each_core (utils_each_core, config_sim_vs_real.TSP_OUTPUT_DIR_PATH + 'exp_' + str(experiment_id) + '/TSP_util_for_each_core.png')
        draw_util_for_each_system (utils_each_system, config_sim_vs_real.TSP_OUTPUT_DIR_PATH + 'exp_' + str(experiment_id) + '/TSP_util_for_each_system.png')

        TSP_report_markdown = '# TSP report Experiment ' + str (experiment_id) + '\n\n'
        TSP_report_markdown += '## Utilizations distribution for each core\n\n'
        TSP_report_markdown += '![ALT](./TSP_util_for_each_core.png)\n\n'
        TSP_report_markdown += '| Average utilizations | Variance utilizations | Min | Max |\n| ------ | ------ | ------ | ------ |\n| ' + str (AVG_util) + ' | ' + str (variance_each_core) + ' | ' + format (min(utils_each_core), '.3f') + ' | '  + format (max(utils_each_core), '.3f') + ' |\n\n'

        TSP_report_markdown += '## Utilizations distribution for each system, i.e. for both cores\n\n'
        TSP_report_markdown += '![ALT](./TSP_util_for_each_system.png)\n\n'
        TSP_report_markdown += '| Average utilizations | Variance utilizations | Min | Max |\n| ------ | ------ | ------ | ------ |\n| ' + str (AVG_util_system) + ' | ' + str (variance_each_system) + ' | ' + format (min(utils_each_system), '.3f') + ' | '  + format (max(utils_each_system), '.3f') + ' |\n\n'

        f = open(config_sim_vs_real.TSP_OUTPUT_DIR_PATH + 'exp_' + str(experiment_id) + '/report_TSP_e' + str(experiment_id) + '.md', 'w')
        f.write(TSP_report_markdown)
        f.close()

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
    # organize_executions()

    #produce_results_TSP_experiment_1()
    #produce_results_TSP_experiment_2()

    if config_sim_vs_real.RUN_FIRST_TEST:
        produce_results_TSP_experiment(1)
    if config_sim_vs_real.RUN_SECOND_TEST:
        produce_results_TSP_experiment(2)
    if config_sim_vs_real.RUN_THIRD_TEST:
        produce_results_TSP_experiment(3)
    if config_sim_vs_real.RUN_FOURTH_TEST:
        produce_results_TSP_experiment(4)

produce_results()