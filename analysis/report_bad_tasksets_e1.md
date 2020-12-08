# Report on Experiment 1



   ## Overall data

  Number of executions: 232

Schedulable executions: 189/232 = 81.46551724137932 %

_Not_ schedulable executions: 7/232 = 3.0172413793103448 %

Budget Exceeded executions: 34/232 = 14.655172413793101 %

Safe Boundary Exceeded executions: 2/232 = 0.8620689655172413 %

NS + BE executions: 41/232 = 17.67241379310345 %

## Bad tasksets

<details><summary markdown="span">Click here to expand this section.</summary>


### **Not schedulable tasksets**

<details><summary markdown="span">Click here to expand this section.</summary>

Ovvero quando almeno un task non completa entra almeno una sua deadline.

  1. Taskset **e1_semi2wf_t1137**

    Taskset execution params: {'id': 'e1_semi2wf_t1137', 'size': '12', 'utilization': '1.848', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 5', 'period': 35000.0, 'C(LO)': 2350.0, 'C(HI)': 2350.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1223', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001412366', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 43.735006156', 'avgresponsejitter': ' 0.001176072', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 0', 'timesmigrated': ' 5', 'timesrestored': ' 5', 'timesonc1': ' 5', 'timesonc2': ' 1216', 'lockedtime': ' 0.000021273'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 113400000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 76559345, 'util': 32.48735008818342}



   CPU: 2

    {'id': 2, 'hyperperiod': 113400000, 'lowtohigh': ' 35', 'hightolow': ' 35', 'idletime': 75512498, 'util': 33.41049559082893}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 3', 'period': 15750.0, 'C(LO)': 1638.0, 'C(HI)': 3277.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 7201', 'preemptions': ' 51', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001696054', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.384256168', 'avgresponsejitter': ' 0.000824000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 7251', 'timesonc2': ' 0', 'lockedtime': ' 0.000034709'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 1', 'period': 94500.0, 'C(LO)': 8783.0, 'C(HI)': 17566.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1201', 'preemptions': ' 51', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.005918405', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.306433832', 'avgresponsejitter': ' 0.004420273', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1251', 'timesonc2': ' 0', 'lockedtime': ' 0.000004733'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 2', 'period': 81000.0, 'C(LO)': 5477.0, 'C(HI)': 10954.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1401', 'preemptions': ' 247', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006644676', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.319005979', 'avgresponsejitter': ' 0.002905565', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1647', 'timesonc2': ' 0', 'lockedtime': ' 0.000014940'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 0', 'period': 200000.0, 'C(LO)': 50475.0, 'C(HI)': 50475.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 568', 'preemptions': ' 1522', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.042755856', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.200699333', 'avgresponsejitter': ' 0.031073198', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2089', 'timesonc2': ' 0', 'lockedtime': ' 0.000053330'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 5', 'period': 42000.0, 'C(LO)': 4857.0, 'C(HI)': 4857.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 2701', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002924934', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.358006087', 'avgresponsejitter': ' 0.002432571', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2701', 'timesonc2': ' 0', 'lockedtime': ' 0.000014934'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 4', 'period': 100000.0, 'C(LO)': 1208.0, 'C(HI)': 1208.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1135', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000731679', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.300006192', 'avgresponsejitter': ' 0.000611222', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1134', 'timesonc2': ' 0', 'lockedtime': ' 0.000015213'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 2', 'period': 135000.0, 'C(LO)': 29248.0, 'C(HI)': 58497.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 841', 'preemptions': ' 113', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.046087631', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.265005889', 'avgresponsejitter': ' 0.015157051', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 9', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 962', 'lockedtime': ' 0.000040604'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 1', 'period': 141750.0, 'C(LO)': 1988.9999999999998, 'C(HI)': 3979.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 801', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004439294', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.258256877', 'avgresponsejitter': ' 0.001021060', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 10', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 811', 'lockedtime': ' 0.000034207'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 3', 'period': 90000.0, 'C(LO)': 490.0, 'C(HI)': 980.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1261', 'preemptions': ' 2', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001501937', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.310006009', 'avgresponsejitter': ' 0.000252979', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 16', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1278', 'lockedtime': ' 0.000009682'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 2', 'priority': ' 0', 'period': 600000.0, 'C(LO)': 189919.0, 'C(HI)': 189919.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 190', 'preemptions': ' 578', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.154986135', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 113.800006754', 'avgresponsejitter': ' 0.107811006', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 767', 'lockedtime': ' 0.000054682'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 4', 'period': 450000.0, 'C(LO)': 37201.0, 'C(HI)': 37201.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 253', 'preemptions': ' 45', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.023586321', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 113.950006988', 'avgresponsejitter': ' 0.018839898', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 0', 'timesonc2': ' 297', 'lockedtime': ' 0.000014787'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 5', 'period': 35000.0, 'C(LO)': 2350.0, 'C(HI)': 2350.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1223', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001412366', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 43.735006156', 'avgresponsejitter': ' 0.001176072', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 0', 'timesmigrated': ' 5', 'timesrestored': ' 5', 'timesonc1': ' 5', 'timesonc2': ' 1216', 'lockedtime': ' 0.000021273'}


   </details>

  2. Taskset **e1_semi2wf_t1431**

    Taskset execution params: {'id': 'e1_semi2wf_t1431', 'size': '12', 'utilization': '1.86', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 4', 'period': 20000.0, 'C(LO)': 5309.0, 'C(HI)': 5309.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 2836', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003190619', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.680005961', 'avgresponsejitter': ' 0.002653117', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 0', 'timesmigrated': ' 3', 'timesrestored': ' 3', 'timesonc1': ' 4', 'timesonc2': ' 2830', 'lockedtime': ' 0.000052793'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 56700000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 38582411, 'util': 31.953419753086422}



   CPU: 2

    {'id': 2, 'hyperperiod': 11340000, 'lowtohigh': ' 20', 'hightolow': ' 20', 'idletime': 35285412, 'util': -211.15883597883595}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 787500.0, 'C(LO)': 109242.0, 'C(HI)': 218485.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 73', 'preemptions': ' 298', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.087841931', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 56.921151186', 'avgresponsejitter': ' 0.067520730', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 370', 'timesonc2': ' 0', 'lockedtime': ' 0.000020315'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 1', 'period': 168750.0, 'C(LO)': 11297.0, 'C(HI)': 22595.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 337', 'preemptions': ' 49', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.017790180', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.531256228', 'avgresponsejitter': ' 0.005966414', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 385', 'timesonc2': ' 0', 'lockedtime': ' 0.000006144'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 2', 'period': 151200.0, 'C(LO)': 4430.0, 'C(HI)': 8861.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 376', 'preemptions': ' 37', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.014842580', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.548806868', 'avgresponsejitter': ' 0.002791745', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 412', 'timesonc2': ' 0', 'lockedtime': ' 0.000013652'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 4', 'period': 65625.0, 'C(LO)': 18773.0, 'C(HI)': 18773.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 865', 'preemptions': ' 296', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.013702712', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.634381135', 'avgresponsejitter': ' 0.009937177', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1160', 'timesonc2': ' 0', 'lockedtime': ' 0.000044886'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 6', 'period': 45000.0, 'C(LO)': 3540.0, 'C(HI)': 3540.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1261', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002131619', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.655006480', 'avgresponsejitter': ' 0.001763243', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1261', 'timesonc2': ' 0', 'lockedtime': ' 0.000018426'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 5', 'period': 54000.0, 'C(LO)': 1792.0, 'C(HI)': 1792.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1051', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001088165', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.646006447', 'avgresponsejitter': ' 0.000904712', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1050', 'timesonc2': ' 0', 'lockedtime': ' 0.000006216'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 3', 'period': 70875.0, 'C(LO)': 349.0, 'C(HI)': 349.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 801', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000210778', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.629131450', 'avgresponsejitter': ' 0.000177435', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 800', 'timesonc2': ' 0', 'lockedtime': ' 0.000004970'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 756000.0, 'C(LO)': 115749.0, 'C(HI)': 231499.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 76', 'preemptions': ' 394', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.235825508', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 56.945531060', 'avgresponsejitter': ' 0.082180429', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 471', 'lockedtime': ' 0.000009483'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 2', 'period': 56700.0, 'C(LO)': 2902.0, 'C(HI)': 5804.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1001', 'preemptions': ' 72', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.013954610', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.649057405', 'avgresponsejitter': ' 0.001823240', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 9', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1081', 'lockedtime': ' 0.000017700'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 1', 'period': 75600.0, 'C(LO)': 2712.0, 'C(HI)': 5424.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 751', 'preemptions': ' 47', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.014648432', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.624405988', 'avgresponsejitter': ' 0.001716532', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 9', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 806', 'lockedtime': ' 0.000017000'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 4', 'period': 20000.0, 'C(LO)': 5309.0, 'C(HI)': 5309.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 2836', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003190619', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.680005961', 'avgresponsejitter': ' 0.002653117', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 0', 'timesmigrated': ' 3', 'timesrestored': ' 3', 'timesonc1': ' 4', 'timesonc2': ' 2830', 'lockedtime': ' 0.000052793'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 3', 'period': 60000.0, 'C(LO)': 14480.0, 'C(HI)': 14480.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 946', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.008714940', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.643141468', 'avgresponsejitter': ' 0.007206601', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 945', 'lockedtime': ' 0.000026075'}


   </details>

  3. Taskset **e1_semi2wf_t2430**

    Taskset execution params: {'id': 'e1_semi2wf_t2430', 'size': '12', 'utilization': '1.9080000000000001', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 4', 'period': 10000.0, 'C(LO)': 826.0, 'C(HI)': 826.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 5671', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000498345', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.690006372', 'avgresponsejitter': ' 0.000410366', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 0', 'timesmigrated': ' 10', 'timesrestored': ' 10', 'timesonc1': ' 5666', 'timesonc2': ' 4', 'lockedtime': ' 0.000083369'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 11340000, 'lowtohigh': ' 11', 'hightolow': ' 11', 'idletime': 37464548, 'util': -230.3752028218695}



   CPU: 2

    {'id': 2, 'hyperperiod': 56700000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 37801737, 'util': 33.33026984126984}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 1', 'period': 101250.0, 'C(LO)': 15533.0, 'C(HI)': 31066.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 561', 'preemptions': ' 570', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.041021706', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.599571556', 'avgresponsejitter': ' 0.008469637', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 7', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1137', 'timesonc2': ' 0', 'lockedtime': ' 0.000031919'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 0', 'period': 105000.0, 'C(LO)': 14092.0, 'C(HI)': 28184.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 541', 'preemptions': ' 487', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.040333949', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.608069000', 'avgresponsejitter': ' 0.008057958', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 4', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1031', 'timesonc2': ' 0', 'lockedtime': ' 0.000023511'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 2', 'period': 118125.0, 'C(LO)': 30282.0, 'C(HI)': 30282.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 481', 'preemptions': ' 985', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.019792279', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.581881285', 'avgresponsejitter': ' 0.016207667', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1465', 'timesonc2': ' 0', 'lockedtime': ' 0.000079099'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 4', 'period': 10000.0, 'C(LO)': 826.0, 'C(HI)': 826.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 5671', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000498345', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.690006372', 'avgresponsejitter': ' 0.000410366', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 0', 'timesmigrated': ' 10', 'timesrestored': ' 10', 'timesonc1': ' 5666', 'timesonc2': ' 4', 'lockedtime': ' 0.000083369'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 3', 'period': 30240.0, 'C(LO)': 1251.0, 'C(HI)': 1251.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1876', 'preemptions': ' 109', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001241928', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.669765994', 'avgresponsejitter': ' 0.000654709', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1984', 'timesonc2': ' 0', 'lockedtime': ' 0.000018360'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 4', 'period': 45000.0, 'C(LO)': 8125.999999999999, 'C(HI)': 16251.999999999998, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1261', 'preemptions': ' 18', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.008754327', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.655005787', 'avgresponsejitter': ' 0.004133841', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1278', 'lockedtime': ' 0.000055210'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 3', 'period': 52500.0, 'C(LO)': 3113.0, 'C(HI)': 6226.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1081', 'preemptions': ' 18', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006146607', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.647506078', 'avgresponsejitter': ' 0.001619075', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1098', 'lockedtime': ' 0.000020390'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 1', 'period': 84000.0, 'C(LO)': 2176.0, 'C(HI)': 4353.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 676', 'preemptions': ' 12', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.005911769', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.616005988', 'avgresponsejitter': ' 0.001140526', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 687', 'lockedtime': ' 0.000005018'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 2', 'period': 64800.0, 'C(LO)': 1445.0, 'C(HI)': 2890.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 876', 'preemptions': ' 23', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.005189150', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.635205961', 'avgresponsejitter': ' 0.000790276', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 898', 'lockedtime': ' 0.000012550'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 2', 'priority': ' 0', 'period': 590625.0, 'C(LO)': 105754.0, 'C(HI)': 105754.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 97', 'preemptions': ' 493', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.085238267', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.109381781', 'avgresponsejitter': ' 0.067908483', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 589', 'lockedtime': ' 0.000059631'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 6', 'period': 50000.0, 'C(LO)': 7218.0, 'C(HI)': 7218.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1135', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004339147', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.650006039', 'avgresponsejitter': ' 0.003598279', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1134', 'lockedtime': ' 0.000113826'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 5', 'period': 78750.0, 'C(LO)': 4151.0, 'C(HI)': 4151.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 721', 'preemptions': ' 18', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006566042', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 57.621256132', 'avgresponsejitter': ' 0.002158517', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 738', 'lockedtime': ' 0.000020174'}


   </details>

  4. Taskset **e1_semi2wf_t2633**

    Taskset execution params: {'id': 'e1_semi2wf_t2633', 'size': '12', 'utilization': '1.9200000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 8', 'period': 20000.0, 'C(LO)': 815.0, 'C(HI)': 815.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 948', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000482330', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 19.920007117', 'avgresponsejitter': ' 0.000405766', 'deadlinesmissed': ' 2', 'budgetexceeded': ' 0', 'timesmigrated': ' 4', 'timesrestored': ' 3', 'timesonc1': ' 944', 'timesonc2': ' 1', 'lockedtime': ' 0.000011892'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 113400000, 'lowtohigh': ' 24', 'hightolow': ' 24', 'idletime': 68072323, 'util': 39.971496472663134}



   CPU: 2

    {'id': 2, 'hyperperiod': 18900000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 70350858, 'util': -272.2267619047619}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 1', 'period': 180000.0, 'C(LO)': 11402.0, 'C(HI)': 22804.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 631', 'preemptions': ' 189', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.031493462', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.220707508', 'avgresponsejitter': ' 0.007618318', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 6', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 825', 'timesonc2': ' 0', 'lockedtime': ' 0.000005012'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 3', 'period': 120000.0, 'C(LO)': 7450.0, 'C(HI)': 14900.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 946', 'preemptions': ' 155', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.030678237', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.280006132', 'avgresponsejitter': ' 0.004865078', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 8', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1108', 'timesonc2': ' 0', 'lockedtime': ' 0.000007126'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 630000.0, 'C(LO)': 23998.0, 'C(HI)': 47996.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 181', 'preemptions': ' 159', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.053616841', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 113.770830075', 'avgresponsejitter': ' 0.016051640', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 341', 'timesonc2': ' 0', 'lockedtime': ' 0.000001892'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 2', 'period': 129600.0, 'C(LO)': 1254.0, 'C(HI)': 2508.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 876', 'preemptions': ' 18', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.021402147', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.270406300', 'avgresponsejitter': ' 0.000746336', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 8', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 901', 'timesonc2': ' 0', 'lockedtime': ' 0.000000255'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 4', 'period': 84375.0, 'C(LO)': 26746.0, 'C(HI)': 26746.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1345', 'preemptions': ' 1256', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.026463237', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.315631153', 'avgresponsejitter': ' 0.015491186', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2600', 'timesonc2': ' 0', 'lockedtime': ' 0.000045928'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 6', 'period': 70875.0, 'C(LO)': 11433.0, 'C(HI)': 11433.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1601', 'preemptions': ' 432', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.007931162', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.329132057', 'avgresponsejitter': ' 0.005920231', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2032', 'timesonc2': ' 0', 'lockedtime': ' 0.000024072'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 5', 'period': 84000.0, 'C(LO)': 5773.0, 'C(HI)': 5773.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1351', 'preemptions': ' 157', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.010473084', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.316006961', 'avgresponsejitter': ' 0.003094162', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1507', 'timesonc2': ' 0', 'lockedtime': ' 0.000009847'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 7', 'period': 22500.0, 'C(LO)': 1462.0, 'C(HI)': 1462.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 5042', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000883459', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.400013982', 'avgresponsejitter': ' 0.000729970', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 8', 'timesrestored': ' 8', 'timesonc1': ' 5037', 'timesonc2': ' 4', 'lockedtime': ' 0.000044030'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 8', 'period': 20000.0, 'C(LO)': 815.0, 'C(HI)': 815.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 948', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000482330', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 19.920007117', 'avgresponsejitter': ' 0.000405766', 'deadlinesmissed': ' 2', 'budgetexceeded': ' 0', 'timesmigrated': ' 4', 'timesrestored': ' 3', 'timesonc1': ' 944', 'timesonc2': ' 1', 'lockedtime': ' 0.000011892'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 0', 'period': 118125.0, 'C(LO)': 13206.0, 'C(HI)': 26412.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 961', 'preemptions': ' 107', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.044153619', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.281881426', 'avgresponsejitter': ' 0.008642772', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1067', 'lockedtime': ' 0.000026048'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 2', 'period': 52500.0, 'C(LO)': 2954.0, 'C(HI)': 5909.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2161', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001775078', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.347506114', 'avgresponsejitter': ' 0.001475916', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 2160', 'lockedtime': ' 0.000056138'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 1', 'period': 100000.0, 'C(LO)': 58458.0, 'C(HI)': 58458.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1135', 'preemptions': ' 598', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.036887126', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.300006063', 'avgresponsejitter': ' 0.030252279', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1732', 'lockedtime': ' 0.000115003'}


   </details>

  5. Taskset **e1_semi2wf_t3480**

    Taskset execution params: {'id': 'e1_semi2wf_t3480', 'size': '12', 'utilization': '1.9560000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 3', 'period': 25200.0, 'C(LO)': 3027.0, 'C(HI)': 3027.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 4501', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001821393', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.374806574', 'avgresponsejitter': ' 0.001514207', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 0', 'timesmigrated': ' 6', 'timesrestored': ' 6', 'timesonc1': ' 2', 'timesonc2': ' 4497', 'lockedtime': ' 0.000043817'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 113400000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 73557210, 'util': 35.13473544973546}



   CPU: 2

    {'id': 2, 'hyperperiod': 3150000, 'lowtohigh': ' 8', 'hightolow': ' 8', 'idletime': 79572269, 'util': -2426.103777777778}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 4', 'period': 135000.0, 'C(LO)': 13595.0, 'C(HI)': 27190.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 841', 'preemptions': ' 296', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.012541940', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.272975688', 'avgresponsejitter': ' 0.007616261', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1136', 'timesonc2': ' 0', 'lockedtime': ' 0.000011009'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 2', 'period': 200000.0, 'C(LO)': 12051.0, 'C(HI)': 24102.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 568', 'preemptions': ' 143', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.027380300', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.208589312', 'avgresponsejitter': ' 0.007314498', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 710', 'timesonc2': ' 0', 'lockedtime': ' 0.000007276'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 590625.0, 'C(LO)': 29580.0, 'C(HI)': 59161.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 193', 'preemptions': ' 158', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.047141859', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 113.811690117', 'avgresponsejitter': ' 0.018558694', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 350', 'timesonc2': ' 0', 'lockedtime': ' 0.000005583'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 3', 'period': 157500.0, 'C(LO)': 5535.0, 'C(HI)': 11070.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 721', 'preemptions': ' 104', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006879691', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.243628156', 'avgresponsejitter': ' 0.003043453', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 824', 'timesonc2': ' 0', 'lockedtime': ' 0.000002925'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 1', 'period': 506250.0, 'C(LO)': 2160.0, 'C(HI)': 4321.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 225', 'preemptions': ' 9', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004381967', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 113.893756108', 'avgresponsejitter': ' 0.001140547', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 233', 'timesonc2': ' 0', 'lockedtime': ' 0.000000646'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 5', 'period': 67500.0, 'C(LO)': 17575.0, 'C(HI)': 17575.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1681', 'preemptions': ' 623', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.014937748', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.332506354', 'avgresponsejitter': ' 0.009501781', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2303', 'timesonc2': ' 0', 'lockedtime': ' 0.000021763'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 7', 'period': 40000.0, 'C(LO)': 6128.0, 'C(HI)': 6128.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 2837', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003683057', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.400014973', 'avgresponsejitter': ' 0.003061673', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2836', 'timesonc2': ' 0', 'lockedtime': ' 0.000041553'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 6', 'period': 45360.0, 'C(LO)': 1655.0, 'C(HI)': 1655.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 2501', 'preemptions': ' 51', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004586970', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.354646369', 'avgresponsejitter': ' 0.000894480', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2551', 'timesonc2': ' 0', 'lockedtime': ' 0.000023033'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 0', 'period': 131250.0, 'C(LO)': 55408.0, 'C(HI)': 110817.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 865', 'preemptions': ' 1301', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.094372751', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.268756213', 'avgresponsejitter': ' 0.030807793', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 8', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 2173', 'lockedtime': ' 0.000059447'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 3', 'period': 25200.0, 'C(LO)': 3027.0, 'C(HI)': 3027.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 4501', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001821393', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.374806574', 'avgresponsejitter': ' 0.001514207', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 0', 'timesmigrated': ' 6', 'timesrestored': ' 6', 'timesonc1': ' 2', 'timesonc2': ' 4497', 'lockedtime': ' 0.000043817'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 1', 'period': 126000.0, 'C(LO)': 3884.0, 'C(HI)': 3884.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 901', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002331429', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.275638465', 'avgresponsejitter': ' 0.001935309', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 900', 'lockedtime': ' 0.000000000'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 2', 'period': 70000.0, 'C(LO)': 677.0, 'C(HI)': 677.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1621', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000406958', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.330005955', 'avgresponsejitter': ' 0.000341159', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 4', 'timesrestored': ' 4', 'timesonc1': ' 1', 'timesonc2': ' 1619', 'lockedtime': ' 0.000019949'}


   </details>

  6. Taskset **e1_semi2wf_t4334**

    Taskset execution params: {'id': 'e1_semi2wf_t4334', 'size': '12', 'utilization': '2.004', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 7', 'period': 15750.0, 'C(LO)': 560.0, 'C(HI)': 560.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 7201', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000339402', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.384256189', 'avgresponsejitter': ' 0.000276204', 'deadlinesmissed': ' 2', 'budgetexceeded': ' 0', 'timesmigrated': ' 11', 'timesrestored': ' 11', 'timesonc1': ' 7199', 'timesonc2': ' 0', 'lockedtime': ' 0.000052736'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 113400000, 'lowtohigh': ' 34', 'hightolow': ' 34', 'idletime': 69634895, 'util': 38.59356701940035}



   CPU: 2

    {'id': 2, 'hyperperiod': 12600000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 71495159, 'util': -467.42189682539686}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 1', 'period': 112500.0, 'C(LO)': 19679.0, 'C(HI)': 39359.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1009', 'preemptions': ' 1085', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.037390658', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.287506132', 'avgresponsejitter': ' 0.011672556', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 8', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2101', 'timesonc2': ' 0', 'lockedtime': ' 0.000008060'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 2', 'period': 100000.0, 'C(LO)': 5415.0, 'C(HI)': 10830.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1135', 'preemptions': ' 285', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.011170931', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.300006117', 'avgresponsejitter': ' 0.002908450', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 9', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1428', 'timesonc2': ' 0', 'lockedtime': ' 0.000006742'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 3', 'period': 60480.0, 'C(LO)': 2016.0, 'C(HI)': 4032.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1876', 'preemptions': ' 154', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.015565438', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.339526171', 'avgresponsejitter': ' 0.001260144', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 17', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2046', 'timesonc2': ' 0', 'lockedtime': ' 0.000004562'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 6', 'period': 60000.0, 'C(LO)': 12177.0, 'C(HI)': 12177.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1891', 'preemptions': ' 702', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.007671574', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.340007246', 'avgresponsejitter': ' 0.006250348', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2592', 'timesonc2': ' 0', 'lockedtime': ' 0.000026408'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 4', 'period': 131250.0, 'C(LO)': 14344.0, 'C(HI)': 14344.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 865', 'preemptions': ' 442', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.017225592', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.268756420', 'avgresponsejitter': ' 0.008090411', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1306', 'timesonc2': ' 0', 'lockedtime': ' 0.000013577'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 567000.0, 'C(LO)': 60903.0, 'C(HI)': 60903.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 201', 'preemptions': ' 725', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.066151865', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 113.833253096', 'avgresponsejitter': ' 0.043453273', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 925', 'timesonc2': ' 0', 'lockedtime': ' 0.000021937'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 5', 'period': 75600.0, 'C(LO)': 3265.0, 'C(HI)': 3265.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1501', 'preemptions': ' 63', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.009070444', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.324406249', 'avgresponsejitter': ' 0.001758553', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1563', 'timesonc2': ' 0', 'lockedtime': ' 0.000002661'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 7', 'period': 15750.0, 'C(LO)': 560.0, 'C(HI)': 560.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 7201', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000339402', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.384256189', 'avgresponsejitter': ' 0.000276204', 'deadlinesmissed': ' 2', 'budgetexceeded': ' 0', 'timesmigrated': ' 11', 'timesrestored': ' 11', 'timesonc1': ' 7199', 'timesonc2': ' 0', 'lockedtime': ' 0.000052736'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 1', 'period': 175000.0, 'C(LO)': 35186.0, 'C(HI)': 70372.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 649', 'preemptions': ' 277', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.022653775', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.225006240', 'avgresponsejitter': ' 0.017874141', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 925', 'lockedtime': ' 0.000031060'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 2', 'period': 72000.0, 'C(LO)': 2734.0, 'C(HI)': 5468.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1576', 'preemptions': ' 9', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001703895', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.328006390', 'avgresponsejitter': ' 0.001360799', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1584', 'lockedtime': ' 0.000033994'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 3', 'period': 52500.0, 'C(LO)': 121.0, 'C(HI)': 243.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2161', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000074670', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.347506345', 'avgresponsejitter': ' 0.000064628', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 2160', 'lockedtime': ' 0.000080868'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 525000.0, 'C(LO)': 261456.00000000003, 'C(HI)': 261456.00000000003, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 217', 'preemptions': ' 915', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.181640132', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 113.890596589', 'avgresponsejitter': ' 0.134166453', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1131', 'lockedtime': ' 0.000080604'}


   </details>

  7. Taskset **e1_semi2wf_t4439**

    Taskset execution params: {'id': 'e1_semi2wf_t4439', 'size': '12', 'utilization': '2.004', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 5', 'period': 18900.0, 'C(LO)': 1945.0, 'C(HI)': 1945.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1383', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001170610', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 27.100906637', 'avgresponsejitter': ' 0.000971580', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 0', 'timesmigrated': ' 5', 'timesrestored': ' 5', 'timesonc1': ' 1371', 'timesonc2': ' 10', 'lockedtime': ' 0.000003985'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 113400000, 'lowtohigh': ' 59', 'hightolow': ' 59', 'idletime': 77830768, 'util': 31.36616578483246}



   CPU: 2

    {'id': 2, 'hyperperiod': 56700000, 'lowtohigh': ' 27', 'hightolow': ' 27', 'idletime': 78636288, 'util': -38.68833862433863}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 840000.0, 'C(LO)': 146523.0, 'C(HI)': 293047.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 136', 'preemptions': ' 937', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.127718018', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 113.560006255', 'avgresponsejitter': ' 0.092750054', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1072', 'timesonc2': ' 0', 'lockedtime': ' 0.000026817'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 3', 'period': 25200.0, 'C(LO)': 2915.0, 'C(HI)': 5831.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 4501', 'preemptions': ' 171', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.005229697', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.374806303', 'avgresponsejitter': ' 0.001535640', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 42', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 4713', 'timesonc2': ' 0', 'lockedtime': ' 0.000007568'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 1', 'period': 131250.0, 'C(LO)': 3145.0, 'C(HI)': 6291.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 865', 'preemptions': ' 73', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.027793249', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.268756267', 'avgresponsejitter': ' 0.001965165', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 17', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 954', 'timesonc2': ' 0', 'lockedtime': ' 0.000013880'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 2', 'period': 181440.0, 'C(LO)': 36857.0, 'C(HI)': 36857.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 626', 'preemptions': ' 860', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.027467697', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.218566438', 'avgresponsejitter': ' 0.020427384', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1485', 'timesonc2': ' 0', 'lockedtime': ' 0.000037423'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 5', 'period': 18900.0, 'C(LO)': 1945.0, 'C(HI)': 1945.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1383', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001170610', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 27.100906637', 'avgresponsejitter': ' 0.000971580', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 0', 'timesmigrated': ' 5', 'timesrestored': ' 5', 'timesonc1': ' 1371', 'timesonc2': ' 10', 'lockedtime': ' 0.000003985'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 4', 'period': 33750.0, 'C(LO)': 2748.0, 'C(HI)': 2748.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 3361', 'preemptions': ' 31', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002808189', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.366256429', 'avgresponsejitter': ' 0.001384459', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 3391', 'timesonc2': ' 0', 'lockedtime': ' 0.000025444'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 700000.0, 'C(LO)': 175193.0, 'C(HI)': 350387.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 163', 'preemptions': ' 727', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.335544189', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 113.710281664', 'avgresponsejitter': ' 0.106141216', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 890', 'lockedtime': ' 0.000037895'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 1', 'period': 196875.0, 'C(LO)': 11935.0, 'C(HI)': 23871.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 577', 'preemptions': ' 62', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.018272532', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.203295090', 'avgresponsejitter': ' 0.006494099', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 6', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 644', 'lockedtime': ' 0.000000613'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 2', 'period': 39375.0, 'C(LO)': 306.0, 'C(HI)': 612.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2881', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000494222', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.360631120', 'avgresponsejitter': ' 0.000155667', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 20', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 2900', 'lockedtime': ' 0.000037964'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 4', 'period': 87500.0, 'C(LO)': 15380.0, 'C(HI)': 15380.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1297', 'preemptions': ' 53', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.015134922', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.312506033', 'avgresponsejitter': ' 0.007942312', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1349', 'lockedtime': ' 0.000034604'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 5', 'period': 81000.0, 'C(LO)': 10031.0, 'C(HI)': 10031.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 624', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006041084', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 51.382006204', 'avgresponsejitter': ' 0.005057435', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 1', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 623', 'lockedtime': ' 0.000018730'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 3', 'period': 100000.0, 'C(LO)': 5132.0, 'C(HI)': 5132.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1135', 'preemptions': ' 15', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.008354538', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.300006369', 'avgresponsejitter': ' 0.002638231', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1149', 'lockedtime': ' 0.000007781'}


   </details>

</details>



### **Criticality Level Budget Exceeded**

<details><summary markdown="span">Click here to expand this section.</summary>

Ovvero quando un task di un taskset ha ecceduto il suo criticality-level budget, cioè un LO-crit task che eccede il suo LO-crit budget, oppure un HI-crit task che eccede il suo HI-crit budget.

  2. Taskset **e1_semi2wf_t1273**

    Taskset execution params: {'id': 'e1_semi2wf_t1273', 'size': '12', 'utilization': '1.86', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 6', 'period': 25200.0, 'C(LO)': 749.0, 'C(HI)': 749.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 870', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000452417', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 22.908886727', 'avgresponsejitter': ' 0.000374655', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 3', 'timesrestored': ' 3', 'timesonc1': ' 867', 'timesonc2': ' 2', 'lockedtime': ' 0.000013279'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 113400000, 'lowtohigh': ' 5', 'hightolow': ' 5', 'idletime': 13721590, 'util': 87.89983245149912}



   CPU: 2

    {'id': 2, 'hyperperiod': 37800000, 'lowtohigh': ' 6', 'hightolow': ' 6', 'idletime': 14020940, 'util': 62.90756613756614}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 4', 'period': 45360.0, 'C(LO)': 5137.0, 'C(HI)': 10274.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 484', 'preemptions': ' 9', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.007964399', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 22.863527195', 'avgresponsejitter': ' 0.002593670', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 3', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 495', 'timesonc2': ' 0', 'lockedtime': ' 0.000002471'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 840000.0, 'C(LO)': 47407.0, 'C(HI)': 94814.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 28', 'preemptions': ' 55', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.056380976', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 22.845277000', 'avgresponsejitter': ' 0.029805102', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 82', 'timesonc2': ' 0', 'lockedtime': ' 0.000003006'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 2', 'period': 162000.0, 'C(LO)': 5588.0, 'C(HI)': 11177.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 137', 'preemptions': ' 30', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.015174544', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 22.870006955', 'avgresponsejitter': ' 0.003394222', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 168', 'timesonc2': ' 0', 'lockedtime': ' 0.000002162'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 5', 'period': 94500.0, 'C(LO)': 20206.0, 'C(HI)': 20206.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 233', 'preemptions': ' 58', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.012432399', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 22.829507165', 'avgresponsejitter': ' 0.010111057', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 290', 'timesonc2': ' 0', 'lockedtime': ' 0.000002763'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 3', 'period': 108000.0, 'C(LO)': 22096.0, 'C(HI)': 22096.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 204', 'preemptions': ' 137', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.029263766', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 22.816006351', 'avgresponsejitter': ' 0.012372706', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 340', 'timesonc2': ' 0', 'lockedtime': ' 0.000006718'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 1', 'period': 600000.0, 'C(LO)': 53430.0, 'C(HI)': 53430.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 38', 'preemptions': ' 77', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.060498928', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 22.609133225', 'avgresponsejitter': ' 0.035459495', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 114', 'timesonc2': ' 0', 'lockedtime': ' 0.000008036'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 6', 'period': 25200.0, 'C(LO)': 749.0, 'C(HI)': 749.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 870', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000452417', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 22.908886727', 'avgresponsejitter': ' 0.000374655', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 3', 'timesrestored': ' 3', 'timesonc1': ' 867', 'timesonc2': ' 2', 'lockedtime': ' 0.000013279'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 1', 'period': 131250.0, 'C(LO)': 16573.0, 'C(HI)': 33147.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 168', 'preemptions': ' 68', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.023216132', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 22.787505955', 'avgresponsejitter': ' 0.010282652', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 237', 'lockedtime': ' 0.000005306'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 0', 'period': 180000.0, 'C(LO)': 8931.0, 'C(HI)': 17862.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 123', 'preemptions': ' 12', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.027305952', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 22.780006252', 'avgresponsejitter': ' 0.005287192', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 136', 'lockedtime': ' 0.000001796'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 2', 'period': 75600.0, 'C(LO)': 1915.0, 'C(HI)': 3831.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 291', 'preemptions': ' 11', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.015056201', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 22.848789162', 'avgresponsejitter': ' 0.001225925', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 303', 'lockedtime': ' 0.000011441'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 3', 'period': 50000.0, 'C(LO)': 21357.0, 'C(HI)': 21357.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 440', 'preemptions': ' 68', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.014696847', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 22.900006063', 'avgresponsejitter': ' 0.010890772', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 507', 'lockedtime': ' 0.000021580'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 4', 'period': 40000.0, 'C(LO)': 3390.0, 'C(HI)': 3390.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 549', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002041538', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 22.880006213', 'avgresponsejitter': ' 0.001702523', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 0', 'timesonc2': ' 548', 'lockedtime': ' 0.000008045'}


   </details>

  3. Taskset **e1_semi2wf_t1296**

    Taskset execution params: {'id': 'e1_semi2wf_t1296', 'size': '12', 'utilization': '1.86', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 5', 'period': 52500.0, 'C(LO)': 29.0, 'C(HI)': 29.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1', 'lockedtime': ' 0.000000000'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 37800000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 16, 'util': 99.99995767195767}



   CPU: 2

    {'id': 2, 'hyperperiod': 113400000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 14, 'util': 99.99998765432099}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 2', 'period': 75600.0, 'C(LO)': 10777.0, 'C(HI)': 21554.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 0', 'period': 175000.0, 'C(LO)': 22679.0, 'C(HI)': 45358.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 1', 'period': 105000.0, 'C(LO)': 3515.0, 'C(HI)': 7030.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 5', 'period': 22500.0, 'C(LO)': 3552.0, 'C(HI)': 3552.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000492'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 3', 'period': 72000.0, 'C(LO)': 6607.0, 'C(HI)': 6607.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 4', 'period': 70000.0, 'C(LO)': 3054.0, 'C(HI)': 3054.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 2', 'priority': ' 0', 'period': 756000.0, 'C(LO)': 126526.0, 'C(HI)': 253052.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 2', 'period': 118125.0, 'C(LO)': 9810.0, 'C(HI)': 19621.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 1', 'period': 181440.0, 'C(LO)': 7518.0, 'C(HI)': 15037.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 4', 'period': 120000.0, 'C(LO)': 36708.0, 'C(HI)': 36708.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 3', 'period': 168750.0, 'C(LO)': 11012.0, 'C(HI)': 11012.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 5', 'period': 52500.0, 'C(LO)': 29.0, 'C(HI)': 29.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1', 'lockedtime': ' 0.000000000'}


   </details>

  4. Taskset **e1_semi2wf_t1466**

    Taskset execution params: {'id': 'e1_semi2wf_t1466', 'size': '12', 'utilization': '1.86', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 6', 'period': 10000.0, 'C(LO)': 7.0, 'C(HI)': 15.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 113400000, 'lowtohigh': ' 1', 'hightolow': ' 0', 'idletime': 17, 'util': 99.99998500881834}



   CPU: 2

    {'id': 2, 'hyperperiod': 28350000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 12, 'util': 99.99995767195767}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 3', 'period': 126000.0, 'C(LO)': 11220.0, 'C(HI)': 22441.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 0', 'period': 189000.0, 'C(LO)': 16734.0, 'C(HI)': 33468.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 1', 'period': 175000.0, 'C(LO)': 7688.0, 'C(HI)': 15376.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 2', 'period': 151200.0, 'C(LO)': 2538.0, 'C(HI)': 5076.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 6', 'period': 10000.0, 'C(LO)': 7.0, 'C(HI)': 15.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 4', 'period': 100800.0, 'C(LO)': 26983.0, 'C(HI)': 26983.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 5', 'period': 81000.0, 'C(LO)': 8306.0, 'C(HI)': 8306.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 1', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 7', 'period': 26250.0, 'C(LO)': 2014.0000000000002, 'C(HI)': 2014.0000000000002, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001075598', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.000018646', 'avgresponsejitter': ' 0.001075598', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 1', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 2', 'priority': ' 0', 'period': 675000.0, 'C(LO)': 173334.0, 'C(HI)': 346668.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 1', 'period': 54000.0, 'C(LO)': 12926.0, 'C(HI)': 12926.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 2', 'period': 52500.0, 'C(LO)': 9426.0, 'C(HI)': 9426.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1', 'lockedtime': ' 0.000000000'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 3', 'period': 45000.0, 'C(LO)': 104.0, 'C(HI)': 104.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000069105', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.000013270', 'avgresponsejitter': ' 0.000069105', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1', 'lockedtime': ' 0.000000000'}


   </details>

  5. Taskset **e1_semi2wf_t1479**

    Taskset execution params: {'id': 'e1_semi2wf_t1479', 'size': '12', 'utilization': '1.86', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 6', 'period': 18900.0, 'C(LO)': 1512.0, 'C(HI)': 1512.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1232', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000913081', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 24.247009150', 'avgresponsejitter': ' 0.000760312', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 0', 'timesmigrated': ' 8', 'timesrestored': ' 7', 'timesonc1': ' 1223', 'timesonc2': ' 7', 'lockedtime': ' 0.000005826'}

Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 5', 'period': 40000.0, 'C(LO)': 2557.0, 'C(HI)': 2557.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1597', 'preemptions': ' 41', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002316829', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 64.840006787', 'avgresponsejitter': ' 0.001293649', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 6', 'timesrestored': ' 6', 'timesonc1': ' 1631', 'timesonc2': ' 5', 'lockedtime': ' 0.000023520'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 22680000, 'lowtohigh': ' 30', 'hightolow': ' 30', 'idletime': 40382454, 'util': -78.05314814814815}



   CPU: 2

    {'id': 2, 'hyperperiod': 113400000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 39077787, 'util': 65.53987037037037}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 2', 'period': 113400.0, 'C(LO)': 7437.0, 'C(HI)': 14874.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 564', 'preemptions': ' 76', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.011430456', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 64.730807150', 'avgresponsejitter': ' 0.003859144', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 641', 'timesonc2': ' 0', 'lockedtime': ' 0.000007456'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 3', 'period': 70875.0, 'C(LO)': 4170.0, 'C(HI)': 8341.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 902', 'preemptions': ' 52', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006584336', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 64.787507201', 'avgresponsejitter': ' 0.002216601', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 13', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 966', 'timesonc2': ' 0', 'lockedtime': ' 0.000005180'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 1', 'period': 129600.0, 'C(LO)': 2378.0, 'C(HI)': 4757.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 494', 'preemptions': ' 11', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003626435', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 64.763206985', 'avgresponsejitter': ' 0.001207480', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 506', 'timesonc2': ' 0', 'lockedtime': ' 0.000003141'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 4', 'period': 42000.0, 'C(LO)': 457.0, 'C(HI)': 915.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1521', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000730718', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 64.798006592', 'avgresponsejitter': ' 0.000233745', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 13', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1533', 'timesonc2': ' 0', 'lockedtime': ' 0.000008219'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 0', 'period': 180000.0, 'C(LO)': 86364.0, 'C(HI)': 86364.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 356', 'preemptions': ' 1405', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.063381985', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 64.721276249', 'avgresponsejitter': ' 0.049103952', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1760', 'timesonc2': ' 0', 'lockedtime': ' 0.000042168'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 6', 'period': 18900.0, 'C(LO)': 1512.0, 'C(HI)': 1512.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1232', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000913081', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 24.247009150', 'avgresponsejitter': ' 0.000760312', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 0', 'timesmigrated': ' 8', 'timesrestored': ' 7', 'timesonc1': ' 1223', 'timesonc2': ' 7', 'lockedtime': ' 0.000005826'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 5', 'period': 40000.0, 'C(LO)': 2557.0, 'C(HI)': 2557.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1597', 'preemptions': ' 41', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002316829', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 64.840006787', 'avgresponsejitter': ' 0.001293649', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 6', 'timesrestored': ' 6', 'timesonc1': ' 1631', 'timesonc2': ' 5', 'lockedtime': ' 0.000023520'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 1', 'period': 200000.0, 'C(LO)': 24837.0, 'C(HI)': 49674.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 321', 'preemptions': ' 282', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.034202099', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 64.802013721', 'avgresponsejitter': ' 0.016928622', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 602', 'lockedtime': ' 0.000025426'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 2', 'priority': ' 0', 'period': 453600.0, 'C(LO)': 14191.0, 'C(HI)': 28382.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 142', 'preemptions': ' 79', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.040082429', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 64.510788489', 'avgresponsejitter': ' 0.010631348', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 220', 'lockedtime': ' 0.000005529'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 4', 'period': 22500.0, 'C(LO)': 6337.0, 'C(HI)': 6337.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 2839', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004115613', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 64.832506066', 'avgresponsejitter': ' 0.003167438', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 2839', 'lockedtime': ' 0.000047988'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 2', 'period': 72000.0, 'C(LO)': 13577.0, 'C(HI)': 13577.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 888', 'preemptions': ' 278', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.017222330', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 64.795711414', 'avgresponsejitter': ' 0.008072817', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1165', 'lockedtime': ' 0.000017649'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 3', 'period': 65625.0, 'C(LO)': 9691.0, 'C(HI)': 9691.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 974', 'preemptions': ' 168', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.009418342', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 64.790598357', 'avgresponsejitter': ' 0.005403565', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1141', 'lockedtime': ' 0.000022589'}


   </details>

  6. Taskset **e1_semi2wf_t150**

    Taskset execution params: {'id': 'e1_semi2wf_t150', 'size': '12', 'utilization': '1.8', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 7', 'period': 22500.0, 'C(LO)': 967.0, 'C(HI)': 967.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 277', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000576742', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.216006279', 'avgresponsejitter': ' 0.000481258', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 0', 'timesonc1': ' 275', 'timesonc2': ' 1', 'lockedtime': ' 0.000002520'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 113400000, 'lowtohigh': ' 3', 'hightolow': ' 2', 'idletime': 3544609, 'util': 96.87424250440917}



   CPU: 2

    {'id': 2, 'hyperperiod': 22680000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 4165042, 'util': 81.63561728395062}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 3', 'period': 50000.0, 'C(LO)': 2633.0, 'C(HI)': 5266.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 126', 'preemptions': ' 7', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002985697', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.200006955', 'avgresponsejitter': ' 0.001369186', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 132', 'timesonc2': ' 0', 'lockedtime': ' 0.000000402'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 4', 'period': 39375.0, 'C(LO)': 1900.0, 'C(HI)': 3800.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 159', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003037904', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.181882099', 'avgresponsejitter': ' 0.000965147', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 160', 'timesonc2': ' 0', 'lockedtime': ' 0.000002006'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 5', 'period': 37800.0, 'C(LO)': 858.0, 'C(HI)': 1716.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 166', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001216688', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.199207000', 'avgresponsejitter': ' 0.000433444', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 167', 'timesonc2': ' 0', 'lockedtime': ' 0.000000844'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 1', 'period': 135000.0, 'C(LO)': 1961.0, 'C(HI)': 3922.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 48', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001791907', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.210007012', 'avgresponsejitter': ' 0.001004883', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 48', 'timesonc2': ' 0', 'lockedtime': ' 0.000000258'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 2', 'period': 72000.0, 'C(LO)': 255.00000000000003, 'C(HI)': 510.00000000000006, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 88', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000383045', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.192006982', 'avgresponsejitter': ' 0.000137318', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 88', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 675000.0, 'C(LO)': 354317.0, 'C(HI)': 354317.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 10', 'preemptions': ' 224', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.240663075', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 6.402640844', 'avgresponsejitter': ' 0.202701129', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 233', 'timesonc2': ' 0', 'lockedtime': ' 0.000007766'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 6', 'period': 162000.0, 'C(LO)': 21254.0, 'C(HI)': 21254.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 40', 'preemptions': ' 13', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.013124862', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.156006916', 'avgresponsejitter': ' 0.010774763', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 1', 'timesrestored': ' 0', 'timesonc1': ' 52', 'timesonc2': ' 0', 'lockedtime': ' 0.000001072'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 7', 'period': 22500.0, 'C(LO)': 967.0, 'C(HI)': 967.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 277', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000576742', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.216006279', 'avgresponsejitter': ' 0.000481258', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 0', 'timesonc1': ' 275', 'timesonc2': ' 1', 'lockedtime': ' 0.000002520'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 0', 'period': 126000.0, 'C(LO)': 21018.0, 'C(HI)': 42037.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 51', 'preemptions': ' 3', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.014898024', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.174222760', 'avgresponsejitter': ' 0.010599658', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 53', 'lockedtime': ' 0.000000219'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 1', 'period': 168000.0, 'C(LO)': 68046.0, 'C(HI)': 68046.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 38', 'preemptions': ' 25', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.043464631', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.048232916', 'avgresponsejitter': ' 0.035665529', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 62', 'lockedtime': ' 0.000003760'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 2', 'period': 78750.0, 'C(LO)': 5673.0, 'C(HI)': 5673.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 80', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003378739', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.142506294', 'avgresponsejitter': ' 0.002849027', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 79', 'lockedtime': ' 0.000003486'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 3', 'period': 63000.0, 'C(LO)': 426.0, 'C(HI)': 426.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 100', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000255234', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.174006970', 'avgresponsejitter': ' 0.000217210', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 99', 'lockedtime': ' 0.000003880'}


   </details>

  7. Taskset **e1_semi2wf_t1581**

    Taskset execution params: {'id': 'e1_semi2wf_t1581', 'size': '12', 'utilization': '1.872', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 5', 'period': 30240.0, 'C(LO)': 2245.0, 'C(HI)': 2245.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 500', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001352003', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.093756865', 'avgresponsejitter': ' 0.001123856', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 4', 'timesrestored': ' 4', 'timesonc1': ' 494', 'timesonc2': ' 5', 'lockedtime': ' 0.000009033'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 56700000, 'lowtohigh': ' 5', 'hightolow': ' 5', 'idletime': 9812745, 'util': 82.69357142857143}



   CPU: 2

    {'id': 2, 'hyperperiod': 18900000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 9698338, 'util': 48.68604232804232}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 2', 'period': 126000.0, 'C(LO)': 14454.0, 'C(HI)': 28909.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 121', 'preemptions': ' 34', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.026440889', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 15.994007880', 'avgresponsejitter': ' 0.007821429', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 155', 'timesonc2': ' 0', 'lockedtime': ' 0.000005339'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 3', 'period': 84375.0, 'C(LO)': 5872.0, 'C(HI)': 11744.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 180', 'preemptions': ' 16', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.014278477', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.018757168', 'avgresponsejitter': ' 0.003117462', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 197', 'timesonc2': ' 0', 'lockedtime': ' 0.000004805'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 1', 'period': 131250.0, 'C(LO)': 8777.0, 'C(HI)': 17555.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 116', 'preemptions': ' 24', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.017298661', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 15.966536766', 'avgresponsejitter': ' 0.004842171', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 141', 'timesonc2': ' 0', 'lockedtime': ' 0.000002721'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 453600.0, 'C(LO)': 106007.0, 'C(HI)': 106007.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 35', 'preemptions': ' 103', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.090582742', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 15.981132408', 'avgresponsejitter': ' 0.066333997', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 137', 'timesonc2': ' 0', 'lockedtime': ' 0.000010679'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 4', 'period': 78750.0, 'C(LO)': 9985.0, 'C(HI)': 9985.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 193', 'preemptions': ' 34', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.007232222', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.041256366', 'avgresponsejitter': ' 0.005185462', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 226', 'timesonc2': ' 0', 'lockedtime': ' 0.000005541'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 5', 'period': 30240.0, 'C(LO)': 2245.0, 'C(HI)': 2245.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 500', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001352003', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.093756865', 'avgresponsejitter': ' 0.001123856', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 4', 'timesrestored': ' 4', 'timesonc1': ' 494', 'timesonc2': ' 5', 'lockedtime': ' 0.000009033'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 3', 'period': 37800.0, 'C(LO)': 7263.0, 'C(HI)': 14527.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 401', 'preemptions': ' 119', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.005401270', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.082206129', 'avgresponsejitter': ' 0.003775850', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 519', 'lockedtime': ' 0.000008444'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 2', 'period': 52500.0, 'C(LO)': 1210.0, 'C(HI)': 2421.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 289', 'preemptions': ' 2', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000859559', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.067506099', 'avgresponsejitter': ' 0.000602883', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 290', 'lockedtime': ' 0.000001294'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 1', 'period': 63000.0, 'C(LO)': 848.0, 'C(HI)': 1696.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 241', 'preemptions': ' 5', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001517318', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.057006144', 'avgresponsejitter': ' 0.000430856', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 245', 'lockedtime': ' 0.000004601'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 196875.0, 'C(LO)': 74903.0, 'C(HI)': 74903.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 78', 'preemptions': ' 410', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.055122408', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 15.964245252', 'avgresponsejitter': ' 0.044650387', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 487', 'lockedtime': ' 0.000014117'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 4', 'period': 22500.0, 'C(LO)': 1912.0, 'C(HI)': 1912.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 672', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001155264', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.075006030', 'avgresponsejitter': ' 0.000956703', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 671', 'lockedtime': ' 0.000011432'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 5', 'period': 20000.0, 'C(LO)': 239.0, 'C(HI)': 239.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 756', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000149483', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.080006207', 'avgresponsejitter': ' 0.000126078', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 755', 'lockedtime': ' 0.000001147'}


   </details>

  8. Taskset **e1_semi2wf_t1733**

    Taskset execution params: {'id': 'e1_semi2wf_t1733', 'size': '12', 'utilization': '1.872', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 8', 'period': 10000.0, 'C(LO)': 576.0, 'C(HI)': 576.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 678', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000347631', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.771059462', 'avgresponsejitter': ' 0.000288952', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 677', 'timesonc2': ' 0', 'lockedtime': ' 0.000005204'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 113400000, 'lowtohigh': ' 3', 'hightolow': ' 3', 'idletime': 4107478, 'util': 96.37788536155203}



   CPU: 2

    {'id': 2, 'hyperperiod': 3780000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 4537598, 'util': -20.042275132275122}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 472500.0, 'C(LO)': 52344.0, 'C(HI)': 104688.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 16', 'preemptions': ' 63', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.055102571', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.618946721', 'avgresponsejitter': ' 0.036024985', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 78', 'timesonc2': ' 0', 'lockedtime': ' 0.000000862'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 5', 'period': 35000.0, 'C(LO)': 2645.0, 'C(HI)': 5291.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 195', 'preemptions': ' 4', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004484006', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.755006838', 'avgresponsejitter': ' 0.001408357', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 199', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 1', 'period': 168750.0, 'C(LO)': 5331.0, 'C(HI)': 10662.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 42', 'preemptions': ' 15', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.017607865', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.753440652', 'avgresponsejitter': ' 0.003241604', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 56', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 2', 'period': 65625.0, 'C(LO)': 641.0, 'C(HI)': 1283.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 105', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000802480', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.768027072', 'avgresponsejitter': ' 0.000335279', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 106', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 4', 'period': 100800.0, 'C(LO)': 21201.0, 'C(HI)': 21201.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 69', 'preemptions': ' 110', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.019183450', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.753607381', 'avgresponsejitter': ' 0.012565565', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 178', 'timesonc2': ' 0', 'lockedtime': ' 0.000002129'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 7', 'period': 45000.0, 'C(LO)': 5525.0, 'C(HI)': 5525.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 152', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003300312', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.750308517', 'avgresponsejitter': ' 0.002712276', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 151', 'timesonc2': ' 0', 'lockedtime': ' 0.000000267'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 6', 'period': 70875.0, 'C(LO)': 5480.0, 'C(HI)': 5480.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 97', 'preemptions': ' 31', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006520354', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.733131063', 'avgresponsejitter': ' 0.002972667', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 127', 'timesonc2': ' 0', 'lockedtime': ' 0.000001048'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 3', 'period': 120000.0, 'C(LO)': 9161.0, 'C(HI)': 9161.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 58', 'preemptions': ' 14', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.015931973', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.721624267', 'avgresponsejitter': ' 0.005255432', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 71', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 8', 'period': 10000.0, 'C(LO)': 576.0, 'C(HI)': 576.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 678', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000347631', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.771059462', 'avgresponsejitter': ' 0.000288952', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 677', 'timesonc2': ' 0', 'lockedtime': ' 0.000005204'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 1', 'period': 151200.0, 'C(LO)': 32506.0, 'C(HI)': 65013.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 46', 'preemptions': ' 7', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.040584709', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.652806787', 'avgresponsejitter': ' 0.019321631', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 52', 'lockedtime': ' 0.000003640'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 180000.0, 'C(LO)': 1927.0, 'C(HI)': 3854.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 39', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001158805', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.685130351', 'avgresponsejitter': ' 0.001010697', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 38', 'lockedtime': ' 0.000000000'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 2', 'period': 90000.0, 'C(LO)': 37858.0, 'C(HI)': 37858.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 76', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.022717514', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.660008414', 'avgresponsejitter': ' 0.019107117', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 76', 'lockedtime': ' 0.000004772'}


   </details>

  9. Taskset **e1_semi2wf_t1772**

    Taskset execution params: {'id': 'e1_semi2wf_t1772', 'size': '12', 'utilization': '1.8840000000000001', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 1', 'period': 135000.0, 'C(LO)': 10.0, 'C(HI)': 20.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000024138', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.027212066', 'avgresponsejitter': ' 0.000024138', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 3', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 4', 'lockedtime': ' 0.000000000'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 113400000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 40, 'util': 99.99996472663139}



   CPU: 2

    {'id': 2, 'hyperperiod': 18900000, 'lowtohigh': ' 2', 'hightolow': ' 1', 'idletime': 83756, 'util': 99.55684656084657}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 945000.0, 'C(LO)': 213140.0, 'C(HI)': 426281.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 7', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.107293664', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.018686838', 'avgresponsejitter': ' 0.107293664', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 8', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 1', 'period': 129600.0, 'C(LO)': 9945.0, 'C(HI)': 19890.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004010360', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.014671946', 'avgresponsejitter': ' 0.004010360', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 2', 'period': 90000.0, 'C(LO)': 3568.0, 'C(HI)': 7136.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 3', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001741270', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.090007090', 'avgresponsejitter': ' 0.001699586', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 7', 'period': 42000.0, 'C(LO)': 4607.0, 'C(HI)': 4607.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 5', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002765835', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.126007252', 'avgresponsejitter': ' 0.002199916', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 4', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 5', 'period': 100000.0, 'C(LO)': 9702.0, 'C(HI)': 9702.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 3', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004615592', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.100006988', 'avgresponsejitter': ' 0.004478105', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 4', 'period': 112500.0, 'C(LO)': 7193.0, 'C(HI)': 7193.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 3', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003261928', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.112507048', 'avgresponsejitter': ' 0.003230330', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 3', 'period': 126000.0, 'C(LO)': 4838.0, 'C(HI)': 4838.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 3', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002211150', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.128780222', 'avgresponsejitter': ' 0.002205306', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 6', 'period': 47250.0, 'C(LO)': 1422.0, 'C(HI)': 1422.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 4', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000845273', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.094506823', 'avgresponsejitter': ' 0.000798706', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 3', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 2', 'period': 108000.0, 'C(LO)': 35926.0, 'C(HI)': 71852.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 3', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.019315559', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.108006646', 'avgresponsejitter': ' 0.018366264', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 2', 'lockedtime': ' 0.000000000'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 150000.0, 'C(LO)': 35.0, 'C(HI)': 70.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000019171', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.027240330', 'avgresponsejitter': ' 0.000019171', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1', 'lockedtime': ' 0.000000000'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 1', 'period': 135000.0, 'C(LO)': 10.0, 'C(HI)': 20.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000024138', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.027212066', 'avgresponsejitter': ' 0.000024138', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 3', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 4', 'lockedtime': ' 0.000000000'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 3', 'period': 87500.0, 'C(LO)': 17065.0, 'C(HI)': 17065.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 3', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.007873435', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.087506754', 'avgresponsejitter': ' 0.007754477', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 2', 'lockedtime': ' 0.000000147'}


   </details>

  10. Taskset **e1_semi2wf_t1886**

    Taskset execution params: {'id': 'e1_semi2wf_t1886', 'size': '12', 'utilization': '1.8840000000000001', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 5', 'period': 18900.0, 'C(LO)': 1755.0, 'C(HI)': 1755.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 4198', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001065949', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 80.326006925', 'avgresponsejitter': ' 0.000881775', 'deadlinesmissed': ' 2', 'budgetexceeded': ' 1', 'timesmigrated': ' 12', 'timesrestored': ' 12', 'timesonc1': ' 4190', 'timesonc2': ' 6', 'lockedtime': ' 0.000078213'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 9450000, 'lowtohigh': ' 49', 'hightolow': ' 49', 'idletime': 49694637, 'util': -425.86917460317466}



   CPU: 2

    {'id': 2, 'hyperperiod': 113400000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 49423704, 'util': 56.41648677248677}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 3', 'period': 26250.0, 'C(LO)': 2178.0, 'C(HI)': 4357.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 3023', 'preemptions': ' 120', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004290697', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 80.301382544', 'avgresponsejitter': ' 0.001149928', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 31', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 3173', 'timesonc2': ' 0', 'lockedtime': ' 0.000014021'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 0', 'period': 175000.0, 'C(LO)': 14334.0, 'C(HI)': 28668.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 455', 'preemptions': ' 349', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.035858853', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 80.285359234', 'avgresponsejitter': ' 0.009811586', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 4', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 807', 'timesonc2': ' 0', 'lockedtime': ' 0.000018105'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 1', 'period': 65625.0, 'C(LO)': 2840.0, 'C(HI)': 5680.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1210', 'preemptions': ' 135', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.015145078', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 80.283777369', 'avgresponsejitter': ' 0.001830045', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 14', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1358', 'timesonc2': ' 0', 'lockedtime': ' 0.000004982'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 2', 'period': 54000.0, 'C(LO)': 20574.0, 'C(HI)': 20574.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1470', 'preemptions': ' 1593', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.017638508', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 80.272006063', 'avgresponsejitter': ' 0.011563691', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 3062', 'timesonc2': ' 0', 'lockedtime': ' 0.000037943'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 5', 'period': 18900.0, 'C(LO)': 1755.0, 'C(HI)': 1755.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 4198', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001065949', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 80.326006925', 'avgresponsejitter': ' 0.000881775', 'deadlinesmissed': ' 2', 'budgetexceeded': ' 1', 'timesmigrated': ' 12', 'timesrestored': ' 12', 'timesonc1': ' 4190', 'timesonc2': ' 6', 'lockedtime': ' 0.000078213'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 4', 'period': 50000.0, 'C(LO)': 2716.0, 'C(HI)': 2716.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1588', 'preemptions': ' 112', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002688108', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 80.300006613', 'avgresponsejitter': ' 0.001427886', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1699', 'timesonc2': ' 0', 'lockedtime': ' 0.000045321'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 4', 'period': 50400.0, 'C(LO)': 4884.0, 'C(HI)': 9769.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1575', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002932489', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 80.279206375', 'avgresponsejitter': ' 0.002453550', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1574', 'lockedtime': ' 0.000030721'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 2', 'priority': ' 0', 'period': 600000.0, 'C(LO)': 42077.0, 'C(HI)': 84155.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 134', 'preemptions': ' 117', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.056591141', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 80.215052880', 'avgresponsejitter': ' 0.028424225', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 250', 'lockedtime': ' 0.000012853'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 1', 'period': 506250.0, 'C(LO)': 10081.0, 'C(HI)': 20162.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 158', 'preemptions': ' 26', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.037393625', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 79.975006372', 'avgresponsejitter': ' 0.005605396', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 183', 'lockedtime': ' 0.000000787'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 3', 'period': 94500.0, 'C(LO)': 50980.0, 'C(HI)': 50980.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 841', 'preemptions': ' 574', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.033918901', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 80.286282036', 'avgresponsejitter': ' 0.026596895', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1414', 'lockedtime': ' 0.000124556'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 2', 'period': 150000.0, 'C(LO)': 3063.0, 'C(HI)': 3063.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 530', 'preemptions': ' 19', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.033571474', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 80.213668751', 'avgresponsejitter': ' 0.001900991', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 548', 'lockedtime': ' 0.000027012'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 5', 'period': 84000.0, 'C(LO)': 466.0, 'C(HI)': 466.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 946', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000280916', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 80.296006886', 'avgresponsejitter': ' 0.000234697', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 945', 'lockedtime': ' 0.000021565'}


   </details>

  11. Taskset **e1_semi2wf_t1904**

    Taskset execution params: {'id': 'e1_semi2wf_t1904', 'size': '12', 'utilization': '1.8840000000000001', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 7', 'period': 20000.0, 'C(LO)': 1010.0, 'C(HI)': 1010.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 662', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000621420', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.230011216', 'avgresponsejitter': ' 0.000511342', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 660', 'timesonc2': ' 1', 'lockedtime': ' 0.000003694'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 18900000, 'lowtohigh': ' 4', 'hightolow': ' 4', 'idletime': 8545295, 'util': 54.78679894179894}



   CPU: 2

    {'id': 2, 'hyperperiod': 11340000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 9144119, 'util': 19.36402998236332}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 2', 'period': 63000.0, 'C(LO)': 8149.999999999999, 'C(HI)': 16301.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 211', 'preemptions': ' 68', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.013767297', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.167006913', 'avgresponsejitter': ' 0.004325931', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 279', 'timesonc2': ' 0', 'lockedtime': ' 0.000000559'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 525000.0, 'C(LO)': 63880.99999999999, 'C(HI)': 127762.99999999999, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 27', 'preemptions': ' 122', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.112134096', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.127055375', 'avgresponsejitter': ' 0.044952003', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 149', 'timesonc2': ' 0', 'lockedtime': ' 0.000003571'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 1', 'period': 84375.0, 'C(LO)': 4892.0, 'C(HI)': 9784.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 158', 'preemptions': ' 39', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.016005961', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.162506982', 'avgresponsejitter': ' 0.003096598', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 198', 'timesonc2': ' 0', 'lockedtime': ' 0.000001754'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 3', 'period': 75600.0, 'C(LO)': 13531.0, 'C(HI)': 13531.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 176', 'preemptions': ' 113', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.010630928', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.154407291', 'avgresponsejitter': ' 0.007342447', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 288', 'timesonc2': ' 0', 'lockedtime': ' 0.000005243'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 6', 'period': 35000.0, 'C(LO)': 2615.0, 'C(HI)': 2615.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 379', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001571183', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.195006622', 'avgresponsejitter': ' 0.001310060', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 378', 'timesonc2': ' 0', 'lockedtime': ' 0.000000559'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 7', 'period': 20000.0, 'C(LO)': 1010.0, 'C(HI)': 1010.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 662', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000621420', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.230011216', 'avgresponsejitter': ' 0.000511342', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 660', 'timesonc2': ' 1', 'lockedtime': ' 0.000003694'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 5', 'period': 45000.0, 'C(LO)': 2091.0, 'C(HI)': 2091.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 295', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001260877', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.185007258', 'avgresponsejitter': ' 0.001051988', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 294', 'timesonc2': ' 0', 'lockedtime': ' 0.000000420'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 4', 'period': 52500.0, 'C(LO)': 1833.0, 'C(HI)': 1833.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 253', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001101829', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.177507114', 'avgresponsejitter': ' 0.000924970', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 252', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 180000.0, 'C(LO)': 30882.0, 'C(HI)': 61765.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 75', 'preemptions': ' 45', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.032104835', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.140006228', 'avgresponsejitter': ' 0.019723784', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 119', 'lockedtime': ' 0.000004492'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 1', 'period': 141750.0, 'C(LO)': 13062.0, 'C(HI)': 26124.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 95', 'preemptions': ' 9', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.015451114', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.183335111', 'avgresponsejitter': ' 0.007264685', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 103', 'lockedtime': ' 0.000001474'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 2', 'period': 101250.0, 'C(LO)': 1566.0, 'C(HI)': 3133.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 132', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.009325396', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.162507556', 'avgresponsejitter': ' 0.000867045', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 132', 'lockedtime': ' 0.000003498'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 3', 'period': 45360.0, 'C(LO)': 14600.0, 'C(HI)': 14600.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 293', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.008792610', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.199766252', 'avgresponsejitter': ' 0.007457093', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 292', 'lockedtime': ' 0.000007703'}


   </details>

  12. Taskset **e1_semi2wf_t1964**

    Taskset execution params: {'id': 'e1_semi2wf_t1964', 'size': '12', 'utilization': '1.8840000000000001', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 4', 'period': 10000.0, 'C(LO)': 1573.0, 'C(HI)': 1573.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1508', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000951111', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.075006634', 'avgresponsejitter': ' 0.000788477', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 2', 'timesonc2': ' 1505', 'lockedtime': ' 0.000023474'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 18900000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 9807303, 'util': 48.10950793650793}



   CPU: 2

    {'id': 2, 'hyperperiod': 11340000, 'lowtohigh': ' 3', 'hightolow': ' 3', 'idletime': 9788988, 'util': 13.6773544973545}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 590625.0, 'C(LO)': 76553.0, 'C(HI)': 153106.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 27', 'preemptions': ' 129', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.075377129', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 15.780679787', 'avgresponsejitter': ' 0.051144423', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 155', 'timesonc2': ' 0', 'lockedtime': ' 0.000012240'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 5', 'period': 15750.0, 'C(LO)': 1118.0, 'C(HI)': 2237.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 959', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000679763', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.072756162', 'avgresponsejitter': ' 0.000568937', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 958', 'timesonc2': ' 0', 'lockedtime': ' 0.000008228'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 3', 'period': 30240.0, 'C(LO)': 1105.0, 'C(HI)': 2211.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 500', 'preemptions': ' 10', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006215517', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.059526171', 'avgresponsejitter': ' 0.000593724', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 509', 'timesonc2': ' 0', 'lockedtime': ' 0.000001165'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 2', 'period': 63000.0, 'C(LO)': 499.0, 'C(HI)': 999.0000000000001, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 241', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002551883', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.059217994', 'avgresponsejitter': ' 0.000255889', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 241', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 1', 'period': 180000.0, 'C(LO)': 38850.0, 'C(HI)': 38850.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 85', 'preemptions': ' 177', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.030763616', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 15.941683832', 'avgresponsejitter': ' 0.021590384', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 261', 'timesonc2': ' 0', 'lockedtime': ' 0.000011279'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 4', 'period': 67500.0, 'C(LO)': 11687.0, 'C(HI)': 11687.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 225', 'preemptions': ' 69', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.007649489', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.053297946', 'avgresponsejitter': ' 0.006077087', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 293', 'timesonc2': ' 0', 'lockedtime': ' 0.000011571'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 6', 'period': 60000.0, 'C(LO)': 3518.0, 'C(HI)': 3518.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 253', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002108961', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.060007679', 'avgresponsejitter': ' 0.001756471', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 252', 'timesonc2': ' 0', 'lockedtime': ' 0.000011892'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 0', 'period': 141750.0, 'C(LO)': 32620.999999999996, 'C(HI)': 65242.99999999999, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 108', 'preemptions': ' 299', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.052541060', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.025506078', 'avgresponsejitter': ' 0.021003156', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 407', 'lockedtime': ' 0.000021441'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 1', 'period': 64800.0, 'C(LO)': 1910.0, 'C(HI)': 3820.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 234', 'preemptions': ' 33', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002567793', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.042771069', 'avgresponsejitter': ' 0.001091706', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 268', 'lockedtime': ' 0.000001141'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 2', 'period': 90000.0, 'C(LO)': 19392.0, 'C(HI)': 19392.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 169', 'preemptions': ' 135', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.012524312', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.031389237', 'avgresponsejitter': ' 0.010398402', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 303', 'lockedtime': ' 0.000004790'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 4', 'period': 10000.0, 'C(LO)': 1573.0, 'C(HI)': 1573.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1508', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000951111', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.075006634', 'avgresponsejitter': ' 0.000788477', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 2', 'timesonc2': ' 1505', 'lockedtime': ' 0.000023474'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 3', 'period': 22500.0, 'C(LO)': 1214.0, 'C(HI)': 1214.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 671', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000732048', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.052507336', 'avgresponsejitter': ' 0.000615574', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 670', 'lockedtime': ' 0.000014330'}


   </details>

  13. Taskset **e1_semi2wf_t2160**

    Taskset execution params: {'id': 'e1_semi2wf_t2160', 'size': '12', 'utilization': '1.8960000000000001', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 5', 'period': 20000.0, 'C(LO)': 17.0, 'C(HI)': 17.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 4', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000013378', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.040007595', 'avgresponsejitter': ' 0.000012267', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 4', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 56700000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 17, 'util': 99.99997001763668}



   CPU: 2

    {'id': 2, 'hyperperiod': 37800000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 31404, 'util': 99.91692063492063}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 2', 'period': 70875.0, 'C(LO)': 12362.0, 'C(HI)': 24724.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006326408', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.009260643', 'avgresponsejitter': ' 0.006326408', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 567000.0, 'C(LO)': 78595.0, 'C(HI)': 157191.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 5', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 5', 'timesonc2': ' 0', 'lockedtime': ' 0.000000489'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 1', 'period': 450000.0, 'C(LO)': 27767.0, 'C(HI)': 55534.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 3', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.014290420', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.015591129', 'avgresponsejitter': ' 0.014290420', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 4', 'timesonc2': ' 0', 'lockedtime': ' 0.000000282'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 3', 'period': 113400.0, 'C(LO)': 15441.0, 'C(HI)': 15441.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.008693700', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.000562210', 'avgresponsejitter': ' 0.008693700', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 6', 'period': 15750.0, 'C(LO)': 437.0, 'C(HI)': 437.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 5', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000224832', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.047256940', 'avgresponsejitter': ' 0.000202111', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 4', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 4', 'period': 22500.0, 'C(LO)': 543.0, 'C(HI)': 543.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 4', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000320126', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.045007048', 'avgresponsejitter': ' 0.000297063', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 3', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 5', 'period': 20000.0, 'C(LO)': 17.0, 'C(HI)': 17.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 4', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000013378', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.040007595', 'avgresponsejitter': ' 0.000012267', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 4', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 2', 'period': 67500.0, 'C(LO)': 13465.0, 'C(HI)': 26931.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.007192285', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.003937577', 'avgresponsejitter': ' 0.007192285', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 2', 'lockedtime': ' 0.000000000'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 0', 'period': 168000.0, 'C(LO)': 22173.0, 'C(HI)': 44346.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.011126889', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.013189973', 'avgresponsejitter': ' 0.011126889', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 2', 'lockedtime': ' 0.000000000'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 1', 'period': 72000.0, 'C(LO)': 3553.0, 'C(HI)': 7107.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002051823', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.011134033', 'avgresponsejitter': ' 0.002051823', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1', 'lockedtime': ' 0.000000000'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 3', 'period': 50000.0, 'C(LO)': 6155.0, 'C(HI)': 6155.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 3', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003587940', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.050321411', 'avgresponsejitter': ' 0.003451360', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 2', 'lockedtime': ' 0.000000000'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 4', 'period': 10000.0, 'C(LO)': 727.0, 'C(HI)': 727.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 7', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000428745', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.050006892', 'avgresponsejitter': ' 0.000354327', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 7', 'lockedtime': ' 0.000000928'}


   </details>

  14. Taskset **e1_semi2wf_t2216**

    Taskset execution params: {'id': 'e1_semi2wf_t2216', 'size': '12', 'utilization': '1.8960000000000001', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 6', 'period': 26250.0, 'C(LO)': 909.0, 'C(HI)': 909.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 15', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000527471', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.378007832', 'avgresponsejitter': ' 0.000441432', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 10', 'timesonc2': ' 4', 'lockedtime': ' 0.000000453'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 113400000, 'lowtohigh': ' 1', 'hightolow': ' 1', 'idletime': 50616, 'util': 99.95536507936508}



   CPU: 2

    {'id': 2, 'hyperperiod': 1890000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 252005, 'util': 86.66640211640211}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 945000.0, 'C(LO)': 148553.0, 'C(HI)': 297106.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 10', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.274207495', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.053195871', 'avgresponsejitter': ' 0.274207495', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 12', 'timesonc2': ' 0', 'lockedtime': ' 0.000003126'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 3', 'period': 126000.0, 'C(LO)': 13751.0, 'C(HI)': 27503.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 4', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.007974399', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.252008877', 'avgresponsejitter': ' 0.007084483', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 4', 'timesonc2': ' 0', 'lockedtime': ' 0.000000276'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 1', 'period': 810000.0, 'C(LO)': 49035.0, 'C(HI)': 98070.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 2', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.027285237', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.025906240', 'avgresponsejitter': ' 0.027285237', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 3', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 2', 'period': 200000.0, 'C(LO)': 100.0, 'C(HI)': 201.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 3', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000058348', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.200007396', 'avgresponsejitter': ' 0.000051568', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 4', 'period': 141750.0, 'C(LO)': 28728.0, 'C(HI)': 28728.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 4', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.015529195', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.283507775', 'avgresponsejitter': ' 0.014241628', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 3', 'timesonc2': ' 0', 'lockedtime': ' 0.000000387'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 5', 'period': 105000.0, 'C(LO)': 4657.0, 'C(HI)': 4657.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 5', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002565511', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.315511063', 'avgresponsejitter': ' 0.002442237', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 3', 'timesonc2': ' 1', 'lockedtime': ' 0.000000000'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 6', 'period': 26250.0, 'C(LO)': 909.0, 'C(HI)': 909.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 15', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000527471', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.378007832', 'avgresponsejitter': ' 0.000441432', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 10', 'timesonc2': ' 4', 'lockedtime': ' 0.000000453'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 1', 'period': 42000.0, 'C(LO)': 11701.0, 'C(HI)': 23403.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 10', 'preemptions': ' 4', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.009081438', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.336005925', 'avgresponsejitter': ' 0.006588018', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 13', 'lockedtime': ' 0.000000000'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 0', 'period': 157500.0, 'C(LO)': 8212.0, 'C(HI)': 16424.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 4', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004366456', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.317818892', 'avgresponsejitter': ' 0.003868330', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 3', 'lockedtime': ' 0.000000000'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 3', 'period': 33750.0, 'C(LO)': 5570.0, 'C(HI)': 5570.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 13', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003333763', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.371256342', 'avgresponsejitter': ' 0.002676946', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 12', 'lockedtime': ' 0.000000000'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 2', 'period': 47250.0, 'C(LO)': 5072.0, 'C(HI)': 5072.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 9', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003038390', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.330756039', 'avgresponsejitter': ' 0.002617817', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 9', 'lockedtime': ' 0.000000000'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 4', 'period': 25200.0, 'C(LO)': 646.0, 'C(HI)': 646.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 17', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000375838', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.378008279', 'avgresponsejitter': ' 0.000322688', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 16', 'lockedtime': ' 0.000000405'}


   </details>

  15. Taskset **e1_semi2wf_t2330**

    Taskset execution params: {'id': 'e1_semi2wf_t2330', 'size': '12', 'utilization': '1.9080000000000001', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 5', 'period': 20000.0, 'C(LO)': 28.0, 'C(HI)': 28.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000411'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 7560000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 16, 'util': 99.99978835978835}



   CPU: 2

    {'id': 2, 'hyperperiod': 5670000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 14, 'util': 99.99975308641976}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 2', 'period': 15750.0, 'C(LO)': 3109.0, 'C(HI)': 6219.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 1', 'period': 18900.0, 'C(LO)': 2901.0, 'C(HI)': 5803.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 0', 'period': 168000.0, 'C(LO)': 37487.0, 'C(HI)': 37487.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 3', 'period': 72000.0, 'C(LO)': 1543.0, 'C(HI)': 1543.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 4', 'period': 40000.0, 'C(LO)': 799.0, 'C(HI)': 799.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 5', 'period': 20000.0, 'C(LO)': 28.0, 'C(HI)': 28.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000411'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 3', 'period': 37800.0, 'C(LO)': 8257.0, 'C(HI)': 16514.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 1', 'period': 81000.0, 'C(LO)': 3906.0, 'C(HI)': 7812.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 2', 'period': 47250.0, 'C(LO)': 1981.0000000000002, 'C(HI)': 3963.0000000000005, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 2', 'priority': ' 0', 'period': 405000.0, 'C(LO)': 5100.0, 'C(HI)': 10200.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 4', 'period': 54000.0, 'C(LO)': 12390.0, 'C(HI)': 12390.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 5', 'period': 25200.0, 'C(LO)': 1717.0, 'C(HI)': 1717.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1', 'lockedtime': ' 0.000000000'}


   </details>

  16. Taskset **e1_semi2wf_t2347**

    Taskset execution params: {'id': 'e1_semi2wf_t2347', 'size': '12', 'utilization': '1.9080000000000001', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 6', 'period': 28350.0, 'C(LO)': 1.0, 'C(HI)': 1.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 56700000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 17, 'util': 99.99997001763668}



   CPU: 2

    {'id': 2, 'hyperperiod': 7560000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 13, 'util': 99.99982804232805}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 3', 'period': 37800.0, 'C(LO)': 3022.0, 'C(HI)': 6045.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 756000.0, 'C(LO)': 52418.0, 'C(HI)': 104837.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 1', 'period': 196875.0, 'C(LO)': 7269.0, 'C(HI)': 14539.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 4', 'period': 30240.0, 'C(LO)': 1054.0, 'C(HI)': 2108.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 2', 'period': 157500.0, 'C(LO)': 70871.0, 'C(HI)': 70871.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 5', 'period': 54000.0, 'C(LO)': 2687.0, 'C(HI)': 2687.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 6', 'period': 28350.0, 'C(LO)': 1.0, 'C(HI)': 1.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 1', 'period': 94500.0, 'C(LO)': 20583.0, 'C(HI)': 41166.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 504000.0, 'C(LO)': 11747.0, 'C(HI)': 23494.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 2', 'period': 63000.0, 'C(LO)': 11307.0, 'C(HI)': 11307.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 3', 'period': 60000.0, 'C(LO)': 9601.0, 'C(HI)': 9601.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 4', 'period': 25200.0, 'C(LO)': 3636.0, 'C(HI)': 3636.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1', 'lockedtime': ' 0.000000000'}


   </details>

  17. Taskset **e1_semi2wf_t2367**

    Taskset execution params: {'id': 'e1_semi2wf_t2367', 'size': '12', 'utilization': '1.9080000000000001', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 6', 'period': 30240.0, 'C(LO)': 1094.0, 'C(HI)': 1094.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 3', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000570051', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.112512685', 'avgresponsejitter': ' 0.000550730', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 113400000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 48482, 'util': 99.95724691358025}



   CPU: 2

    {'id': 2, 'hyperperiod': 56700000, 'lowtohigh': ' 2', 'hightolow': ' 2', 'idletime': 35148, 'util': 99.93801058201058}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 1', 'period': 180000.0, 'C(LO)': 21333.0, 'C(HI)': 42667.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.011855330', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.014444105', 'avgresponsejitter': ' 0.011855330', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 4', 'period': 28350.0, 'C(LO)': 2171.0, 'C(HI)': 4342.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000895511', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.010330589', 'avgresponsejitter': ' 0.000895511', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 2', 'period': 112500.0, 'C(LO)': 2413.0, 'C(HI)': 4827.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001371228', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.013068517', 'avgresponsejitter': ' 0.001371228', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 5', 'period': 63000.0, 'C(LO)': 22224.0, 'C(HI)': 22224.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.009762045', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.000563622', 'avgresponsejitter': ' 0.009762045', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 630000.0, 'C(LO)': 72861.0, 'C(HI)': 72861.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.037731874', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.026303940', 'avgresponsejitter': ' 0.037731874', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 6', 'period': 30240.0, 'C(LO)': 1094.0, 'C(HI)': 1094.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 3', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000570051', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.112512685', 'avgresponsejitter': ' 0.000550730', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 3', 'period': 200000.0, 'C(LO)': 3894.0, 'C(HI)': 3894.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001833087', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.011230772', 'avgresponsejitter': ' 0.001833087', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 2', 'period': 100000.0, 'C(LO)': 15478.0, 'C(HI)': 30957.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 3', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.009047691', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.100005865', 'avgresponsejitter': ' 0.008273676', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 3', 'lockedtime': ' 0.000000000'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 1', 'period': 151200.0, 'C(LO)': 6778.0, 'C(HI)': 13556.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003951051', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.028887036', 'avgresponsejitter': ' 0.003951051', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1', 'lockedtime': ' 0.000000000'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 4', 'period': 35000.0, 'C(LO)': 15.0, 'C(HI)': 31.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 5', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000038231', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.105006937', 'avgresponsejitter': ' 0.000026039', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 6', 'lockedtime': ' 0.000000000'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 3', 'period': 108000.0, 'C(LO)': 41040.0, 'C(HI)': 41040.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.019770868', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.000059135', 'avgresponsejitter': ' 0.019770868', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 2', 'lockedtime': ' 0.000000000'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 405000.0, 'C(LO)': 69116.0, 'C(HI)': 69116.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.033260919', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.032842471', 'avgresponsejitter': ' 0.033260919', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 2', 'lockedtime': ' 0.000000000'}


   </details>

  18. Taskset **e1_semi2wf_t2470**

    Taskset execution params: {'id': 'e1_semi2wf_t2470', 'size': '12', 'utilization': '1.9080000000000001', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 5', 'period': 35000.0, 'C(LO)': 5852.0, 'C(HI)': 5852.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 101', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003507811', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.510006360', 'avgresponsejitter': ' 0.002890219', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 1', 'timesonc2': ' 99', 'lockedtime': ' 0.000001643'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 12600000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 2263281, 'util': 82.03745238095237}



   CPU: 2

    {'id': 2, 'hyperperiod': 113400000, 'lowtohigh': ' 3', 'hightolow': ' 3', 'idletime': 2327123, 'util': 97.94786331569665}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 4', 'period': 42000.0, 'C(LO)': 5447.0, 'C(HI)': 10894.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 85', 'preemptions': ' 4', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003851607', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.486006180', 'avgresponsejitter': ' 0.002754420', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 88', 'timesonc2': ' 0', 'lockedtime': ' 0.000001571'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 787500.0, 'C(LO)': 69289.0, 'C(HI)': 138579.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 6', 'preemptions': ' 15', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.073553829', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.156874667', 'avgresponsejitter': ' 0.043575910', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 20', 'timesonc2': ' 0', 'lockedtime': ' 0.000000505'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 1', 'period': 175000.0, 'C(LO)': 7485.0, 'C(HI)': 14970.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 22', 'preemptions': ' 3', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004980231', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.500006072', 'avgresponsejitter': ' 0.003859847', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 24', 'timesonc2': ' 0', 'lockedtime': ' 0.000000565'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 3', 'period': 50400.0, 'C(LO)': 1855.0, 'C(HI)': 3710.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 71', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001907592', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.477606249', 'avgresponsejitter': ' 0.000946919', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 71', 'timesonc2': ' 0', 'lockedtime': ' 0.000000231'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 2', 'period': 168000.0, 'C(LO)': 55589.0, 'C(HI)': 55589.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 22', 'preemptions': ' 24', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.034340649', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.363032234', 'avgresponsejitter': ' 0.029416057', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 45', 'timesonc2': ' 0', 'lockedtime': ' 0.000002643'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 5', 'period': 40000.0, 'C(LO)': 1483.0, 'C(HI)': 1483.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 89', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000890060', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.480006081', 'avgresponsejitter': ' 0.000756964', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 88', 'timesonc2': ' 0', 'lockedtime': ' 0.000001333'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 0', 'period': 135000.0, 'C(LO)': 39868.0, 'C(HI)': 79736.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 27', 'preemptions': ' 37', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.072009859', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.376410483', 'avgresponsejitter': ' 0.025204997', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 64', 'lockedtime': ' 0.000002237'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 1', 'period': 90720.0, 'C(LO)': 139.0, 'C(HI)': 279.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 40', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003507502', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.447366982', 'avgresponsejitter': ' 0.000167670', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 42', 'lockedtime': ' 0.000000000'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 5', 'period': 35000.0, 'C(LO)': 5852.0, 'C(HI)': 5852.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 101', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003507811', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.510006360', 'avgresponsejitter': ' 0.002890219', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 1', 'timesonc2': ' 99', 'lockedtime': ' 0.000001643'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 4', 'period': 72000.0, 'C(LO)': 7095.0, 'C(HI)': 7095.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 50', 'preemptions': ' 3', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006764967', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.456006183', 'avgresponsejitter': ' 0.003773709', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 52', 'lockedtime': ' 0.000001574'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 2', 'period': 113400.0, 'C(LO)': 6535.0, 'C(HI)': 6535.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 32', 'preemptions': ' 3', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.008579369', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.402007267', 'avgresponsejitter': ' 0.003642351', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 34', 'lockedtime': ' 0.000001027'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 3', 'period': 84375.0, 'C(LO)': 2394.0, 'C(HI)': 2394.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 43', 'preemptions': ' 3', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.007924865', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.459381057', 'avgresponsejitter': ' 0.001511003', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 45', 'lockedtime': ' 0.000000000'}


   </details>

  19. Taskset **e1_semi2wf_t2562**

    Taskset execution params: {'id': 'e1_semi2wf_t2562', 'size': '12', 'utilization': '1.9200000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 5', 'period': 25200.0, 'C(LO)': 1262.0, 'C(HI)': 1262.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 980', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000762604', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 25.700007856', 'avgresponsejitter': ' 0.000639688', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 978', 'timesonc2': ' 1', 'lockedtime': ' 0.000024661'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 37800000, 'lowtohigh': ' 1', 'hightolow': ' 1', 'idletime': 16436458, 'util': 56.517306878306876}



   CPU: 2

    {'id': 2, 'hyperperiod': 7560000, 'lowtohigh': ' 5', 'hightolow': ' 5', 'idletime': 16374352, 'util': -116.59195767195766}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 2', 'period': 100000.0, 'C(LO)': 19221.0, 'C(HI)': 38442.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 248', 'preemptions': ' 122', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.028187126', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 25.600837054', 'avgresponsejitter': ' 0.009978616', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 370', 'timesonc2': ' 0', 'lockedtime': ' 0.000010991'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 1', 'period': 200000.0, 'C(LO)': 26398.0, 'C(HI)': 52797.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 125', 'preemptions': ' 86', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.016561453', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 25.629031619', 'avgresponsejitter': ' 0.013511712', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 210', 'timesonc2': ' 0', 'lockedtime': ' 0.000007090'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 900000.0, 'C(LO)': 207673.0, 'C(HI)': 207673.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 29', 'preemptions': ' 268', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.157917075', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 25.308203405', 'avgresponsejitter': ' 0.129034225', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 296', 'timesonc2': ' 0', 'lockedtime': ' 0.000023321'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 5', 'period': 25200.0, 'C(LO)': 1262.0, 'C(HI)': 1262.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 980', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000762604', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 25.700007856', 'avgresponsejitter': ' 0.000639688', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 978', 'timesonc2': ' 1', 'lockedtime': ' 0.000024661'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 4', 'period': 40000.0, 'C(LO)': 1913.0, 'C(HI)': 1913.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 618', 'preemptions': ' 20', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001817219', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 25.640006393', 'avgresponsejitter': ' 0.000986444', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 636', 'timesonc2': ' 1', 'lockedtime': ' 0.000010718'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 3', 'period': 84375.0, 'C(LO)': 73.0, 'C(HI)': 73.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 294', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000051429', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 25.637507898', 'avgresponsejitter': ' 0.000042781', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 293', 'timesonc2': ' 0', 'lockedtime': ' 0.000000703'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 1', 'period': 140000.0, 'C(LO)': 36374.0, 'C(HI)': 72749.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 178', 'preemptions': ' 345', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.032970637', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 25.640940910', 'avgresponsejitter': ' 0.020888811', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 522', 'lockedtime': ' 0.000020486'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 504000.0, 'C(LO)': 3709.0, 'C(HI)': 7419.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 51', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.005702213', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 25.696805366', 'avgresponsejitter': ' 0.001970303', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 52', 'lockedtime': ' 0.000000000'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 2', 'period': 75600.0, 'C(LO)': 454.0, 'C(HI)': 908.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 328', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000641204', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 25.645607685', 'avgresponsejitter': ' 0.000233177', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 329', 'lockedtime': ' 0.000020057'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 3', 'period': 54000.0, 'C(LO)': 214.0, 'C(HI)': 429.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 459', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000275459', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 25.678005853', 'avgresponsejitter': ' 0.000110529', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 460', 'lockedtime': ' 0.000002114'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 4', 'period': 60000.0, 'C(LO)': 17178.0, 'C(HI)': 17178.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 413', 'preemptions': ' 214', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.011263502', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 25.660006667', 'avgresponsejitter': ' 0.009031979', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 626', 'lockedtime': ' 0.000030153'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 5', 'period': 15750.0, 'C(LO)': 1597.0, 'C(HI)': 1597.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1570', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000966399', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 25.696007099', 'avgresponsejitter': ' 0.000803748', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1569', 'lockedtime': ' 0.000017255'}


   </details>

  20. Taskset **e1_semi2wf_t2574**

    Taskset execution params: {'id': 'e1_semi2wf_t2574', 'size': '12', 'utilization': '1.9200000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 4', 'period': 42000.0, 'C(LO)': 14.0, 'C(HI)': 28.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 41', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000036222', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.638006303', 'avgresponsejitter': ' 0.000018661', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 18', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 58', 'timesonc2': ' 0', 'lockedtime': ' 0.000000459'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 18900000, 'lowtohigh': ' 21', 'hightolow': ' 20', 'idletime': 1078317, 'util': 94.29461904761905}



   CPU: 2

    {'id': 2, 'hyperperiod': 28350000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 1020188, 'util': 96.40145326278659}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 0', 'period': 420000.0, 'C(LO)': 49529.0, 'C(HI)': 99059.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 5', 'preemptions': ' 5', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.028951450', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.267294682', 'avgresponsejitter': ' 0.026121919', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 9', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 2', 'period': 131250.0, 'C(LO)': 7508.0, 'C(HI)': 15016.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 14', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.009743619', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.614031435', 'avgresponsejitter': ' 0.003942679', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 15', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 5', 'period': 22500.0, 'C(LO)': 285.0, 'C(HI)': 570.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 76', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000465240', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.665006264', 'avgresponsejitter': ' 0.000160366', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 3', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 78', 'timesonc2': ' 0', 'lockedtime': ' 0.000000709'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 4', 'period': 42000.0, 'C(LO)': 14.0, 'C(HI)': 28.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 41', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000036222', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.638006303', 'avgresponsejitter': ' 0.000018661', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 18', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 58', 'timesonc2': ' 0', 'lockedtime': ' 0.000000459'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 1', 'period': 157500.0, 'C(LO)': 35.0, 'C(HI)': 70.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 12', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000025060', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.617897784', 'avgresponsejitter': ' 0.000020033', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 11', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 3', 'period': 175000.0, 'C(LO)': 92686.0, 'C(HI)': 92686.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 11', 'preemptions': ' 27', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.052676036', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.575151523', 'avgresponsejitter': ' 0.042920000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 37', 'timesonc2': ' 0', 'lockedtime': ' 0.000002159'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 6', 'period': 37800.0, 'C(LO)': 1914.0, 'C(HI)': 1914.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001062108', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.000018219', 'avgresponsejitter': ' 0.001062108', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 1', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 3', 'period': 28350.0, 'C(LO)': 5517.0, 'C(HI)': 11035.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 61', 'preemptions': ' 4', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004834438', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.672656252', 'avgresponsejitter': ' 0.002921276', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 64', 'lockedtime': ' 0.000000682'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 2', 'period': 54000.0, 'C(LO)': 23236.0, 'C(HI)': 23236.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 32', 'preemptions': ' 18', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.017354096', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.620006036', 'avgresponsejitter': ' 0.012828432', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 49', 'lockedtime': ' 0.000002168'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 2', 'priority': ' 0', 'period': 945000.0, 'C(LO)': 71776.0, 'C(HI)': 71776.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 3', 'preemptions': ' 7', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.059540598', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.945006204', 'avgresponsejitter': ' 0.041793589', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 9', 'lockedtime': ' 0.000000000'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 4', 'period': 50000.0, 'C(LO)': 2948.0, 'C(HI)': 2948.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 35', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001722318', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.650005874', 'avgresponsejitter': ' 0.001433207', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 34', 'lockedtime': ' 0.000000781'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 1', 'period': 56250.0, 'C(LO)': 475.0, 'C(HI)': 475.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 31', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000285748', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.631255820', 'avgresponsejitter': ' 0.000231483', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 30', 'lockedtime': ' 0.000000664'}


   </details>

  21. Taskset **e1_semi2wf_t2739**

    Taskset execution params: {'id': 'e1_semi2wf_t2739', 'size': '12', 'utilization': '1.9200000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 3', 'period': 26250.0, 'C(LO)': 1731.0, 'C(HI)': 1731.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 615', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001041877', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 17.128006676', 'avgresponsejitter': ' 0.000869613', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 4', 'timesonc2': ' 610', 'lockedtime': ' 0.000013829'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 113400000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 9499238, 'util': 91.62324691358025}



   CPU: 2

    {'id': 2, 'hyperperiod': 113400000, 'lowtohigh': ' 1', 'hightolow': ' 1', 'idletime': 10254683, 'util': 90.957069664903}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 0', 'period': 200000.0, 'C(LO)': 11263.0, 'C(HI)': 22526.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 82', 'preemptions': ' 25', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.055522336', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 17.003608450', 'avgresponsejitter': ' 0.006895288', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 106', 'timesonc2': ' 0', 'lockedtime': ' 0.000000880'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 6', 'period': 10000.0, 'C(LO)': 180.0, 'C(HI)': 361.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1614', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000111943', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 17.120008871', 'avgresponsejitter': ' 0.000094601', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1613', 'timesonc2': ' 0', 'lockedtime': ' 0.000003369'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 4', 'period': 40000.0, 'C(LO)': 614.0, 'C(HI)': 1228.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 405', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000369658', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 17.120126661', 'avgresponsejitter': ' 0.000308063', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 404', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 1', 'period': 131250.0, 'C(LO)': 443.0, 'C(HI)': 887.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 124', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000270697', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 17.013373517', 'avgresponsejitter': ' 0.000224949', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 123', 'timesonc2': ' 0', 'lockedtime': ' 0.000003177'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 5', 'period': 20000.0, 'C(LO)': 19.0, 'C(HI)': 39.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 808', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000017474', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 17.120103805', 'avgresponsejitter': ' 0.000012429', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 807', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 3', 'period': 140000.0, 'C(LO)': 69798.0, 'C(HI)': 69798.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 116', 'preemptions': ' 352', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.043163261', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.961044553', 'avgresponsejitter': ' 0.034943928', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 467', 'timesonc2': ' 0', 'lockedtime': ' 0.000008222'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 2', 'period': 141750.0, 'C(LO)': 31348.0, 'C(HI)': 31348.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 115', 'preemptions': ' 184', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.058601970', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 17.017755994', 'avgresponsejitter': ' 0.018962769', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 298', 'timesonc2': ' 0', 'lockedtime': ' 0.000004556'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 7', 'period': 120000.0, 'C(LO)': 1018.0, 'C(HI)': 1018.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 136', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000610655', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 17.080009300', 'avgresponsejitter': ' 0.000511703', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 135', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 1', 'period': 100800.0, 'C(LO)': 28758.0, 'C(HI)': 57517.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 161', 'preemptions': ' 97', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.053964775', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 17.027206877', 'avgresponsejitter': ' 0.015617363', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 258', 'lockedtime': ' 0.000006192'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 2', 'priority': ' 0', 'period': 590625.0, 'C(LO)': 163472.0, 'C(HI)': 163472.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 29', 'preemptions': ' 123', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.131611688', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 16.980377907', 'avgresponsejitter': ' 0.100022757', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 151', 'lockedtime': ' 0.000004796'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 2', 'period': 129600.0, 'C(LO)': 11698.0, 'C(HI)': 11698.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 126', 'preemptions': ' 26', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.008003204', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 17.070406880', 'avgresponsejitter': ' 0.005992075', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 151', 'lockedtime': ' 0.000001703'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 3', 'period': 26250.0, 'C(LO)': 1731.0, 'C(HI)': 1731.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 615', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001041877', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 17.128006676', 'avgresponsejitter': ' 0.000869613', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 4', 'timesonc2': ' 610', 'lockedtime': ' 0.000013829'}


   </details>

  22. Taskset **e1_semi2wf_t2831**

    Taskset execution params: {'id': 'e1_semi2wf_t2831', 'size': '12', 'utilization': '1.9320000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 1', 'period': 168750.0, 'C(LO)': 2.0, 'C(HI)': 5.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 113400000, 'lowtohigh': ' 1', 'hightolow': ' 0', 'idletime': 16, 'util': 99.99998589065255}



   CPU: 2

    {'id': 2, 'hyperperiod': 113400000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 14, 'util': 99.99998765432099}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 2', 'period': 60480.0, 'C(LO)': 13915.0, 'C(HI)': 27830.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006898195', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.004674132', 'avgresponsejitter': ' 0.006898195', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 700000.0, 'C(LO)': 49400.0, 'C(HI)': 98801.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 1', 'period': 168750.0, 'C(LO)': 2.0, 'C(HI)': 5.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 5', 'period': 33750.0, 'C(LO)': 9935.0, 'C(HI)': 9935.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004077387', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.000017240', 'avgresponsejitter': ' 0.004077387', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000240'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 3', 'period': 70875.0, 'C(LO)': 894.0, 'C(HI)': 894.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000380192', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.004289610', 'avgresponsejitter': ' 0.000380192', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 4', 'period': 39375.0, 'C(LO)': 331.0, 'C(HI)': 331.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000184538', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.004100601', 'avgresponsejitter': ' 0.000184538', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 648000.0, 'C(LO)': 155087.0, 'C(HI)': 310175.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 2', 'period': 84000.0, 'C(LO)': 3552.0, 'C(HI)': 7104.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 1', 'period': 131250.0, 'C(LO)': 4333.0, 'C(HI)': 8666.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 5', 'period': 67500.0, 'C(LO)': 10653.0, 'C(HI)': 10653.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004818300', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.000015471', 'avgresponsejitter': ' 0.004818300', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1', 'lockedtime': ' 0.000000000'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 3', 'period': 180000.0, 'C(LO)': 21868.0, 'C(HI)': 21868.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 4', 'period': 175000.0, 'C(LO)': 18659.0, 'C(HI)': 18659.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1', 'lockedtime': ' 0.000000000'}


   </details>

  23. Taskset **e1_semi2wf_t2840**

    Taskset execution params: {'id': 'e1_semi2wf_t2840', 'size': '12', 'utilization': '1.9320000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 4', 'period': 10000.0, 'C(LO)': 2067.0, 'C(HI)': 2067.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1390', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001245940', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.892523532', 'avgresponsejitter': ' 0.001031562', 'deadlinesmissed': ' 2', 'budgetexceeded': ' 1', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 3', 'timesonc2': ' 1385', 'lockedtime': ' 0.000017408'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 113400000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 9068115, 'util': 92.00342592592592}



   CPU: 2

    {'id': 2, 'hyperperiod': 3780000, 'lowtohigh': ' 2', 'hightolow': ' 2', 'idletime': 9093857, 'util': -140.57822751322752}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 3', 'period': 100800.0, 'C(LO)': 16401.0, 'C(HI)': 32803.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 139', 'preemptions': ' 62', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.024102574', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.809606087', 'avgresponsejitter': ' 0.009881417', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 200', 'timesonc2': ' 0', 'lockedtime': ' 0.000010111'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 1', 'period': 504000.0, 'C(LO)': 50588.0, 'C(HI)': 101177.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 29', 'preemptions': ' 43', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.042906709', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.627414640', 'avgresponsejitter': ' 0.029737162', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 71', 'timesonc2': ' 0', 'lockedtime': ' 0.000005529'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 525000.0, 'C(LO)': 11934.0, 'C(HI)': 23869.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 28', 'preemptions': ' 10', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.017385450', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.655754763', 'avgresponsejitter': ' 0.007580529', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 37', 'timesonc2': ' 0', 'lockedtime': ' 0.000002276'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 2', 'period': 129600.0, 'C(LO)': 61.0, 'C(HI)': 123.00000000000001, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 109', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000043568', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.867206087', 'avgresponsejitter': ' 0.000033880', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 108', 'timesonc2': ' 0', 'lockedtime': ' 0.000000234'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 5', 'period': 70875.0, 'C(LO)': 20595.0, 'C(HI)': 20595.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 197', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.012376063', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.820631378', 'avgresponsejitter': ' 0.010551441', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 196', 'timesonc2': ' 0', 'lockedtime': ' 0.000010183'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 4', 'period': 90000.0, 'C(LO)': 7552.0, 'C(HI)': 7552.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 156', 'preemptions': ' 31', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.016205465', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.860006381', 'avgresponsejitter': ' 0.004283354', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 186', 'timesonc2': ' 0', 'lockedtime': ' 0.000008505'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 6', 'period': 28350.0, 'C(LO)': 629.0, 'C(HI)': 629.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 491', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000376673', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.863157006', 'avgresponsejitter': ' 0.000317387', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 490', 'timesonc2': ' 0', 'lockedtime': ' 0.000010889'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 0', 'period': 189000.0, 'C(LO)': 52744.0, 'C(HI)': 105489.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 75', 'preemptions': ' 329', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.097194550', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.797124087', 'avgresponsejitter': ' 0.033957159', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 405', 'lockedtime': ' 0.000011721'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 1', 'period': 157500.0, 'C(LO)': 2075.0, 'C(HI)': 4150.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 90', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001226868', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.865405532', 'avgresponsejitter': ' 0.001054069', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 89', 'lockedtime': ' 0.000000300'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 4', 'period': 10000.0, 'C(LO)': 2067.0, 'C(HI)': 2067.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1390', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001245940', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.892523532', 'avgresponsejitter': ' 0.001031562', 'deadlinesmissed': ' 2', 'budgetexceeded': ' 1', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 3', 'timesonc2': ' 1385', 'lockedtime': ' 0.000017408'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 2', 'period': 60000.0, 'C(LO)': 9524.0, 'C(HI)': 9524.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 233', 'preemptions': ' 59', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.005849859', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.861169973', 'avgresponsejitter': ' 0.004739853', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 291', 'lockedtime': ' 0.000004862'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 3', 'period': 18900.0, 'C(LO)': 240.0, 'C(HI)': 240.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 737', 'preemptions': ' 7', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001279021', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 14.891507321', 'avgresponsejitter': ' 0.000134616', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 743', 'lockedtime': ' 0.000018414'}


   </details>

  24. Taskset **e1_semi2wf_t2849**

    Taskset execution params: {'id': 'e1_semi2wf_t2849', 'size': '12', 'utilization': '1.9320000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 2', 'period': 15750.0, 'C(LO)': 1164.0, 'C(HI)': 1164.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 51', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000693571', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.787508141', 'avgresponsejitter': ' 0.000579796', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 1', 'timesonc2': ' 49', 'lockedtime': ' 0.000001459'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 113400000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 455824, 'util': 99.59803880070547}



   CPU: 2

    {'id': 2, 'hyperperiod': 12600000, 'lowtohigh': ' 1', 'hightolow': ' 1', 'idletime': 540540, 'util': 95.71}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 5', 'period': 26250.0, 'C(LO)': 1796.0, 'C(HI)': 3593.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 31', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001071700', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.761256691', 'avgresponsejitter': ' 0.000888832', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 30', 'timesonc2': ' 0', 'lockedtime': ' 0.000000631'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 3', 'period': 56700.0, 'C(LO)': 2088.0, 'C(HI)': 4177.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 15', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001249192', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.737106330', 'avgresponsejitter': ' 0.001063805', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 14', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 1', 'period': 181440.0, 'C(LO)': 3208.0, 'C(HI)': 6416.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 6', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002316285', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.728130547', 'avgresponsejitter': ' 0.001858520', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 6', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 630000.0, 'C(LO)': 7934.0, 'C(HI)': 15869.000000000002, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 3', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004372679', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.636390030', 'avgresponsejitter': ' 0.004213718', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 4', 'period': 50000.0, 'C(LO)': 430.0, 'C(HI)': 860.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 17', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000255045', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.750006303', 'avgresponsejitter': ' 0.000220988', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 16', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 8', 'period': 45000.0, 'C(LO)': 10176.0, 'C(HI)': 10176.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 19', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006051294', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.765006345', 'avgresponsejitter': ' 0.005254970', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 18', 'timesonc2': ' 0', 'lockedtime': ' 0.000001234'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 2', 'period': 100800.0, 'C(LO)': 22218.0, 'C(HI)': 22218.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 9', 'preemptions': ' 10', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.022517465', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.705606006', 'avgresponsejitter': ' 0.014760159', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 18', 'timesonc2': ' 0', 'lockedtime': ' 0.000000604'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 7', 'period': 47250.0, 'C(LO)': 7485.0, 'C(HI)': 7485.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 18', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004406294', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.756685333', 'avgresponsejitter': ' 0.003609622', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 17', 'timesonc2': ' 0', 'lockedtime': ' 0.000000634'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 6', 'period': 56250.0, 'C(LO)': 2553.0, 'C(HI)': 2553.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 15', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001446991', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.731256237', 'avgresponsejitter': ' 0.001213477', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 15', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 0', 'period': 72000.0, 'C(LO)': 32117.0, 'C(HI)': 64234.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 12', 'preemptions': ' 14', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.050576459', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.720006285', 'avgresponsejitter': ' 0.019260492', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 26', 'lockedtime': ' 0.000001574'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 2', 'period': 15750.0, 'C(LO)': 1164.0, 'C(HI)': 1164.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 51', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000693571', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.787508141', 'avgresponsejitter': ' 0.000579796', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 1', 'timesonc2': ' 49', 'lockedtime': ' 0.000001459'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 1', 'period': 65625.0, 'C(LO)': 1784.0, 'C(HI)': 1784.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 13', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001056444', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.721881631', 'avgresponsejitter': ' 0.000892625', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 12', 'lockedtime': ' 0.000000408'}


   </details>

  25. Taskset **e1_semi2wf_t3477**

    Taskset execution params: {'id': 'e1_semi2wf_t3477', 'size': '12', 'utilization': '1.9560000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 4', 'period': 50000.0, 'C(LO)': 2904.0, 'C(HI)': 2904.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 684', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001744835', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 35.155006637', 'avgresponsejitter': ' 0.001455547', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 680', 'timesonc2': ' 3', 'lockedtime': ' 0.000041898'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 113400000, 'lowtohigh': ' 3', 'hightolow': ' 3', 'idletime': 23576961, 'util': 79.20902910052911}



   CPU: 2

    {'id': 2, 'hyperperiod': 56700000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 22062227, 'util': 61.089546737213404}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 1', 'period': 135000.0, 'C(LO)': 25302.0, 'C(HI)': 50605.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 254', 'preemptions': ' 84', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.038058853', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 35.020006931', 'avgresponsejitter': ' 0.013903285', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 339', 'timesonc2': ' 0', 'lockedtime': ' 0.000027189'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 900000.0, 'C(LO)': 168682.0, 'C(HI)': 337365.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 39', 'preemptions': ' 107', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.296539655', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 34.301403877', 'avgresponsejitter': ' 0.111498150', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 146', 'timesonc2': ' 0', 'lockedtime': ' 0.000023321'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 3', 'period': 129600.0, 'C(LO)': 19569.0, 'C(HI)': 19569.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 265', 'preemptions': ' 51', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.013304664', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 35.084807168', 'avgresponsejitter': ' 0.009988366', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 315', 'timesonc2': ' 0', 'lockedtime': ' 0.000027486'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 4', 'period': 50000.0, 'C(LO)': 2904.0, 'C(HI)': 2904.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 684', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001744835', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 35.155006637', 'avgresponsejitter': ' 0.001455547', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 680', 'timesonc2': ' 3', 'lockedtime': ' 0.000041898'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 2', 'period': 196875.0, 'C(LO)': 5456.0, 'C(HI)': 5456.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 175', 'preemptions': ' 5', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.014981339', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 35.059381336', 'avgresponsejitter': ' 0.002926333', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 179', 'timesonc2': ' 0', 'lockedtime': ' 0.000007039'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 4', 'period': 26250.0, 'C(LO)': 5158.0, 'C(HI)': 10316.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1303', 'preemptions': ' 268', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004768844', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 35.151256730', 'avgresponsejitter': ' 0.002744387', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1570', 'lockedtime': ' 0.000020859'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 2', 'period': 64800.0, 'C(LO)': 2715.0, 'C(HI)': 5431.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 529', 'preemptions': ' 100', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006732970', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 35.149605979', 'avgresponsejitter': ' 0.001624330', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 628', 'lockedtime': ' 0.000019288'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 810000.0, 'C(LO)': 20875.0, 'C(HI)': 41750.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 44', 'preemptions': ' 80', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.016729670', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 35.053759841', 'avgresponsejitter': ' 0.012872024', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 123', 'lockedtime': ' 0.000000934'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 3', 'period': 30240.0, 'C(LO)': 151.0, 'C(HI)': 303.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1131', 'preemptions': ' 10', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000976721', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 35.140965916', 'avgresponsejitter': ' 0.000085477', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1140', 'lockedtime': ' 0.000002646'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 1', 'period': 180000.0, 'C(LO)': 44364.0, 'C(HI)': 44364.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 191', 'preemptions': ' 799', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.037650114', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 35.026415667', 'avgresponsejitter': ' 0.027689426', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 989', 'lockedtime': ' 0.000028514'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 6', 'period': 10000.0, 'C(LO)': 1476.0, 'C(HI)': 1476.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 3417', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000898330', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 35.150006679', 'avgresponsejitter': ' 0.000738748', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 3416', 'lockedtime': ' 0.000058793'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 5', 'period': 101250.0, 'C(LO)': 3747.0, 'C(HI)': 3747.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 339', 'preemptions': ' 42', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003078970', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 35.121256318', 'avgresponsejitter': ' 0.001964027', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 380', 'lockedtime': ' 0.000007631'}


   </details>

  26. Taskset **e1_semi2wf_t3875**

    Taskset execution params: {'id': 'e1_semi2wf_t3875', 'size': '12', 'utilization': '1.9800000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 4', 'period': 10000.0, 'C(LO)': 726.0, 'C(HI)': 726.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 327', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000437931', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.281256526', 'avgresponsejitter': ' 0.000368637', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 325', 'lockedtime': ' 0.000004216'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 113400000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 2142294, 'util': 98.11085185185185}



   CPU: 2

    {'id': 2, 'hyperperiod': 18900000, 'lowtohigh': ' 2', 'hightolow': ' 1', 'idletime': 1973182, 'util': 89.5598835978836}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 708750.0, 'C(LO)': 84638.0, 'C(HI)': 169276.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 6', 'preemptions': ' 10', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.056091874', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.841278249', 'avgresponsejitter': ' 0.049626928', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 15', 'timesonc2': ' 0', 'lockedtime': ' 0.000001030'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 3', 'period': 67500.0, 'C(LO)': 5976.0, 'C(HI)': 11952.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 50', 'preemptions': ' 3', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.012727384', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.240006309', 'avgresponsejitter': ' 0.003467745', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 52', 'timesonc2': ' 0', 'lockedtime': ' 0.000000784'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 2', 'period': 78750.0, 'C(LO)': 5453.0, 'C(HI)': 10906.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 43', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003265949', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.236162120', 'avgresponsejitter': ' 0.002659781', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 43', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 1', 'period': 94500.0, 'C(LO)': 1783.0, 'C(HI)': 3566.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 36', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001067955', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.213006441', 'avgresponsejitter': ' 0.000918387', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 35', 'timesonc2': ' 0', 'lockedtime': ' 0.000000231'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 5', 'period': 70000.0, 'C(LO)': 16416.0, 'C(HI)': 16416.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 48', 'preemptions': ' 3', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.009792111', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.220006219', 'avgresponsejitter': ' 0.007879402', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 50', 'timesonc2': ' 0', 'lockedtime': ' 0.000002408'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 4', 'period': 100800.0, 'C(LO)': 14074.0, 'C(HI)': 14074.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 34', 'preemptions': ' 6', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.015758577', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.227688450', 'avgresponsejitter': ' 0.007777204', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 39', 'timesonc2': ' 0', 'lockedtime': ' 0.000000967'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 6', 'period': 65625.0, 'C(LO)': 157.0, 'C(HI)': 157.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 51', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000099904', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.215631399', 'avgresponsejitter': ' 0.000086222', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 50', 'timesonc2': ' 0', 'lockedtime': ' 0.000000405'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 2', 'period': 30240.0, 'C(LO)': 7470.0, 'C(HI)': 14941.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 110', 'preemptions': ' 31', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.010613390', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.265926550', 'avgresponsejitter': ' 0.003935580', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 141', 'lockedtime': ' 0.000001934'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 1', 'period': 151200.0, 'C(LO)': 4730.0, 'C(HI)': 9461.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 23', 'preemptions': ' 7', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006680456', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.178387838', 'avgresponsejitter': ' 0.002602790', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 30', 'lockedtime': ' 0.000000000'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 540000.0, 'C(LO)': 181659.0, 'C(HI)': 181659.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 7', 'preemptions': ' 93', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.140625177', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.702183526', 'avgresponsejitter': ' 0.127350973', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 99', 'lockedtime': ' 0.000002495'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 4', 'period': 10000.0, 'C(LO)': 726.0, 'C(HI)': 726.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 327', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000437931', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.281256526', 'avgresponsejitter': ' 0.000368637', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 325', 'lockedtime': ' 0.000004216'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 3', 'period': 100000.0, 'C(LO)': 4551.0, 'C(HI)': 4551.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 34', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002724354', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 4.200313135', 'avgresponsejitter': ' 0.002219652', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 33', 'lockedtime': ' 0.000000237'}


   </details>

  27. Taskset **e1_semi2wf_t3896**

    Taskset execution params: {'id': 'e1_semi2wf_t3896', 'size': '12', 'utilization': '1.9800000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 6', 'period': 10000.0, 'C(LO)': 543.0, 'C(HI)': 543.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 954', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000323616', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 10.534648057', 'avgresponsejitter': ' 0.000274414', 'deadlinesmissed': ' 3', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 1', 'timesonc2': ' 950', 'lockedtime': ' 0.000017135'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 56700000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 6650681, 'util': 88.27040388007055}



   CPU: 2

    {'id': 2, 'hyperperiod': 113400000, 'lowtohigh': ' 2', 'hightolow': ' 2', 'idletime': 6435853, 'util': 94.32464462081128}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 1', 'period': 94500.0, 'C(LO)': 21872.0, 'C(HI)': 43744.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 102', 'preemptions': ' 33', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.017923697', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 10.453954057', 'avgresponsejitter': ' 0.012212447', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 134', 'timesonc2': ' 0', 'lockedtime': ' 0.000008417'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 0', 'period': 453600.0, 'C(LO)': 62255.0, 'C(HI)': 124511.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 22', 'preemptions': ' 30', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.050296099', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 10.088945471', 'avgresponsejitter': ' 0.037682483', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 51', 'timesonc2': ' 0', 'lockedtime': ' 0.000004162'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 4', 'period': 50000.0, 'C(LO)': 8217.0, 'C(HI)': 8217.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 192', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004924568', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 10.500545943', 'avgresponsejitter': ' 0.004118432', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 191', 'timesonc2': ' 0', 'lockedtime': ' 0.000009664'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 2', 'period': 113400.0, 'C(LO)': 6630.0, 'C(HI)': 6630.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 86', 'preemptions': ' 5', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.008102991', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 10.525607204', 'avgresponsejitter': ' 0.003606423', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 90', 'timesonc2': ' 0', 'lockedtime': ' 0.000001447'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 3', 'period': 101250.0, 'C(LO)': 233.0, 'C(HI)': 233.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 96', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000142177', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 10.517506174', 'avgresponsejitter': ' 0.000124601', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 95', 'timesonc2': ' 0', 'lockedtime': ' 0.000000514'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 2', 'period': 150000.0, 'C(LO)': 35959.0, 'C(HI)': 71918.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 65', 'preemptions': ' 133', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.049443444', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 10.452199778', 'avgresponsejitter': ' 0.021054153', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 198', 'lockedtime': ' 0.000001045'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 1', 'period': 168000.0, 'C(LO)': 14170.0, 'C(HI)': 28341.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 58', 'preemptions': ' 56', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.032538946', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 10.408006237', 'avgresponsejitter': ' 0.008371835', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 113', 'lockedtime': ' 0.000002715'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 2', 'priority': ' 0', 'period': 648000.0, 'C(LO)': 24483.0, 'C(HI)': 48966.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 16', 'preemptions': ' 28', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.031589985', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 10.086296898', 'avgresponsejitter': ' 0.016183565', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 43', 'lockedtime': ' 0.000002282'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 3', 'period': 84375.0, 'C(LO)': 1932.0, 'C(HI)': 3864.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 114', 'preemptions': ' 7', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002712622', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 10.451382568', 'avgresponsejitter': ' 0.001017153', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 121', 'lockedtime': ' 0.000001168'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 4', 'period': 72000.0, 'C(LO)': 11428.0, 'C(HI)': 11428.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 134', 'preemptions': ' 74', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.007982640', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 10.504006000', 'avgresponsejitter': ' 0.005944147', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 207', 'lockedtime': ' 0.000002871'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 6', 'period': 10000.0, 'C(LO)': 543.0, 'C(HI)': 543.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 954', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000323616', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 10.534648057', 'avgresponsejitter': ' 0.000274414', 'deadlinesmissed': ' 3', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 1', 'timesonc2': ' 950', 'lockedtime': ' 0.000017135'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 5', 'period': 52500.0, 'C(LO)': 1833.0, 'C(HI)': 1833.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 183', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001101991', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 10.502506171', 'avgresponsejitter': ' 0.000909808', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 182', 'lockedtime': ' 0.000001264'}


   </details>

  28. Taskset **e1_semi2wf_t4046**

    Taskset execution params: {'id': 'e1_semi2wf_t4046', 'size': '12', 'utilization': '1.9920000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 5', 'period': 10000.0, 'C(LO)': 1767.0, 'C(HI)': 1767.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 64', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001064676', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.630768550', 'avgresponsejitter': ' 0.000886477', 'deadlinesmissed': ' 2', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 1', 'timesonc2': ' 61', 'lockedtime': ' 0.000002258'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 22680000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 360821, 'util': 98.40907848324515}



   CPU: 2

    {'id': 2, 'hyperperiod': 5670000, 'lowtohigh': ' 1', 'hightolow': ' 1', 'idletime': 377536, 'util': 93.34151675485009}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 1', 'period': 113400.0, 'C(LO)': 16531.0, 'C(HI)': 33063.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 7', 'preemptions': ' 5', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.010654709', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.571119805', 'avgresponsejitter': ' 0.008918592', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 11', 'timesonc2': ' 0', 'lockedtime': ' 0.000000808'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 3', 'period': 26250.0, 'C(LO)': 1849.0, 'C(HI)': 3698.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 26', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001076730', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.630285375', 'avgresponsejitter': ' 0.000901850', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 25', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 2', 'period': 40000.0, 'C(LO)': 2417.0, 'C(HI)': 4835.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 17', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001435180', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.600836883', 'avgresponsejitter': ' 0.001212027', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 16', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 810000.0, 'C(LO)': 226876.0, 'C(HI)': 226876.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 11', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.141585640', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.015295799', 'avgresponsejitter': ' 0.141585640', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 12', 'timesonc2': ' 0', 'lockedtime': ' 0.000001670'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 5', 'period': 56700.0, 'C(LO)': 8545.0, 'C(HI)': 8545.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 13', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.005118378', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.623706195', 'avgresponsejitter': ' 0.004349943', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 12', 'timesonc2': ' 0', 'lockedtime': ' 0.000001075'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 4', 'period': 70000.0, 'C(LO)': 642.0, 'C(HI)': 642.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 11', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000376150', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.630007381', 'avgresponsejitter': ' 0.000324393', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 10', 'timesonc2': ' 0', 'lockedtime': ' 0.000000808'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 2', 'period': 90000.0, 'C(LO)': 17320.0, 'C(HI)': 34641.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 8', 'preemptions': ' 5', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.011756039', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.540896249', 'avgresponsejitter': ' 0.009321180', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 12', 'lockedtime': ' 0.000000288'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 1', 'period': 118125.0, 'C(LO)': 8111.999999999999, 'C(HI)': 16225.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 7', 'preemptions': ' 2', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.011934315', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.591283468', 'avgresponsejitter': ' 0.005531282', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 9', 'lockedtime': ' 0.000000925'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 3', 'period': 39375.0, 'C(LO)': 1047.0, 'C(HI)': 2094.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 17', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001379180', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.590753087', 'avgresponsejitter': ' 0.000596429', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 17', 'lockedtime': ' 0.000000565'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 708750.0, 'C(LO)': 157647.0, 'C(HI)': 157647.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 12', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.115301577', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.018276754', 'avgresponsejitter': ' 0.115301577', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 13', 'lockedtime': ' 0.000000000'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 5', 'period': 10000.0, 'C(LO)': 1767.0, 'C(HI)': 1767.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 64', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001064676', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.630768550', 'avgresponsejitter': ' 0.000886477', 'deadlinesmissed': ' 2', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 1', 'timesonc2': ' 61', 'lockedtime': ' 0.000002258'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 4', 'period': 141750.0, 'C(LO)': 3403.0, 'C(HI)': 3403.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 6', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001987246', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.567006327', 'avgresponsejitter': ' 0.001734565', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 5', 'lockedtime': ' 0.000000000'}


   </details>

  29. Taskset **e1_semi2wf_t4225**

    Taskset execution params: {'id': 'e1_semi2wf_t4225', 'size': '12', 'utilization': '1.9920000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 4', 'period': 20000.0, 'C(LO)': 774.0, 'C(HI)': 774.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 619', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000460054', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 13.360608078', 'avgresponsejitter': ' 0.000389405', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 1', 'timesonc2': ' 617', 'lockedtime': ' 0.000017321'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 56700000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 7072453, 'util': 87.52653791887126}



   CPU: 2

    {'id': 2, 'hyperperiod': 56700000, 'lowtohigh': ' 2', 'hightolow': ' 2', 'idletime': 7921014, 'util': 86.02995767195767}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 3', 'period': 37800.0, 'C(LO)': 4295.0, 'C(HI)': 8591.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 328', 'preemptions': ' 35', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004341429', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 13.322806324', 'avgresponsejitter': ' 0.002230526', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 362', 'timesonc2': ' 0', 'lockedtime': ' 0.000006327'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 4', 'period': 35000.0, 'C(LO)': 2116.0, 'C(HI)': 4233.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 355', 'preemptions': ' 2', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001277171', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 13.355006450', 'avgresponsejitter': ' 0.001063673', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 356', 'timesonc2': ' 0', 'lockedtime': ' 0.000007976'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 2', 'period': 70875.0, 'C(LO)': 617.0, 'C(HI)': 1235.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 176', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000368682', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 13.332299991', 'avgresponsejitter': ' 0.000309285', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 175', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 5', 'period': 15750.0, 'C(LO)': 65.0, 'C(HI)': 130.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 786', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000043919', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 13.348006120', 'avgresponsejitter': ' 0.000038526', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 785', 'timesonc2': ' 0', 'lockedtime': ' 0.000004174'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 1', 'period': 81000.0, 'C(LO)': 333.0, 'C(HI)': 666.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 154', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000202763', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 13.312007435', 'avgresponsejitter': ' 0.000170517', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 153', 'timesonc2': ' 0', 'lockedtime': ' 0.000005240'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 900000.0, 'C(LO)': 510460.0, 'C(HI)': 510460.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 15', 'preemptions': ' 603', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.346164399', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 12.701018288', 'avgresponsejitter': ' 0.310487568', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 617', 'timesonc2': ' 0', 'lockedtime': ' 0.000044883'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 6', 'period': 50000.0, 'C(LO)': 1883.0, 'C(HI)': 1883.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 249', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001132538', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 13.350006021', 'avgresponsejitter': ' 0.000947628', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 248', 'timesonc2': ' 0', 'lockedtime': ' 0.000012192'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 2', 'period': 28350.0, 'C(LO)': 8182.999999999999, 'C(HI)': 16367.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 437', 'preemptions': ' 118', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.013556700', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 13.332256922', 'avgresponsejitter': ' 0.004267700', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 556', 'lockedtime': ' 0.000019417'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 1', 'period': 56700.0, 'C(LO)': 18042.0, 'C(HI)': 18042.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 219', 'preemptions': ' 131', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.012188033', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 13.317470471', 'avgresponsejitter': ' 0.009290814', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 349', 'lockedtime': ' 0.000012598'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 4', 'period': 20000.0, 'C(LO)': 774.0, 'C(HI)': 774.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 619', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000460054', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 13.360608078', 'avgresponsejitter': ' 0.000389405', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 1', 'timesonc2': ' 617', 'lockedtime': ' 0.000017321'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 150000.0, 'C(LO)': 5720.0, 'C(HI)': 5720.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 84', 'preemptions': ' 12', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.016824249', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 13.300443601', 'avgresponsejitter': ' 0.003859306', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 95', 'lockedtime': ' 0.000003856'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 3', 'period': 54000.0, 'C(LO)': 1760.0, 'C(HI)': 1760.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 230', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001064099', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 13.312007126', 'avgresponsejitter': ' 0.000881961', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 1', 'timesonc2': ' 228', 'lockedtime': ' 0.000003450'}


   </details>

  30. Taskset **e1_semi2wf_t4796**

    Taskset execution params: {'id': 'e1_semi2wf_t4796', 'size': '12', 'utilization': '2.028', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 5', 'period': 18900.0, 'C(LO)': 4808.0, 'C(HI)': 4808.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 63', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002872177', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.170006459', 'avgresponsejitter': ' 0.002421060', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 1', 'timesonc2': ' 61', 'lockedtime': ' 0.000001814'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 18900000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 765402, 'util': 95.95025396825397}



   CPU: 2

    {'id': 2, 'hyperperiod': 113400000, 'lowtohigh': ' 1', 'hightolow': ' 1', 'idletime': 676393, 'util': 99.40353350970018}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 2', 'period': 45000.0, 'C(LO)': 6231.0, 'C(HI)': 12462.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 27', 'preemptions': ' 2', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004594165', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.125007009', 'avgresponsejitter': ' 0.003259057', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 28', 'timesonc2': ' 0', 'lockedtime': ' 0.000000411'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 3', 'period': 37800.0, 'C(LO)': 3325.0, 'C(HI)': 6650.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 32', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001934532', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.134006363', 'avgresponsejitter': ' 0.001662306', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 31', 'timesonc2': ' 0', 'lockedtime': ' 0.000000919'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 675000.0, 'C(LO)': 37328.0, 'C(HI)': 74657.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 3', 'preemptions': ' 4', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.024529667', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.678136213', 'avgresponsejitter': ' 0.022916306', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 6', 'timesonc2': ' 0', 'lockedtime': ' 0.000000411'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 5', 'period': 39375.0, 'C(LO)': 8437.0, 'C(HI)': 8437.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 31', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.005013117', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.141881423', 'avgresponsejitter': ' 0.004322486', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 30', 'timesonc2': ' 0', 'lockedtime': ' 0.000001102'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 1', 'period': 150000.0, 'C(LO)': 26861.0, 'C(HI)': 26861.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 9', 'preemptions': ' 12', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.020966246', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.050006336', 'avgresponsejitter': ' 0.016599697', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 20', 'timesonc2': ' 0', 'lockedtime': ' 0.000002492'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 4', 'period': 84000.0, 'C(LO)': 60.0, 'C(HI)': 60.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 15', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000043294', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.092006300', 'avgresponsejitter': ' 0.000036222', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 14', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 567000.0, 'C(LO)': 102983.0, 'C(HI)': 205966.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 4', 'preemptions': ' 8', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.077481907', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.140898102', 'avgresponsejitter': ' 0.056426832', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 11', 'lockedtime': ' 0.000001330'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 2', 'period': 112500.0, 'C(LO)': 7243.0, 'C(HI)': 14486.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 12', 'preemptions': ' 3', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006901081', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.125006438', 'avgresponsejitter': ' 0.004067387', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 14', 'lockedtime': ' 0.000000841'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 1', 'period': 113400.0, 'C(LO)': 2678.0, 'C(HI)': 5357.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 12', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004087069', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.136803856', 'avgresponsejitter': ' 0.002023565', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 13', 'lockedtime': ' 0.000000000'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 5', 'period': 18900.0, 'C(LO)': 4808.0, 'C(HI)': 4808.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 63', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002872177', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.170006459', 'avgresponsejitter': ' 0.002421060', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 1', 'timesonc2': ' 61', 'lockedtime': ' 0.000001814'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 3', 'period': 157500.0, 'C(LO)': 24326.0, 'C(HI)': 24326.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 9', 'preemptions': ' 9', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.018524150', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.102506048', 'avgresponsejitter': ' 0.014502829', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 17', 'lockedtime': ' 0.000000462'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 4', 'period': 40000.0, 'C(LO)': 4891.0, 'C(HI)': 4891.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 31', 'preemptions': ' 4', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.005644931', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.160006856', 'avgresponsejitter': ' 0.002805228', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 34', 'lockedtime': ' 0.000000766'}


   </details>

  31. Taskset **e1_semi2wf_t5240**

    Taskset execution params: {'id': 'e1_semi2wf_t5240', 'size': '12', 'utilization': '2.04', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 3', 'period': 10000.0, 'C(LO)': 2950.0, 'C(HI)': 2950.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 261', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001775465', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.600646601', 'avgresponsejitter': ' 0.001468237', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 259', 'timesonc2': ' 1', 'lockedtime': ' 0.000003517'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 22680000, 'lowtohigh': ' 2', 'hightolow': ' 2', 'idletime': 1534350, 'util': 93.23478835978835}



   CPU: 2

    {'id': 2, 'hyperperiod': 7560000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 1611254, 'util': 78.6871164021164}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 2', 'period': 50400.0, 'C(LO)': 7915.999999999999, 'C(HI)': 15833.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 53', 'preemptions': ' 21', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.012006982', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.571486979', 'avgresponsejitter': ' 0.004759351', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 75', 'timesonc2': ' 0', 'lockedtime': ' 0.000003556'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 1', 'period': 60480.0, 'C(LO)': 8311.0, 'C(HI)': 16622.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 44', 'preemptions': ' 17', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006461718', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.541440976', 'avgresponsejitter': ' 0.004780733', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 60', 'timesonc2': ' 0', 'lockedtime': ' 0.000001063'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 3', 'period': 10000.0, 'C(LO)': 2950.0, 'C(HI)': 2950.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 261', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001775465', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.600646601', 'avgresponsejitter': ' 0.001468237', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 259', 'timesonc2': ' 1', 'lockedtime': ' 0.000003517'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 0', 'period': 141750.0, 'C(LO)': 28515.0, 'C(HI)': 28515.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 20', 'preemptions': ' 41', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.024484754', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.551506372', 'avgresponsejitter': ' 0.019729180', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 60', 'timesonc2': ' 0', 'lockedtime': ' 0.000002255'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 1', 'period': 126000.0, 'C(LO)': 24825.0, 'C(HI)': 49651.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 22', 'preemptions': ' 24', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.015496261', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.521071844', 'avgresponsejitter': ' 0.012811477', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 45', 'lockedtime': ' 0.000001249'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 4', 'period': 18900.0, 'C(LO)': 634.0, 'C(HI)': 1268.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 139', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001643739', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.589307144', 'avgresponsejitter': ' 0.000331435', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 139', 'lockedtime': ' 0.000000420'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 2', 'period': 47250.0, 'C(LO)': 964.0, 'C(HI)': 1929.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 57', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000572679', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.598973793', 'avgresponsejitter': ' 0.000488231', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 56', 'lockedtime': ' 0.000000414'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 3', 'period': 33750.0, 'C(LO)': 471.0, 'C(HI)': 942.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 79', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000285051', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.598757514', 'avgresponsejitter': ' 0.000234616', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 78', 'lockedtime': ' 0.000000255'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 2', 'priority': ' 0', 'period': 840000.0, 'C(LO)': 277375.0, 'C(HI)': 277375.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 4', 'preemptions': ' 74', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.186287381', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 2.680987901', 'avgresponsejitter': ' 0.172909652', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 77', 'lockedtime': ' 0.000004228'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 5', 'period': 151200.0, 'C(LO)': 7635.0, 'C(HI)': 7635.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 19', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004474150', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.570408661', 'avgresponsejitter': ' 0.003868243', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 18', 'lockedtime': ' 0.000000883'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 6', 'period': 60000.0, 'C(LO)': 2403.0, 'C(HI)': 2403.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 45', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001443628', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.581274910', 'avgresponsejitter': ' 0.001187919', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 44', 'lockedtime': ' 0.000002592'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 7', 'period': 54000.0, 'C(LO)': 217.0, 'C(HI)': 217.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 50', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000133844', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.592006904', 'avgresponsejitter': ' 0.000117508', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 49', 'lockedtime': ' 0.000000805'}


   </details>

  32. Taskset **e1_semi2wf_t60**

    Taskset execution params: {'id': 'e1_semi2wf_t60', 'size': '12', 'utilization': '1.8', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 6', 'period': 20000.0, 'C(LO)': 2239.0, 'C(HI)': 2239.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 3', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001128408', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.078756502', 'avgresponsejitter': ' 0.001119685', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 37800000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 10206, 'util': 99.973}



   CPU: 2

    {'id': 2, 'hyperperiod': 37800000, 'lowtohigh': ' 1', 'hightolow': ' 1', 'idletime': 37421, 'util': 99.90100264550264}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 675000.0, 'C(LO)': 75464.0, 'C(HI)': 150928.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 2', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.039146051', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.029415790', 'avgresponsejitter': ' 0.039146051', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 3', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 1', 'period': 504000.0, 'C(LO)': 45874.0, 'C(HI)': 91749.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.019290309', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.010120321', 'avgresponsejitter': ' 0.019290309', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 2', 'period': 112500.0, 'C(LO)': 5101.0, 'C(HI)': 10202.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002271261', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.007844297', 'avgresponsejitter': ' 0.002271261', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 5', 'period': 39375.0, 'C(LO)': 8094.000000000001, 'C(HI)': 8094.000000000001, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 3', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004602829', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.039382595', 'avgresponsejitter': ' 0.004518072', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 6', 'period': 20000.0, 'C(LO)': 2239.0, 'C(HI)': 2239.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 3', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001128408', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.078756502', 'avgresponsejitter': ' 0.001119685', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 4', 'period': 42000.0, 'C(LO)': 2904.0, 'C(HI)': 2904.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 3', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001627691', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.043738745', 'avgresponsejitter': ' 0.001325517', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 3', 'period': 65625.0, 'C(LO)': 1739.0, 'C(HI)': 1739.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 3', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000951354', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.065632252', 'avgresponsejitter': ' 0.000918640', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 0', 'period': 131250.0, 'C(LO)': 17472.0, 'C(HI)': 34945.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.008223279', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.020448429', 'avgresponsejitter': ' 0.008223279', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1', 'lockedtime': ' 0.000000000'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 1', 'period': 120000.0, 'C(LO)': 9396.0, 'C(HI)': 18792.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004313811', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.016130108', 'avgresponsejitter': ' 0.004313811', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1', 'lockedtime': ' 0.000000000'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 4', 'period': 15750.0, 'C(LO)': 40.0, 'C(HI)': 81.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 7', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000055688', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.078757213', 'avgresponsejitter': ' 0.000036429', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 7', 'lockedtime': ' 0.000000000'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 3', 'period': 56250.0, 'C(LO)': 24381.0, 'C(HI)': 24381.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 3', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.014570505', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.056256108', 'avgresponsejitter': ' 0.013912511', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 3', 'lockedtime': ' 0.000000000'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 2', 'period': 108000.0, 'C(LO)': 3132.0, 'C(HI)': 3132.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001474820', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.014651210', 'avgresponsejitter': ' 0.001474820', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 2', 'lockedtime': ' 0.000000000'}


   </details>

  33. Taskset **e1_semi2wf_t683**

    Taskset execution params: {'id': 'e1_semi2wf_t683', 'size': '12', 'utilization': '1.824', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 5', 'period': 26250.0, 'C(LO)': 2739.0, 'C(HI)': 2739.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1123', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001647165', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 30.453767195', 'avgresponsejitter': ' 0.001369505', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 4', 'timesrestored': ' 4', 'timesonc1': ' 1120', 'timesonc2': ' 2', 'lockedtime': ' 0.000005814'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 37800000, 'lowtohigh': ' 7', 'hightolow': ' 7', 'idletime': 19748982, 'util': 47.754015873015874}



   CPU: 2

    {'id': 2, 'hyperperiod': 56700000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 19179582, 'util': 66.17357671957672}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 2', 'period': 108000.0, 'C(LO)': 12390.0, 'C(HI)': 24780.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 274', 'preemptions': ' 86', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.028780288', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 30.376006354', 'avgresponsejitter': ' 0.007397694', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 3', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 362', 'timesonc2': ' 0', 'lockedtime': ' 0.000000559'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 1', 'period': 131250.0, 'C(LO)': 12299.0, 'C(HI)': 24599.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 226', 'preemptions': ' 39', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.033990802', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 30.404792910', 'avgresponsejitter': ' 0.007871354', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 4', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 268', 'timesonc2': ' 0', 'lockedtime': ' 0.000004492'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 0', 'period': 189000.0, 'C(LO)': 2436.0, 'C(HI)': 4873.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 157', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.009892054', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 30.296638943', 'avgresponsejitter': ' 0.001276643', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 157', 'timesonc2': ' 0', 'lockedtime': ' 0.000003075'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 4', 'period': 60480.0, 'C(LO)': 16460.0, 'C(HI)': 16460.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 488', 'preemptions': ' 149', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.011410354', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 30.393287261', 'avgresponsejitter': ' 0.008646144', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 636', 'timesonc2': ' 0', 'lockedtime': ' 0.000007676'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 5', 'period': 26250.0, 'C(LO)': 2739.0, 'C(HI)': 2739.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1123', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001647165', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 30.453767195', 'avgresponsejitter': ' 0.001369505', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 4', 'timesrestored': ' 4', 'timesonc1': ' 1120', 'timesonc2': ' 2', 'lockedtime': ' 0.000005814'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 3', 'period': 151200.0, 'C(LO)': 8002.0, 'C(HI)': 8002.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 196', 'preemptions': ' 27', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006362871', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 30.341367586', 'avgresponsejitter': ' 0.004162390', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 222', 'timesonc2': ' 0', 'lockedtime': ' 0.000006285'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 1', 'period': 101250.0, 'C(LO)': 12399.0, 'C(HI)': 24799.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 292', 'preemptions': ' 116', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.014901297', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 30.362507333', 'avgresponsejitter': ' 0.007453246', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 407', 'lockedtime': ' 0.000007655'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 3', 'period': 37800.0, 'C(LO)': 3006.0, 'C(HI)': 6012.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 781', 'preemptions': ' 23', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.009199898', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 30.446206033', 'avgresponsejitter': ' 0.001606961', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 803', 'lockedtime': ' 0.000019583'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 2', 'period': 50400.0, 'C(LO)': 3281.0, 'C(HI)': 6562.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 586', 'preemptions': ' 18', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006267589', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 30.433606210', 'avgresponsejitter': ' 0.001763279', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 603', 'lockedtime': ' 0.000000000'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 2', 'priority': ' 0', 'period': 506250.0, 'C(LO)': 84301.0, 'C(HI)': 84301.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 60', 'preemptions': ' 200', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.067429336', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 30.369779739', 'avgresponsejitter': ' 0.054602574', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 259', 'lockedtime': ' 0.000011474'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 5', 'period': 50000.0, 'C(LO)': 7482.0, 'C(HI)': 7482.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 591', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004483471', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 30.450006087', 'avgresponsejitter': ' 0.003753417', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 590', 'lockedtime': ' 0.000010150'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 4', 'period': 84000.0, 'C(LO)': 8525.0, 'C(HI)': 8525.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 352', 'preemptions': ' 20', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.009018123', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 30.405406108', 'avgresponsejitter': ' 0.004454913', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 371', 'lockedtime': ' 0.000007216'}


   </details>

  34. Taskset **e1_semi2wf_t764**

    Taskset execution params: {'id': 'e1_semi2wf_t764', 'size': '12', 'utilization': '1.836', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 6', 'period': 18900.0, 'C(LO)': 1446.0, 'C(HI)': 1446.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 351', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000867985', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.615008225', 'avgresponsejitter': ' 0.000723477', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 343', 'timesonc2': ' 7', 'lockedtime': ' 0.000001868'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 22680000, 'lowtohigh': ' 2', 'hightolow': ' 2', 'idletime': 3759865, 'util': 83.42211199294533}



   CPU: 2

    {'id': 2, 'hyperperiod': 14175000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 3895555, 'util': 72.51813051146385}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 3', 'period': 78750.0, 'C(LO)': 3356.0, 'C(HI)': 6713.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 85', 'preemptions': ' 7', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006966447', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.536257012', 'avgresponsejitter': ' 0.001823384', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 92', 'timesonc2': ' 0', 'lockedtime': ' 0.000001207'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 648000.0, 'C(LO)': 19195.0, 'C(HI)': 38391.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 12', 'preemptions': ' 9', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.021556330', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.573085324', 'avgresponsejitter': ' 0.011207928', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 20', 'timesonc2': ' 0', 'lockedtime': ' 0.000000228'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 2', 'period': 151200.0, 'C(LO)': 2656.0, 'C(HI)': 5312.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 45', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003926553', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.502525288', 'avgresponsejitter': ' 0.001396802', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 46', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 4', 'period': 63000.0, 'C(LO)': 22722.0, 'C(HI)': 22722.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 106', 'preemptions': ' 58', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.016524360', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.552007156', 'avgresponsejitter': ' 0.012023916', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 163', 'timesonc2': ' 0', 'lockedtime': ' 0.000001994'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 1', 'period': 405000.0, 'C(LO)': 100310.0, 'C(HI)': 100310.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 18', 'preemptions': ' 88', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.093296414', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.480007435', 'avgresponsejitter': ' 0.067980018', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 105', 'timesonc2': ' 0', 'lockedtime': ' 0.000002033'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 6', 'period': 18900.0, 'C(LO)': 1446.0, 'C(HI)': 1446.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 351', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000867985', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.615008225', 'avgresponsejitter': ' 0.000723477', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 343', 'timesonc2': ' 7', 'lockedtime': ' 0.000001868'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 5', 'period': 60480.0, 'C(LO)': 4237.0, 'C(HI)': 4237.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 111', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002547285', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.592326835', 'avgresponsejitter': ' 0.002172691', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 110', 'timesonc2': ' 0', 'lockedtime': ' 0.000000270'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 3', 'period': 22500.0, 'C(LO)': 1156.0, 'C(HI)': 2313.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 296', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000701766', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.615006652', 'avgresponsejitter': ' 0.000577886', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 295', 'lockedtime': ' 0.000002114'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 1', 'period': 112500.0, 'C(LO)': 3275.0, 'C(HI)': 6551.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 60', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001960369', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.526328502', 'avgresponsejitter': ' 0.001613826', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 60', 'lockedtime': ' 0.000000000'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 2', 'period': 65625.0, 'C(LO)': 506.99999999999994, 'C(HI)': 1013.9999999999999, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 102', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000301198', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.570725105', 'avgresponsejitter': ' 0.000253249', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 101', 'lockedtime': ' 0.000001096'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 0', 'period': 168750.0, 'C(LO)': 87121.0, 'C(HI)': 87121.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 40', 'preemptions': ' 110', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.063083324', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.414917838', 'avgresponsejitter': ' 0.049174396', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 149', 'lockedtime': ' 0.000004811'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 4', 'period': 81000.0, 'C(LO)': 16897.0, 'C(HI)': 16897.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 83', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.010165375', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.561006123', 'avgresponsejitter': ' 0.008516823', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 82', 'lockedtime': ' 0.000002889'}


   </details>

  35. Taskset **e1_semi2wf_t966**

    Taskset execution params: {'id': 'e1_semi2wf_t966', 'size': '12', 'utilization': '1.836', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 5', 'period': 18900.0, 'C(LO)': 3064.0, 'C(HI)': 3064.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 2927', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001843844', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 56.321881649', 'avgresponsejitter': ' 0.001532898', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 4', 'timesrestored': ' 4', 'timesonc1': ' 2', 'timesonc2': ' 2924', 'lockedtime': ' 0.000047477'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 56700000, 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': 35416781, 'util': 37.53654144620812}



   CPU: 2

    {'id': 2, 'hyperperiod': 113400000, 'lowtohigh': ' 13', 'hightolow': ' 13', 'idletime': 36983269, 'util': 67.38688800705467}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 756000.0, 'C(LO)': 120365.0, 'C(HI)': 240731.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 75', 'preemptions': ' 379', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.104593892', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 56.190274718', 'avgresponsejitter': ' 0.080677282', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 453', 'timesonc2': ' 0', 'lockedtime': ' 0.000028315'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 3', 'period': 45360.0, 'C(LO)': 3569.0, 'C(HI)': 7138.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1221', 'preemptions': ' 29', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.008713508', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 56.293846300', 'avgresponsejitter': ' 0.001861423', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1249', 'timesonc2': ' 0', 'lockedtime': ' 0.000010622'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 5', 'period': 25200.0, 'C(LO)': 5559.0, 'C(HI)': 5559.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 2197', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003345712', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 56.314006312', 'avgresponsejitter': ' 0.002786835', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2196', 'timesonc2': ' 0', 'lockedtime': ' 0.000054453'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 2', 'period': 131250.0, 'C(LO)': 22888.0, 'C(HI)': 22888.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 423', 'preemptions': ' 296', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.018643084', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 56.256256162', 'avgresponsejitter': ' 0.013310556', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 718', 'timesonc2': ' 0', 'lockedtime': ' 0.000034811'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 4', 'period': 105000.0, 'C(LO)': 6615.0, 'C(HI)': 6615.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 528', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003968883', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 56.230007009', 'avgresponsejitter': ' 0.003316655', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 527', 'timesonc2': ' 0', 'lockedtime': ' 0.000007886'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 1', 'period': 140000.0, 'C(LO)': 2342.0, 'C(HI)': 2342.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 397', 'preemptions': ' 12', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004318015', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 56.300006252', 'avgresponsejitter': ' 0.001237664', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 408', 'timesonc2': ' 0', 'lockedtime': ' 0.000000315'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 3', 'period': 100800.0, 'C(LO)': 18229.0, 'C(HI)': 36458.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 550', 'preemptions': ' 247', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.045805577', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 56.238406093', 'avgresponsejitter': ' 0.011495673', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 8', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 804', 'lockedtime': ' 0.000031646'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 2', 'period': 181440.0, 'C(LO)': 3469.0, 'C(HI)': 6938.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 306', 'preemptions': ' 7', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.022516508', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 56.157766306', 'avgresponsejitter': ' 0.001975814', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 314', 'lockedtime': ' 0.000018655'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 1', 'period': 196875.0, 'C(LO)': 3291.0, 'C(HI)': 6582.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 282', 'preemptions': ' 25', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.013596634', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 56.125006949', 'avgresponsejitter': ' 0.001870147', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 3', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 309', 'lockedtime': ' 0.000007646'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 630000.0, 'C(LO)': 9601.0, 'C(HI)': 19202.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 89', 'preemptions': ' 28', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.017013357', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 55.828637231', 'avgresponsejitter': ' 0.005807592', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 116', 'lockedtime': ' 0.000002027'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 4', 'period': 135000.0, 'C(LO)': 35026.0, 'C(HI)': 35026.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 411', 'preemptions': ' 367', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.024061961', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 56.215006006', 'avgresponsejitter': ' 0.018912583', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 777', 'lockedtime': ' 0.000049384'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 5', 'period': 18900.0, 'C(LO)': 3064.0, 'C(HI)': 3064.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 2927', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001843844', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 56.321881649', 'avgresponsejitter': ' 0.001532898', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 4', 'timesrestored': ' 4', 'timesonc1': ' 2', 'timesonc2': ' 2924', 'lockedtime': ' 0.000047477'}


   </details>

</details>



### **Safe Boundary Exceeded**

<details><summary markdown="span">Click here to expand this section.</summary>

Ovvero quando un taskset ha troppi core (2 nel contesto dual-core) eseguenti in HI-crit mode.

  1. Taskset **e1_semi2wf_t2948**

    Taskset execution params: {'id': 'e1_semi2wf_t2948', 'size': '12', 'utilization': '1.9320000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 113400000, 'lowtohigh': ' 38', 'hightolow': ' 37', 'idletime': 73896251, 'util': 34.835757495590826}



   CPU: 2

    {'id': 2, 'hyperperiod': 113400000, 'lowtohigh': ' 63', 'hightolow': ' 62', 'idletime': 76993154, 'util': 32.104802469135805}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 3', 'period': 50400.0, 'C(LO)': 9065.0, 'C(HI)': 18131.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2134', 'preemptions': ' 69', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.015457195', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 108.452807453', 'avgresponsejitter': ' 0.004669120', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 15', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2217', 'timesonc2': ' 0', 'lockedtime': ' 0.000024988'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 2', 'period': 81000.0, 'C(LO)': 10414.0, 'C(HI)': 20829.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1328', 'preemptions': ' 149', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.020025589', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 108.407033835', 'avgresponsejitter': ' 0.005803387', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 13', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1489', 'timesonc2': ' 0', 'lockedtime': ' 0.000019414'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 1', 'period': 140000.0, 'C(LO)': 3600.0, 'C(HI)': 7200.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 769', 'preemptions': ' 28', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.012828336', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 108.380007517', 'avgresponsejitter': ' 0.001996868', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 10', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 806', 'timesonc2': ' 0', 'lockedtime': ' 0.000016276'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 756000.0, 'C(LO)': 188337.0, 'C(HI)': 188337.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 143', 'preemptions': ' 557', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.141924901', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 107.606354225', 'avgresponsejitter': ' 0.111442378', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 699', 'timesonc2': ' 0', 'lockedtime': ' 0.000021363'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 4', 'period': 84375.0, 'C(LO)': 5317.0, 'C(HI)': 5317.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 774', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003191294', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 66.137506387', 'avgresponsejitter': ' 0.002669003', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 770', 'timesonc2': ' 3', 'lockedtime': ' 0.000019282'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 0', 'period': 112500.0, 'C(LO)': 23196.0, 'C(HI)': 46392.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 957', 'preemptions': ' 646', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.044913946', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 108.437506042', 'avgresponsejitter': ' 0.013986520', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 12', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1614', 'lockedtime': ' 0.000037505'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 1', 'period': 63000.0, 'C(LO)': 7939.999999999999, 'C(HI)': 15881.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1707', 'preemptions': ' 175', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.022891805', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 108.415006015', 'avgresponsejitter': ' 0.004252622', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 26', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1907', 'lockedtime': ' 0.000001796'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 2', 'period': 42000.0, 'C(LO)': 609.0, 'C(HI)': 1219.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2560', 'preemptions': ' 3', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002901847', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 108.436006030', 'avgresponsejitter': ' 0.000312141', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 25', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 2587', 'lockedtime': ' 0.000036048'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 6', 'period': 40000.0, 'C(LO)': 5175.0, 'C(HI)': 5175.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1658', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003114568', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 67.240005859', 'avgresponsejitter': ' 0.002588613', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 3', 'timesrestored': ' 2', 'timesonc1': ' 0', 'timesonc2': ' 1657', 'lockedtime': ' 0.000025709'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 4', 'period': 113400.0, 'C(LO)': 12237.0, 'C(HI)': 12237.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 949', 'preemptions': ' 151', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.010746264', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 108.389806183', 'avgresponsejitter': ' 0.006452706', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1099', 'lockedtime': ' 0.000028928'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 5', 'period': 87500.0, 'C(LO)': 1139.0, 'C(HI)': 1139.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1230', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000686967', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 108.450005877', 'avgresponsejitter': ' 0.000571751', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1229', 'lockedtime': ' 0.000008267'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 3', 'period': 196875.0, 'C(LO)': 1514.0, 'C(HI)': 1514.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 547', 'preemptions': ' 6', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003383970', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 108.296881108', 'avgresponsejitter': ' 0.000785093', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 552', 'lockedtime': ' 0.000007237'}


   </details>

  2. Taskset **e1_semi2wf_t4902**

    Taskset execution params: {'id': 'e1_semi2wf_t4902', 'size': '12', 'utilization': '2.028', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU: 1

    {'id': 1, 'hyperperiod': 14175000, 'lowtohigh': ' 26', 'hightolow': ' 25', 'idletime': 33855923, 'util': -138.84249029982362}



   CPU: 2

    {'id': 2, 'hyperperiod': 113400000, 'lowtohigh': ' 20', 'hightolow': ' 19', 'idletime': 31941048, 'util': 71.833291005291}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 1', 'period': 101250.0, 'C(LO)': 22514.0, 'C(HI)': 45028.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 474', 'preemptions': ' 293', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.038028910', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 48.790964330', 'avgresponsejitter': ' 0.012706604', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 5', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 771', 'timesonc2': ' 0', 'lockedtime': ' 0.000019066'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 2', 'period': 26250.0, 'C(LO)': 3777.0, 'C(HI)': 7555.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1823', 'preemptions': ' 4', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.007742694', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 48.801256691', 'avgresponsejitter': ' 0.001926039', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 21', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1847', 'timesonc2': ' 0', 'lockedtime': ' 0.000030318'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 4', 'period': 22500.0, 'C(LO)': 3511.0, 'C(HI)': 3511.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 984', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002108502', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 23.095007877', 'avgresponsejitter': ' 0.001759126', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 0', 'timesmigrated': ' 2', 'timesrestored': ' 1', 'timesonc1': ' 981', 'timesonc2': ' 1', 'lockedtime': ' 0.000011532'}



   Task:  12

    {'id': ' 12', 'basecpu': ' 1', 'priority': ' 0', 'period': 787500.0, 'C(LO)': 73624.0, 'C(HI)': 73624.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 62', 'preemptions': ' 172', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.081391477', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 48.252494363', 'avgresponsejitter': ' 0.048383979', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 233', 'timesonc2': ' 0', 'lockedtime': ' 0.000008189'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 3', 'period': 45000.0, 'C(LO)': 1746.0, 'C(HI)': 1746.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1064', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001049718', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 48.790007147', 'avgresponsejitter': ' 0.000875120', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1063', 'timesonc2': ' 0', 'lockedtime': ' 0.000009790'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 1', 'period': 151200.0, 'C(LO)': 39336.0, 'C(HI)': 78673.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 317', 'preemptions': ' 271', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.060426805', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 48.631310237', 'avgresponsejitter': ' 0.021334228', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 5', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 592', 'lockedtime': ' 0.000032045'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 4', 'period': 52500.0, 'C(LO)': 3320.0, 'C(HI)': 6640.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 913', 'preemptions': ' 3', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.005306823', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 48.827507372', 'avgresponsejitter': ' 0.001707985', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 9', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 924', 'lockedtime': ' 0.000056805'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 3', 'period': 108000.0, 'C(LO)': 2167.0, 'C(HI)': 4334.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 444', 'preemptions': ' 2', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003368123', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 48.736005955', 'avgresponsejitter': ' 0.001120267', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 4', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 449', 'lockedtime': ' 0.000003622'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 2', 'period': 150000.0, 'C(LO)': 1003.9999999999999, 'C(HI)': 2007.9999999999998, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 320', 'preemptions': ' 2', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002906246', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 48.700860129', 'avgresponsejitter': ' 0.000521736', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 323', 'lockedtime': ' 0.000004312'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 648000.0, 'C(LO)': 147684.0, 'C(HI)': 147684.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 75', 'preemptions': ' 287', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.123282709', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 48.304918517', 'avgresponsejitter': ' 0.089162907', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 361', 'lockedtime': ' 0.000029273'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 6', 'period': 70875.0, 'C(LO)': 4265.0, 'C(HI)': 4265.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 676', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002555982', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 48.769756381', 'avgresponsejitter': ' 0.002126565', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 3', 'timesrestored': ' 3', 'timesonc1': ' 3', 'timesonc2': ' 672', 'lockedtime': ' 0.000003162'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 5', 'period': 175000.0, 'C(LO)': 3268.0, 'C(HI)': 3268.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 275', 'preemptions': ' 6', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004418231', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 48.775007378', 'avgresponsejitter': ' 0.001673024', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 1', 'timesonc2': ' 279', 'lockedtime': ' 0.000004826'}


   </details>

</details></details>



## Focus for each Utilization level.

<details><summary markdown="span">Click here to expand this section.</summary>

### Level 1.8

   Tasksets executed: 13

   - Tasksets actually schedulable: 11/13 = 84.61538461538461 %

   - Tasksets **not** schedulable: 0/13 = 0.0 %

   - Tasksets exceeding level-criticality budget: 2/13 = 15.384615384615385 %

   - Tasksets exceeding safe boundary: 0/13 = 0.0 %

### Level 1.812

   Tasksets executed: 14

   - Tasksets actually schedulable: 14/14 = 100.0 %

   - Tasksets **not** schedulable: 0/14 = 0.0 %

   - Tasksets exceeding level-criticality budget: 0/14 = 0.0 %

   - Tasksets exceeding safe boundary: 0/14 = 0.0 %

### Level 1.824

   Tasksets executed: 12

   - Tasksets actually schedulable: 11/12 = 91.66666666666666 %

   - Tasksets **not** schedulable: 0/12 = 0.0 %

   - Tasksets exceeding level-criticality budget: 1/12 = 8.333333333333332 %

   - Tasksets exceeding safe boundary: 0/12 = 0.0 %

### Level 1.836

   Tasksets executed: 12

   - Tasksets actually schedulable: 10/12 = 83.33333333333334 %

   - Tasksets **not** schedulable: 0/12 = 0.0 %

   - Tasksets exceeding level-criticality budget: 2/12 = 16.666666666666664 %

   - Tasksets exceeding safe boundary: 0/12 = 0.0 %

### Level 1.848

   Tasksets executed: 17

   - Tasksets actually schedulable: 16/17 = 94.11764705882352 %

   - Tasksets **not** schedulable: 1/17 = 5.88235294117647 %

   - Tasksets exceeding level-criticality budget: 0/17 = 0.0 %

   - Tasksets exceeding safe boundary: 0/17 = 0.0 %

### Level 1.86

   Tasksets executed: 15

   - Tasksets actually schedulable: 10/15 = 66.66666666666666 %

   - Tasksets **not** schedulable: 1/15 = 6.666666666666667 %

   - Tasksets exceeding level-criticality budget: 4/15 = 26.666666666666668 %

   - Tasksets exceeding safe boundary: 0/15 = 0.0 %

### Level 1.872

   Tasksets executed: 13

   - Tasksets actually schedulable: 11/13 = 84.61538461538461 %

   - Tasksets **not** schedulable: 0/13 = 0.0 %

   - Tasksets exceeding level-criticality budget: 2/13 = 15.384615384615385 %

   - Tasksets exceeding safe boundary: 0/13 = 0.0 %

### Level 1.8840000000000001

   Tasksets executed: 18

   - Tasksets actually schedulable: 14/18 = 77.77777777777779 %

   - Tasksets **not** schedulable: 0/18 = 0.0 %

   - Tasksets exceeding level-criticality budget: 4/18 = 22.22222222222222 %

   - Tasksets exceeding safe boundary: 0/18 = 0.0 %

### Level 1.8960000000000001

   Tasksets executed: 22

   - Tasksets actually schedulable: 20/22 = 90.9090909090909 %

   - Tasksets **not** schedulable: 0/22 = 0.0 %

   - Tasksets exceeding level-criticality budget: 2/22 = 9.090909090909092 %

   - Tasksets exceeding safe boundary: 0/22 = 0.0 %

### Level 1.9080000000000001

   Tasksets executed: 17

   - Tasksets actually schedulable: 12/17 = 70.58823529411765 %

   - Tasksets **not** schedulable: 1/17 = 5.88235294117647 %

   - Tasksets exceeding level-criticality budget: 4/17 = 23.52941176470588 %

   - Tasksets exceeding safe boundary: 0/17 = 0.0 %

### Level 1.9200000000000002

   Tasksets executed: 17

   - Tasksets actually schedulable: 13/17 = 76.47058823529412 %

   - Tasksets **not** schedulable: 1/17 = 5.88235294117647 %

   - Tasksets exceeding level-criticality budget: 3/17 = 17.647058823529413 %

   - Tasksets exceeding safe boundary: 0/17 = 0.0 %

### Level 1.9320000000000002

   Tasksets executed: 13

   - Tasksets actually schedulable: 9/13 = 69.23076923076923 %

   - Tasksets **not** schedulable: 0/13 = 0.0 %

   - Tasksets exceeding level-criticality budget: 3/13 = 23.076923076923077 %

   - Tasksets exceeding safe boundary: 1/13 = 7.6923076923076925 %

### Level 1.9440000000000002

   Tasksets executed: 7

   - Tasksets actually schedulable: 7/7 = 100.0 %

   - Tasksets **not** schedulable: 0/7 = 0.0 %

   - Tasksets exceeding level-criticality budget: 0/7 = 0.0 %

   - Tasksets exceeding safe boundary: 0/7 = 0.0 %

### Level 1.9560000000000002

   Tasksets executed: 13

   - Tasksets actually schedulable: 11/13 = 84.61538461538461 %

   - Tasksets **not** schedulable: 1/13 = 7.6923076923076925 %

   - Tasksets exceeding level-criticality budget: 1/13 = 7.6923076923076925 %

   - Tasksets exceeding safe boundary: 0/13 = 0.0 %

### Level 1.9680000000000002

   Tasksets executed: 9

   - Tasksets actually schedulable: 9/9 = 100.0 %

   - Tasksets **not** schedulable: 0/9 = 0.0 %

   - Tasksets exceeding level-criticality budget: 0/9 = 0.0 %

   - Tasksets exceeding safe boundary: 0/9 = 0.0 %

### Level 1.9800000000000002

   Tasksets executed: 7

   - Tasksets actually schedulable: 5/7 = 71.42857142857143 %

   - Tasksets **not** schedulable: 0/7 = 0.0 %

   - Tasksets exceeding level-criticality budget: 2/7 = 28.57142857142857 %

   - Tasksets exceeding safe boundary: 0/7 = 0.0 %

### Level 1.9920000000000002

   Tasksets executed: 6

   - Tasksets actually schedulable: 4/6 = 66.66666666666666 %

   - Tasksets **not** schedulable: 0/6 = 0.0 %

   - Tasksets exceeding level-criticality budget: 2/6 = 33.33333333333333 %

   - Tasksets exceeding safe boundary: 0/6 = 0.0 %

### Level 2.004

   Tasksets executed: 3

   - Tasksets actually schedulable: 1/3 = 33.33333333333333 %

   - Tasksets **not** schedulable: 2/3 = 66.66666666666666 %

   - Tasksets exceeding level-criticality budget: 0/3 = 0.0 %

   - Tasksets exceeding safe boundary: 0/3 = 0.0 %

### Level 2.016

   Tasksets executed: 0

   - Tasksets actually schedulable: 0/0 = 0 %

   - Tasksets **not** schedulable: 0/0 = 0 %

   - Tasksets exceeding level-criticality budget: 0/0 = 0 %

   - Tasksets exceeding safe boundary: 0/0 = 0 %

### Level 2.028

   Tasksets executed: 2

   - Tasksets actually schedulable: 0/2 = 0.0 %

   - Tasksets **not** schedulable: 0/2 = 0.0 %

   - Tasksets exceeding level-criticality budget: 1/2 = 50.0 %

   - Tasksets exceeding safe boundary: 1/2 = 50.0 %

### Level 2.04

   Tasksets executed: 1

   - Tasksets actually schedulable: 0/1 = 0.0 %

   - Tasksets **not** schedulable: 0/1 = 0.0 %

   - Tasksets exceeding level-criticality budget: 1/1 = 100.0 %

   - Tasksets exceeding safe boundary: 0/1 = 0.0 %

### Level 2.052

   Tasksets executed: 1

   - Tasksets actually schedulable: 1/1 = 100.0 %

   - Tasksets **not** schedulable: 0/1 = 0.0 %

   - Tasksets exceeding level-criticality budget: 0/1 = 0.0 %

   - Tasksets exceeding safe boundary: 0/1 = 0.0 %

### Level 2.064

   Tasksets executed: 0

   - Tasksets actually schedulable: 0/0 = 0 %

   - Tasksets **not** schedulable: 0/0 = 0 %

   - Tasksets exceeding level-criticality budget: 0/0 = 0 %

   - Tasksets exceeding safe boundary: 0/0 = 0 %

### Level 2.076

   Tasksets executed: 0

   - Tasksets actually schedulable: 0/0 = 0 %

   - Tasksets **not** schedulable: 0/0 = 0 %

   - Tasksets exceeding level-criticality budget: 0/0 = 0 %

   - Tasksets exceeding safe boundary: 0/0 = 0 %

### Level 2.088

   Tasksets executed: 0

   - Tasksets actually schedulable: 0/0 = 0 %

   - Tasksets **not** schedulable: 0/0 = 0 %

   - Tasksets exceeding level-criticality budget: 0/0 = 0 %

   - Tasksets exceeding safe boundary: 0/0 = 0 %

### Level 2.1

   Tasksets executed: 0

   - Tasksets actually schedulable: 0/0 = 0 %

   - Tasksets **not** schedulable: 0/0 = 0 %

   - Tasksets exceeding level-criticality budget: 0/0 = 0 %

   - Tasksets exceeding safe boundary: 0/0 = 0 %

</details>


