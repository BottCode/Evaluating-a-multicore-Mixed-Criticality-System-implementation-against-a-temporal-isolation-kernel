# Report on Experiment 1

## Bad tasksets


### **Not schedulable tasksets**

Ovvero quando almeno un task non completa entra almeno una sua deadline.

  1. Taskset **e1_semi2wf_t123**

    Taskset execution params: {'id': 'e1_semi2wf_t123', 'size': '12', 'utilization': '1.812', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 5', 'period': 47250.0, 'C(LO)': 5343.0, 'C(HI)': 5343.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 2401', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003197853', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.352756276', 'avgresponsejitter': ' 0.002658889', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 0', 'timesmigrated': ' 9', 'timesrestored': ' 9', 'timesonc1': ' 2', 'timesonc2': ' 2397', 'lockedtime': ' 0.000043450'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU:  1

    {'id': ' 1', 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': ' 76.138110793'}



   CPU:  2

    {'id': ' 2', 'lowtohigh': ' 25', 'hightolow': ' 25', 'idletime': ' 84.337077829'}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 0', 'period': 504000.0, 'C(LO)': 76244.0, 'C(HI)': 152489.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 226', 'preemptions': ' 604', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.067970243', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 113.896006141', 'avgresponsejitter': ' 0.049972150', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 829', 'timesonc2': ' 0', 'lockedtime': ' 0.000014096'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 1', 'period': 129600.0, 'C(LO)': 17522.0, 'C(HI)': 35044.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 876', 'preemptions': ' 374', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.022491820', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.271757664', 'avgresponsejitter': ' 0.009821060', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1249', 'timesonc2': ' 0', 'lockedtime': ' 0.000004171'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 2', 'period': 67500.0, 'C(LO)': 1236.0, 'C(HI)': 2472.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1681', 'preemptions': ' 21', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.007666213', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.332506093', 'avgresponsejitter': ' 0.000668231', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1701', 'timesonc2': ' 0', 'lockedtime': ' 0.000005006'}



   Task:  0

    {'id': ' 0', 'basecpu': ' 1', 'priority': ' 5', 'period': 45360.0, 'C(LO)': 7256.0, 'C(HI)': 7256.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 0', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004354060', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.354646261', 'avgresponsejitter': ' 0.003945054', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2501', 'timesonc2': ' 0', 'lockedtime': ' 0.000026859'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 3', 'period': 81000.0, 'C(LO)': 8310.0, 'C(HI)': 8310.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1401', 'preemptions': ' 187', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.011802429', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.319006144', 'avgresponsejitter': ' 0.004611889', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1587', 'timesonc2': ' 0', 'lockedtime': ' 0.000007742'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 4', 'period': 65625.0, 'C(LO)': 5839.0, 'C(HI)': 5839.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1729', 'preemptions': ' 107', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.007789399', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.334381117', 'avgresponsejitter': ' 0.003129336', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1835', 'timesonc2': ' 0', 'lockedtime': ' 0.000010021'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 2', 'period': 118125.0, 'C(LO)': 19396.0, 'C(HI)': 38792.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 961', 'preemptions': ' 161', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.026534664', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.281881123', 'avgresponsejitter': ' 0.010144201', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 12', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1133', 'lockedtime': ' 0.000019748'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 0', 'period': 200000.0, 'C(LO)': 18907.0, 'C(HI)': 37814.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 568', 'preemptions': ' 233', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.034456757', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.200006099', 'avgresponsejitter': ' 0.011450541', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 6', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 806', 'lockedtime': ' 0.000012012'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 1', 'period': 151200.0, 'C(LO)': 13622.0, 'C(HI)': 27244.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 751', 'preemptions': ' 43', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.026796982', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.248806090', 'avgresponsejitter': ' 0.007317835', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 7', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 800', 'lockedtime': ' 0.000000700'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 5', 'period': 47250.0, 'C(LO)': 5343.0, 'C(HI)': 5343.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 2401', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003197853', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.352756276', 'avgresponsejitter': ' 0.002658889', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 0', 'timesmigrated': ' 9', 'timesrestored': ' 9', 'timesonc1': ' 2', 'timesonc2': ' 2397', 'lockedtime': ' 0.000043450'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 4', 'period': 56700.0, 'C(LO)': 1740.0, 'C(HI)': 1740.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 2001', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001048604', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.343306342', 'avgresponsejitter': ' 0.000869754', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 1', 'timesonc2': ' 1999', 'lockedtime': ' 0.000028147'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 3', 'period': 113400.0, 'C(LO)': 1069.0, 'C(HI)': 1069.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1001', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000643402', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.287600099', 'avgresponsejitter': ' 0.000535222', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1000', 'lockedtime': ' 0.000000000'}


   </details>

  2. Taskset **e1_semi2wf_t1328**

    Taskset execution params: {'id': 'e1_semi2wf_t1328', 'size': '12', 'utilization': '1.9560000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  0

    {'id': ' 0', 'basecpu': ' 1', 'priority': ' 7', 'period': 22500.0, 'C(LO)': 472.0, 'C(HI)': 472.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 0', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000286655', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 13.150009174', 'avgresponsejitter': ' 0.000255973', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 0', 'timesmigrated': ' 3', 'timesrestored': ' 2', 'timesonc1': ' 537', 'timesonc2': ' 3', 'lockedtime': ' 0.000001565'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU:  1

    {'id': ' 1', 'lowtohigh': ' 24', 'hightolow': ' 24', 'idletime': ' 83.932164805'}



   CPU:  2

    {'id': ' 2', 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': ' 74.654947336'}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 1', 'period': 200000.0, 'C(LO)': 24014.0, 'C(HI)': 48028.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 568', 'preemptions': ' 208', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.050419811', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.200006078', 'avgresponsejitter': ' 0.013744754', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 7', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 782', 'timesonc2': ' 0', 'lockedtime': ' 0.000015387'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 0', 'period': 405000.0, 'C(LO)': 47715.0, 'C(HI)': 95431.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 281', 'preemptions': ' 265', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.059044078', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 113.995006348', 'avgresponsejitter': ' 0.028558598', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 545', 'timesonc2': ' 0', 'lockedtime': ' 0.000013195'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 3', 'period': 70000.0, 'C(LO)': 2257.0, 'C(HI)': 4515.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1621', 'preemptions': ' 11', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.018363664', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.330006258', 'avgresponsejitter': ' 0.001209826', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 8', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1639', 'timesonc2': ' 0', 'lockedtime': ' 0.000004832'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 2', 'period': 162000.0, 'C(LO)': 5049.0, 'C(HI)': 10099.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 701', 'preemptions': ' 24', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.019239622', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.238006300', 'avgresponsejitter': ' 0.002614198', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 9', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 733', 'timesonc2': ' 0', 'lockedtime': ' 0.000001057'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 4', 'period': 181440.0, 'C(LO)': 29037.0, 'C(HI)': 29037.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 626', 'preemptions': ' 191', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.025034814', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.218566234', 'avgresponsejitter': ' 0.014900237', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 816', 'timesonc2': ' 0', 'lockedtime': ' 0.000032562'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 5', 'period': 94500.0, 'C(LO)': 14734.0, 'C(HI)': 14734.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 105', 'preemptions': ' 31', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.010024138', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 10.745881607', 'avgresponsejitter': ' 0.007561204', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 132', 'timesonc2': ' 3', 'lockedtime': ' 0.000001348'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 6', 'period': 60000.0, 'C(LO)': 2388.0, 'C(HI)': 2388.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1891', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001434769', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.340006288', 'avgresponsejitter': ' 0.001197637', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 3', 'timesrestored': ' 3', 'timesonc1': ' 1888', 'timesonc2': ' 3', 'lockedtime': ' 0.000011730'}



   Task:  0

    {'id': ' 0', 'basecpu': ' 1', 'priority': ' 7', 'period': 22500.0, 'C(LO)': 472.0, 'C(HI)': 472.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 0', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000286655', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 13.150009174', 'avgresponsejitter': ' 0.000255973', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 0', 'timesmigrated': ' 3', 'timesrestored': ' 2', 'timesonc1': ' 537', 'timesonc2': ' 3', 'lockedtime': ' 0.000001565'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 1', 'period': 56700.0, 'C(LO)': 16081.999999999998, 'C(HI)': 32165.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2001', 'preemptions': ' 354', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.011164838', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.343306084', 'avgresponsejitter': ' 0.008281850', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 2354', 'lockedtime': ' 0.000018607'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 2', 'period': 45360.0, 'C(LO)': 521.0, 'C(HI)': 1043.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2501', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000317354', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.354645976', 'avgresponsejitter': ' 0.000261018', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 2500', 'lockedtime': ' 0.000047309'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 0', 'period': 168750.0, 'C(LO)': 54296.0, 'C(HI)': 54296.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 673', 'preemptions': ' 1139', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.045185294', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.238870607', 'avgresponsejitter': ' 0.032107562', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1811', 'lockedtime': ' 0.000050264'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 3', 'period': 42000.0, 'C(LO)': 2711.0, 'C(HI)': 2711.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 2701', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001628339', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 114.358005949', 'avgresponsejitter': ' 0.001347237', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 2700', 'lockedtime': ' 0.000019649'}


   </details>


### **Criticality Level Budget Exceeded**

Ovvero quando un task di un taskset ha ecceduto il suo criticality-level budget, cioè un LO-crit task che eccede il suo LO-crit budget, oppure un HI-crit task che eccede il suo HI-crit budget.

  1. Taskset **e1_semi2wf_t1005**

    Taskset execution params: {'id': 'e1_semi2wf_t1005', 'size': '12', 'utilization': '1.9200000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 6', 'period': 42000.0, 'C(LO)': 5777.0, 'C(HI)': 5777.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 162', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003453180', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.720009384', 'avgresponsejitter': ' 0.002850844', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 4', 'timesonc2': ' 157', 'lockedtime': ' 0.000004210'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU:  1

    {'id': ' 1', 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': ' 3.867934045'}



   CPU:  2

    {'id': ' 2', 'lowtohigh': ' 4', 'hightolow': ' 4', 'idletime': ' 3.694375748'}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 3', 'period': 84375.0, 'C(LO)': 4074.9999999999995, 'C(HI)': 8149.999999999999, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 82', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002435216', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.750007787', 'avgresponsejitter': ' 0.002054156', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 81', 'timesonc2': ' 0', 'lockedtime': ' 0.000001219'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 2', 'period': 126000.0, 'C(LO)': 5303.0, 'C(HI)': 10606.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 55', 'preemptions': ' 4', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.005137054', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.681083336', 'avgresponsejitter': ' 0.002792658', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 58', 'timesonc2': ' 0', 'lockedtime': ' 0.000000646'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 0', 'period': 420000.0, 'C(LO)': 823.0, 'C(HI)': 1646.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 17', 'preemptions': ' 2', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002503144', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.314137610', 'avgresponsejitter': ' 0.000641225', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 18', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 1', 'period': 168000.0, 'C(LO)': 78400.0, 'C(HI)': 78400.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 41', 'preemptions': ' 38', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.051422048', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.567924312', 'avgresponsejitter': ' 0.041487126', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 78', 'timesonc2': ' 0', 'lockedtime': ' 0.000009946'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 4', 'period': 84000.0, 'C(LO)': 23574.0, 'C(HI)': 23574.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 82', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.014064159', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.722858940', 'avgresponsejitter': ' 0.011773186', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 81', 'timesonc2': ' 0', 'lockedtime': ' 0.000010754'}



   Task:  0

    {'id': ' 0', 'basecpu': ' 2', 'priority': ' 5', 'period': 28350.0, 'C(LO)': 1777.0, 'C(HI)': 3555.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 0', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003812562', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.747306183', 'avgresponsejitter': ' 0.001064003', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 241', 'lockedtime': ' 0.000000000'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 1', 'period': 168750.0, 'C(LO)': 4002.9999999999995, 'C(HI)': 8005.999999999999, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 42', 'preemptions': ' 5', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004871249', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.750006138', 'avgresponsejitter': ' 0.002172348', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 46', 'lockedtime': ' 0.000003006'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 4', 'period': 37800.0, 'C(LO)': 451.0, 'C(HI)': 903.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 180', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000571988', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.728407619', 'avgresponsejitter': ' 0.000233441', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 3', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 182', 'lockedtime': ' 0.000000000'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 3', 'period': 65625.0, 'C(LO)': 30476.0, 'C(HI)': 30476.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 104', 'preemptions': ' 114', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.022291988', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.693756450', 'avgresponsejitter': ' 0.016816315', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 217', 'lockedtime': ' 0.000005045'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 6', 'period': 42000.0, 'C(LO)': 5777.0, 'C(HI)': 5777.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 162', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003453180', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.720009384', 'avgresponsejitter': ' 0.002850844', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 4', 'timesonc2': ' 157', 'lockedtime': ' 0.000004210'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 945000.0, 'C(LO)': 126318.00000000001, 'C(HI)': 126318.00000000001, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 9', 'preemptions': ' 50', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.111264667', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.615582261', 'avgresponsejitter': ' 0.093886294', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 58', 'lockedtime': ' 0.000000000'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 2', 'period': 72000.0, 'C(LO)': 4002.9999999999995, 'C(HI)': 4002.9999999999995, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 95', 'preemptions': ' 15', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.020170483', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 7.708585474', 'avgresponsejitter': ' 0.002839673', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 109', 'lockedtime': ' 0.000000604'}


   </details>

  2. Taskset **e1_semi2wf_t1041**

    Taskset execution params: {'id': 'e1_semi2wf_t1041', 'size': '12', 'utilization': '1.9200000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 3', 'period': 64800.0, 'C(LO)': 4.0, 'C(HI)': 9.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 2', 'lockedtime': ' 0.000000165'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU:  1

    {'id': ' 1', 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': ' 0.000015613'}



   CPU:  2

    {'id': ' 2', 'lowtohigh': ' 1', 'hightolow': ' 0', 'idletime': ' 0.000016003'}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 4', 'period': 50400.0, 'C(LO)': 3022.0, 'C(HI)': 6045.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001323069', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.000989207', 'avgresponsejitter': ' 0.001323069', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 0', 'period': 900000.0, 'C(LO)': 33518.0, 'C(HI)': 67037.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 3', 'period': 54000.0, 'C(LO)': 1639.0, 'C(HI)': 3278.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000764090', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.002316682', 'avgresponsejitter': ' 0.000764090', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 2', 'period': 141750.0, 'C(LO)': 47262.0, 'C(HI)': 47262.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  0

    {'id': ' 0', 'basecpu': ' 1', 'priority': ' 5', 'period': 10000.0, 'C(LO)': 2214.0, 'C(HI)': 2214.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 0', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000967814', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.000016402', 'avgresponsejitter': ' 0.000967814', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 1', 'period': 175000.0, 'C(LO)': 20622.0, 'C(HI)': 20622.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 4', 'period': 52500.0, 'C(LO)': 4887.0, 'C(HI)': 9775.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002461186', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.001134387', 'avgresponsejitter': ' 0.002461186', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1', 'lockedtime': ' 0.000000000'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 2', 'period': 100800.0, 'C(LO)': 3358.0, 'C(HI)': 6716.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 3', 'period': 64800.0, 'C(LO)': 4.0, 'C(HI)': 9.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 2', 'lockedtime': ' 0.000000165'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 1', 'period': 189000.0, 'C(LO)': 92261.0, 'C(HI)': 92261.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 0', 'period': 648000.0, 'C(LO)': 93405.0, 'C(HI)': 93405.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 5', 'period': 20000.0, 'C(LO)': 2137.0, 'C(HI)': 2137.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 2', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001113048', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 1.000016781', 'avgresponsejitter': ' 0.001113048', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 1', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1', 'lockedtime': ' 0.000000270'}


   </details>

  3. Taskset **e1_semi2wf_t1143**

    Taskset execution params: {'id': 'e1_semi2wf_t1143', 'size': '12', 'utilization': '1.9320000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 2', 'period': 42000.0, 'C(LO)': 2825.0, 'C(HI)': 2825.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 854', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001696441', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 36.831256459', 'avgresponsejitter': ' 0.001413090', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 2', 'timesonc2': ' 851', 'lockedtime': ' 0.000017766'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU:  1

    {'id': ' 1', 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': ' 22.054139868'}



   CPU:  2

    {'id': ' 2', 'lowtohigh': ' 1', 'hightolow': ' 1', 'idletime': ' 25.018311949'}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 5', 'period': 60480.0, 'C(LO)': 3401.0, 'C(HI)': 6803.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 594', 'preemptions': ' 57', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.012578703', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 36.804166117', 'avgresponsejitter': ' 0.002095081', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 650', 'timesonc2': ' 0', 'lockedtime': ' 0.000002697'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 4', 'period': 63000.0, 'C(LO)': 3124.0, 'C(HI)': 6249.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 570', 'preemptions': ' 3', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003786147', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 36.784007399', 'avgresponsejitter': ' 0.001572438', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 572', 'timesonc2': ' 0', 'lockedtime': ' 0.000008012'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 3', 'period': 64800.0, 'C(LO)': 2379.0, 'C(HI)': 4758.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 554', 'preemptions': ' 48', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.012502781', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 36.769606138', 'avgresponsejitter': ' 0.001479565', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 601', 'timesonc2': ' 0', 'lockedtime': ' 0.000001159'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 2', 'period': 90000.0, 'C(LO)': 1238.0, 'C(HI)': 2476.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 400', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000745505', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 36.820007165', 'avgresponsejitter': ' 0.000618207', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 399', 'timesonc2': ' 0', 'lockedtime': ' 0.000000165'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 0', 'period': 700000.0, 'C(LO)': 3649.0, 'C(HI)': 7298.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 53', 'preemptions': ' 5', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.007050532', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 36.713279336', 'avgresponsejitter': ' 0.002219201', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 57', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  0

    {'id': ' 0', 'basecpu': ' 1', 'priority': ' 8', 'period': 26250.0, 'C(LO)': 9303.0, 'C(HI)': 9303.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 0', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.005568802', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 36.805008820', 'avgresponsejitter': ' 0.004320099', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1366', 'timesonc2': ' 0', 'lockedtime': ' 0.000012300'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 1', 'period': 180000.0, 'C(LO)': 24861.0, 'C(HI)': 24861.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 200', 'preemptions': ' 281', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.026929273', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 36.641725868', 'avgresponsejitter': ' 0.016003754', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 480', 'timesonc2': ' 0', 'lockedtime': ' 0.000003204'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 6', 'period': 105000.0, 'C(LO)': 9856.0, 'C(HI)': 9856.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 343', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.005885583', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 36.809621246', 'avgresponsejitter': ' 0.004936505', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 342', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 7', 'period': 35000.0, 'C(LO)': 659.0, 'C(HI)': 659.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1025', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000392414', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 36.809333763', 'avgresponsejitter': ' 0.000325126', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1024', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 840000.0, 'C(LO)': 354656.0, 'C(HI)': 709312.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 44', 'preemptions': ' 324', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.473398532', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 36.281203763', 'avgresponsejitter': ' 0.200238553', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 368', 'lockedtime': ' 0.000027931'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 1', 'period': 56250.0, 'C(LO)': 5173.0, 'C(HI)': 5173.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 638', 'preemptions': ' 30', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004663934', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 36.775006288', 'avgresponsejitter': ' 0.002638805', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 667', 'lockedtime': ' 0.000012631'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 2', 'period': 42000.0, 'C(LO)': 2825.0, 'C(HI)': 2825.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 854', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001696441', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 36.831256459', 'avgresponsejitter': ' 0.001413090', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 2', 'timesonc2': ' 851', 'lockedtime': ' 0.000017766'}


   </details>

  4. Taskset **e1_semi2wf_t1326**

    Taskset execution params: {'id': 'e1_semi2wf_t1326', 'size': '12', 'utilization': '1.9560000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  0

    {'id': ' 0', 'basecpu': ' 2', 'priority': ' 3', 'period': 20000.0, 'C(LO)': 2102.0, 'C(HI)': 2102.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 0', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001265919', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 19.300007063', 'avgresponsejitter': ' 0.001221453', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 3', 'timesonc2': ' 911', 'lockedtime': ' 0.000022559'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU:  1

    {'id': ' 1', 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': ' 11.095135703'}



   CPU:  2

    {'id': ' 2', 'lowtohigh': ' 1', 'hightolow': ' 1', 'idletime': ' 11.121409333'}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 0', 'period': 450000.0, 'C(LO)': 51661.0, 'C(HI)': 103323.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 42', 'preemptions': ' 84', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.045977673', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 19.001636619', 'avgresponsejitter': ' 0.035456541', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 125', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 4', 'period': 65625.0, 'C(LO)': 1782.0, 'C(HI)': 3565.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 280', 'preemptions': ' 7', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006590237', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 19.243756087', 'avgresponsejitter': ' 0.001006429', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 286', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 3', 'period': 72000.0, 'C(LO)': 1884.0, 'C(HI)': 3769.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 256', 'preemptions': ' 8', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006877192', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 19.288006204', 'avgresponsejitter': ' 0.001054568', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 263', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 2', 'period': 78750.0, 'C(LO)': 836.0, 'C(HI)': 1673.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 234', 'preemptions': ' 4', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006628216', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 19.279938411', 'avgresponsejitter': ' 0.000454538', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 237', 'timesonc2': ' 0', 'lockedtime': ' 0.000000402'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 1', 'period': 157500.0, 'C(LO)': 646.0, 'C(HI)': 1292.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 118', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001447279', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 19.286572910', 'avgresponsejitter': ' 0.000331330', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 118', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 5', 'period': 52500.0, 'C(LO)': 17353.0, 'C(HI)': 17353.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 350', 'preemptions': ' 117', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.016645036', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 19.270007928', 'avgresponsejitter': ' 0.009861111', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 466', 'timesonc2': ' 0', 'lockedtime': ' 0.000007565'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 7', 'period': 45360.0, 'C(LO)': 10482.0, 'C(HI)': 10482.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 405', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006290562', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 19.280086574', 'avgresponsejitter': ' 0.005245730', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 404', 'timesonc2': ' 0', 'lockedtime': ' 0.000008255'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 6', 'period': 50000.0, 'C(LO)': 1875.0, 'C(HI)': 1875.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 368', 'preemptions': ' 7', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.007327171', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 19.300006192', 'avgresponsejitter': ' 0.001049282', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 374', 'timesonc2': ' 0', 'lockedtime': ' 0.000007447'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 600000.0, 'C(LO)': 134855.0, 'C(HI)': 269710.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 32', 'preemptions': ' 133', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.227187276', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 19.025157117', 'avgresponsejitter': ' 0.086904303', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 165', 'lockedtime': ' 0.000005988'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 2', 'period': 100000.0, 'C(LO)': 25109.0, 'C(HI)': 25109.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 184', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.015040306', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 19.200008285', 'avgresponsejitter': ' 0.012586435', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 183', 'lockedtime': ' 0.000001369'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 1', 'period': 112500.0, 'C(LO)': 20853.0, 'C(HI)': 20853.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 164', 'preemptions': ' 98', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.013632544', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 19.225006508', 'avgresponsejitter': ' 0.011094249', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 261', 'lockedtime': ' 0.000001414'}



   Task:  0

    {'id': ' 0', 'basecpu': ' 2', 'priority': ' 3', 'period': 20000.0, 'C(LO)': 2102.0, 'C(HI)': 2102.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 0', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001265919', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 19.300007063', 'avgresponsejitter': ' 0.001221453', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 3', 'timesonc2': ' 911', 'lockedtime': ' 0.000022559'}


   </details>

  5. Taskset **e1_semi2wf_t1549**

    Taskset execution params: {'id': 'e1_semi2wf_t1549', 'size': '12', 'utilization': '1.9800000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 7', 'period': 101250.0, 'C(LO)': 11.0, 'C(HI)': 11.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU:  1

    {'id': ' 1', 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': ' 0.000017363'}



   CPU:  2

    {'id': ' 2', 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': ' 0.000013679'}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 4', 'period': 37800.0, 'C(LO)': 4521.0, 'C(HI)': 9043.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 2', 'period': 67500.0, 'C(LO)': 4834.0, 'C(HI)': 9668.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 3', 'period': 50400.0, 'C(LO)': 2146.0, 'C(HI)': 4292.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  0

    {'id': ' 0', 'basecpu': ' 1', 'priority': ' 5', 'period': 22500.0, 'C(LO)': 305.0, 'C(HI)': 611.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 0', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 1', 'period': 105000.0, 'C(LO)': 806.0, 'C(HI)': 1613.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 0', 'period': 405000.0, 'C(LO)': 178628.0, 'C(HI)': 178628.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 6', 'period': 112500.0, 'C(LO)': 2457.0, 'C(HI)': 2457.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 7', 'period': 101250.0, 'C(LO)': 11.0, 'C(HI)': 11.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 2', 'period': 84375.0, 'C(LO)': 21891.0, 'C(HI)': 43782.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 1', 'period': 200000.0, 'C(LO)': 44839.0, 'C(HI)': 44839.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 945000.0, 'C(LO)': 138592.0, 'C(HI)': 138592.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 3', 'period': 180000.0, 'C(LO)': 21064.0, 'C(HI)': 21064.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000000000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 0.000000000', 'avgresponsejitter': ' 0.000000000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1', 'lockedtime': ' 0.000000000'}


   </details>

  6. Taskset **e1_semi2wf_t1873**

    Taskset execution params: {'id': 'e1_semi2wf_t1873', 'size': '12', 'utilization': '2.016', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 5', 'period': 20000.0, 'C(LO)': 1453.0, 'C(HI)': 1453.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 540', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000875994', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 11.795686934', 'avgresponsejitter': ' 0.000727667', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 537', 'timesonc2': ' 2', 'lockedtime': ' 0.000032874'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU:  1

    {'id': ' 1', 'lowtohigh': ' 8', 'hightolow': ' 8', 'idletime': ' 6.413113553'}



   CPU:  2

    {'id': ' 2', 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': ' 6.765223988'}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 3', 'period': 45360.0, 'C(LO)': 5355.0, 'C(HI)': 10710.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 239', 'preemptions': ' 35', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.007502123', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 11.750326628', 'avgresponsejitter': ' 0.002891964', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 5', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 278', 'timesonc2': ' 0', 'lockedtime': ' 0.000010751'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 2', 'period': 54000.0, 'C(LO)': 5392.0, 'C(HI)': 10785.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 201', 'preemptions': ' 32', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.010334574', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 11.746006757', 'avgresponsejitter': ' 0.002985447', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 3', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 235', 'timesonc2': ' 0', 'lockedtime': ' 0.000006589'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 1', 'period': 84375.0, 'C(LO)': 3337.0, 'C(HI)': 6674.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 129', 'preemptions': ' 12', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.009024072', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 11.715631706', 'avgresponsejitter': ' 0.001899988', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 140', 'timesonc2': ' 0', 'lockedtime': ' 0.000004829'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 0', 'period': 756000.0, 'C(LO)': 304736.0, 'C(HI)': 304736.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 16', 'preemptions': ' 272', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.223015267', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 11.588299817', 'avgresponsejitter': ' 0.190821000', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 287', 'timesonc2': ' 0', 'lockedtime': ' 0.000036853'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 5', 'period': 20000.0, 'C(LO)': 1453.0, 'C(HI)': 1453.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 540', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000875994', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 11.795686934', 'avgresponsejitter': ' 0.000727667', 'deadlinesmissed': ' 1', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 537', 'timesonc2': ' 2', 'lockedtime': ' 0.000032874'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 4', 'period': 84000.0, 'C(LO)': 2746.0, 'C(HI)': 2746.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 130', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001643474', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 11.752006931', 'avgresponsejitter': ' 0.001393339', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 129', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 2', 'period': 140000.0, 'C(LO)': 17269.0, 'C(HI)': 34538.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 79', 'preemptions': ' 35', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.025120240', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 11.780697111', 'avgresponsejitter': ' 0.009985841', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 113', 'lockedtime': ' 0.000001568'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 0', 'period': 590625.0, 'C(LO)': 50382.0, 'C(HI)': 100764.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 20', 'preemptions': ' 66', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.064985553', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 11.635314360', 'avgresponsejitter': ' 0.035909562', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 85', 'lockedtime': ' 0.000005459'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 1', 'period': 196875.0, 'C(LO)': 8759.0, 'C(HI)': 17519.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 56', 'preemptions': ' 33', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.022145111', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 11.631257000', 'avgresponsejitter': ' 0.005620258', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 88', 'lockedtime': ' 0.000003009'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 3', 'period': 151200.0, 'C(LO)': 27232.0, 'C(HI)': 27232.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 73', 'preemptions': ' 121', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.023203027', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 11.737505438', 'avgresponsejitter': ' 0.015924243', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 193', 'lockedtime': ' 0.000013297'}



   Task:  0

    {'id': ' 0', 'basecpu': ' 2', 'priority': ' 5', 'period': 10000.0, 'C(LO)': 1700.0, 'C(HI)': 1700.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 0', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001025769', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 11.790006030', 'avgresponsejitter': ' 0.000760718', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 1080', 'lockedtime': ' 0.000050495'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 4', 'period': 67500.0, 'C(LO)': 9185.0, 'C(HI)': 9185.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 161', 'preemptions': ' 46', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006322721', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 11.732505883', 'avgresponsejitter': ' 0.004814057', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 206', 'lockedtime': ' 0.000004309'}


   </details>

  7. Taskset **e1_semi2wf_t457**

    Taskset execution params: {'id': 'e1_semi2wf_t457', 'size': '12', 'utilization': '1.848', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  0

    {'id': ' 0', 'basecpu': ' 1', 'priority': ' 6', 'period': 15750.0, 'C(LO)': 1024.0, 'C(HI)': 1024.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 0', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000617886', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.835515216', 'avgresponsejitter': ' 0.000506805', 'deadlinesmissed': ' 3', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 175', 'timesonc2': ' 3', 'lockedtime': ' 0.000001444'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU:  1

    {'id': ' 1', 'lowtohigh': ' 3', 'hightolow': ' 3', 'idletime': ' 1.635668847'}



   CPU:  2

    {'id': ' 2', 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': ' 1.880988051'}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 0', 'period': 900000.0, 'C(LO)': 98553.0, 'C(HI)': 197107.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 5', 'preemptions': ' 20', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.096565444', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.700081165', 'avgresponsejitter': ' 0.058609838', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 24', 'timesonc2': ' 0', 'lockedtime': ' 0.000000790'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 1', 'period': 567000.0, 'C(LO)': 19860.0, 'C(HI)': 39720.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 6', 'preemptions': ' 8', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.013779934', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.322498213', 'avgresponsejitter': ' 0.010291628', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 13', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 2', 'period': 200000.0, 'C(LO)': 2847.0, 'C(HI)': 5694.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 16', 'preemptions': ' 3', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002000465', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.800006976', 'avgresponsejitter': ' 0.001502517', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 18', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 4', 'period': 33750.0, 'C(LO)': 122.0, 'C(HI)': 245.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 85', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000169802', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.801256832', 'avgresponsejitter': ' 0.000068889', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 3', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 87', 'timesonc2': ' 0', 'lockedtime': ' 0.000001084'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 3', 'period': 162000.0, 'C(LO)': 87959.0, 'C(HI)': 87959.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 19', 'preemptions': ' 75', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.055484868', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.754006607', 'avgresponsejitter': ' 0.044409511', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 93', 'timesonc2': ' 0', 'lockedtime': ' 0.000001934'}



   Task:  0

    {'id': ' 0', 'basecpu': ' 1', 'priority': ' 6', 'period': 15750.0, 'C(LO)': 1024.0, 'C(HI)': 1024.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 0', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000617886', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.835515216', 'avgresponsejitter': ' 0.000506805', 'deadlinesmissed': ' 3', 'budgetexceeded': ' 1', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 175', 'timesonc2': ' 3', 'lockedtime': ' 0.000001444'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 5', 'period': 56700.0, 'C(LO)': 3206.0, 'C(HI)': 3206.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 51', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001922000', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.788219535', 'avgresponsejitter': ' 0.001582243', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 49', 'timesonc2': ' 1', 'lockedtime': ' 0.000000000'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 2', 'period': 70875.0, 'C(LO)': 10230.0, 'C(HI)': 20461.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 41', 'preemptions': ' 6', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.010382261', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.765150135', 'avgresponsejitter': ' 0.005550943', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 46', 'lockedtime': ' 0.000001850'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 0', 'period': 189000.0, 'C(LO)': 6473.0, 'C(HI)': 12947.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 16', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.025118297', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.646007162', 'avgresponsejitter': ' 0.004564171', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 16', 'lockedtime': ' 0.000000538'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 1', 'period': 168750.0, 'C(LO)': 51749.0, 'C(HI)': 51749.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 18', 'preemptions': ' 12', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.039024715', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.700006655', 'avgresponsejitter': ' 0.027558444', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 29', 'lockedtime': ' 0.000001778'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 4', 'period': 84000.0, 'C(LO)': 9264.0, 'C(HI)': 9264.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 35', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.005365817', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.772599432', 'avgresponsejitter': ' 0.004615150', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 34', 'lockedtime': ' 0.000002898'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 3', 'period': 87500.0, 'C(LO)': 7392.0, 'C(HI)': 7392.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 34', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.008513462', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 3.800006129', 'avgresponsejitter': ' 0.003871414', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 34', 'lockedtime': ' 0.000001066'}


   </details>

  8. Taskset **e1_semi2wf_t705**

    Taskset execution params: {'id': 'e1_semi2wf_t705', 'size': '12', 'utilization': '1.8840000000000001', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the guilty tasks list.</summary>

   Time values are expressed as **micro-seconds**.

Task:  0

    {'id': ' 0', 'basecpu': ' 2', 'priority': ' 4', 'period': 25200.0, 'C(LO)': 2219.0, 'C(HI)': 2219.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 0', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001336042', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 31.801310096', 'avgresponsejitter': ' 0.000914174', 'deadlinesmissed': ' 2', 'budgetexceeded': ' 1', 'timesmigrated': ' 5', 'timesrestored': ' 5', 'timesonc1': ' 4', 'timesonc2': ' 1216', 'lockedtime': ' 0.000009667'}


   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU:  1

    {'id': ' 1', 'lowtohigh': ' 0', 'hightolow': ' 0', 'idletime': ' 20.514185508'}



   CPU:  2

    {'id': ' 2', 'lowtohigh': ' 9', 'hightolow': ' 9', 'idletime': ' 19.936994979'}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 2', 'period': 140000.0, 'C(LO)': 12792.0, 'C(HI)': 25584.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 221', 'preemptions': ' 44', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.026196204', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 31.663214934', 'avgresponsejitter': ' 0.007747526', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 264', 'timesonc2': ' 0', 'lockedtime': ' 0.000004120'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 1', 'period': 151200.0, 'C(LO)': 11968.0, 'C(HI)': 23936.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 205', 'preemptions': ' 65', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.014840562', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 31.694515895', 'avgresponsejitter': ' 0.006954688', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 269', 'timesonc2': ' 0', 'lockedtime': ' 0.000011970'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 1', 'priority': ' 0', 'period': 907200.0, 'C(LO)': 58185.0, 'C(HI)': 116371.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 35', 'preemptions': ' 62', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.052282174', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 30.955541670', 'avgresponsejitter': ' 0.035746514', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 96', 'timesonc2': ' 0', 'lockedtime': ' 0.000004303'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 3', 'period': 108000.0, 'C(LO)': 5166.0, 'C(HI)': 10332.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 287', 'preemptions': ' 30', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.008668742', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 31.780006117', 'avgresponsejitter': ' 0.002858697', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 316', 'timesonc2': ' 0', 'lockedtime': ' 0.000003264'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 5', 'period': 56250.0, 'C(LO)': 9843.0, 'C(HI)': 9843.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 549', 'preemptions': ' 68', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006952544', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 31.768756444', 'avgresponsejitter': ' 0.005062069', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 616', 'timesonc2': ' 0', 'lockedtime': ' 0.000011144'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 1', 'priority': ' 4', 'period': 181440.0, 'C(LO)': 27189.0, 'C(HI)': 27189.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 171', 'preemptions': ' 109', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.021930237', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 31.663366733', 'avgresponsejitter': ' 0.015034928', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 279', 'timesonc2': ' 0', 'lockedtime': ' 0.000012087'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 6', 'period': 35000.0, 'C(LO)': 2074.0, 'C(HI)': 2074.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 882', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001244832', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 31.800007369', 'avgresponsejitter': ' 0.001039805', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 881', 'timesonc2': ' 0', 'lockedtime': ' 0.000009237'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 2', 'priority': ' 0', 'period': 200000.0, 'C(LO)': 49115.0, 'C(HI)': 98230.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 155', 'preemptions': ' 226', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.098625820', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 31.601279961', 'avgresponsejitter': ' 0.030626622', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 4', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 384', 'lockedtime': ' 0.000015631'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 1', 'period': 87500.0, 'C(LO)': 335.0, 'C(HI)': 671.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 353', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001135634', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 31.713757369', 'avgresponsejitter': ' 0.000175670', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 5', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 358', 'lockedtime': ' 0.000000000'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 2', 'period': 175000.0, 'C(LO)': 56315.0, 'C(HI)': 56315.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 177', 'preemptions': ' 244', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.037703916', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 31.625007883', 'avgresponsejitter': ' 0.030285868', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 420', 'lockedtime': ' 0.000028991'}



   Task:  0

    {'id': ' 0', 'basecpu': ' 2', 'priority': ' 4', 'period': 25200.0, 'C(LO)': 2219.0, 'C(HI)': 2219.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 0', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001336042', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 31.801310096', 'avgresponsejitter': ' 0.000914174', 'deadlinesmissed': ' 2', 'budgetexceeded': ' 1', 'timesmigrated': ' 5', 'timesrestored': ' 5', 'timesonc1': ' 4', 'timesonc2': ' 1216', 'lockedtime': ' 0.000009667'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 3', 'period': 112500.0, 'C(LO)': 2939.0, 'C(HI)': 2939.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 275', 'preemptions': ' 10', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003071790', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 31.712507547', 'avgresponsejitter': ' 0.001512006', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 284', 'lockedtime': ' 0.000025297'}


   </details>


### **Safe Boundary Exceeded**

Ovvero quando un taskset ha troppi core (2 nel contesto dual-core) eseguenti in HI-crit mode.

  1. Taskset **e1_semi2wf_t1391**

    Taskset execution params: {'id': 'e1_semi2wf_t1391', 'size': '12', 'utilization': '1.9560000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU:  1

    {'id': ' 1', 'lowtohigh': ' 36', 'hightolow': ' 35', 'idletime': ' 63.834118495'}



   CPU:  2

    {'id': ' 2', 'lowtohigh': ' 11', 'hightolow': ' 10', 'idletime': ' 67.264203357'}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 1', 'period': 112500.0, 'C(LO)': 23126.0, 'C(HI)': 46252.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 835', 'preemptions': ' 394', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.039873835', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 94.712506201', 'avgresponsejitter': ' 0.013561435', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 9', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1237', 'timesonc2': ' 0', 'lockedtime': ' 0.000030108'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 0', 'period': 504000.0, 'C(LO)': 53414.0, 'C(HI)': 106829.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 188', 'preemptions': ' 189', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.097711940', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 94.744488664', 'avgresponsejitter': ' 0.035150661', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 2', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 378', 'timesonc2': ' 0', 'lockedtime': ' 0.000009294'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 2', 'period': 47250.0, 'C(LO)': 825.0, 'C(HI)': 1651.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 1987', 'preemptions': ' 1', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001067604', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 94.791256081', 'avgresponsejitter': ' 0.000417922', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 25', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 2012', 'timesonc2': ' 0', 'lockedtime': ' 0.000004838'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 1', 'priority': ' 3', 'period': 64800.0, 'C(LO)': 17872.0, 'C(HI)': 17872.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 1450', 'preemptions': ' 124', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.011986480', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 94.830406952', 'avgresponsejitter': ' 0.009039087', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 1573', 'timesonc2': ' 0', 'lockedtime': ' 0.000043039'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 4', 'period': 63000.0, 'C(LO)': 2287.0, 'C(HI)': 2287.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1019', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001372312', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 65.071006390', 'avgresponsejitter': ' 0.001148345', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 1017', 'timesonc2': ' 1', 'lockedtime': ' 0.000005844'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 2', 'period': 140000.0, 'C(LO)': 31203.0, 'C(HI)': 62406.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 671', 'preemptions': ' 273', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.045845553', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 94.660006033', 'avgresponsejitter': ' 0.017218339', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 5', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 948', 'lockedtime': ' 0.000037835'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 525000.0, 'C(LO)': 37520.0, 'C(HI)': 75041.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 180', 'preemptions': ' 128', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.070672805', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 94.450005949', 'avgresponsejitter': ' 0.021949502', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 3', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 310', 'lockedtime': ' 0.000011697'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 1', 'period': 189000.0, 'C(LO)': 9933.0, 'C(HI)': 19866.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 498', 'preemptions': ' 35', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.023147003', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 94.749218634', 'avgresponsejitter': ' 0.005196877', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 3', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 535', 'lockedtime': ' 0.000016138'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 2', 'priority': ' 4', 'period': 108000.0, 'C(LO)': 12403.0, 'C(HI)': 12403.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 870', 'preemptions': ' 69', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.010417399', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 94.744006958', 'avgresponsejitter': ' 0.006307438', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 938', 'lockedtime': ' 0.000027691'}



   Task:  0

    {'id': ' 0', 'basecpu': ' 2', 'priority': ' 6', 'period': 40000.0, 'C(LO)': 4448.0, 'C(HI)': 4448.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 0', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002671096', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 27.600007132', 'avgresponsejitter': ' 0.002375414', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 1', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 666', 'lockedtime': ' 0.000006931'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 2', 'priority': ' 3', 'period': 129600.0, 'C(LO)': 5561.0, 'C(HI)': 5561.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 726', 'preemptions': ' 17', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.005840126', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 94.830407267', 'avgresponsejitter': ' 0.002827613', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 742', 'lockedtime': ' 0.000049883'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 5', 'period': 90720.0, 'C(LO)': 2090.0, 'C(HI)': 2090.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1036', 'preemptions': ' 7', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003502093', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 94.804486637', 'avgresponsejitter': ' 0.001057492', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 2', 'timesrestored': ' 2', 'timesonc1': ' 0', 'timesonc2': ' 1042', 'lockedtime': ' 0.000017667'}


   </details>

  2. Taskset **e1_semi2wf_t1633**

    Taskset execution params: {'id': 'e1_semi2wf_t1633', 'size': '12', 'utilization': '1.9920000000000002', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU:  1

    {'id': ' 1', 'lowtohigh': ' 14', 'hightolow': ' 13', 'idletime': ' 42.514142856'}



   CPU:  2

    {'id': ' 2', 'lowtohigh': ' 26', 'hightolow': ' 25', 'idletime': ' 42.764535144'}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 2', 'period': 129600.0, 'C(LO)': 20858.0, 'C(HI)': 41717.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 498', 'preemptions': ' 215', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.027788120', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 65.281606297', 'avgresponsejitter': ' 0.010955550', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 4', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 716', 'timesonc2': ' 0', 'lockedtime': ' 0.000002967'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 1', 'priority': ' 1', 'period': 150000.0, 'C(LO)': 21856.0, 'C(HI)': 43712.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 430', 'preemptions': ' 306', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.039346390', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 65.200006186', 'avgresponsejitter': ' 0.012493526', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 4', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 739', 'timesonc2': ' 0', 'lockedtime': ' 0.000016303'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 3', 'period': 90720.0, 'C(LO)': 36.0, 'C(HI)': 73.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 710', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000063396', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 65.229766450', 'avgresponsejitter': ' 0.000023940', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 6', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 715', 'timesonc2': ' 0', 'lockedtime': ' 0.000000000'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 0', 'period': 405000.0, 'C(LO)': 111675.0, 'C(HI)': 111675.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 160', 'preemptions': ' 627', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.105590835', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 64.990006453', 'avgresponsejitter': ' 0.067170535', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 786', 'timesonc2': ' 0', 'lockedtime': ' 0.000026547'}



   Task:  0

    {'id': ' 0', 'basecpu': ' 1', 'priority': ' 5', 'period': 25200.0, 'C(LO)': 2189.0, 'C(HI)': 2189.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 0', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.001312462', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 65.285207108', 'avgresponsejitter': ' 0.000888604', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 5', 'timesrestored': ' 4', 'timesonc1': ' 2552', 'timesonc2': ' 0', 'lockedtime': ' 0.000026601'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 1', 'priority': ' 4', 'period': 63000.0, 'C(LO)': 103.0, 'C(HI)': 103.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 1022', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.000068282', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 65.261022727', 'avgresponsejitter': ' 0.000055946', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 1', 'timesrestored': ' 0', 'timesonc1': ' 1021', 'timesonc2': ' 0', 'lockedtime': ' 0.000001108'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 1', 'period': 151200.0, 'C(LO)': 34204.0, 'C(HI)': 68408.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 426', 'preemptions': ' 284', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.051499643', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 65.108807276', 'avgresponsejitter': ' 0.020157577', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 4', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 713', 'lockedtime': ' 0.000029342'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 2', 'priority': ' 3', 'period': 70000.0, 'C(LO)': 5546.0, 'C(HI)': 11092.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 920', 'preemptions': ' 51', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.014948616', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 65.260008742', 'avgresponsejitter': ' 0.003139030', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 14', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 984', 'lockedtime': ' 0.000008228'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 2', 'priority': ' 2', 'period': 81000.0, 'C(LO)': 3497.0, 'C(HI)': 6994.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 795', 'preemptions': ' 13', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.005269180', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 65.233006183', 'avgresponsejitter': ' 0.001821514', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 8', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 815', 'lockedtime': ' 0.000019072'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 5', 'period': 70875.0, 'C(LO)': 16097.0, 'C(HI)': 16097.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 909', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.009662429', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 65.283631730', 'avgresponsejitter': ' 0.008035375', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 0', 'timesonc2': ' 908', 'lockedtime': ' 0.000013640'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 945000.0, 'C(LO)': 52681.0, 'C(HI)': 52681.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 69', 'preemptions': ' 56', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.064560033', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 64.315007270', 'avgresponsejitter': ' 0.030462198', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 124', 'lockedtime': ' 0.000000553'}



   Task:  6

    {'id': ' 6', 'basecpu': ' 2', 'priority': ' 4', 'period': 113400.0, 'C(LO)': 3796.0, 'C(HI)': 3796.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 569', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002279003', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 65.297806511', 'avgresponsejitter': ' 0.001895018', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 568', 'lockedtime': ' 0.000016973'}


   </details>

  3. Taskset **e1_semi2wf_t2088**

    Taskset execution params: {'id': 'e1_semi2wf_t2088', 'size': '12', 'utilization': '2.04', 'criticality_factor': '2', 'hicrit_proportion': '0.5'}

   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.



   CPU:  1

    {'id': ' 1', 'lowtohigh': ' 15', 'hightolow': ' 14', 'idletime': ' 11.850836168'}



   CPU:  2

    {'id': ' 2', 'lowtohigh': ' 15', 'hightolow': ' 14', 'idletime': ' 12.115054754'}


   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  6

    {'id': ' 6', 'basecpu': ' 1', 'priority': ' 2', 'period': 63000.0, 'C(LO)': 8697.0, 'C(HI)': 17395.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 304', 'preemptions': ' 103', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.017635937', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 20.026006231', 'avgresponsejitter': ' 0.004993381', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 4', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 410', 'timesonc2': ' 0', 'lockedtime': ' 0.000006168'}



   Task:  2

    {'id': ' 2', 'basecpu': ' 1', 'priority': ' 4', 'period': 22500.0, 'C(LO)': 2720.0, 'C(HI)': 5440.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 847', 'preemptions': ' 69', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006393192', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 20.012506117', 'avgresponsejitter': ' 0.001552471', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 7', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 922', 'timesonc2': ' 0', 'lockedtime': ' 0.000015306'}



   Task:  5

    {'id': ' 5', 'basecpu': ' 1', 'priority': ' 3', 'period': 60000.0, 'C(LO)': 1062.0, 'C(HI)': 2125.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 319', 'preemptions': ' 16', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003928495', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 20.020006126', 'avgresponsejitter': ' 0.000645931', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 3', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 337', 'timesonc2': ' 0', 'lockedtime': ' 0.000004766'}



   Task:  7

    {'id': ' 7', 'basecpu': ' 1', 'priority': ' 1', 'period': 72000.0, 'C(LO)': 495.0, 'C(HI)': 990.9999999999999, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 266', 'preemptions': ' 3', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003077042', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 20.009051751', 'avgresponsejitter': ' 0.000272568', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 1', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 269', 'timesonc2': ' 0', 'lockedtime': ' 0.000000402'}



   Task:  0

    {'id': ' 0', 'basecpu': ' 1', 'priority': ' 6', 'period': 18900.0, 'C(LO)': 3647.0, 'C(HI)': 3647.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 0', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.002196024', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 20.032306294', 'avgresponsejitter': ' 0.001795772', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 5', 'timesrestored': ' 4', 'timesonc1': ' 1006', 'timesonc2': ' 2', 'lockedtime': ' 0.000014781'}



   Task:  10

    {'id': ' 10', 'basecpu': ' 1', 'priority': ' 0', 'period': 196875.0, 'C(LO)': 28346.0, 'C(HI)': 28346.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 98', 'preemptions': ' 236', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.030943339', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 19.907528315', 'avgresponsejitter': ' 0.019889282', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 333', 'timesonc2': ' 0', 'lockedtime': ' 0.000015970'}



   Task:  4

    {'id': ' 4', 'basecpu': ' 1', 'priority': ' 5', 'period': 45360.0, 'C(LO)': 5635.0, 'C(HI)': 5635.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 421', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.003373051', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 20.005846357', 'avgresponsejitter': ' 0.002820354', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 420', 'timesonc2': ' 0', 'lockedtime': ' 0.000011165'}



   Task:  1

    {'id': ' 1', 'basecpu': ' 2', 'priority': ' 3', 'period': 20000.0, 'C(LO)': 4223.0, 'C(HI)': 8447.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 953', 'preemptions': ' 22', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.006445114', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 20.020006841', 'avgresponsejitter': ' 0.002232559', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 11', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 985', 'lockedtime': ' 0.000027336'}



   Task:  3

    {'id': ' 3', 'basecpu': ' 2', 'priority': ' 2', 'period': 33750.0, 'C(LO)': 2838.0, 'C(HI)': 5676.0, 'criticality': 'HIGH', 'migrable': 'False', 'completedruns': ' 565', 'preemptions': ' 37', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.007149913', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 20.001987802', 'avgresponsejitter': ' 0.001596796', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 4', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 605', 'lockedtime': ' 0.000020877'}



   Task:  11

    {'id': ' 11', 'basecpu': ' 2', 'priority': ' 0', 'period': 840000.0, 'C(LO)': 161918.0, 'C(HI)': 161918.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 24', 'preemptions': ' 195', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.135572835', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 19.482448456', 'avgresponsejitter': ' 0.105760351', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 218', 'lockedtime': ' 0.000020228'}



   Task:  9

    {'id': ' 9', 'basecpu': ' 2', 'priority': ' 1', 'period': 181440.0, 'C(LO)': 24566.0, 'C(HI)': 24566.0, 'criticality': 'LOW', 'migrable': 'False', 'completedruns': ' 106', 'preemptions': ' 107', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.021093105', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 19.869766414', 'avgresponsejitter': ' 0.014761339', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 0', 'timesrestored': ' 0', 'timesonc1': ' 0', 'timesonc2': ' 212', 'lockedtime': ' 0.000016958'}



   Task:  8

    {'id': ' 8', 'basecpu': ' 2', 'priority': ' 4', 'period': 75600.0, 'C(LO)': 7025.0, 'C(HI)': 7025.0, 'criticality': 'LOW', 'migrable': 'True', 'completedruns': ' 253', 'preemptions': ' 0', 'minresponsejitter': ' 0.000000000', 'maxresponsejitter': ' 0.004204081', 'minreleasejitter': ' 0.000000000', 'maxreleasejitter': ' 19.975606210', 'avgresponsejitter': ' 0.003482964', 'deadlinesmissed': ' 0', 'budgetexceeded': ' 0', 'timesmigrated': ' 1', 'timesrestored': ' 1', 'timesonc1': ' 1', 'timesonc2': ' 251', 'lockedtime': ' 0.000017114'}


   </details>


## Focus for each Utilization level.

### Level 1.8

   Tasksets executed: 4

   - Tasksets actually schedulable: 4/4 = 100.0 %

   - Tasksets **not** schedulable: 0/4 = 0.0 %

   - Tasksets exceeding level-criticality budget: 0/4 = 0.0 %

   - Tasksets exceeding safe boundary: 0/4 = 0.0 %

### Level 1.812

   Tasksets executed: 3

   - Tasksets actually schedulable: 2/3 = 66.66666666666666 %

   - Tasksets **not** schedulable: 1/3 = 33.33333333333333 %

   - Tasksets exceeding level-criticality budget: 0/3 = 0.0 %

   - Tasksets exceeding safe boundary: 0/3 = 0.0 %

### Level 1.824

   Tasksets executed: 4

   - Tasksets actually schedulable: 4/4 = 100.0 %

   - Tasksets **not** schedulable: 0/4 = 0.0 %

   - Tasksets exceeding level-criticality budget: 0/4 = 0.0 %

   - Tasksets exceeding safe boundary: 0/4 = 0.0 %

### Level 1.836

   Tasksets executed: 0

   - Tasksets actually schedulable: 0/0 = 0 %

   - Tasksets **not** schedulable: 0/0 = 0 %

   - Tasksets exceeding level-criticality budget: 0/0 = 0 %

   - Tasksets exceeding safe boundary: 0/0 = 0 %

### Level 1.848

   Tasksets executed: 9

   - Tasksets actually schedulable: 8/9 = 88.88888888888889 %

   - Tasksets **not** schedulable: 0/9 = 0.0 %

   - Tasksets exceeding level-criticality budget: 1/9 = 11.11111111111111 %

   - Tasksets exceeding safe boundary: 0/9 = 0.0 %

### Level 1.86

   Tasksets executed: 5

   - Tasksets actually schedulable: 5/5 = 100.0 %

   - Tasksets **not** schedulable: 0/5 = 0.0 %

   - Tasksets exceeding level-criticality budget: 0/5 = 0.0 %

   - Tasksets exceeding safe boundary: 0/5 = 0.0 %

### Level 1.872

   Tasksets executed: 4

   - Tasksets actually schedulable: 4/4 = 100.0 %

   - Tasksets **not** schedulable: 0/4 = 0.0 %

   - Tasksets exceeding level-criticality budget: 0/4 = 0.0 %

   - Tasksets exceeding safe boundary: 0/4 = 0.0 %

### Level 1.8840000000000001

   Tasksets executed: 5

   - Tasksets actually schedulable: 4/5 = 80.0 %

   - Tasksets **not** schedulable: 0/5 = 0.0 %

   - Tasksets exceeding level-criticality budget: 1/5 = 20.0 %

   - Tasksets exceeding safe boundary: 0/5 = 0.0 %

### Level 1.8960000000000001

   Tasksets executed: 7

   - Tasksets actually schedulable: 7/7 = 100.0 %

   - Tasksets **not** schedulable: 0/7 = 0.0 %

   - Tasksets exceeding level-criticality budget: 0/7 = 0.0 %

   - Tasksets exceeding safe boundary: 0/7 = 0.0 %

### Level 1.9080000000000001

   Tasksets executed: 5

   - Tasksets actually schedulable: 5/5 = 100.0 %

   - Tasksets **not** schedulable: 0/5 = 0.0 %

   - Tasksets exceeding level-criticality budget: 0/5 = 0.0 %

   - Tasksets exceeding safe boundary: 0/5 = 0.0 %

### Level 1.9200000000000002

   Tasksets executed: 5

   - Tasksets actually schedulable: 3/5 = 60.0 %

   - Tasksets **not** schedulable: 0/5 = 0.0 %

   - Tasksets exceeding level-criticality budget: 2/5 = 40.0 %

   - Tasksets exceeding safe boundary: 0/5 = 0.0 %

### Level 1.9320000000000002

   Tasksets executed: 1

   - Tasksets actually schedulable: 0/1 = 0.0 %

   - Tasksets **not** schedulable: 0/1 = 0.0 %

   - Tasksets exceeding level-criticality budget: 1/1 = 100.0 %

   - Tasksets exceeding safe boundary: 0/1 = 0.0 %

### Level 1.9440000000000002

   Tasksets executed: 3

   - Tasksets actually schedulable: 3/3 = 100.0 %

   - Tasksets **not** schedulable: 0/3 = 0.0 %

   - Tasksets exceeding level-criticality budget: 0/3 = 0.0 %

   - Tasksets exceeding safe boundary: 0/3 = 0.0 %

### Level 1.9560000000000002

   Tasksets executed: 8

   - Tasksets actually schedulable: 5/8 = 62.5 %

   - Tasksets **not** schedulable: 1/8 = 12.5 %

   - Tasksets exceeding level-criticality budget: 1/8 = 12.5 %

   - Tasksets exceeding safe boundary: 1/8 = 12.5 %

### Level 1.9680000000000002

   Tasksets executed: 6

   - Tasksets actually schedulable: 6/6 = 100.0 %

   - Tasksets **not** schedulable: 0/6 = 0.0 %

   - Tasksets exceeding level-criticality budget: 0/6 = 0.0 %

   - Tasksets exceeding safe boundary: 0/6 = 0.0 %

### Level 1.9800000000000002

   Tasksets executed: 2

   - Tasksets actually schedulable: 1/2 = 50.0 %

   - Tasksets **not** schedulable: 0/2 = 0.0 %

   - Tasksets exceeding level-criticality budget: 1/2 = 50.0 %

   - Tasksets exceeding safe boundary: 0/2 = 0.0 %

### Level 1.9920000000000002

   Tasksets executed: 2

   - Tasksets actually schedulable: 1/2 = 50.0 %

   - Tasksets **not** schedulable: 0/2 = 0.0 %

   - Tasksets exceeding level-criticality budget: 0/2 = 0.0 %

   - Tasksets exceeding safe boundary: 1/2 = 50.0 %

### Level 2.004

   Tasksets executed: 0

   - Tasksets actually schedulable: 0/0 = 0 %

   - Tasksets **not** schedulable: 0/0 = 0 %

   - Tasksets exceeding level-criticality budget: 0/0 = 0 %

   - Tasksets exceeding safe boundary: 0/0 = 0 %

### Level 2.016

   Tasksets executed: 1

   - Tasksets actually schedulable: 0/1 = 0.0 %

   - Tasksets **not** schedulable: 0/1 = 0.0 %

   - Tasksets exceeding level-criticality budget: 1/1 = 100.0 %

   - Tasksets exceeding safe boundary: 0/1 = 0.0 %

### Level 2.028

   Tasksets executed: 0

   - Tasksets actually schedulable: 0/0 = 0 %

   - Tasksets **not** schedulable: 0/0 = 0 %

   - Tasksets exceeding level-criticality budget: 0/0 = 0 %

   - Tasksets exceeding safe boundary: 0/0 = 0 %

### Level 2.04

   Tasksets executed: 1

   - Tasksets actually schedulable: 0/1 = 0.0 %

   - Tasksets **not** schedulable: 0/1 = 0.0 %

   - Tasksets exceeding level-criticality budget: 0/1 = 0.0 %

   - Tasksets exceeding safe boundary: 1/1 = 100.0 %

### Level 2.052

   Tasksets executed: 0

   - Tasksets actually schedulable: 0/0 = 0 %

   - Tasksets **not** schedulable: 0/0 = 0 %

   - Tasksets exceeding level-criticality budget: 0/0 = 0 %

   - Tasksets exceeding safe boundary: 0/0 = 0 %

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



   ## Number of executions: **75**

