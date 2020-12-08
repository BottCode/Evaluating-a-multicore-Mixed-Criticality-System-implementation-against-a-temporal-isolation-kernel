# Report on Experiment 4

## Bad tasksets


### **Not schedulable tasksets**

Ovvero quando almeno un task non completa entra almeno una sua deadline.


### **Criticality Level Budget Exceeded**

Ovvero quando un task di un taskset ha ecceduto il suo criticality-level budget, cioè un LO-crit task che eccede il suo LO-crit budget, oppure un HI-crit task che eccede il suo HI-crit budget.

  1. Taskset **e4_semi2wf_t558**

    Taskset execution params: {'id': 'e4_semi2wf_t558', 'size': '8', 'utilization': '1.9320000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 1', 'period': 525000.0, 'C(LO)': 97800.0, 'C(HI)': 97800.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 7', 'preemptions': ' 24', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.065954132', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.634550508', 'avgresponsejitter': ' 0.059796066', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 0', 'timesonc1': ' 12', 'timesonc2': ' 18', 'lockedtime': ' 0.000000000'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 56700000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 2418732, 'util': 95.73415873015873}



   CPU: 2

    {'id': 2, 'hyperperiod': 28350000, 'lowtohigh': ' 3', 'hightolow': ' 2', 'idletime': 2144266, 'util': 92.43645149911816}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 2', 'period': 64800.0, 'C(LO)': 11027.0, 'C(HI)': 22054.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 52', 'preemptions': ' 31', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.007435003', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.240985691', 'avgresponsejitter': ' 0.005879024', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 82', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 1', 'period': 67500.0, 'C(LO)': 10407.0, 'C(HI)': 20815.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 50', 'preemptions': ' 27', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.012313736', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.245746559', 'avgresponsejitter': ' 0.005998024', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 76', 'timesonc2': ' 0', 'lockedtime': ' 0.000000261'}



   Task:  0

    {'id': ' 0', 'basecpu': ' 1', 'priority': ' 5', 'period': 10000.0, 'C(LO)': 1884.0, 'C(HI)': 1884.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 0', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001130276', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.280006601', 'avgresponsejitter': ' 0.000971093', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 329', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 3', 'period': 630000.0, 'C(LO)': 1987.0, 'C(HI)': 1987.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 7', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001125796', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.150908120', 'avgresponsejitter': ' 0.000999886', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 6', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 4', 'period': 47250.0, 'C(LO)': 47.0, 'C(HI)': 47.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 71', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000036375', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.261059805', 'avgresponsejitter': ' 0.000031342', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 70', 'timesonc2': ' 0', 'lockedtime': ' 0.000000357'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 2', 'period': 52500.0, 'C(LO)': 15659.0, 'C(HI)': 31318.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 63', 'preemptions': ' 11', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.013551505', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.202505982', 'avgresponsejitter': ' 0.008396069', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 73', 'lockedtime': ' 0.000001045'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 3', 'period': 45360.0, 'C(LO)': 6980.0, 'C(HI)': 13961.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 73', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.008776727', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.220565988', 'avgresponsejitter': ' 0.003701003', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 3', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 75', 'lockedtime': ' 0.000001015'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 1', 'period': 525000.0, 'C(LO)': 97800.0, 'C(HI)': 97800.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 7', 'preemptions': ' 24', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.065954132', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.634550508', 'avgresponsejitter': ' 0.059796066', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 0', 'timesonc1': ' 12', 'timesonc2': ' 18', 'lockedtime': ' 0.000000000'}


   </details>


### **Safe Boundary Exceeded**

Ovvero quando un taskset ha troppi core (2 nel contesto dual-core) eseguenti in HI-crit mode.


## Focus for each Taskset size level.

### Level 8

   Tasksets executed: 2

   - Tasksets actually schedulable: 1/2 = 50.0 %

   - Tasksets **not** schedulable: 0/2 = 0.0 %

   - Tasksets exceeding level-criticality budget: 1/2 = 50.0 %

   - Tasksets exceeding safe boundary: 0/2 = 0.0 %

### Level 10

   Tasksets executed: 0

   - Tasksets actually schedulable: 0/0 = 0 %

   - Tasksets **not** schedulable: 0/0 = 0 %

   - Tasksets exceeding level-criticality budget: 0/0 = 0 %

   - Tasksets exceeding safe boundary: 0/0 = 0 %

### Level 12

   Tasksets executed: 0

   - Tasksets actually schedulable: 0/0 = 0 %

   - Tasksets **not** schedulable: 0/0 = 0 %

   - Tasksets exceeding level-criticality budget: 0/0 = 0 %

   - Tasksets exceeding safe boundary: 0/0 = 0 %

### Level 15

   Tasksets executed: 0

   - Tasksets actually schedulable: 0/0 = 0 %

   - Tasksets **not** schedulable: 0/0 = 0 %

   - Tasksets exceeding level-criticality budget: 0/0 = 0 %

   - Tasksets exceeding safe boundary: 0/0 = 0 %

### Level 20

   Tasksets executed: 0

   - Tasksets actually schedulable: 0/0 = 0 %

   - Tasksets **not** schedulable: 0/0 = 0 %

   - Tasksets exceeding level-criticality budget: 0/0 = 0 %

   - Tasksets exceeding safe boundary: 0/0 = 0 %

### Level 25

   Tasksets executed: 0

   - Tasksets actually schedulable: 0/0 = 0 %

   - Tasksets **not** schedulable: 0/0 = 0 %

   - Tasksets exceeding level-criticality budget: 0/0 = 0 %

   - Tasksets exceeding safe boundary: 0/0 = 0 %

### Level 30

   Tasksets executed: 0

   - Tasksets actually schedulable: 0/0 = 0 %

   - Tasksets **not** schedulable: 0/0 = 0 %

   - Tasksets exceeding level-criticality budget: 0/0 = 0 %

   - Tasksets exceeding safe boundary: 0/0 = 0 %

### Level 35

   Tasksets executed: 0

   - Tasksets actually schedulable: 0/0 = 0 %

   - Tasksets **not** schedulable: 0/0 = 0 %

   - Tasksets exceeding level-criticality budget: 0/0 = 0 %

   - Tasksets exceeding safe boundary: 0/0 = 0 %



   ## Number of executions: **2**

