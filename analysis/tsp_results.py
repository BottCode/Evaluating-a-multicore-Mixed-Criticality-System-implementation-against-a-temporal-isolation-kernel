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
    print (utilizations, "\n#\n")
    plt.hist (utilizations, color = 'blue', alpha = 0.8, bins = 52, label = 'Schedulable tasksets')
    plt.savefig(output)
    plt.close()

    print ("TSP result saved in " + output)

def draw_util_for_each_core (utilizations, output):
    plt.hist (utilizations, color = 'blue', alpha = 0.8, bins = 52, label = 'Schedulable tasksets')
    plt.savefig(output)
    plt.close()

    print ("TSP result saved in " + output)

def produce_results_TSP_experiment_IWRR_MAST_schema2 (experiment_id):
    number_of_partitions_for_each_core = 2
    number_of_cores = 2
    number_of_partitions = number_of_partitions_for_each_core * number_of_cores

    with open(config_sim_vs_real.TSP_MAIN_LOG, 'r') as f:
        line = f.readline()
        idle_time = []

        # execution means the idle time of both core. i.e. the overall system
        executions_idle_time = []
        execution_idle_percentage = 0
        idle_for_each_partition = {
            'C1LOW': [], 'C1HIGH': [], 'C2LOW': [], 'C2HIGH': []
        }
        partitions_idle_ok = 0
        partitions_idle_not_ok = 0

        while line:

            # A new execution must be parsed.
            if 'Start Resident Software' in line:
                partition_checked = 0
                current_partition = None
                already_checked = {
                    'C1LOW': False, 'C1HIGH': False, 'C2LOW': False, 'C2HIGH': False
                }
                execution_idle_percentage = 0
                
                line = f.readline()
                

                while (line and 'Start Resident Software' not in line):
                    if 'C1LOW' in line:
                        current_partition = 'C1LOW'
                        already_checked[current_partition] = True
                    elif 'C1HIGH' in line:
                        current_partition = 'C1HIGH'
                        already_checked[current_partition] = True
                    elif 'C2LOW' in line:
                        current_partition = 'C2LOW'
                        already_checked[current_partition] = True
                    elif 'C2HIGH' in line:
                        current_partition = 'C2HIGH'
                        already_checked[current_partition] = True
                    
                    if 'Partition_Utilization' in line:
                        partition_nominal_util_percentage = []
                        for n in range(len(line) - 1, -1, -1):
                            if line[n] == ':':
                                partition_nominal_util_percentage = float (listToString  (partition_nominal_util_percentage))
                                print (current_partition, "partition_nominal_util_percentage is ", partition_nominal_util_percentage, "\n")
                                break
                            else:
                                partition_nominal_util_percentage = [line[n]] + partition_nominal_util_percentage

                    if 'Is Valid: FALSE' in line:
                        for p in idle_for_each_partition:
                            if already_checked[p] and len (idle_for_each_partition[p]) > 0 and p != current_partition:
                                idle_for_each_partition[p].pop ()
                        break

                    if 'IDLE' in line:
                        idle_percentage = []
                        # print("#### new\n", line, "\n")
                        # print ("REVERSE", "\n")
                        for n in range(len(line) - 1, -1, -1):
                            if line[n] == '|':
                                # print ("casting ", idle_percentage, "\n")
                                idle_percentage = float(listToString(idle_percentage))
                                idle_for_each_partition[current_partition].append (idle_percentage)
                                # idle_time.append(idle_percentage)
                                execution_idle_percentage += idle_percentage
                                partition_checked += 1

                                if partition_checked == 4:
                                    # the overall system has been analyzed
                                    executions_idle_time.append(execution_idle_percentage)
         
                                break
    
                            if line[n] != ' ' and line[n] != '\n':
                                idle_percentage = [line[n]] + idle_percentage
                        
                        minimum_idle_time = 100 - (partition_nominal_util_percentage * 100)
                        if minimum_idle_time > idle_percentage:
                            print ("!!!!! Lower bound is ", minimum_idle_time, "while actual idle is ", idle_percentage, "\n\n")
                            partitions_idle_not_ok = partitions_idle_not_ok + 1
                            for p in idle_for_each_partition:
                                if already_checked[p] and len (idle_for_each_partition[p]) > 0:
                                    idle_for_each_partition[p][-1] = minimum_idle_time
                            if partition_checked == 4:
                                # executions_idle_time.pop()
                                None
                            # break
                        else:
                            print ("Ok: Lower bound is ", minimum_idle_time, "while actual idle is ", idle_percentage, "\n\n")
                            partitions_idle_ok = partitions_idle_ok + 1

                    line = f.readline()



            line = f.readline()

        print ("\n --------\n not ok: " ,partitions_idle_not_ok, "/", partitions_idle_not_ok + partitions_idle_ok, "=", partitions_idle_not_ok/(partitions_idle_not_ok+partitions_idle_ok) ,"\n ------\n")
        utils_each_core = []
        utils_each_system = []

        for i in range (0, len (idle_for_each_partition['C1LOW'])):
            c1 = idle_for_each_partition['C1LOW'][i] + idle_for_each_partition['C1HIGH'][i]
            utils_each_core.append (float (format ((number_of_partitions_for_each_core)-(c1/100),'.3f')))

            c2 = idle_for_each_partition['C2LOW'][i] + idle_for_each_partition['C2HIGH'][i]
            utils_each_core.append (float (format ((number_of_partitions_for_each_core)-(c2/100),'.3f')))
        print ((idle_for_each_partition['C1LOW']))
        print ((idle_for_each_partition['C2LOW']))
        print ((idle_for_each_partition['C1HIGH']))
        print ((idle_for_each_partition['C2HIGH']))

        # for t in idle_time:
        #     utils_each_core.append (float (format (1-(t/100),'.3f')))
        for t in executions_idle_time:
            utils_each_system.append (float (format ((number_of_partitions)-(t/100),'.3f')))
        
        AVG_util = float (format ((sum(utils_each_core) / len(utils_each_core)), '.3f'))
        AVG_util_system = float (format ((sum(utils_each_system) / len(utils_each_system)), '.3f'))
        
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


def produce_results_TSP_experiment (experiment_id):
    with open(config_sim_vs_real.TSP_MAIN_LOG, 'r') as f:
        line = f.readline()
        idle_time = []

        # execution means the idle time of both core. i.e. the overall system
        executions_idle_time = []
        execution_idle_percentage = 0

        while line:

            # A new execution must be parsed.
            if 'Start Resident Software' in line:
                partition_checked = 0

                execution_idle_percentage = 0
                line = f.readline()
                while (line and 'Start Resident Software' not in line):
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
        AVG_util_system = float (format ((sum(utils_each_system) / len(utils_each_system)), '.3f'))
        
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

    if config_sim_vs_real.RUN_FIRST_TEST:
        produce_results_TSP_experiment_IWRR_MAST_schema2 (1)
    if config_sim_vs_real.RUN_SECOND_TEST:
        produce_results_TSP_experiment_IWRR_MAST_schema2 (2)
    if config_sim_vs_real.RUN_THIRD_TEST:
        produce_results_TSP_experiment_IWRR_MAST_schema2 (3)
    if config_sim_vs_real.RUN_FOURTH_TEST:
        produce_results_TSP_experiment_IWRR_MAST_schema2 (4)

produce_results()