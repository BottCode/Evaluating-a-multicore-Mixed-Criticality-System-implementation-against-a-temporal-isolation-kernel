PATH_TO_LOG = {
  1: '../results/xu-burns-real-execution/log_e1.xml',
  2: '../results/xu-burns-real-execution/log_e2.xml',
  3: '../results/xu-burns-real-execution/log_e3.xml',
  4: '../results/xu-burns-real-execution/log_e4.xml'
}

'''PATH_TO_LOG = {
  1: '../results/xu-burns-real-execution/log.xml',
  2: '../results/xu-burns-real-execution/log.xml',
  3: '../results/xu-burns-real-execution/log.xml',
  4: '../results/xu-burns-real-execution/log.xml'
}'''

OUTPUT_DIR_PATH = '../results/xu-burns-real-execution/'
SIMULATIONS_RESULTS = '../py-xu-burns-2019-rta/dual-core-version/results_dualcore_2/'

MAIN_LOG = '../results/xu-burns-real-execution/log.xml'

# Enable/disable tests to run
RUN_FIRST_TEST = True
RUN_SECOND_TEST = False
RUN_THIRD_TEST = False
RUN_FOURTH_TEST = False

# Number of tests to run for each Utilization step
NUMBER_OF_TESTS = 1

UTIL_STEP = 0.012
UTIL_LOWER_BOUND = 1.6
UTIL_HIGHER_BOUND = 2.2

CRITICALITY_STEP = 0.25
CRITICALITY_LOWER_BOUND = 1.5
CRITICALITY_HIGHER_BOUND = 4

PROPORTION_STEP = 0.1
PROPORTION_LOWER_BOUND = 0.1
PROPORTION_HIGHER_BOUND = 0.9

TASKSETS_SIZE = [8, 10, 12, 15, 20, 25, 30, 35]

XML_Files = {
  1: {
    'SEMI2WF': '../results/xu-burns-real-execution/XML_results/experiment_1/semi2-WF.xml'
  },

  2: {
    'SEMI2WF': '../results/xu-burns-real-execution/XML_results/experiment_2/semi2-WF.xml'
  },
  
  3: {
    'SEMI2WF': '../results/xu-burns-real-execution/XML_results/experiment_3/semi2-WF.xml'
  },

  4: {
    'SEMI2WF': '../results/xu-burns-real-execution/XML_results/experiment_4/semi2-WF.xml'
  },
}

'''XML_Files = {
  1: {
    'SEMI1FF': '../results/xu-burns-real-execution/XML_results/experiment_1/semi1-FF.xml',
    'SEMI1BF': '../results/xu-burns-real-execution/XML_results/experiment_1/semi1-BF.xml',
    'SEMI1WF': '../results/xu-burns-real-execution/XML_results/experiment_1/semi1-WF.xml',
    'SEMI2FF': '../results/xu-burns-real-execution/XML_results/experiment_1/semi2-FF.xml',
    'SEMI2BF': '../results/xu-burns-real-execution/XML_results/experiment_1/semi2-BF.xml',
    'SEMI2WF': '../results/xu-burns-real-execution/XML_results/experiment_1/semi2-WF.xml'
  },

  2: {
    'SEMI1FF': '../results/xu-burns-real-execution/XML_results/experiment_2/semi1-FF.xml',
    'SEMI1BF': '../results/xu-burns-real-execution/XML_results/experiment_2/semi1-BF.xml',
    'SEMI1WF': '../results/xu-burns-real-execution/XML_results/experiment_2/semi1-WF.xml',
    'SEMI2FF': '../results/xu-burns-real-execution/XML_results/experiment_2/semi2-FF.xml',
    'SEMI2BF': '../results/xu-burns-real-execution/XML_results/experiment_2/semi2-BF.xml',
    'SEMI2WF': '../results/xu-burns-real-execution/XML_results/experiment_2/semi2-WF.xml'
  },
  
  3: {
    'SEMI1FF': '../results/xu-burns-real-execution/XML_results/experiment_3/semi1-FF.xml',
    'SEMI1BF': '../results/xu-burns-real-execution/XML_results/experiment_3/semi1-BF.xml',
    'SEMI1WF': '../results/xu-burns-real-execution/XML_results/experiment_3/semi1-WF.xml',
    'SEMI2FF': '../results/xu-burns-real-execution/XML_results/experiment_3/semi2-FF.xml',
    'SEMI2BF': '../results/xu-burns-real-execution/XML_results/experiment_3/semi2-BF.xml',
    'SEMI2WF': '../results/xu-burns-real-execution/XML_results/experiment_3/semi2-WF.xml'
  },

  4: {
    'SEMI1FF': '../results/xu-burns-real-execution/XML_results/experiment_4/semi1-FF.xml',
    'SEMI1BF': '../results/xu-burns-real-execution/XML_results/experiment_4/semi1-BF.xml',
    'SEMI1WF': '../results/xu-burns-real-execution/XML_results/experiment_4/semi1-WF.xml',
    'SEMI2FF': '../results/xu-burns-real-execution/XML_results/experiment_4/semi2-FF.xml',
    'SEMI2BF': '../results/xu-burns-real-execution/XML_results/experiment_4/semi2-BF.xml',
    'SEMI2WF': '../results/xu-burns-real-execution/XML_results/experiment_4/semi2-WF.xml'
  },
}'''