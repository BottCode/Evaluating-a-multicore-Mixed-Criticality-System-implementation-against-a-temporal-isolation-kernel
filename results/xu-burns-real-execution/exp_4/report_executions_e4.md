# Report on Experiment 4



   ## Overall data

   Utilization range = [1.848, 2.1] with step = 0.012

 Taskset sizes = [8, 10, 12, 15, 20, 25, 30, 35]

  Number of executions: 116

Schedulable executions: 77/116 = 66.37931034482759 %

_Not_ schedulable executions: 0/116 = 0.0 %

Budget Exceeded executions: 28/116 = 24.137931034482758 %

Safe Boundary Exceeded executions: 11/116 = 9.482758620689655 %

NS + BE executions: 28/116 = 24.137931034482758 %

### **Simulations**

#### **Weighted schedulability experiment 4 according to simulations.**

![ALT](result_4.png)

#### **Percentage of (schedulable tasksets with at least one migrating tasks / number of schedulable tasksets) of experiment 4 according to simulations.** 

![ALT](result_taskset_sched_4.png) 


### **Real Executions**

#### **Schedulability for each level**

![ALT](./overall_4.png)


#### **Tasksets, grouped by (LO-crit budget, Period & Migrability), with a Budget_Exceeded task.**

![ALT](./BE_4.png)


#### **Tasksets, grouped by (Period & Migrability), with at least one task missing one (or more) of its deadlines.**

![ALT](./NS_4.png)

## Bad tasksets

<details><summary markdown="span">Click here to expand this section.</summary>


### **Not schedulable tasksets**

<details><summary markdown="span">Click here to expand this section.</summary>

Ovvero quando almeno un task non completa entra almeno una sua deadline.

</details>



### **Criticality Level Budget Exceeded**

<details><summary markdown="span">Click here to expand this section.</summary>

Ovvero quando un task di un taskset ha ecceduto il suo criticality-level budget, cioè un LO-crit task che eccede il suo LO-crit budget, oppure un HI-crit task che eccede il suo HI-crit budget.



  2. Taskset **e4_semi2wf_t1011**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t1011",
    "size": "8",
    "utilization": "1.9680000000000002",
    "realutilization": 1.999999118165785,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 2",
    "period": 22500.0,
    "C(LO)": 1.0,
    "C(HI)": 1.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 7560000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 14,
    "util": 99.99995061728396




   CPU: 2

    
    "id": 2,
    "hyperperiod": 28350000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 11,
    "util": 99.99996119929453




   Real Utilization: 1.999999118165785
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 2",
    "period": 120000.0,
    "C(LO)": 20309.0,
    "C(HI)": 40619.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 1",
    "period": 126000.0,
    "C(LO)": 12845.0,
    "C(HI)": 25690.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 0",
    "period": 945000.0,
    "C(LO)": 60578.0,
    "C(HI)": 121157.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  4

    
    "id": " 4",
    "basecpu": " 1",
    "priority": " 3",
    "period": 100800.0,
    "C(LO)": 23709.0,
    "C(HI)": 23709.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 4",
    "period": 37800.0,
    "C(LO)": 4041.0000000000005,
    "C(HI)": 4041.0000000000005,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002073661",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000015676",
    "avgresponsejitter": " 0.002073661",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  7

    
    "id": " 7",
    "basecpu": " 2",
    "priority": " 0",
    "period": 450000.0,
    "C(LO)": 175256.0,
    "C(HI)": 350513.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  3

    
    "id": " 3",
    "basecpu": " 2",
    "priority": " 1",
    "period": 56700.0,
    "C(LO)": 9996.0,
    "C(HI)": 9996.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 2",
    "period": 22500.0,
    "C(LO)": 1.0,
    "C(HI)": 1.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"



   </details>



  3. Taskset **e4_semi2wf_t1024**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t1024",
    "size": "8",
    "utilization": "1.9680000000000002",
    "realutilization": 1.0986725220458553,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  6

    
    "id": " 6",
    "basecpu": " 2",
    "priority": " 1",
    "period": 141750.0,
    "C(LO)": 34345.0,
    "C(HI)": 34345.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 135",
    "preemptions": " 81",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.027281934",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 19.856509333",
    "avgresponsejitter": " 0.020113204",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 1",
    "budgetexceededaftermigration": " 1",
    "timesmigrated": " 2",
    "timesrestored": " 1",
    "timesonc1": " 2",
    "timesonc2": " 213",
    "lockedtime": " 0.000005228"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 28350000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 13018440,
    "util": 54.07957671957672




   CPU: 2

    
    "id": 2,
    "hyperperiod": 4536000,
    "lowtohigh": " 8",
    "hightolow": " 7",
    "idletime": 12534194,
    "util": 55.78767548500882




   Real Utilization: 1.0986725220458553
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  1

    
    "id": " 1",
    "basecpu": " 1",
    "priority": " 2",
    "period": 25200.0,
    "C(LO)": 5350.0,
    "C(HI)": 10701.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 757",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003215432",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.026006766",
    "avgresponsejitter": " 0.002668667",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 756",
    "timesonc2": " 0",
    "lockedtime": " 0.000019225"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 1",
    "period": 56250.0,
    "C(LO)": 7763.0,
    "C(HI)": 15527.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 340",
    "preemptions": " 54",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.011184129",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.012505979",
    "avgresponsejitter": " 0.004399225",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 393",
    "timesonc2": " 0",
    "lockedtime": " 0.000000312"




   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 0",
    "period": 525000.0,
    "C(LO)": 84626.0,
    "C(HI)": 84626.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 38",
    "preemptions": " 105",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.062544252",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 19.912267459",
    "avgresponsejitter": " 0.052530874",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 142",
    "timesonc2": " 0",
    "lockedtime": " 0.000003363"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 3",
    "period": 105000.0,
    "C(LO)": 11812.0,
    "C(HI)": 11812.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 183",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007054312",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.005006012",
    "avgresponsejitter": " 0.005843505",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 182",
    "timesonc2": " 0",
    "lockedtime": " 0.000000757"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 3",
    "period": 50400.0,
    "C(LO)": 12864.0,
    "C(HI)": 25729.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 379",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.020309532",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.000807087",
    "avgresponsejitter": " 0.006667102",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 7",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 385",
    "lockedtime": " 0.000018595"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 2",
    "period": 60480.0,
    "C(LO)": 4518.0,
    "C(HI)": 9037.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 316",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005987141",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 19.990725955",
    "avgresponsejitter": " 0.002263643",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 316",
    "lockedtime": " 0.000000000"




   Task:  6

    
    "id": " 6",
    "basecpu": " 2",
    "priority": " 1",
    "period": 141750.0,
    "C(LO)": 34345.0,
    "C(HI)": 34345.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 135",
    "preemptions": " 81",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.027281934",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 19.856509333",
    "avgresponsejitter": " 0.020113204",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 1",
    "budgetexceededaftermigration": " 1",
    "timesmigrated": " 2",
    "timesrestored": " 1",
    "timesonc1": " 2",
    "timesonc2": " 213",
    "lockedtime": " 0.000005228"




   Task:  8

    
    "id": " 8",
    "basecpu": " 2",
    "priority": " 0",
    "period": 567000.0,
    "C(LO)": 51810.0,
    "C(HI)": 51810.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 35",
    "preemptions": " 37",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.041281378",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 19.728242904",
    "avgresponsejitter": " 0.032654111",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 71",
    "lockedtime": " 0.000006829"



   </details>



  4. Taskset **e4_semi2wf_t1025**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t1025",
    "size": "8",
    "utilization": "1.9680000000000002",
    "realutilization": 1.5227608818342153,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    
    "id": " 1",
    "basecpu": " 1",
    "priority": " 3",
    "period": 20000.0,
    "C(LO)": 2580.0,
    "C(HI)": 2580.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 970",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001331405",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.401664598",
    "avgresponsejitter": " 0.001308210",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 1",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 1",
    "timesonc1": " 969",
    "timesonc2": " 0",
    "lockedtime": " 0.000000778"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 56700000,
    "lowtohigh": " 7",
    "hightolow": " 7",
    "idletime": 13557058,
    "util": 76.08984479717813




   CPU: 2

    
    "id": 2,
    "hyperperiod": 22680000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 13502400,
    "util": 76.18624338624339




   Real Utilization: 1.5227608818342153
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 1",
    "period": 33750.0,
    "C(LO)": 8121.0,
    "C(HI)": 16242.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 576",
    "preemptions": " 125",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.014276652",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.372506709",
    "avgresponsejitter": " 0.004417703",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 6",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 706",
    "timesonc2": " 0",
    "lockedtime": " 0.000000526"




   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 0",
    "period": 506250.0,
    "C(LO)": 91570.0,
    "C(HI)": 183141.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 40",
    "preemptions": " 164",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.157960805",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.243693384",
    "avgresponsejitter": " 0.055753700",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 204",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  1

    
    "id": " 1",
    "basecpu": " 1",
    "priority": " 3",
    "period": 20000.0,
    "C(LO)": 2580.0,
    "C(HI)": 2580.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 970",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001331405",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.401664598",
    "avgresponsejitter": " 0.001308210",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 1",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 1",
    "timesonc1": " 969",
    "timesonc2": " 0",
    "lockedtime": " 0.000000778"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 2",
    "period": 65625.0,
    "C(LO)": 2494.0,
    "C(HI)": 2494.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 297",
    "preemptions": " 14",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002822526",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.359381580",
    "avgresponsejitter": " 0.001315811",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 310",
    "timesonc2": " 0",
    "lockedtime": " 0.000000646"




   Task:  8

    
    "id": " 8",
    "basecpu": " 2",
    "priority": " 0",
    "period": 648000.0,
    "C(LO)": 173636.0,
    "C(HI)": 347272.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 31",
    "preemptions": " 52",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.124350862",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 19.793859961",
    "avgresponsejitter": " 0.100252520",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 82",
    "lockedtime": " 0.000002018"




   Task:  6

    
    "id": " 6",
    "basecpu": " 2",
    "priority": " 1",
    "period": 181440.0,
    "C(LO)": 14363.0,
    "C(HI)": 28726.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 108",
    "preemptions": " 5",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.025190123",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.232645937",
    "avgresponsejitter": " 0.007877372",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 112",
    "lockedtime": " 0.000000000"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 3",
    "period": 126000.0,
    "C(LO)": 33098.0,
    "C(HI)": 33098.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 155",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.019854607",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.278006787",
    "avgresponsejitter": " 0.016393456",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 155",
    "lockedtime": " 0.000002429"




   Task:  5

    
    "id": " 5",
    "basecpu": " 2",
    "priority": " 2",
    "period": 141750.0,
    "C(LO)": 141.0,
    "C(HI)": 141.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 138",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000091132",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.291364589",
    "avgresponsejitter": " 0.000075961",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 137",
    "lockedtime": " 0.000001589"



   </details>



  5. Taskset **e4_semi2wf_t11029**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t11029",
    "size": "25",
    "utilization": "1.848",
    "realutilization": 1.6951472222222224,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 11",
    "period": 25200.0,
    "C(LO)": 3155.0,
    "C(HI)": 3155.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1032",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001626249",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.987508928",
    "avgresponsejitter": " 0.001597405",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 4",
    "timesrestored": " 4",
    "timesonc1": " 1",
    "timesonc2": " 1030",
    "lockedtime": " 0.000043183"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 38",
    "hightolow": " 38",
    "idletime": 17865923,
    "util": 84.24521781305114




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 10",
    "hightolow": " 10",
    "idletime": 16704382,
    "util": 85.26950440917108




   Real Utilization: 1.6951472222222224
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  13

    
    "id": " 13",
    "basecpu": " 1",
    "priority": " 3",
    "period": 84375.0,
    "C(LO)": 7102.0,
    "C(HI)": 14205.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 309",
    "preemptions": " 122",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.017710775",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.903131090",
    "avgresponsejitter": " 0.004343255",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 433",
    "timesonc2": " 0",
    "lockedtime": " 0.000002087"




   Task:  20

    
    "id": " 20",
    "basecpu": " 1",
    "priority": " 0",
    "period": 168750.0,
    "C(LO)": 8700.0,
    "C(HI)": 17401.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 155",
    "preemptions": " 73",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.013118390",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.822416255",
    "avgresponsejitter": " 0.005217267",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 228",
    "timesonc2": " 0",
    "lockedtime": " 0.000005156"




   Task:  19

    
    "id": " 19",
    "basecpu": " 1",
    "priority": " 1",
    "period": 150000.0,
    "C(LO)": 5600.0,
    "C(HI)": 11201.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 175",
    "preemptions": " 52",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.015196505",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.950020976",
    "avgresponsejitter": " 0.003564679",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 5",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 231",
    "timesonc2": " 0",
    "lockedtime": " 0.000002360"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 5",
    "period": 33750.0,
    "C(LO)": 989.0000000000001,
    "C(HI)": 1978.0000000000002,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 772",
    "preemptions": " 11",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.014166318",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.988150159",
    "avgresponsejitter": " 0.000535444",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 8",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 790",
    "timesonc2": " 0",
    "lockedtime": " 0.000012751"




   Task:  1

    
    "id": " 1",
    "basecpu": " 1",
    "priority": " 7",
    "period": 18900.0,
    "C(LO)": 506.00000000000006,
    "C(HI)": 1012.0000000000001,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1377",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001464655",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.987915673",
    "avgresponsejitter": " 0.000257733",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 16",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1393",
    "timesonc2": " 0",
    "lockedtime": " 0.000004526"




   Task:  17

    
    "id": " 17",
    "basecpu": " 1",
    "priority": " 2",
    "period": 113400.0,
    "C(LO)": 1806.0,
    "C(HI)": 3613.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 231",
    "preemptions": " 17",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007769931",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.969519904",
    "avgresponsejitter": " 0.001023411",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 250",
    "timesonc2": " 0",
    "lockedtime": " 0.000000432"




   Task:  12

    
    "id": " 12",
    "basecpu": " 1",
    "priority": " 4",
    "period": 84000.0,
    "C(LO)": 1265.0,
    "C(HI)": 2531.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 311",
    "preemptions": " 15",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006866012",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.956224195",
    "avgresponsejitter": " 0.000680580",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 327",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  9

    
    "id": " 9",
    "basecpu": " 1",
    "priority": " 8",
    "period": 70875.0,
    "C(LO)": 11020.0,
    "C(HI)": 11020.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 368",
    "preemptions": " 74",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.008242102",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.940256048",
    "avgresponsejitter": " 0.005618739",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 441",
    "timesonc2": " 0",
    "lockedtime": " 0.000008474"




   Task:  15

    
    "id": " 15",
    "basecpu": " 1",
    "priority": " 6",
    "period": 100800.0,
    "C(LO)": 13524.0,
    "C(HI)": 13524.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 259",
    "preemptions": " 118",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.014774048",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.905606562",
    "avgresponsejitter": " 0.007470700",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 376",
    "timesonc2": " 0",
    "lockedtime": " 0.000014895"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 9",
    "period": 60000.0,
    "C(LO)": 2336.0,
    "C(HI)": 2336.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 157",
    "preemptions": " 3",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001886565",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.301088670",
    "avgresponsejitter": " 0.001197345",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 2",
    "timesonc1": " 158",
    "timesonc2": " 1",
    "lockedtime": " 0.000001030"




   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 10",
    "period": 56700.0,
    "C(LO)": 1326.0,
    "C(HI)": 1326.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 460",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000687483",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.968607976",
    "avgresponsejitter": " 0.000677072",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 1",
    "timesonc1": " 458",
    "timesonc2": " 1",
    "lockedtime": " 0.000006781"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 11",
    "period": 52500.0,
    "C(LO)": 782.0,
    "C(HI)": 782.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 497",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000399898",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.987510526",
    "avgresponsejitter": " 0.000393874",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 2",
    "timesonc1": " 495",
    "timesonc2": " 1",
    "lockedtime": " 0.000004393"




   Task:  4

    
    "id": " 4",
    "basecpu": " 1",
    "priority": " 12",
    "period": 42000.0,
    "C(LO)": 401.0,
    "C(HI)": 401.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 620",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000219787",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.956008141",
    "avgresponsejitter": " 0.000209483",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 1",
    "timesonc1": " 618",
    "timesonc2": " 1",
    "lockedtime": " 0.000010679"




   Task:  11

    
    "id": " 11",
    "basecpu": " 2",
    "priority": " 5",
    "period": 81000.0,
    "C(LO)": 10185.0,
    "C(HI)": 20370.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 322",
    "preemptions": " 119",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.017478018",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.920007411",
    "avgresponsejitter": " 0.005881309",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 441",
    "lockedtime": " 0.000007775"




   Task:  16

    
    "id": " 16",
    "basecpu": " 2",
    "priority": " 4",
    "period": 112500.0,
    "C(LO)": 4236.0,
    "C(HI)": 8473.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 232",
    "preemptions": " 34",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.009672811",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.876614727",
    "avgresponsejitter": " 0.002521261",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 268",
    "lockedtime": " 0.000001820"




   Task:  18

    
    "id": " 18",
    "basecpu": " 2",
    "priority": " 3",
    "period": 135000.0,
    "C(LO)": 4127.0,
    "C(HI)": 8255.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 194",
    "preemptions": " 22",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.008808417",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.937491649",
    "avgresponsejitter": " 0.002312553",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 216",
    "lockedtime": " 0.000010210"




   Task:  10

    
    "id": " 10",
    "basecpu": " 2",
    "priority": " 6",
    "period": 78750.0,
    "C(LO)": 2281.0,
    "C(HI)": 4562.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 331",
    "preemptions": " 6",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003812556",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.908755796",
    "avgresponsejitter": " 0.001217856",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 5",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 341",
    "lockedtime": " 0.000011886"




   Task:  25

    
    "id": " 25",
    "basecpu": " 2",
    "priority": " 0",
    "period": 907200.0,
    "C(LO)": 22753.0,
    "C(HI)": 45506.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 30",
    "preemptions": " 26",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.021362414",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.406110096",
    "avgresponsejitter": " 0.013715471",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 55",
    "lockedtime": " 0.000002414"




   Task:  22

    
    "id": " 22",
    "basecpu": " 2",
    "priority": " 2",
    "period": 189000.0,
    "C(LO)": 1174.0,
    "C(HI)": 2349.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 139",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002530841",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.893007036",
    "avgresponsejitter": " 0.000606640",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 140",
    "lockedtime": " 0.000004252"




   Task:  24

    
    "id": " 24",
    "basecpu": " 2",
    "priority": " 1",
    "period": 630000.0,
    "C(LO)": 112116.0,
    "C(HI)": 112116.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 43",
    "preemptions": " 253",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.089306486",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.832917099",
    "avgresponsejitter": " 0.073361210",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 295",
    "lockedtime": " 0.000026865"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 11",
    "period": 25200.0,
    "C(LO)": 3155.0,
    "C(HI)": 3155.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1032",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001626249",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.987508928",
    "avgresponsejitter": " 0.001597405",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 4",
    "timesrestored": " 4",
    "timesonc1": " 1",
    "timesonc2": " 1030",
    "lockedtime": " 0.000043183"




   Task:  6

    
    "id": " 6",
    "basecpu": " 2",
    "priority": " 10",
    "period": 56250.0,
    "C(LO)": 3138.0,
    "C(HI)": 3138.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 463",
    "preemptions": " 24",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003472408",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.931256423",
    "avgresponsejitter": " 0.001650030",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 486",
    "lockedtime": " 0.000007856"




   Task:  14

    
    "id": " 14",
    "basecpu": " 2",
    "priority": " 9",
    "period": 90720.0,
    "C(LO)": 4278.0,
    "C(HI)": 4278.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 288",
    "preemptions": " 12",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004283435",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.945925928",
    "avgresponsejitter": " 0.002181637",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 299",
    "lockedtime": " 0.000001387"




   Task:  23

    
    "id": " 23",
    "basecpu": " 2",
    "priority": " 7",
    "period": 200000.0,
    "C(LO)": 5568.0,
    "C(HI)": 5568.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 131",
    "preemptions": " 20",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006097940",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.800007111",
    "avgresponsejitter": " 0.003095132",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 150",
    "lockedtime": " 0.000001898"




   Task:  21

    
    "id": " 21",
    "basecpu": " 2",
    "priority": " 8",
    "period": 175000.0,
    "C(LO)": 1520.0,
    "C(HI)": 1520.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 150",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000913030",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 26.900006309",
    "avgresponsejitter": " 0.000760234",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 149",
    "lockedtime": " 0.000002547"



   </details>



  6. Taskset **e4_semi2wf_t11038**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t11038",
    "size": "25",
    "utilization": "1.848",
    "realutilization": 1.9999358377425045,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 12",
    "period": 10000.0,
    "C(LO)": 609.0,
    "C(HI)": 609.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 5",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000319529",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.045006312",
    "avgresponsejitter": " 0.000314174",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 4",
    "lockedtime": " 0.000000165"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 1",
    "hightolow": " 1",
    "idletime": 57,
    "util": 99.99994973544973




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 7219,
    "util": 99.9936340388007




   Real Utilization: 1.9999358377425045
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 8",
    "period": 22500.0,
    "C(LO)": 1827.0,
    "C(HI)": 3654.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 3",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000849303",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.022508081",
    "avgresponsejitter": " 0.000832817",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 3",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  16

    
    "id": " 16",
    "basecpu": " 1",
    "priority": " 4",
    "period": 75000.0,
    "C(LO)": 2660.0,
    "C(HI)": 5321.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001197718",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.009160610",
    "avgresponsejitter": " 0.001197718",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 6",
    "period": 39375.0,
    "C(LO)": 1091.0,
    "C(HI)": 2183.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 3",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000622177",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.039381781",
    "avgresponsejitter": " 0.000605748",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 2",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  15

    
    "id": " 15",
    "basecpu": " 1",
    "priority": " 5",
    "period": 72000.0,
    "C(LO)": 1869.0,
    "C(HI)": 3738.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001121628",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.008034952",
    "avgresponsejitter": " 0.001121628",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  17

    
    "id": " 17",
    "basecpu": " 1",
    "priority": " 3",
    "period": 75600.0,
    "C(LO)": 1347.0,
    "C(HI)": 2694.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000682580",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.010362378",
    "avgresponsejitter": " 0.000682580",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  25

    
    "id": " 25",
    "basecpu": " 1",
    "priority": " 0",
    "period": 907200.0,
    "C(LO)": 1240.0,
    "C(HI)": 2480.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000705474",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.044263024",
    "avgresponsejitter": " 0.000705474",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 7",
    "period": 26250.0,
    "C(LO)": 12.0,
    "C(HI)": 25.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 3",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000027580",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.026256949",
    "avgresponsejitter": " 0.000015670",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 3",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  22

    
    "id": " 22",
    "basecpu": " 1",
    "priority": " 2",
    "period": 180000.0,
    "C(LO)": 48004.0,
    "C(HI)": 48004.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.024983532",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.011049069",
    "avgresponsejitter": " 0.024983532",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 3",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  10

    
    "id": " 10",
    "basecpu": " 1",
    "priority": " 11",
    "period": 52500.0,
    "C(LO)": 5323.0,
    "C(HI)": 5323.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002801099",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000023712",
    "avgresponsejitter": " 0.002801099",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000252"




   Task:  24

    
    "id": " 24",
    "basecpu": " 1",
    "priority": " 1",
    "period": 200000.0,
    "C(LO)": 16219.0,
    "C(HI)": 16219.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.008221829",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.036037084",
    "avgresponsejitter": " 0.008221829",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 2",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  18

    
    "id": " 18",
    "basecpu": " 1",
    "priority": " 9",
    "period": 94500.0,
    "C(LO)": 5699.0,
    "C(HI)": 5699.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002695000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.003843237",
    "avgresponsejitter": " 0.002695000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  11

    
    "id": " 11",
    "basecpu": " 1",
    "priority": " 10",
    "period": 56250.0,
    "C(LO)": 1836.0,
    "C(HI)": 1836.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001009279",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.002830030",
    "avgresponsejitter": " 0.001009279",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  20

    
    "id": " 20",
    "basecpu": " 2",
    "priority": " 1",
    "period": 108000.0,
    "C(LO)": 14336.0,
    "C(HI)": 28672.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005901357",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.020524910",
    "avgresponsejitter": " 0.005901357",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  14

    
    "id": " 14",
    "basecpu": " 2",
    "priority": " 2",
    "period": 70875.0,
    "C(LO)": 1887.0,
    "C(HI)": 3774.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001350826",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.019170249",
    "avgresponsejitter": " 0.001350826",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 2",
    "lockedtime": " 0.000000000"




   Task:  13

    
    "id": " 13",
    "basecpu": " 2",
    "priority": " 3",
    "period": 60480.0,
    "C(LO)": 1247.0,
    "C(HI)": 2494.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000690471",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.018475847",
    "avgresponsejitter": " 0.000690471",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  21

    
    "id": " 21",
    "basecpu": " 2",
    "priority": " 0",
    "period": 120000.0,
    "C(LO)": 825.0,
    "C(HI)": 1651.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000418135",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.026430396",
    "avgresponsejitter": " 0.000418135",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 6",
    "period": 30240.0,
    "C(LO)": 101.0,
    "C(HI)": 203.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000062562",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.009566477",
    "avgresponsejitter": " 0.000062562",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  12

    
    "id": " 12",
    "basecpu": " 2",
    "priority": " 7",
    "period": 56700.0,
    "C(LO)": 8844.0,
    "C(HI)": 8844.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004955871",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.004606646",
    "avgresponsejitter": " 0.004955871",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  19

    
    "id": " 19",
    "basecpu": " 2",
    "priority": " 5",
    "period": 100000.0,
    "C(LO)": 12813.0,
    "C(HI)": 12813.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.008000535",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.009632805",
    "avgresponsejitter": " 0.008000535",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 2",
    "lockedtime": " 0.000000000"




   Task:  8

    
    "id": " 8",
    "basecpu": " 2",
    "priority": " 9",
    "period": 50000.0,
    "C(LO)": 5041.0,
    "C(HI)": 5041.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002392757",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.002052601",
    "avgresponsejitter": " 0.002392757",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 12",
    "period": 10000.0,
    "C(LO)": 609.0,
    "C(HI)": 609.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 5",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000319529",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.045006312",
    "avgresponsejitter": " 0.000314174",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 4",
    "lockedtime": " 0.000000165"




   Task:  5

    
    "id": " 5",
    "basecpu": " 2",
    "priority": " 11",
    "period": 37800.0,
    "C(LO)": 2123.0,
    "C(HI)": 2123.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001083736",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000346396",
    "avgresponsejitter": " 0.001083736",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  7

    
    "id": " 7",
    "basecpu": " 2",
    "priority": " 10",
    "period": 45000.0,
    "C(LO)": 1213.0,
    "C(HI)": 1213.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000614931",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.001433862",
    "avgresponsejitter": " 0.000614931",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  23

    
    "id": " 23",
    "basecpu": " 2",
    "priority": " 4",
    "period": 181440.0,
    "C(LO)": 1716.0,
    "C(HI)": 1716.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000834417",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.017637447",
    "avgresponsejitter": " 0.000834417",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  9

    
    "id": " 9",
    "basecpu": " 2",
    "priority": " 8",
    "period": 50400.0,
    "C(LO)": 342.0,
    "C(HI)": 342.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000153571",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.004449258",
    "avgresponsejitter": " 0.000153571",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"



   </details>



  7. Taskset **e4_semi2wf_t1112**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t1112",
    "size": "8",
    "utilization": "1.9800000000000002",
    "realutilization": 1.8951954938271605,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 3",
    "period": 30240.0,
    "C(LO)": 2930.0,
    "C(HI)": 2930.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 301",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001501126",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.072008096",
    "avgresponsejitter": " 0.001483093",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 1",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 1",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 299",
    "lockedtime": " 0.000000715"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 37800000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 6144399,
    "util": 94.58165873015874




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 2",
    "hightolow": " 1",
    "idletime": 5740432,
    "util": 94.93789065255731




   Real Utilization: 1.8951954938271605
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 1",
    "period": 120000.0,
    "C(LO)": 22657.0,
    "C(HI)": 45314.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 77",
    "preemptions": " 9",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.021685036",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.002476595",
    "avgresponsejitter": " 0.012369508",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 85",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 2",
    "period": 87500.0,
    "C(LO)": 15261.0,
    "C(HI)": 30523.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 105",
    "preemptions": " 11",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.011624667",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.012506012",
    "avgresponsejitter": " 0.007903462",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 115",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 0",
    "period": 756000.0,
    "C(LO)": 153040.0,
    "C(HI)": 153040.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 13",
    "preemptions": " 29",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.122074255",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 9.320119498",
    "avgresponsejitter": " 0.096592886",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 41",
    "timesonc2": " 0",
    "lockedtime": " 0.000000420"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 3",
    "period": 72000.0,
    "C(LO)": 4861.0,
    "C(HI)": 4861.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 127",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002479411",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.000007072",
    "avgresponsejitter": " 0.002458694",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 126",
    "timesonc2": " 0",
    "lockedtime": " 0.000000402"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 1",
    "period": 84375.0,
    "C(LO)": 20366.0,
    "C(HI)": 40732.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 109",
    "preemptions": " 36",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.013634928",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.028131727",
    "avgresponsejitter": " 0.010671399",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 144",
    "lockedtime": " 0.000000547"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 2",
    "period": 60480.0,
    "C(LO)": 94.0,
    "C(HI)": 189.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 152",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000144949",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.072006465",
    "avgresponsejitter": " 0.000051982",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 153",
    "lockedtime": " 0.000000000"




   Task:  8

    
    "id": " 8",
    "basecpu": " 2",
    "priority": " 0",
    "period": 810000.0,
    "C(LO)": 324621.0,
    "C(HI)": 324621.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 12",
    "preemptions": " 81",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.221524240",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 9.110444688",
    "avgresponsejitter": " 0.175463508",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 92",
    "lockedtime": " 0.000000330"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 3",
    "period": 30240.0,
    "C(LO)": 2930.0,
    "C(HI)": 2930.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 301",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001501126",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.072008096",
    "avgresponsejitter": " 0.001483093",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 1",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 1",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 299",
    "lockedtime": " 0.000000715"



   </details>



  8. Taskset **e4_semi2wf_t11254**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t11254",
    "size": "25",
    "utilization": "1.872",
    "realutilization": 1.9999996208112876,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 13",
    "period": 15750.0,
    "C(LO)": 3.0,
    "C(HI)": 3.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 21,
    "util": 99.99998148148148




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 22,
    "util": 99.99998059964727




   Real Utilization: 1.9999996208112876
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  21

    
    "id": " 21",
    "basecpu": " 1",
    "priority": " 1",
    "period": 131250.0,
    "C(LO)": 11640.0,
    "C(HI)": 23280.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  19

    
    "id": " 19",
    "basecpu": " 1",
    "priority": " 2",
    "period": 108000.0,
    "C(LO)": 6857.0,
    "C(HI)": 13714.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 6",
    "period": 40000.0,
    "C(LO)": 2228.0,
    "C(HI)": 4457.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  14

    
    "id": " 14",
    "basecpu": " 1",
    "priority": " 4",
    "period": 70875.0,
    "C(LO)": 3511.0,
    "C(HI)": 7023.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  13

    
    "id": " 13",
    "basecpu": " 1",
    "priority": " 5",
    "period": 67500.0,
    "C(LO)": 765.0,
    "C(HI)": 1531.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  15

    
    "id": " 15",
    "basecpu": " 1",
    "priority": " 3",
    "period": 84375.0,
    "C(LO)": 519.0,
    "C(HI)": 1039.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  23

    
    "id": " 23",
    "basecpu": " 1",
    "priority": " 0",
    "period": 150000.0,
    "C(LO)": 686.0,
    "C(HI)": 1372.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  11

    
    "id": " 11",
    "basecpu": " 1",
    "priority": " 8",
    "period": 60480.0,
    "C(LO)": 10101.0,
    "C(HI)": 10101.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  20

    
    "id": " 20",
    "basecpu": " 1",
    "priority": " 7",
    "period": 112500.0,
    "C(LO)": 14278.0,
    "C(HI)": 14278.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 9",
    "period": 50000.0,
    "C(LO)": 883.0,
    "C(HI)": 883.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  4

    
    "id": " 4",
    "basecpu": " 1",
    "priority": " 10",
    "period": 37800.0,
    "C(LO)": 405.0,
    "C(HI)": 405.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000306"




   Task:  24

    
    "id": " 24",
    "basecpu": " 2",
    "priority": " 1",
    "period": 181440.0,
    "C(LO)": 27692.0,
    "C(HI)": 55384.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  25

    
    "id": " 25",
    "basecpu": " 2",
    "priority": " 0",
    "period": 810000.0,
    "C(LO)": 44985.0,
    "C(HI)": 89971.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  10

    
    "id": " 10",
    "basecpu": " 2",
    "priority": " 4",
    "period": 56700.0,
    "C(LO)": 2801.0,
    "C(HI)": 5603.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  16

    
    "id": " 16",
    "basecpu": " 2",
    "priority": " 3",
    "period": 87500.0,
    "C(LO)": 942.0,
    "C(HI)": 1885.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  22

    
    "id": " 22",
    "basecpu": " 2",
    "priority": " 2",
    "period": 141750.0,
    "C(LO)": 1113.0,
    "C(HI)": 2226.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  9

    
    "id": " 9",
    "basecpu": " 2",
    "priority": " 8",
    "period": 54000.0,
    "C(LO)": 9757.0,
    "C(HI)": 9757.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  18

    
    "id": " 18",
    "basecpu": " 2",
    "priority": " 5",
    "period": 100800.0,
    "C(LO)": 10605.0,
    "C(HI)": 10605.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  17

    
    "id": " 17",
    "basecpu": " 2",
    "priority": " 6",
    "period": 90000.0,
    "C(LO)": 8181.000000000001,
    "C(HI)": 8181.000000000001,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  3

    
    "id": " 3",
    "basecpu": " 2",
    "priority": " 11",
    "period": 35000.0,
    "C(LO)": 898.0,
    "C(HI)": 898.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 12",
    "period": 30240.0,
    "C(LO)": 526.0,
    "C(HI)": 526.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  8

    
    "id": " 8",
    "basecpu": " 2",
    "priority": " 9",
    "period": 52500.0,
    "C(LO)": 472.0,
    "C(HI)": 472.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  6

    
    "id": " 6",
    "basecpu": " 2",
    "priority": " 10",
    "period": 47250.0,
    "C(LO)": 227.0,
    "C(HI)": 227.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  12

    
    "id": " 12",
    "basecpu": " 2",
    "priority": " 7",
    "period": 65625.0,
    "C(LO)": 279.0,
    "C(HI)": 279.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 13",
    "period": 15750.0,
    "C(LO)": 3.0,
    "C(HI)": 3.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"



   </details>



  9. Taskset **e4_semi2wf_t11394**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t11394",
    "size": "25",
    "utilization": "1.8840000000000001",
    "realutilization": 1.9999996031746032,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 10",
    "period": 10000.0,
    "C(LO)": 3.0,
    "C(HI)": 6.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 2",
    "lockedtime": " 0.000000378"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 56700000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 23,
    "util": 99.99997971781305




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 1",
    "hightolow": " 0",
    "idletime": 22,
    "util": 99.99998059964727




   Real Utilization: 1.9999996031746032
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  22

    
    "id": " 22",
    "basecpu": " 1",
    "priority": " 1",
    "period": 150000.0,
    "C(LO)": 15425.0,
    "C(HI)": 30851.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  15

    
    "id": " 15",
    "basecpu": " 1",
    "priority": " 3",
    "period": 78750.0,
    "C(LO)": 5807.0,
    "C(HI)": 11615.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  21

    
    "id": " 21",
    "basecpu": " 1",
    "priority": " 2",
    "period": 141750.0,
    "C(LO)": 6934.0,
    "C(HI)": 13868.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  24

    
    "id": " 24",
    "basecpu": " 1",
    "priority": " 0",
    "period": 180000.0,
    "C(LO)": 5742.0,
    "C(HI)": 11485.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 6",
    "period": 15750.0,
    "C(LO)": 340.0,
    "C(HI)": 681.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  16

    
    "id": " 16",
    "basecpu": " 1",
    "priority": " 5",
    "period": 84375.0,
    "C(LO)": 7565.0,
    "C(HI)": 7565.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 11",
    "period": 39375.0,
    "C(LO)": 2945.0,
    "C(HI)": 2945.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001492219",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000024075",
    "avgresponsejitter": " 0.001492219",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  9

    
    "id": " 9",
    "basecpu": " 1",
    "priority": " 8",
    "period": 56700.0,
    "C(LO)": 3582.0,
    "C(HI)": 3582.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  20

    
    "id": " 20",
    "basecpu": " 1",
    "priority": " 4",
    "period": 118125.0,
    "C(LO)": 7313.0,
    "C(HI)": 7313.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  11

    
    "id": " 11",
    "basecpu": " 1",
    "priority": " 7",
    "period": 63000.0,
    "C(LO)": 3259.0,
    "C(HI)": 3259.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 9",
    "period": 50400.0,
    "C(LO)": 642.0,
    "C(HI)": 642.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 10",
    "period": 45360.0,
    "C(LO)": 181.0,
    "C(HI)": 181.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000094183",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.001521529",
    "avgresponsejitter": " 0.000094183",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  25

    
    "id": " 25",
    "basecpu": " 2",
    "priority": " 0",
    "period": 590625.0,
    "C(LO)": 113442.0,
    "C(HI)": 226884.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  10

    
    "id": " 10",
    "basecpu": " 2",
    "priority": " 3",
    "period": 60480.0,
    "C(LO)": 2147.0,
    "C(HI)": 4295.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  17

    
    "id": " 17",
    "basecpu": " 2",
    "priority": " 2",
    "period": 87500.0,
    "C(LO)": 2125.0,
    "C(HI)": 4250.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 5",
    "period": 42000.0,
    "C(LO)": 954.0,
    "C(HI)": 1909.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  23

    
    "id": " 23",
    "basecpu": " 2",
    "priority": " 1",
    "period": 151200.0,
    "C(LO)": 469.0,
    "C(HI)": 939.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 10",
    "period": 10000.0,
    "C(LO)": 3.0,
    "C(HI)": 6.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 2",
    "lockedtime": " 0.000000378"




   Task:  8

    
    "id": " 8",
    "basecpu": " 2",
    "priority": " 4",
    "period": 54000.0,
    "C(LO)": 8.0,
    "C(HI)": 17.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  13

    
    "id": " 13",
    "basecpu": " 2",
    "priority": " 9",
    "period": 70875.0,
    "C(LO)": 18067.0,
    "C(HI)": 18067.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  18

    
    "id": " 18",
    "basecpu": " 2",
    "priority": " 7",
    "period": 100000.0,
    "C(LO)": 6123.0,
    "C(HI)": 6123.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  6

    
    "id": " 6",
    "basecpu": " 2",
    "priority": " 12",
    "period": 50000.0,
    "C(LO)": 2787.0,
    "C(HI)": 2787.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001409907",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000022844",
    "avgresponsejitter": " 0.001409907",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000327"




   Task:  19

    
    "id": " 19",
    "basecpu": " 2",
    "priority": " 6",
    "period": 113400.0,
    "C(LO)": 1813.0,
    "C(HI)": 1813.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  14

    
    "id": " 14",
    "basecpu": " 2",
    "priority": " 8",
    "period": 75600.0,
    "C(LO)": 1006.0,
    "C(HI)": 1006.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  12

    
    "id": " 12",
    "basecpu": " 2",
    "priority": " 11",
    "period": 70000.0,
    "C(LO)": 719.0,
    "C(HI)": 719.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000395949",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.001436757",
    "avgresponsejitter": " 0.000395949",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"



   </details>



  10. Taskset **e4_semi2wf_t11404**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t11404",
    "size": "25",
    "utilization": "1.8960000000000001",
    "realutilization": 1.7273874426807758,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 12",
    "period": 10000.0,
    "C(LO)": 326.0,
    "C(HI)": 326.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2393",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000184000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.920006523",
    "avgresponsejitter": " 0.000171303",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 2",
    "timesonc1": " 1",
    "timesonc2": " 2391",
    "lockedtime": " 0.000023201"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 15090226,
    "util": 86.69292239858906




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 10",
    "hightolow": " 10",
    "idletime": 15824038,
    "util": 86.04582186948853




   Real Utilization: 1.7273874426807758
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  22

    
    "id": " 22",
    "basecpu": " 1",
    "priority": " 2",
    "period": 168750.0,
    "C(LO)": 16816.0,
    "C(HI)": 33633.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 143",
    "preemptions": " 142",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.019458793",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.794888123",
    "avgresponsejitter": " 0.010581429",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 284",
    "timesonc2": " 0",
    "lockedtime": " 0.000013054"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 4",
    "period": 52500.0,
    "C(LO)": 2608.0,
    "C(HI)": 5216.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 457",
    "preemptions": " 10",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005931408",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.887506808",
    "avgresponsejitter": " 0.001357300",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 466",
    "timesonc2": " 0",
    "lockedtime": " 0.000001733"




   Task:  25

    
    "id": " 25",
    "basecpu": " 1",
    "priority": " 0",
    "period": 787500.0,
    "C(LO)": 33488.0,
    "C(HI)": 66976.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 32",
    "preemptions": " 75",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.033694757",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.646183429",
    "avgresponsejitter": " 0.022025793",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 106",
    "timesonc2": " 0",
    "lockedtime": " 0.000007036"




   Task:  23

    
    "id": " 23",
    "basecpu": " 1",
    "priority": " 1",
    "period": 175000.0,
    "C(LO)": 5555.0,
    "C(HI)": 11111.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 138",
    "preemptions": " 42",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.014476123",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.807883180",
    "avgresponsejitter": " 0.003439390",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 179",
    "timesonc2": " 0",
    "lockedtime": " 0.000003432"




   Task:  20

    
    "id": " 20",
    "basecpu": " 1",
    "priority": " 3",
    "period": 157500.0,
    "C(LO)": 1334.0,
    "C(HI)": 2668.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 153",
    "preemptions": " 4",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005247306",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.783812213",
    "avgresponsejitter": " 0.000717456",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 156",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 5",
    "period": 50400.0,
    "C(LO)": 104.0,
    "C(HI)": 209.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 476",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001344880",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.891176931",
    "avgresponsejitter": " 0.000059381",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 476",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 9",
    "period": 45000.0,
    "C(LO)": 5850.0,
    "C(HI)": 5850.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 533",
    "preemptions": " 26",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005076745",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.895007994",
    "avgresponsejitter": " 0.003003303",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 558",
    "timesonc2": " 0",
    "lockedtime": " 0.000014330"




   Task:  9

    
    "id": " 9",
    "basecpu": " 1",
    "priority": " 8",
    "period": 63000.0,
    "C(LO)": 7233.0,
    "C(HI)": 7233.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 381",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004335480",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.877006009",
    "avgresponsejitter": " 0.003623796",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 380",
    "timesonc2": " 0",
    "lockedtime": " 0.000004081"




   Task:  15

    
    "id": " 15",
    "basecpu": " 1",
    "priority": " 7",
    "period": 90720.0,
    "C(LO)": 7566.0,
    "C(HI)": 7566.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 265",
    "preemptions": " 62",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.012433168",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.859366033",
    "avgresponsejitter": " 0.004336520",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 326",
    "timesonc2": " 0",
    "lockedtime": " 0.000012462"




   Task:  4

    
    "id": " 4",
    "basecpu": " 1",
    "priority": " 10",
    "period": 37800.0,
    "C(LO)": 2845.0,
    "C(HI)": 2845.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 634",
    "preemptions": " 13",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003156862",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.889606985",
    "avgresponsejitter": " 0.001459919",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 646",
    "timesonc2": " 0",
    "lockedtime": " 0.000003973"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 11",
    "period": 35000.0,
    "C(LO)": 2572.0,
    "C(HI)": 2572.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 685",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001559775",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.905184571",
    "avgresponsejitter": " 0.001285297",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 684",
    "timesonc2": " 0",
    "lockedtime": " 0.000012664"




   Task:  16

    
    "id": " 16",
    "basecpu": " 1",
    "priority": " 6",
    "period": 101250.0,
    "C(LO)": 2055.0,
    "C(HI)": 2055.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 238",
    "preemptions": " 4",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005427910",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.897841213",
    "avgresponsejitter": " 0.001090417",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 241",
    "timesonc2": " 0",
    "lockedtime": " 0.000000673"




   Task:  19

    
    "id": " 19",
    "basecpu": " 2",
    "priority": " 1",
    "period": 131250.0,
    "C(LO)": 14865.0,
    "C(HI)": 29731.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 184",
    "preemptions": " 254",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.026514360",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.892167526",
    "avgresponsejitter": " 0.009964511",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 438",
    "lockedtime": " 0.000007793"




   Task:  11

    
    "id": " 11",
    "basecpu": " 2",
    "priority": " 5",
    "period": 67500.0,
    "C(LO)": 3163.0,
    "C(HI)": 6326.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 356",
    "preemptions": " 32",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004977303",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.895007502",
    "avgresponsejitter": " 0.001701505",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 389",
    "lockedtime": " 0.000013850"




   Task:  13

    
    "id": " 13",
    "basecpu": " 2",
    "priority": " 4",
    "period": 81000.0,
    "C(LO)": 3313.0,
    "C(HI)": 6627.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 297",
    "preemptions": " 72",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005629541",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.896569895",
    "avgresponsejitter": " 0.001815844",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 369",
    "lockedtime": " 0.000001321"




   Task:  24

    
    "id": " 24",
    "basecpu": " 2",
    "priority": " 0",
    "period": 180000.0,
    "C(LO)": 2946.0,
    "C(HI)": 5892.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 134",
    "preemptions": " 15",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.011129297",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.768805246",
    "avgresponsejitter": " 0.001883486",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 149",
    "lockedtime": " 0.000000000"




   Task:  18

    
    "id": " 18",
    "basecpu": " 2",
    "priority": " 2",
    "period": 126000.0,
    "C(LO)": 1128.0,
    "C(HI)": 2257.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 191",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001712120",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.825659787",
    "avgresponsejitter": " 0.000586210",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 195",
    "lockedtime": " 0.000006180"




   Task:  17

    
    "id": " 17",
    "basecpu": " 2",
    "priority": " 3",
    "period": 112500.0,
    "C(LO)": 838.0,
    "C(HI)": 1677.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 214",
    "preemptions": " 6",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001786267",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.853385610",
    "avgresponsejitter": " 0.000430345",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 221",
    "lockedtime": " 0.000003733"




   Task:  12

    
    "id": " 12",
    "basecpu": " 2",
    "priority": " 8",
    "period": 70875.0,
    "C(LO)": 15554.0,
    "C(HI)": 15554.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 339",
    "preemptions": " 346",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.011656207",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.884880874",
    "avgresponsejitter": " 0.008177949",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 684",
    "lockedtime": " 0.000017919"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 11",
    "period": 30240.0,
    "C(LO)": 2648.0,
    "C(HI)": 2648.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 518",
    "preemptions": " 64",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001544063",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 16.603847120",
    "avgresponsejitter": " 0.001365595",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 1",
    "timesonc1": " 1",
    "timesonc2": " 580",
    "lockedtime": " 0.000014736"




   Task:  14

    
    "id": " 14",
    "basecpu": " 2",
    "priority": " 7",
    "period": 90000.0,
    "C(LO)": 7093.0,
    "C(HI)": 7093.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 267",
    "preemptions": " 62",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.013861255",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.850185393",
    "avgresponsejitter": " 0.004153081",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 328",
    "lockedtime": " 0.000002532"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 12",
    "period": 10000.0,
    "C(LO)": 326.0,
    "C(HI)": 326.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2393",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000184000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.920006523",
    "avgresponsejitter": " 0.000171303",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 2",
    "timesonc1": " 1",
    "timesonc2": " 2391",
    "lockedtime": " 0.000023201"




   Task:  10

    
    "id": " 10",
    "basecpu": " 2",
    "priority": " 9",
    "period": 65625.0,
    "C(LO)": 1530.0,
    "C(HI)": 1530.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 366",
    "preemptions": " 29",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002326270",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.887507808",
    "avgresponsejitter": " 0.000815363",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 1",
    "timesonc1": " 0",
    "timesonc2": " 394",
    "lockedtime": " 0.000003180"




   Task:  21

    
    "id": " 21",
    "basecpu": " 2",
    "priority": " 6",
    "period": 162000.0,
    "C(LO)": 2914.0,
    "C(HI)": 2914.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 149",
    "preemptions": " 8",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002705471",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.821632477",
    "avgresponsejitter": " 0.001504619",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 156",
    "lockedtime": " 0.000000000"




   Task:  5

    
    "id": " 5",
    "basecpu": " 2",
    "priority": " 10",
    "period": 40000.0,
    "C(LO)": 117.0,
    "C(HI)": 117.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 599",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000063820",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 24.880184613",
    "avgresponsejitter": " 0.000062081",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 598",
    "lockedtime": " 0.000000000"



   </details>



  11. Taskset **e4_semi2wf_t11584**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t11584",
    "size": "25",
    "utilization": "1.9080000000000001",
    "realutilization": 1.9155514109347442,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 11",
    "period": 15750.0,
    "C(LO)": 1994.0,
    "C(HI)": 1994.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 453",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001036967",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.120007078",
    "avgresponsejitter": " 0.001014105",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 1",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 1",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 3",
    "timesrestored": " 2",
    "timesonc1": " 2",
    "timesonc2": " 450",
    "lockedtime": " 0.000015931"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 2",
    "hightolow": " 2",
    "idletime": 4908969,
    "util": 95.67110317460318




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 8",
    "hightolow": " 7",
    "idletime": 4667501,
    "util": 95.88403791887126




   Real Utilization: 1.9155514109347442
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  18

    
    "id": " 18",
    "basecpu": " 1",
    "priority": " 3",
    "period": 105000.0,
    "C(LO)": 13571.0,
    "C(HI)": 27142.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 69",
    "preemptions": " 43",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.015814691",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.035006126",
    "avgresponsejitter": " 0.007644814",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 111",
    "timesonc2": " 0",
    "lockedtime": " 0.000007775"




   Task:  23

    
    "id": " 23",
    "basecpu": " 1",
    "priority": " 1",
    "period": 168750.0,
    "C(LO)": 18139.0,
    "C(HI)": 36278.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 44",
    "preemptions": " 55",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.023813132",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.090291084",
    "avgresponsejitter": " 0.011283652",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 98",
    "timesonc2": " 0",
    "lockedtime": " 0.000007682"




   Task:  17

    
    "id": " 17",
    "basecpu": " 1",
    "priority": " 4",
    "period": 100800.0,
    "C(LO)": 4086.0,
    "C(HI)": 8173.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 72",
    "preemptions": " 9",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.008423180",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.056072429",
    "avgresponsejitter": " 0.002200823",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 80",
    "timesonc2": " 0",
    "lockedtime": " 0.000000411"




   Task:  21

    
    "id": " 21",
    "basecpu": " 1",
    "priority": " 2",
    "period": 157500.0,
    "C(LO)": 2963.0,
    "C(HI)": 5927.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 47",
    "preemptions": " 10",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.010692925",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.088770411",
    "avgresponsejitter": " 0.002108862",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 56",
    "timesonc2": " 0",
    "lockedtime": " 0.000000556"




   Task:  24

    
    "id": " 24",
    "basecpu": " 1",
    "priority": " 0",
    "period": 567000.0,
    "C(LO)": 8615.0,
    "C(HI)": 17231.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 14",
    "preemptions": " 6",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006409222",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 7.810997598",
    "avgresponsejitter": " 0.004468967",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 19",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  11

    
    "id": " 11",
    "basecpu": " 1",
    "priority": " 5",
    "period": 67500.0,
    "C(LO)": 335.0,
    "C(HI)": 670.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 107",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000473072",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.088573532",
    "avgresponsejitter": " 0.000174384",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 107",
    "timesonc2": " 0",
    "lockedtime": " 0.000001928"




   Task:  9

    
    "id": " 9",
    "basecpu": " 1",
    "priority": " 6",
    "period": 60480.0,
    "C(LO)": 49.0,
    "C(HI)": 99.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 119",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000080892",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.076166126",
    "avgresponsejitter": " 0.000032024",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 119",
    "timesonc2": " 0",
    "lockedtime": " 0.000000673"




   Task:  14

    
    "id": " 14",
    "basecpu": " 1",
    "priority": " 8",
    "period": 81000.0,
    "C(LO)": 13112.0,
    "C(HI)": 13112.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 89",
    "preemptions": " 52",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.009203754",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.047006033",
    "avgresponsejitter": " 0.006832685",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 140",
    "timesonc2": " 0",
    "lockedtime": " 0.000005550"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 12",
    "period": 20000.0,
    "C(LO)": 1246.0,
    "C(HI)": 1246.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 357",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000650183",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.100006571",
    "avgresponsejitter": " 0.000636357",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 356",
    "timesonc2": " 0",
    "lockedtime": " 0.000013261"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 11",
    "period": 39375.0,
    "C(LO)": 1525.0,
    "C(HI)": 1525.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 182",
    "preemptions": " 6",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001446300",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.087510505",
    "avgresponsejitter": " 0.000797886",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 187",
    "timesonc2": " 0",
    "lockedtime": " 0.000000652"




   Task:  22

    
    "id": " 22",
    "basecpu": " 1",
    "priority": " 7",
    "period": 162000.0,
    "C(LO)": 1990.0,
    "C(HI)": 1990.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 45",
    "preemptions": " 6",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001933060",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 7.973996459",
    "avgresponsejitter": " 0.001075862",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 50",
    "timesonc2": " 0",
    "lockedtime": " 0.000001090"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 9",
    "period": 47250.0,
    "C(LO)": 541.0,
    "C(HI)": 541.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 152",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000925105",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.088293450",
    "avgresponsejitter": " 0.000285078",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 153",
    "timesonc2": " 0",
    "lockedtime": " 0.000002324"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 10",
    "period": 42000.0,
    "C(LO)": 95.0,
    "C(HI)": 95.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 171",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000059838",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.098006550",
    "avgresponsejitter": " 0.000057877",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 170",
    "timesonc2": " 0",
    "lockedtime": " 0.000000231"




   Task:  19

    
    "id": " 19",
    "basecpu": " 2",
    "priority": " 2",
    "period": 120000.0,
    "C(LO)": 19306.0,
    "C(HI)": 38612.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 61",
    "preemptions": " 114",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.025913018",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.080351919",
    "avgresponsejitter": " 0.011634051",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 175",
    "lockedtime": " 0.000003910"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 7",
    "period": 10000.0,
    "C(LO)": 605.0,
    "C(HI)": 1211.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 714",
    "preemptions": " 16",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001393694",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.120006468",
    "avgresponsejitter": " 0.000327258",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 4",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 733",
    "lockedtime": " 0.000024595"




   Task:  12

    
    "id": " 12",
    "basecpu": " 2",
    "priority": " 4",
    "period": 75000.0,
    "C(LO)": 3211.0,
    "C(HI)": 6422.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 96",
    "preemptions": " 20",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005537435",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.050320441",
    "avgresponsejitter": " 0.001891517",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 115",
    "lockedtime": " 0.000000399"




   Task:  15

    
    "id": " 15",
    "basecpu": " 2",
    "priority": " 3",
    "period": 84375.0,
    "C(LO)": 2318.0,
    "C(HI)": 4637.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 86",
    "preemptions": " 17",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004626622",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.089601592",
    "avgresponsejitter": " 0.001350985",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 104",
    "lockedtime": " 0.000001712"




   Task:  7

    
    "id": " 7",
    "basecpu": " 2",
    "priority": " 5",
    "period": 45000.0,
    "C(LO)": 721.0,
    "C(HI)": 1443.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 160",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001061009",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.110336090",
    "avgresponsejitter": " 0.000368955",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 160",
    "lockedtime": " 0.000000886"




   Task:  20

    
    "id": " 20",
    "basecpu": " 2",
    "priority": " 1",
    "period": 140000.0,
    "C(LO)": 1761.0,
    "C(HI)": 3522.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 52",
    "preemptions": " 4",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002311994",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.001599955",
    "avgresponsejitter": " 0.000948462",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 55",
    "lockedtime": " 0.000000306"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 11",
    "period": 15750.0,
    "C(LO)": 1994.0,
    "C(HI)": 1994.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 453",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001036967",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.120007078",
    "avgresponsejitter": " 0.001014105",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 1",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 1",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 3",
    "timesrestored": " 2",
    "timesonc1": " 2",
    "timesonc2": " 450",
    "lockedtime": " 0.000015931"




   Task:  25

    
    "id": " 25",
    "basecpu": " 2",
    "priority": " 0",
    "period": 708750.0,
    "C(LO)": 72733.0,
    "C(HI)": 72733.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 11",
    "preemptions": " 101",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.059611808",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 7.379781988",
    "avgresponsejitter": " 0.048853105",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 111",
    "lockedtime": " 0.000007502"




   Task:  13

    
    "id": " 13",
    "basecpu": " 2",
    "priority": " 8",
    "period": 75600.0,
    "C(LO)": 4233.0,
    "C(HI)": 4233.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 96",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003468012",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.106752048",
    "avgresponsejitter": " 0.002150066",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 96",
    "lockedtime": " 0.000001595"




   Task:  16

    
    "id": " 16",
    "basecpu": " 2",
    "priority": " 6",
    "period": 87500.0,
    "C(LO)": 2169.0,
    "C(HI)": 2169.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 83",
    "preemptions": " 3",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003436610",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.088527117",
    "avgresponsejitter": " 0.001129411",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 85",
    "lockedtime": " 0.000000000"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 10",
    "period": 37800.0,
    "C(LO)": 643.0,
    "C(HI)": 643.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 190",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000384030",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.106407351",
    "avgresponsejitter": " 0.000326054",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 189",
    "lockedtime": " 0.000000589"




   Task:  10

    
    "id": " 10",
    "basecpu": " 2",
    "priority": " 9",
    "period": 64800.0,
    "C(LO)": 1098.0,
    "C(HI)": 1098.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 111",
    "preemptions": " 3",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001565838",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.063205904",
    "avgresponsejitter": " 0.000580751",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 113",
    "lockedtime": " 0.000001718"



   </details>



  12. Taskset **e4_semi2wf_t11722**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t11722",
    "size": "25",
    "utilization": "1.9320000000000002",
    "realutilization": 1.9999996208112876,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  19

    
    "id": " 19",
    "basecpu": " 1",
    "priority": " 5",
    "period": 112500.0,
    "C(LO)": 3.0,
    "C(HI)": 3.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 24,
    "util": 99.99997883597884




   CPU: 2

    
    "id": 2,
    "hyperperiod": 56700000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 19,
    "util": 99.9999832451499




   Real Utilization: 1.9999996208112876
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  17

    
    "id": " 17",
    "basecpu": " 1",
    "priority": " 3",
    "period": 90720.0,
    "C(LO)": 10527.0,
    "C(HI)": 21054.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  25

    
    "id": " 25",
    "basecpu": " 1",
    "priority": " 0",
    "period": 756000.0,
    "C(LO)": 66116.0,
    "C(HI)": 132233.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 4",
    "period": 54000.0,
    "C(LO)": 1785.0,
    "C(HI)": 3571.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  23

    
    "id": " 23",
    "basecpu": " 1",
    "priority": " 1",
    "period": 200000.0,
    "C(LO)": 6351.0,
    "C(HI)": 12703.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  20

    
    "id": " 20",
    "basecpu": " 1",
    "priority": " 2",
    "period": 126000.0,
    "C(LO)": 1371.0,
    "C(HI)": 2742.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  1

    
    "id": " 1",
    "basecpu": " 1",
    "priority": " 8",
    "period": 15750.0,
    "C(LO)": 154.0,
    "C(HI)": 309.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000071526",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.006702757",
    "avgresponsejitter": " 0.000071526",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  4

    
    "id": " 4",
    "basecpu": " 1",
    "priority": " 12",
    "period": 35000.0,
    "C(LO)": 3590.0,
    "C(HI)": 3590.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002044342",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000272213",
    "avgresponsejitter": " 0.002044342",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  12

    
    "id": " 12",
    "basecpu": " 1",
    "priority": " 9",
    "period": 65625.0,
    "C(LO)": 6412.0,
    "C(HI)": 6412.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003405372",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.003293616",
    "avgresponsejitter": " 0.003405372",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  14

    
    "id": " 14",
    "basecpu": " 1",
    "priority": " 7",
    "period": 78750.0,
    "C(LO)": 6084.0,
    "C(HI)": 6084.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002679453",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.006778225",
    "avgresponsejitter": " 0.002679453",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  18

    
    "id": " 18",
    "basecpu": " 1",
    "priority": " 6",
    "period": 101250.0,
    "C(LO)": 4517.0,
    "C(HI)": 4517.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002626144",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.009461718",
    "avgresponsejitter": " 0.002626144",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 11",
    "period": 37800.0,
    "C(LO)": 1459.0,
    "C(HI)": 1459.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000841691",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.002320685",
    "avgresponsejitter": " 0.000841691",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 13",
    "period": 22500.0,
    "C(LO)": 436.0,
    "C(HI)": 436.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000242231",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000025090",
    "avgresponsejitter": " 0.000242231",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  11

    
    "id": " 11",
    "basecpu": " 1",
    "priority": " 10",
    "period": 64800.0,
    "C(LO)": 276.0,
    "C(HI)": 276.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000123390",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.003166402",
    "avgresponsejitter": " 0.000123390",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  19

    
    "id": " 19",
    "basecpu": " 1",
    "priority": " 5",
    "period": 112500.0,
    "C(LO)": 3.0,
    "C(HI)": 3.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  9

    
    "id": " 9",
    "basecpu": " 2",
    "priority": " 4",
    "period": 60000.0,
    "C(LO)": 6976.0,
    "C(HI)": 13952.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  24

    
    "id": " 24",
    "basecpu": " 2",
    "priority": " 0",
    "period": 506250.0,
    "C(LO)": 36390.0,
    "C(HI)": 72780.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  10

    
    "id": " 10",
    "basecpu": " 2",
    "priority": " 3",
    "period": 63000.0,
    "C(LO)": 3640.0,
    "C(HI)": 7280.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  15

    
    "id": " 15",
    "basecpu": " 2",
    "priority": " 2",
    "period": 81000.0,
    "C(LO)": 1191.0,
    "C(HI)": 2382.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  7

    
    "id": " 7",
    "basecpu": " 2",
    "priority": " 5",
    "period": 45360.0,
    "C(LO)": 628.0,
    "C(HI)": 1257.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  22

    
    "id": " 22",
    "basecpu": " 2",
    "priority": " 1",
    "period": 175000.0,
    "C(LO)": 1797.0,
    "C(HI)": 3594.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  16

    
    "id": " 16",
    "basecpu": " 2",
    "priority": " 7",
    "period": 84000.0,
    "C(LO)": 21404.0,
    "C(HI)": 21404.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  3

    
    "id": " 3",
    "basecpu": " 2",
    "priority": " 10",
    "period": 30240.0,
    "C(LO)": 1459.0,
    "C(HI)": 1459.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000749823",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000019718",
    "avgresponsejitter": " 0.000749823",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  6

    
    "id": " 6",
    "basecpu": " 2",
    "priority": " 9",
    "period": 42000.0,
    "C(LO)": 1699.0,
    "C(HI)": 1699.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000698970",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000773589",
    "avgresponsejitter": " 0.000698970",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  13

    
    "id": " 13",
    "basecpu": " 2",
    "priority": " 8",
    "period": 67500.0,
    "C(LO)": 2560.0,
    "C(HI)": 2560.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001431703",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.001476420",
    "avgresponsejitter": " 0.001431703",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  21

    
    "id": " 21",
    "basecpu": " 2",
    "priority": " 6",
    "period": 150000.0,
    "C(LO)": 2756.0,
    "C(HI)": 2756.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"



   </details>



  13. Taskset **e4_semi2wf_t11862**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t11862",
    "size": "25",
    "utilization": "1.9440000000000002",
    "realutilization": 1.9999996208112876,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  13

    
    "id": " 13",
    "basecpu": " 1",
    "priority": " 3",
    "period": 87500.0,
    "C(LO)": 8.0,
    "C(HI)": 17.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 2",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 1",
    "hightolow": " 0",
    "idletime": 21,
    "util": 99.99998148148148




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 22,
    "util": 99.99998059964727




   Real Utilization: 1.9999996208112876
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  25

    
    "id": " 25",
    "basecpu": " 1",
    "priority": " 0",
    "period": 907200.0,
    "C(LO)": 89472.0,
    "C(HI)": 178945.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  16

    
    "id": " 16",
    "basecpu": " 1",
    "priority": " 2",
    "period": 118125.0,
    "C(LO)": 6597.0,
    "C(HI)": 13194.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  1

    
    "id": " 1",
    "basecpu": " 1",
    "priority": " 9",
    "period": 25200.0,
    "C(LO)": 414.0,
    "C(HI)": 829.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 3",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000248366",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.025208114",
    "avgresponsejitter": " 0.000226297",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 2",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 4",
    "period": 60480.0,
    "C(LO)": 852.0,
    "C(HI)": 1705.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000372733",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.026501523",
    "avgresponsejitter": " 0.000372733",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  23

    
    "id": " 23",
    "basecpu": " 1",
    "priority": " 1",
    "period": 180000.0,
    "C(LO)": 735.0,
    "C(HI)": 1471.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  13

    
    "id": " 13",
    "basecpu": " 1",
    "priority": " 3",
    "period": 87500.0,
    "C(LO)": 8.0,
    "C(HI)": 17.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 2",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  12

    
    "id": " 12",
    "basecpu": " 1",
    "priority": " 8",
    "period": 81000.0,
    "C(LO)": 25555.0,
    "C(HI)": 25555.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.010530132",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.002941042",
    "avgresponsejitter": " 0.010530132",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  20

    
    "id": " 20",
    "basecpu": " 1",
    "priority": " 6",
    "period": 140000.0,
    "C(LO)": 11963.0,
    "C(HI)": 11963.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006786330",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.015084595",
    "avgresponsejitter": " 0.006786330",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  9

    
    "id": " 9",
    "basecpu": " 1",
    "priority": " 10",
    "period": 63000.0,
    "C(LO)": 5103.0,
    "C(HI)": 5103.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002693468",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000022492",
    "avgresponsejitter": " 0.002693468",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  21

    
    "id": " 21",
    "basecpu": " 1",
    "priority": " 5",
    "period": 162000.0,
    "C(LO)": 9202.0,
    "C(HI)": 9202.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004622012",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.021875321",
    "avgresponsejitter": " 0.004622012",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 2",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  14

    
    "id": " 14",
    "basecpu": " 1",
    "priority": " 7",
    "period": 90720.0,
    "C(LO)": 3065.0,
    "C(HI)": 3065.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001605486",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.013475270",
    "avgresponsejitter": " 0.001605486",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  24

    
    "id": " 24",
    "basecpu": " 2",
    "priority": " 0",
    "period": 525000.0,
    "C(LO)": 65459.0,
    "C(HI)": 130918.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  15

    
    "id": " 15",
    "basecpu": " 2",
    "priority": " 2",
    "period": 105000.0,
    "C(LO)": 2767.0,
    "C(HI)": 5534.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  3

    
    "id": " 3",
    "basecpu": " 2",
    "priority": " 7",
    "period": 28350.0,
    "C(LO)": 673.0,
    "C(HI)": 1346.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000327246",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.011893760",
    "avgresponsejitter": " 0.000327246",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  6

    
    "id": " 6",
    "basecpu": " 2",
    "priority": " 6",
    "period": 54000.0,
    "C(LO)": 427.0,
    "C(HI)": 855.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000199024",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.012224619",
    "avgresponsejitter": " 0.000199024",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  11

    
    "id": " 11",
    "basecpu": " 2",
    "priority": " 3",
    "period": 75000.0,
    "C(LO)": 377.0,
    "C(HI)": 755.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  22

    
    "id": " 22",
    "basecpu": " 2",
    "priority": " 1",
    "period": 168000.0,
    "C(LO)": 445.0,
    "C(HI)": 891.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  18

    
    "id": " 18",
    "basecpu": " 2",
    "priority": " 5",
    "period": 131250.0,
    "C(LO)": 23884.0,
    "C(HI)": 23884.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.011195420",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.012427459",
    "avgresponsejitter": " 0.011195420",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  10

    
    "id": " 10",
    "basecpu": " 2",
    "priority": " 9",
    "period": 70875.0,
    "C(LO)": 12680.0,
    "C(HI)": 12680.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006301003",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.004017637",
    "avgresponsejitter": " 0.006301003",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  5

    
    "id": " 5",
    "basecpu": " 2",
    "priority": " 11",
    "period": 50000.0,
    "C(LO)": 4154.0,
    "C(HI)": 4154.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002089811",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000760793",
    "avgresponsejitter": " 0.002089811",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  19

    
    "id": " 19",
    "basecpu": " 2",
    "priority": " 4",
    "period": 135000.0,
    "C(LO)": 8689.0,
    "C(HI)": 8689.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 2",
    "lockedtime": " 0.000000000"




   Task:  7

    
    "id": " 7",
    "basecpu": " 2",
    "priority": " 10",
    "period": 56250.0,
    "C(LO)": 2307.0,
    "C(HI)": 2307.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001159330",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.002854526",
    "avgresponsejitter": " 0.001159330",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  17

    
    "id": " 17",
    "basecpu": " 2",
    "priority": " 8",
    "period": 120000.0,
    "C(LO)": 2737.0,
    "C(HI)": 2737.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001567438",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.010322474",
    "avgresponsejitter": " 0.001567438",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 13",
    "period": 26250.0,
    "C(LO)": 569.0,
    "C(HI)": 569.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 3",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000295820",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.026256622",
    "avgresponsejitter": " 0.000292252",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 2",
    "lockedtime": " 0.000000144"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 12",
    "period": 47250.0,
    "C(LO)": 865.0,
    "C(HI)": 865.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000433751",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000323309",
    "avgresponsejitter": " 0.000433751",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"



   </details>



  14. Taskset **e4_semi2wf_t1201**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t1201",
    "size": "8",
    "utilization": "1.9920000000000002",
    "realutilization": 1.834965291005291,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  5

    
    "id": " 5",
    "basecpu": " 2",
    "priority": " 0",
    "period": 140000.0,
    "C(LO)": 63433.0,
    "C(HI)": 63433.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 34",
    "preemptions": " 55",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.043976174",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 5.481943877",
    "avgresponsejitter": " 0.039642622",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 1",
    "budgetexceededaftermigration": " 1",
    "timesmigrated": " 1",
    "timesrestored": " 0",
    "timesonc1": " 3",
    "timesonc2": " 85",
    "lockedtime": " 0.000002219"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 37800000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 3709150,
    "util": 90.18743386243386




   CPU: 2

    
    "id": 2,
    "hyperperiod": 1260000,
    "lowtohigh": " 4",
    "hightolow": " 3",
    "idletime": 2529162,
    "util": 93.30909523809524




   Real Utilization: 1.834965291005291
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 2",
    "period": 56250.0,
    "C(LO)": 7528.0,
    "C(HI)": 15057.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 85",
    "preemptions": " 8",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005134514",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 5.668756667",
    "avgresponsejitter": " 0.003807817",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 92",
    "timesonc2": " 0",
    "lockedtime": " 0.000000577"




   Task:  4

    
    "id": " 4",
    "basecpu": " 1",
    "priority": " 1",
    "period": 75600.0,
    "C(LO)": 5592.0,
    "C(HI)": 11184.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 64",
    "preemptions": " 5",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006828583",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 5.687961021",
    "avgresponsejitter": " 0.003074649",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 68",
    "timesonc2": " 0",
    "lockedtime": " 0.000000432"




   Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 3",
    "period": 37800.0,
    "C(LO)": 1609.0,
    "C(HI)": 3218.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 126",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000966003",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 5.687207631",
    "avgresponsejitter": " 0.000803270",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 125",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 0",
    "period": 900000.0,
    "C(LO)": 71537.0,
    "C(HI)": 71537.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 7",
    "preemptions": " 5",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.040909661",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 5.503581646",
    "avgresponsejitter": " 0.034590535",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 11",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 5",
    "period": 168000.0,
    "C(LO)": 12417.0,
    "C(HI)": 12417.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 29",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007470243",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 5.536007952",
    "avgresponsejitter": " 0.005972673",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 28",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 4",
    "period": 600000.0,
    "C(LO)": 6810.0,
    "C(HI)": 6810.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 9",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003849261",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 5.205480270",
    "avgresponsejitter": " 0.003346592",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 8",
    "timesonc2": " 0",
    "lockedtime": " 0.000000240"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 1",
    "period": 22500.0,
    "C(LO)": 9825.0,
    "C(HI)": 19650.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 208",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.015357456",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 5.635006261",
    "avgresponsejitter": " 0.005037249",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 4",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 211",
    "lockedtime": " 0.000004135"




   Task:  5

    
    "id": " 5",
    "basecpu": " 2",
    "priority": " 0",
    "period": 140000.0,
    "C(LO)": 63433.0,
    "C(HI)": 63433.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 34",
    "preemptions": " 55",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.043976174",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 5.481943877",
    "avgresponsejitter": " 0.039642622",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 1",
    "budgetexceededaftermigration": " 1",
    "timesmigrated": " 1",
    "timesrestored": " 0",
    "timesonc1": " 3",
    "timesonc2": " 85",
    "lockedtime": " 0.000002219"



   </details>



  15. Taskset **e4_semi2wf_t13241**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t13241",
    "size": "30",
    "utilization": "1.848",
    "realutilization": 1.9999995590828923,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 11",
    "period": 25200.0,
    "C(LO)": 4.0,
    "C(HI)": 8.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 2",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 1",
    "hightolow": " 0",
    "idletime": 29,
    "util": 99.99997442680775




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 21,
    "util": 99.99998148148148




   Real Utilization: 1.9999995590828923
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  30

    
    "id": " 30",
    "basecpu": " 1",
    "priority": " 0",
    "period": 945000.0,
    "C(LO)": 96964.0,
    "C(HI)": 193928.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  19

    
    "id": " 19",
    "basecpu": " 1",
    "priority": " 3",
    "period": 105000.0,
    "C(LO)": 6307.0,
    "C(HI)": 12614.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  11

    
    "id": " 11",
    "basecpu": " 1",
    "priority": " 6",
    "period": 70875.0,
    "C(LO)": 2350.0,
    "C(HI)": 4701.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 7",
    "period": 60000.0,
    "C(LO)": 1737.0,
    "C(HI)": 3474.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  14

    
    "id": " 14",
    "basecpu": " 1",
    "priority": " 4",
    "period": 78750.0,
    "C(LO)": 1940.0,
    "C(HI)": 3881.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  29

    
    "id": " 29",
    "basecpu": " 1",
    "priority": " 1",
    "period": 405000.0,
    "C(LO)": 4888.0,
    "C(HI)": 9776.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  12

    
    "id": " 12",
    "basecpu": " 1",
    "priority": " 5",
    "period": 72000.0,
    "C(LO)": 286.0,
    "C(HI)": 573.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  23

    
    "id": " 23",
    "basecpu": " 1",
    "priority": " 2",
    "period": 131250.0,
    "C(LO)": 42.0,
    "C(HI)": 85.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 11",
    "period": 25200.0,
    "C(LO)": 4.0,
    "C(HI)": 8.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 2",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  16

    
    "id": " 16",
    "basecpu": " 1",
    "priority": " 13",
    "period": 90720.0,
    "C(LO)": 15245.0,
    "C(HI)": 15245.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.008707006",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.003200580",
    "avgresponsejitter": " 0.008707006",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 17",
    "period": 26250.0,
    "C(LO)": 1701.0,
    "C(HI)": 1701.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000839114",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000030279",
    "avgresponsejitter": " 0.000839114",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  4

    
    "id": " 4",
    "basecpu": " 1",
    "priority": " 16",
    "period": 35000.0,
    "C(LO)": 1772.0,
    "C(HI)": 1772.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000963090",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000874538",
    "avgresponsejitter": " 0.000963090",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  20

    
    "id": " 20",
    "basecpu": " 1",
    "priority": " 9",
    "period": 113400.0,
    "C(LO)": 5375.0,
    "C(HI)": 5375.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  28

    
    "id": " 28",
    "basecpu": " 1",
    "priority": " 8",
    "period": 200000.0,
    "C(LO)": 4724.0,
    "C(HI)": 4724.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  17

    
    "id": " 17",
    "basecpu": " 1",
    "priority": " 12",
    "period": 94500.0,
    "C(LO)": 2127.0,
    "C(HI)": 2127.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001023192",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.011911634",
    "avgresponsejitter": " 0.001023192",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  13

    
    "id": " 13",
    "basecpu": " 1",
    "priority": " 15",
    "period": 75000.0,
    "C(LO)": 1454.0,
    "C(HI)": 1454.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000743435",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.001841919",
    "avgresponsejitter": " 0.000743435",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  18

    
    "id": " 18",
    "basecpu": " 1",
    "priority": " 10",
    "period": 101250.0,
    "C(LO)": 1733.0,
    "C(HI)": 1733.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  15

    
    "id": " 15",
    "basecpu": " 1",
    "priority": " 14",
    "period": 84375.0,
    "C(LO)": 1281.0,
    "C(HI)": 1281.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000607613",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.002589144",
    "avgresponsejitter": " 0.000607613",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  9

    
    "id": " 9",
    "basecpu": " 2",
    "priority": " 4",
    "period": 63000.0,
    "C(LO)": 7456.0,
    "C(HI)": 14912.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  25

    
    "id": " 25",
    "basecpu": " 2",
    "priority": " 2",
    "period": 157500.0,
    "C(LO)": 5665.0,
    "C(HI)": 11331.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  27

    
    "id": " 27",
    "basecpu": " 2",
    "priority": " 0",
    "period": 196875.0,
    "C(LO)": 6969.0,
    "C(HI)": 13939.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  26

    
    "id": " 26",
    "basecpu": " 2",
    "priority": " 1",
    "period": 162000.0,
    "C(LO)": 4906.0,
    "C(HI)": 9812.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  21

    
    "id": " 21",
    "basecpu": " 2",
    "priority": " 3",
    "period": 126000.0,
    "C(LO)": 3199.0,
    "C(HI)": 6399.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  7

    
    "id": " 7",
    "basecpu": " 2",
    "priority": " 5",
    "period": 50400.0,
    "C(LO)": 1044.0,
    "C(HI)": 2088.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000501141",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.012243667",
    "avgresponsejitter": " 0.000501141",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  6

    
    "id": " 6",
    "basecpu": " 2",
    "priority": " 9",
    "period": 39375.0,
    "C(LO)": 6172.0,
    "C(HI)": 6172.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003140682",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000397372",
    "avgresponsejitter": " 0.003140682",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  10

    
    "id": " 10",
    "basecpu": " 2",
    "priority": " 8",
    "period": 64800.0,
    "C(LO)": 6359.0,
    "C(HI)": 6359.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003686054",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.003541985",
    "avgresponsejitter": " 0.003686054",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  24

    
    "id": " 24",
    "basecpu": " 2",
    "priority": " 6",
    "period": 140000.0,
    "C(LO)": 6799.0,
    "C(HI)": 6799.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003436243",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.008803523",
    "avgresponsejitter": " 0.003436243",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  22

    
    "id": " 22",
    "basecpu": " 2",
    "priority": " 7",
    "period": 129600.0,
    "C(LO)": 3552.0,
    "C(HI)": 3552.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001567565",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.007232042",
    "avgresponsejitter": " 0.001567565",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 11",
    "period": 20000.0,
    "C(LO)": 245.0,
    "C(HI)": 245.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000137538",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000022480",
    "avgresponsejitter": " 0.000137538",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  5

    
    "id": " 5",
    "basecpu": " 2",
    "priority": " 10",
    "period": 37800.0,
    "C(LO)": 449.0,
    "C(HI)": 449.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000228853",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000164790",
    "avgresponsejitter": " 0.000228853",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"



   </details>



  16. Taskset **e4_semi2wf_t13361**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t13361",
    "size": "30",
    "utilization": "1.86",
    "realutilization": 1.999886111111111,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 12",
    "period": 45360.0,
    "C(LO)": 13.0,
    "C(HI)": 13.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000009529",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.002866622",
    "avgresponsejitter": " 0.000009529",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 2",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 26,
    "util": 99.9999770723104




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 12889,
    "util": 99.98863403880071




   Real Utilization: 1.999886111111111
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  25

    
    "id": " 25",
    "basecpu": " 1",
    "priority": " 2",
    "period": 157500.0,
    "C(LO)": 13342.0,
    "C(HI)": 26684.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006073760",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.018996285",
    "avgresponsejitter": " 0.006073760",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  19

    
    "id": " 19",
    "basecpu": " 1",
    "priority": " 3",
    "period": 87500.0,
    "C(LO)": 4676.0,
    "C(HI)": 9352.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002680336",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.016311486",
    "avgresponsejitter": " 0.002680336",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 2",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  11

    
    "id": " 11",
    "basecpu": " 1",
    "priority": " 5",
    "period": 56700.0,
    "C(LO)": 2616.0,
    "C(HI)": 5233.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001408372",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.013410607",
    "avgresponsejitter": " 0.001408372",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  18

    
    "id": " 18",
    "basecpu": " 1",
    "priority": " 4",
    "period": 84375.0,
    "C(LO)": 2522.0,
    "C(HI)": 5044.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001484231",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.014823105",
    "avgresponsejitter": " 0.001484231",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  9

    
    "id": " 9",
    "basecpu": " 1",
    "priority": " 6",
    "period": 47250.0,
    "C(LO)": 479.0,
    "C(HI)": 959.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000228511",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.013178126",
    "avgresponsejitter": " 0.000228511",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  4

    
    "id": " 4",
    "basecpu": " 1",
    "priority": " 7",
    "period": 26250.0,
    "C(LO)": 241.0,
    "C(HI)": 482.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 3",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000141222",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.026256739",
    "avgresponsejitter": " 0.000138994",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 2",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  26

    
    "id": " 26",
    "basecpu": " 1",
    "priority": " 1",
    "period": 162000.0,
    "C(LO)": 1239.0,
    "C(HI)": 2478.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000568817",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.025074306",
    "avgresponsejitter": " 0.000568817",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 9",
    "period": 18900.0,
    "C(LO)": 24.0,
    "C(HI)": 48.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 4",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000020495",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.037806586",
    "avgresponsejitter": " 0.000018661",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 3",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  30

    
    "id": " 30",
    "basecpu": " 1",
    "priority": " 0",
    "period": 708750.0,
    "C(LO)": 109834.0,
    "C(HI)": 109834.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 6",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 6",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 13",
    "period": 40000.0,
    "C(LO)": 4028.0000000000005,
    "C(HI)": 4028.0000000000005,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 3",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002334631",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.040006736",
    "avgresponsejitter": " 0.001959177",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 2",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  23

    
    "id": " 23",
    "basecpu": " 1",
    "priority": " 10",
    "period": 129600.0,
    "C(LO)": 8637.0,
    "C(HI)": 8637.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004652483",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.003150778",
    "avgresponsejitter": " 0.004652483",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  27

    
    "id": " 27",
    "basecpu": " 1",
    "priority": " 8",
    "period": 168750.0,
    "C(LO)": 9934.0,
    "C(HI)": 9934.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005204378",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.007827886",
    "avgresponsejitter": " 0.005204378",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 14",
    "period": 35000.0,
    "C(LO)": 1379.0,
    "C(HI)": 1379.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 3",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000784081",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.035006955",
    "avgresponsejitter": " 0.000671261",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 2",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 15",
    "period": 33750.0,
    "C(LO)": 913.0,
    "C(HI)": 913.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 3",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000438757",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.033756775",
    "avgresponsejitter": " 0.000417799",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 2",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  16

    
    "id": " 16",
    "basecpu": " 1",
    "priority": " 11",
    "period": 75600.0,
    "C(LO)": 603.0,
    "C(HI)": 603.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000266637",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.002880111",
    "avgresponsejitter": " 0.000266637",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 12",
    "period": 45360.0,
    "C(LO)": 13.0,
    "C(HI)": 13.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000009529",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.002866622",
    "avgresponsejitter": " 0.000009529",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 2",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  14

    
    "id": " 14",
    "basecpu": " 2",
    "priority": " 4",
    "period": 65625.0,
    "C(LO)": 5891.0,
    "C(HI)": 11782.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003089742",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.017861423",
    "avgresponsejitter": " 0.003089742",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 2",
    "lockedtime": " 0.000000000"




   Task:  10

    
    "id": " 10",
    "basecpu": " 2",
    "priority": " 5",
    "period": 50400.0,
    "C(LO)": 2642.0,
    "C(HI)": 5284.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002333850",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.015523709",
    "avgresponsejitter": " 0.002333850",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 2",
    "lockedtime": " 0.000000000"




   Task:  22

    
    "id": " 22",
    "basecpu": " 2",
    "priority": " 2",
    "period": 120000.0,
    "C(LO)": 5266.0,
    "C(HI)": 10533.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002860090",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.022488228",
    "avgresponsejitter": " 0.002860090",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 9",
    "period": 10000.0,
    "C(LO)": 265.0,
    "C(HI)": 531.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 6",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000148640",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.040006946",
    "avgresponsejitter": " 0.000118805",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 5",
    "lockedtime": " 0.000000240"




   Task:  20

    
    "id": " 20",
    "basecpu": " 2",
    "priority": " 3",
    "period": 113400.0,
    "C(LO)": 2651.0,
    "C(HI)": 5302.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001529132",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.020955141",
    "avgresponsejitter": " 0.001529132",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  28

    
    "id": " 28",
    "basecpu": " 2",
    "priority": " 1",
    "period": 189000.0,
    "C(LO)": 1151.0,
    "C(HI)": 2302.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000599333",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.025352754",
    "avgresponsejitter": " 0.000599333",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  29

    
    "id": " 29",
    "basecpu": " 2",
    "priority": " 0",
    "period": 196875.0,
    "C(LO)": 174.0,
    "C(HI)": 349.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000100279",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.025956207",
    "avgresponsejitter": " 0.000100279",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  17

    
    "id": " 17",
    "basecpu": " 2",
    "priority": " 8",
    "period": 84000.0,
    "C(LO)": 12309.0,
    "C(HI)": 12309.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007227348",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.004453898",
    "avgresponsejitter": " 0.007227348",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 2",
    "lockedtime": " 0.000000000"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 13",
    "period": 15750.0,
    "C(LO)": 1814.0,
    "C(HI)": 1814.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 4",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000930766",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.031505760",
    "avgresponsejitter": " 0.000925360",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 3",
    "lockedtime": " 0.000000000"




   Task:  12

    
    "id": " 12",
    "basecpu": " 2",
    "priority": " 12",
    "period": 60000.0,
    "C(LO)": 3717.0,
    "C(HI)": 3717.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001893063",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000958817",
    "avgresponsejitter": " 0.001893063",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  21

    
    "id": " 21",
    "basecpu": " 2",
    "priority": " 7",
    "period": 118125.0,
    "C(LO)": 4744.0,
    "C(HI)": 4744.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002217880",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.011685096",
    "avgresponsejitter": " 0.002217880",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  15

    
    "id": " 15",
    "basecpu": " 2",
    "priority": " 10",
    "period": 72000.0,
    "C(LO)": 1763.0,
    "C(HI)": 1763.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000727940",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.003610628",
    "avgresponsejitter": " 0.000727940",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  13

    
    "id": " 13",
    "basecpu": " 2",
    "priority": " 11",
    "period": 64800.0,
    "C(LO)": 1466.0,
    "C(HI)": 1466.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000751027",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.002855676",
    "avgresponsejitter": " 0.000751027",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  24

    
    "id": " 24",
    "basecpu": " 2",
    "priority": " 6",
    "period": 131250.0,
    "C(LO)": 2888.0,
    "C(HI)": 2888.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001612649",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.013906925",
    "avgresponsejitter": " 0.001612649",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"



   </details>



  17. Taskset **e4_semi2wf_t13508**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t13508",
    "size": "30",
    "utilization": "1.8840000000000001",
    "realutilization": 1.9999995767195768,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 14",
    "period": 28350.0,
    "C(LO)": 5.0,
    "C(HI)": 5.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 25,
    "util": 99.99997795414463




   CPU: 2

    
    "id": 2,
    "hyperperiod": 37800000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 23,
    "util": 99.99997971781305




   Real Utilization: 1.9999995767195768
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  27

    
    "id": " 27",
    "basecpu": " 1",
    "priority": " 2",
    "period": 168750.0,
    "C(LO)": 15090.0,
    "C(HI)": 30181.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  12

    
    "id": " 12",
    "basecpu": " 1",
    "priority": " 6",
    "period": 56700.0,
    "C(LO)": 3831.0,
    "C(HI)": 7662.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  29

    
    "id": " 29",
    "basecpu": " 1",
    "priority": " 1",
    "period": 450000.0,
    "C(LO)": 26106.0,
    "C(HI)": 52213.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  26

    
    "id": " 26",
    "basecpu": " 1",
    "priority": " 3",
    "period": 141750.0,
    "C(LO)": 4026.0,
    "C(HI)": 8052.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  16

    
    "id": " 16",
    "basecpu": " 1",
    "priority": " 5",
    "period": 78750.0,
    "C(LO)": 1774.0,
    "C(HI)": 3548.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  22

    
    "id": " 22",
    "basecpu": " 1",
    "priority": " 4",
    "period": 112500.0,
    "C(LO)": 1767.0,
    "C(HI)": 3534.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 7",
    "period": 20000.0,
    "C(LO)": 126.0,
    "C(HI)": 252.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  30

    
    "id": " 30",
    "basecpu": " 1",
    "priority": " 0",
    "period": 700000.0,
    "C(LO)": 1660.0,
    "C(HI)": 3320.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 13",
    "period": 30240.0,
    "C(LO)": 4485.0,
    "C(HI)": 4485.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 12",
    "period": 50000.0,
    "C(LO)": 4123.0,
    "C(HI)": 4123.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  10

    
    "id": " 10",
    "basecpu": " 1",
    "priority": " 10",
    "period": 52500.0,
    "C(LO)": 3981.0,
    "C(HI)": 3981.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  9

    
    "id": " 9",
    "basecpu": " 1",
    "priority": " 11",
    "period": 50400.0,
    "C(LO)": 1952.0,
    "C(HI)": 1952.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  19

    
    "id": " 19",
    "basecpu": " 1",
    "priority": " 9",
    "period": 101250.0,
    "C(LO)": 2154.0,
    "C(HI)": 2154.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  20

    
    "id": " 20",
    "basecpu": " 1",
    "priority": " 8",
    "period": 105000.0,
    "C(LO)": 68.0,
    "C(HI)": 68.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 14",
    "period": 28350.0,
    "C(LO)": 5.0,
    "C(HI)": 5.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  28

    
    "id": " 28",
    "basecpu": " 2",
    "priority": " 0",
    "period": 175000.0,
    "C(LO)": 20515.0,
    "C(HI)": 41031.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  24

    
    "id": " 24",
    "basecpu": " 2",
    "priority": " 2",
    "period": 131250.0,
    "C(LO)": 7997.000000000001,
    "C(HI)": 15994.000000000002,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 7",
    "period": 18900.0,
    "C(LO)": 1085.0,
    "C(HI)": 2170.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  23

    
    "id": " 23",
    "basecpu": " 2",
    "priority": " 3",
    "period": 120000.0,
    "C(LO)": 2988.0,
    "C(HI)": 5976.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  7

    
    "id": " 7",
    "basecpu": " 2",
    "priority": " 5",
    "period": 33750.0,
    "C(LO)": 715.0,
    "C(HI)": 1431.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  21

    
    "id": " 21",
    "basecpu": " 2",
    "priority": " 4",
    "period": 108000.0,
    "C(LO)": 671.0,
    "C(HI)": 1343.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  25

    
    "id": " 25",
    "basecpu": " 2",
    "priority": " 1",
    "period": 140000.0,
    "C(LO)": 349.0,
    "C(HI)": 698.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  18

    
    "id": " 18",
    "basecpu": " 2",
    "priority": " 6",
    "period": 94500.0,
    "C(LO)": 11959.0,
    "C(HI)": 11959.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  15

    
    "id": " 15",
    "basecpu": " 2",
    "priority": " 9",
    "period": 67500.0,
    "C(LO)": 6586.0,
    "C(HI)": 6586.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  13

    
    "id": " 13",
    "basecpu": " 2",
    "priority": " 11",
    "period": 60000.0,
    "C(LO)": 4060.0000000000005,
    "C(HI)": 4060.0000000000005,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  17

    
    "id": " 17",
    "basecpu": " 2",
    "priority": " 8",
    "period": 90000.0,
    "C(LO)": 2300.0,
    "C(HI)": 2300.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  11

    
    "id": " 11",
    "basecpu": " 2",
    "priority": " 12",
    "period": 56250.0,
    "C(LO)": 675.0,
    "C(HI)": 675.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  14

    
    "id": " 14",
    "basecpu": " 2",
    "priority": " 10",
    "period": 60480.0,
    "C(LO)": 698.0,
    "C(HI)": 698.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 13",
    "period": 26250.0,
    "C(LO)": 188.0,
    "C(HI)": 188.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  3

    
    "id": " 3",
    "basecpu": " 2",
    "priority": " 14",
    "period": 25200.0,
    "C(LO)": 174.0,
    "C(HI)": 174.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"



   </details>



  18. Taskset **e4_semi2wf_t13920**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t13920",
    "size": "30",
    "utilization": "1.9320000000000002",
    "realutilization": 1.6957758906525573,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    
    "id": " 1",
    "basecpu": " 1",
    "priority": " 15",
    "period": 10000.0,
    "C(LO)": 220.0,
    "C(HI)": 220.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2798",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000128652",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.972008093",
    "avgresponsejitter": " 0.000118309",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 10",
    "timesrestored": " 10",
    "timesonc1": " 2778",
    "timesonc2": " 19",
    "lockedtime": " 0.000029529"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 36",
    "hightolow": " 36",
    "idletime": 17349459,
    "util": 84.70065343915344




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 17149555,
    "util": 84.8769356261023




   Real Utilization: 1.6957758906525573
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 10",
    "period": 33750.0,
    "C(LO)": 2504.0,
    "C(HI)": 5008.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 830",
    "preemptions": " 76",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004086736",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.946555865",
    "avgresponsejitter": " 0.001306691",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 11",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 916",
    "timesonc2": " 0",
    "lockedtime": " 0.000011306"




   Task:  18

    
    "id": " 18",
    "basecpu": " 1",
    "priority": " 6",
    "period": 100000.0,
    "C(LO)": 4151.0,
    "C(HI)": 8302.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 281",
    "preemptions": " 70",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.014511787",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.903017258",
    "avgresponsejitter": " 0.002413832",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 4",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 354",
    "timesonc2": " 0",
    "lockedtime": " 0.000002375"




   Task:  13

    
    "id": " 13",
    "basecpu": " 1",
    "priority": " 7",
    "period": 75000.0,
    "C(LO)": 1792.0,
    "C(HI)": 3584.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 374",
    "preemptions": " 24",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002819450",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.902079399",
    "avgresponsejitter": " 0.000914577",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 398",
    "timesonc2": " 0",
    "lockedtime": " 0.000001676"




   Task:  22

    
    "id": " 22",
    "basecpu": " 1",
    "priority": " 2",
    "period": 113400.0,
    "C(LO)": 2504.0,
    "C(HI)": 5009.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 248",
    "preemptions": " 56",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004651868",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.896707514",
    "avgresponsejitter": " 0.001410793",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 304",
    "timesonc2": " 0",
    "lockedtime": " 0.000000793"




   Task:  19

    
    "id": " 19",
    "basecpu": " 1",
    "priority": " 5",
    "period": 100800.0,
    "C(LO)": 1765.0,
    "C(HI)": 3530.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 279",
    "preemptions": " 39",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005973060",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.921606462",
    "avgresponsejitter": " 0.000974967",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 4",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 321",
    "timesonc2": " 0",
    "lockedtime": " 0.000000480"




   Task:  20

    
    "id": " 20",
    "basecpu": " 1",
    "priority": " 4",
    "period": 105000.0,
    "C(LO)": 1623.0,
    "C(HI)": 3247.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 268",
    "preemptions": " 11",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002933111",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.930131514",
    "avgresponsejitter": " 0.000864180",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 281",
    "timesonc2": " 0",
    "lockedtime": " 0.000001030"




   Task:  21

    
    "id": " 21",
    "basecpu": " 1",
    "priority": " 3",
    "period": 112500.0,
    "C(LO)": 1097.0,
    "C(HI)": 2195.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 250",
    "preemptions": " 13",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001956526",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.905225859",
    "avgresponsejitter": " 0.000584288",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 264",
    "timesonc2": " 0",
    "lockedtime": " 0.000001526"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 11",
    "period": 18900.0,
    "C(LO)": 73.0,
    "C(HI)": 147.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1481",
    "preemptions": " 4",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000177874",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.953360465",
    "avgresponsejitter": " 0.000040967",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 7",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1491",
    "timesonc2": " 0",
    "lockedtime": " 0.000008664"




   Task:  27

    
    "id": " 27",
    "basecpu": " 1",
    "priority": " 1",
    "period": 189000.0,
    "C(LO)": 471.0,
    "C(HI)": 943.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 149",
    "preemptions": " 5",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000844333",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.786229246",
    "avgresponsejitter": " 0.000254384",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 156",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  29

    
    "id": " 29",
    "basecpu": " 1",
    "priority": " 0",
    "period": 506250.0,
    "C(LO)": 105046.0,
    "C(HI)": 105046.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 57",
    "preemptions": " 655",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.089327733",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.844812336",
    "avgresponsejitter": " 0.067545141",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 711",
    "timesonc2": " 0",
    "lockedtime": " 0.000049871"




   Task:  23

    
    "id": " 23",
    "basecpu": " 1",
    "priority": " 9",
    "period": 118125.0,
    "C(LO)": 23388.0,
    "C(HI)": 23388.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 238",
    "preemptions": " 442",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.018402177",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.878767688",
    "avgresponsejitter": " 0.012450150",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 679",
    "timesonc2": " 0",
    "lockedtime": " 0.000025135"




   Task:  17

    
    "id": " 17",
    "basecpu": " 1",
    "priority": " 12",
    "period": 90000.0,
    "C(LO)": 4548.0,
    "C(HI)": 4548.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 312",
    "preemptions": " 11",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002947565",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.900135384",
    "avgresponsejitter": " 0.002286973",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 322",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  14

    
    "id": " 14",
    "basecpu": " 1",
    "priority": " 13",
    "period": 81000.0,
    "C(LO)": 3244.0,
    "C(HI)": 3244.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 347",
    "preemptions": " 36",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002057165",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.945008898",
    "avgresponsejitter": " 0.001633943",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 382",
    "timesonc2": " 0",
    "lockedtime": " 0.000008054"




   Task:  1

    
    "id": " 1",
    "basecpu": " 1",
    "priority": " 15",
    "period": 10000.0,
    "C(LO)": 220.0,
    "C(HI)": 220.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2798",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000128652",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.972008093",
    "avgresponsejitter": " 0.000118309",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 10",
    "timesrestored": " 10",
    "timesonc1": " 2778",
    "timesonc2": " 19",
    "lockedtime": " 0.000029529"




   Task:  24

    
    "id": " 24",
    "basecpu": " 1",
    "priority": " 8",
    "period": 135000.0,
    "C(LO)": 1213.0,
    "C(HI)": 1213.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 209",
    "preemptions": " 6",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000828216",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.949645514",
    "avgresponsejitter": " 0.000609000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 214",
    "timesonc2": " 0",
    "lockedtime": " 0.000000637"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 14",
    "period": 56700.0,
    "C(LO)": 484.0,
    "C(HI)": 484.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 495",
    "preemptions": " 8",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000379724",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.953107126",
    "avgresponsejitter": " 0.000248868",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 3",
    "timesrestored": " 3",
    "timesonc1": " 499",
    "timesonc2": " 3",
    "lockedtime": " 0.000005526"




   Task:  15

    
    "id": " 15",
    "basecpu": " 2",
    "priority": " 3",
    "period": 84000.0,
    "C(LO)": 12508.0,
    "C(HI)": 25017.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 334",
    "preemptions": " 360",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.023591441",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.888006015",
    "avgresponsejitter": " 0.007881946",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 693",
    "lockedtime": " 0.000018811"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 10",
    "period": 22500.0,
    "C(LO)": 430.0,
    "C(HI)": 861.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1245",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000260853",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.967505787",
    "avgresponsejitter": " 0.000216465",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1246",
    "lockedtime": " 0.000040703"




   Task:  25

    
    "id": " 25",
    "basecpu": " 2",
    "priority": " 2",
    "period": 157500.0,
    "C(LO)": 2526.0,
    "C(HI)": 5053.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 179",
    "preemptions": " 8",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.009173441",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.878518360",
    "avgresponsejitter": " 0.001325733",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 186",
    "lockedtime": " 0.000000000"




   Task:  9

    
    "id": " 9",
    "basecpu": " 2",
    "priority": " 4",
    "period": 63000.0,
    "C(LO)": 730.0,
    "C(HI)": 1460.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 445",
    "preemptions": " 6",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001350237",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.909501727",
    "avgresponsejitter": " 0.000366132",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 450",
    "lockedtime": " 0.000000000"




   Task:  7

    
    "id": " 7",
    "basecpu": " 2",
    "priority": " 5",
    "period": 50000.0,
    "C(LO)": 343.0,
    "C(HI)": 687.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 561",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.010872880",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.950130913",
    "avgresponsejitter": " 0.000193435",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 562",
    "lockedtime": " 0.000019309"




   Task:  26

    
    "id": " 26",
    "basecpu": " 2",
    "priority": " 1",
    "period": 180000.0,
    "C(LO)": 1091.0,
    "C(HI)": 2182.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 157",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007724577",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.900360219",
    "avgresponsejitter": " 0.000599489",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 158",
    "lockedtime": " 0.000000000"




   Task:  11

    
    "id": " 11",
    "basecpu": " 2",
    "priority": " 9",
    "period": 70875.0,
    "C(LO)": 20033.0,
    "C(HI)": 20033.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 396",
    "preemptions": " 453",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.012975796",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.925236474",
    "avgresponsejitter": " 0.010442204",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 848",
    "lockedtime": " 0.000029874"




   Task:  30

    
    "id": " 30",
    "basecpu": " 2",
    "priority": " 0",
    "period": 567000.0,
    "C(LO)": 64568.0,
    "C(HI)": 64568.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 51",
    "preemptions": " 309",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.050459826",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.794626129",
    "avgresponsejitter": " 0.039198180",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 359",
    "lockedtime": " 0.000016943"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 13",
    "period": 15750.0,
    "C(LO)": 930.0,
    "C(HI)": 930.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1777",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000558390",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.956257784",
    "avgresponsejitter": " 0.000459808",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1777",
    "lockedtime": " 0.000031459"




   Task:  28

    
    "id": " 28",
    "basecpu": " 2",
    "priority": " 6",
    "period": 196875.0,
    "C(LO)": 8417.0,
    "C(HI)": 8417.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 144",
    "preemptions": " 35",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006027330",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.957062691",
    "avgresponsejitter": " 0.004311664",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 178",
    "lockedtime": " 0.000002009"




   Task:  12

    
    "id": " 12",
    "basecpu": " 2",
    "priority": " 8",
    "period": 72000.0,
    "C(LO)": 2310.0,
    "C(HI)": 2310.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 390",
    "preemptions": " 11",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.013660877",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.936005814",
    "avgresponsejitter": " 0.001254535",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 400",
    "lockedtime": " 0.000000553"




   Task:  6

    
    "id": " 6",
    "basecpu": " 2",
    "priority": " 12",
    "period": 39375.0,
    "C(LO)": 664.0,
    "C(HI)": 664.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 712",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000398384",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.956737477",
    "avgresponsejitter": " 0.000331571",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 711",
    "lockedtime": " 0.000007856"




   Task:  16

    
    "id": " 16",
    "basecpu": " 2",
    "priority": " 7",
    "period": 84375.0,
    "C(LO)": 808.0,
    "C(HI)": 808.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 333",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000669057",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.934527042",
    "avgresponsejitter": " 0.000401495",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 334",
    "lockedtime": " 0.000004141"




   Task:  10

    
    "id": " 10",
    "basecpu": " 2",
    "priority": " 11",
    "period": 64800.0,
    "C(LO)": 28.0,
    "C(HI)": 28.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 433",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.065071847",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.928806231",
    "avgresponsejitter": " 0.000169871",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 433",
    "lockedtime": " 0.000007408"



   </details>



  19. Taskset **e4_semi2wf_t1401**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t1401",
    "size": "8",
    "utilization": "2.016",
    "realutilization": 1.7899185890652558,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 1",
    "period": 81000.0,
    "C(LO)": 8769.0,
    "C(HI)": 8769.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 120",
    "preemptions": " 52",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006366913",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.558007096",
    "avgresponsejitter": " 0.005021324",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 1",
    "budgetexceededaftermigration": " 1",
    "timesmigrated": " 3",
    "timesrestored": " 2",
    "timesonc1": " 6",
    "timesonc2": " 165",
    "lockedtime": " 0.000002550"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 56700000,
    "lowtohigh": " 3",
    "hightolow": " 3",
    "idletime": 5893441,
    "util": 89.6059241622575




   CPU: 2

    
    "id": 2,
    "hyperperiod": 28350000,
    "lowtohigh": " 10",
    "hightolow": " 9",
    "idletime": 6018175,
    "util": 89.38593474426807




   Real Utilization: 1.7899185890652558
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 0",
    "period": 540000.0,
    "C(LO)": 77996.0,
    "C(HI)": 155993.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 19",
    "preemptions": " 23",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.167527306",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.198458222",
    "avgresponsejitter": " 0.052548517",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 42",
    "timesonc2": " 0",
    "lockedtime": " 0.000002742"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 2",
    "period": 162000.0,
    "C(LO)": 11955.0,
    "C(HI)": 23911.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 61",
    "preemptions": " 8",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.009000763",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.558006144",
    "avgresponsejitter": " 0.006281703",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 68",
    "timesonc2": " 0",
    "lockedtime": " 0.000000916"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 1",
    "period": 180000.0,
    "C(LO)": 5027.0,
    "C(HI)": 10055.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 55",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006459643",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.540006874",
    "avgresponsejitter": " 0.002638550",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 56",
    "timesonc2": " 0",
    "lockedtime": " 0.000001072"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 3",
    "period": 67500.0,
    "C(LO)": 29597.0,
    "C(HI)": 29597.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 145",
    "preemptions": " 29",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.019569129",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.652506646",
    "avgresponsejitter": " 0.015426805",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 173",
    "timesonc2": " 0",
    "lockedtime": " 0.000004222"




   Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 4",
    "period": 65625.0,
    "C(LO)": 3802.0,
    "C(HI)": 3802.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 149",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001952880",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.646881231",
    "avgresponsejitter": " 0.001924042",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 2",
    "timesonc1": " 147",
    "timesonc2": " 1",
    "lockedtime": " 0.000000165"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 2",
    "period": 10000.0,
    "C(LO)": 2870.0,
    "C(HI)": 5740.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 966",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004533327",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.640006264",
    "avgresponsejitter": " 0.001469658",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 10",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 975",
    "lockedtime": " 0.000001105"




   Task:  8

    
    "id": " 8",
    "basecpu": " 2",
    "priority": " 0",
    "period": 787500.0,
    "C(LO)": 271663.0,
    "C(HI)": 271663.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 14",
    "preemptions": " 206",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.178385724",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.451478357",
    "avgresponsejitter": " 0.158901613",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 219",
    "lockedtime": " 0.000002970"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 1",
    "period": 81000.0,
    "C(LO)": 8769.0,
    "C(HI)": 8769.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 120",
    "preemptions": " 52",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006366913",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.558007096",
    "avgresponsejitter": " 0.005021324",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 1",
    "budgetexceededaftermigration": " 1",
    "timesmigrated": " 3",
    "timesrestored": " 2",
    "timesonc1": " 6",
    "timesonc2": " 165",
    "lockedtime": " 0.000002550"



   </details>



  20. Taskset **e4_semi2wf_t14218**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t14218",
    "size": "30",
    "utilization": "1.9680000000000002",
    "realutilization": 1.9741343915343916,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 15",
    "period": 15750.0,
    "C(LO)": 1648.0,
    "C(HI)": 1648.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 165",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000855351",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.592009330",
    "avgresponsejitter": " 0.000836715",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 2",
    "timesonc1": " 159",
    "timesonc2": " 5",
    "lockedtime": " 0.000000982"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 2",
    "hightolow": " 2",
    "idletime": 1439506,
    "util": 98.73059435626102




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 2",
    "hightolow": " 2",
    "idletime": 1493654,
    "util": 98.68284479717813




   Real Utilization: 1.9741343915343916
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 7",
    "period": 60480.0,
    "C(LO)": 3079.0,
    "C(HI)": 6159.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 44",
    "preemptions": " 5",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003561514",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.543846483",
    "avgresponsejitter": " 0.001696183",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 48",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  9

    
    "id": " 9",
    "basecpu": " 1",
    "priority": " 6",
    "period": 64800.0,
    "C(LO)": 2998.0,
    "C(HI)": 5996.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 41",
    "preemptions": " 9",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004466357",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.527206574",
    "avgresponsejitter": " 0.001685844",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 49",
    "timesonc2": " 0",
    "lockedtime": " 0.000000402"




   Task:  22

    
    "id": " 22",
    "basecpu": " 1",
    "priority": " 3",
    "period": 126000.0,
    "C(LO)": 4863.0,
    "C(HI)": 9727.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 22",
    "preemptions": " 3",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003506297",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.520284784",
    "avgresponsejitter": " 0.002409276",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 24",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  11

    
    "id": " 11",
    "basecpu": " 1",
    "priority": " 5",
    "period": 75000.0,
    "C(LO)": 1864.0,
    "C(HI)": 3729.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 36",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.016732997",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.550007342",
    "avgresponsejitter": " 0.001407685",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 38",
    "timesonc2": " 0",
    "lockedtime": " 0.000000411"




   Task:  24

    
    "id": " 24",
    "basecpu": " 1",
    "priority": " 2",
    "period": 141750.0,
    "C(LO)": 1965.0000000000002,
    "C(HI)": 3930.9999999999995,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 20",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002053736",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.551506529",
    "avgresponsejitter": " 0.001053282",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 20",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  18

    
    "id": " 18",
    "basecpu": " 1",
    "priority": " 4",
    "period": 105000.0,
    "C(LO)": 631.0,
    "C(HI)": 1263.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 26",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005842417",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.520008435",
    "avgresponsejitter": " 0.000524976",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 27",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  27

    
    "id": " 27",
    "basecpu": " 1",
    "priority": " 1",
    "period": 189000.0,
    "C(LO)": 647.0,
    "C(HI)": 1295.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 15",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001373486",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.457850688",
    "avgresponsejitter": " 0.000412366",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 16",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  30

    
    "id": " 30",
    "basecpu": " 1",
    "priority": " 0",
    "period": 810000.0,
    "C(LO)": 164741.0,
    "C(HI)": 164741.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 5",
    "preemptions": " 66",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.139933895",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.430948934",
    "avgresponsejitter": " 0.116006420",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 70",
    "timesonc2": " 0",
    "lockedtime": " 0.000004150"




   Task:  23

    
    "id": " 23",
    "basecpu": " 1",
    "priority": " 8",
    "period": 129600.0,
    "C(LO)": 20653.0,
    "C(HI)": 20653.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 21",
    "preemptions": " 24",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.013942000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.462407462",
    "avgresponsejitter": " 0.011345126",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 44",
    "timesonc2": " 0",
    "lockedtime": " 0.000001183"




   Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 15",
    "period": 15750.0,
    "C(LO)": 1648.0,
    "C(HI)": 1648.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 165",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000855351",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.592009330",
    "avgresponsejitter": " 0.000836715",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 2",
    "timesonc1": " 159",
    "timesonc2": " 5",
    "lockedtime": " 0.000000982"




   Task:  16

    
    "id": " 16",
    "basecpu": " 1",
    "priority": " 9",
    "period": 90720.0,
    "C(LO)": 6148.0,
    "C(HI)": 6148.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 30",
    "preemptions": " 6",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005030495",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.540167616",
    "avgresponsejitter": " 0.003300186",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 35",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  12

    
    "id": " 12",
    "basecpu": " 1",
    "priority": " 12",
    "period": 81000.0,
    "C(LO)": 2189.0,
    "C(HI)": 2189.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 33",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001305739",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.511006709",
    "avgresponsejitter": " 0.001071568",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 32",
    "timesonc2": " 0",
    "lockedtime": " 0.000000411"




   Task:  13

    
    "id": " 13",
    "basecpu": " 1",
    "priority": " 11",
    "period": 84375.0,
    "C(LO)": 1921.0,
    "C(HI)": 1921.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 32",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001154670",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.531257580",
    "avgresponsejitter": " 0.000984111",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 31",
    "timesonc2": " 0",
    "lockedtime": " 0.000000898"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 14",
    "period": 56700.0,
    "C(LO)": 1234.0,
    "C(HI)": 1234.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 47",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000634321",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.554969952",
    "avgresponsejitter": " 0.000627946",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 1",
    "timesonc1": " 44",
    "timesonc2": " 2",
    "lockedtime": " 0.000001910"




   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 13",
    "period": 60000.0,
    "C(LO)": 598.0,
    "C(HI)": 598.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 44",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000308351",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.521430072",
    "avgresponsejitter": " 0.000302529",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 1",
    "timesonc1": " 42",
    "timesonc2": " 1",
    "lockedtime": " 0.000003078"




   Task:  14

    
    "id": " 14",
    "basecpu": " 1",
    "priority": " 10",
    "period": 87500.0,
    "C(LO)": 547.0,
    "C(HI)": 547.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 31",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000322730",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.537506604",
    "avgresponsejitter": " 0.000269790",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 30",
    "timesonc2": " 0",
    "lockedtime": " 0.000000231"




   Task:  15

    
    "id": " 15",
    "basecpu": " 2",
    "priority": " 6",
    "period": 90000.0,
    "C(LO)": 6898.0,
    "C(HI)": 13796.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 30",
    "preemptions": " 6",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.009665021",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.521838910",
    "avgresponsejitter": " 0.003770607",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 35",
    "lockedtime": " 0.000000835"




   Task:  19

    
    "id": " 19",
    "basecpu": " 2",
    "priority": " 4",
    "period": 108000.0,
    "C(LO)": 4476.0,
    "C(HI)": 8953.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 25",
    "preemptions": " 5",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004685964",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.484005850",
    "avgresponsejitter": " 0.002343486",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 29",
    "lockedtime": " 0.000000144"




   Task:  10

    
    "id": " 10",
    "basecpu": " 2",
    "priority": " 7",
    "period": 70875.0,
    "C(LO)": 1788.0,
    "C(HI)": 3576.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 38",
    "preemptions": " 3",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001209856",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.555598186",
    "avgresponsejitter": " 0.000901015",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 40",
    "lockedtime": " 0.000000565"




   Task:  26

    
    "id": " 26",
    "basecpu": " 2",
    "priority": " 1",
    "period": 168750.0,
    "C(LO)": 3428.0,
    "C(HI)": 6857.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 17",
    "preemptions": " 3",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003858078",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.531256045",
    "avgresponsejitter": " 0.001899760",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 19",
    "lockedtime": " 0.000000375"




   Task:  21

    
    "id": " 21",
    "basecpu": " 2",
    "priority": " 3",
    "period": 120000.0,
    "C(LO)": 1110.0,
    "C(HI)": 2220.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 23",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000659673",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.527294183",
    "avgresponsejitter": " 0.000567934",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 22",
    "lockedtime": " 0.000000000"




   Task:  3

    
    "id": " 3",
    "basecpu": " 2",
    "priority": " 9",
    "period": 22500.0,
    "C(LO)": 181.0,
    "C(HI)": 362.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 117",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002726435",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.587505760",
    "avgresponsejitter": " 0.000117883",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 118",
    "lockedtime": " 0.000000144"




   Task:  25

    
    "id": " 25",
    "basecpu": " 2",
    "priority": " 2",
    "period": 162000.0,
    "C(LO)": 339.0,
    "C(HI)": 678.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 17",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000494114",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.434777628",
    "avgresponsejitter": " 0.000205420",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 18",
    "lockedtime": " 0.000000453"




   Task:  17

    
    "id": " 17",
    "basecpu": " 2",
    "priority": " 5",
    "period": 100000.0,
    "C(LO)": 35.0,
    "C(HI)": 71.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 27",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000024739",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.502862210",
    "avgresponsejitter": " 0.000021105",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 26",
    "lockedtime": " 0.000000000"




   Task:  29

    
    "id": " 29",
    "basecpu": " 2",
    "priority": " 0",
    "period": 756000.0,
    "C(LO)": 204699.0,
    "C(HI)": 204699.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 5",
    "preemptions": " 87",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.149289946",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.276933736",
    "avgresponsejitter": " 0.128641036",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 91",
    "lockedtime": " 0.000004775"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 12",
    "period": 28350.0,
    "C(LO)": 4439.0,
    "C(HI)": 4439.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 93",
    "preemptions": " 19",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002782808",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.579855760",
    "avgresponsejitter": " 0.002273778",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 111",
    "lockedtime": " 0.000003895"




   Task:  20

    
    "id": " 20",
    "basecpu": " 2",
    "priority": " 10",
    "period": 113400.0,
    "C(LO)": 7936.0,
    "C(HI)": 7936.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 24",
    "preemptions": " 12",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004903574",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.498072111",
    "avgresponsejitter": " 0.004237802",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 35",
    "lockedtime": " 0.000000682"




   Task:  28

    
    "id": " 28",
    "basecpu": " 2",
    "priority": " 8",
    "period": 200000.0,
    "C(LO)": 12959.0,
    "C(HI)": 12959.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 14",
    "preemptions": " 5",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007665640",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.400157387",
    "avgresponsejitter": " 0.006552117",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 18",
    "lockedtime": " 0.000001000"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 13",
    "period": 10000.0,
    "C(LO)": 263.0,
    "C(HI)": 263.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 261",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000152174",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.590005760",
    "avgresponsejitter": " 0.000141075",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 260",
    "lockedtime": " 0.000003279"




   Task:  5

    
    "id": " 5",
    "basecpu": " 2",
    "priority": " 11",
    "period": 45000.0,
    "C(LO)": 977.0,
    "C(HI)": 977.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 59",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000583910",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.565006955",
    "avgresponsejitter": " 0.000486865",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 58",
    "lockedtime": " 0.000000372"



   </details>



  21. Taskset **e4_semi2wf_t15522**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t15522",
    "size": "35",
    "utilization": "1.86",
    "realutilization": 1.687409065255732,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  28

    
    "id": " 28",
    "basecpu": " 2",
    "priority": " 4",
    "period": 141750.0,
    "C(LO)": 12.0,
    "C(HI)": 25.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 198",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000028153",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.793675700",
    "avgresponsejitter": " 0.000016153",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 95",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 292",
    "lockedtime": " 0.000009450"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 17",
    "hightolow": " 17",
    "idletime": 17178420,
    "util": 84.85148148148149




   CPU: 2

    
    "id": 2,
    "hyperperiod": 56700000,
    "lowtohigh": " 113",
    "hightolow": " 112",
    "idletime": 18269392,
    "util": 83.88942504409171




   Real Utilization: 1.687409065255732
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  33

    
    "id": " 33",
    "basecpu": " 1",
    "priority": " 1",
    "period": 200000.0,
    "C(LO)": 8730.0,
    "C(HI)": 17460.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 141",
    "preemptions": " 119",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.023459099",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.805751477",
    "avgresponsejitter": " 0.006506661",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 261",
    "timesonc2": " 0",
    "lockedtime": " 0.000005288"




   Task:  35

    
    "id": " 35",
    "basecpu": " 1",
    "priority": " 0",
    "period": 700000.0,
    "C(LO)": 25367.0,
    "C(HI)": 50734.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 41",
    "preemptions": " 87",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.033622399",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.301166000",
    "avgresponsejitter": " 0.018735787",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 127",
    "timesonc2": " 0",
    "lockedtime": " 0.000009252"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 12",
    "period": 28350.0,
    "C(LO)": 903.0,
    "C(HI)": 1807.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 181",
    "preemptions": " 8",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006106928",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.074656492",
    "avgresponsejitter": " 0.000527222",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 190",
    "timesonc2": " 0",
    "lockedtime": " 0.000001384"




   Task:  25

    
    "id": " 25",
    "basecpu": " 1",
    "priority": " 4",
    "period": 120000.0,
    "C(LO)": 3183.0,
    "C(HI)": 6366.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 234",
    "preemptions": " 22",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.010017072",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.840006174",
    "avgresponsejitter": " 0.001788114",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 258",
    "timesonc2": " 0",
    "lockedtime": " 0.000002318"




   Task:  13

    
    "id": " 13",
    "basecpu": " 1",
    "priority": " 7",
    "period": 67500.0,
    "C(LO)": 1370.0,
    "C(HI)": 2741.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 415",
    "preemptions": " 18",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005292348",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.880536673",
    "avgresponsejitter": " 0.000742378",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 434",
    "timesonc2": " 0",
    "lockedtime": " 0.000002315"




   Task:  30

    
    "id": " 30",
    "basecpu": " 1",
    "priority": " 2",
    "period": 162000.0,
    "C(LO)": 2537.0,
    "C(HI)": 5074.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 174",
    "preemptions": " 38",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007296775",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.881111805",
    "avgresponsejitter": " 0.001522207",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 213",
    "timesonc2": " 0",
    "lockedtime": " 0.000004420"




   Task:  22

    
    "id": " 22",
    "basecpu": " 1",
    "priority": " 6",
    "period": 101250.0,
    "C(LO)": 1207.0,
    "C(HI)": 2415.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 277",
    "preemptions": " 12",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007337607",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.843756033",
    "avgresponsejitter": " 0.000770982",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 291",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  24

    
    "id": " 24",
    "basecpu": " 1",
    "priority": " 5",
    "period": 112500.0,
    "C(LO)": 1257.0,
    "C(HI)": 2515.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 250",
    "preemptions": " 8",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007091336",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.900633153",
    "avgresponsejitter": " 0.000732075",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 258",
    "timesonc2": " 0",
    "lockedtime": " 0.000001360"




   Task:  26

    
    "id": " 26",
    "basecpu": " 1",
    "priority": " 3",
    "period": 131250.0,
    "C(LO)": 504.0,
    "C(HI)": 1008.9999999999999,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 214",
    "preemptions": " 3",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006138189",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.825006213",
    "avgresponsejitter": " 0.000288237",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 218",
    "timesonc2": " 0",
    "lockedtime": " 0.000001706"




   Task:  10

    
    "id": " 10",
    "basecpu": " 1",
    "priority": " 16",
    "period": 50400.0,
    "C(LO)": 9778.0,
    "C(HI)": 9778.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 555",
    "preemptions": " 183",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006862631",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.871207321",
    "avgresponsejitter": " 0.004992787",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 737",
    "timesonc2": " 0",
    "lockedtime": " 0.000061429"




   Task:  12

    
    "id": " 12",
    "basecpu": " 1",
    "priority": " 14",
    "period": 64800.0,
    "C(LO)": 11221.0,
    "C(HI)": 11221.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 432",
    "preemptions": " 218",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.013914571",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.865034168",
    "avgresponsejitter": " 0.005969159",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 649",
    "timesonc2": " 0",
    "lockedtime": " 0.000025688"




   Task:  15

    
    "id": " 15",
    "basecpu": " 1",
    "priority": " 11",
    "period": 72000.0,
    "C(LO)": 4014.0,
    "C(HI)": 4014.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 389",
    "preemptions": " 62",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.008108661",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.876588622",
    "avgresponsejitter": " 0.002186523",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 450",
    "timesonc2": " 0",
    "lockedtime": " 0.000003117"




   Task:  11

    
    "id": " 11",
    "basecpu": " 1",
    "priority": " 15",
    "period": 54000.0,
    "C(LO)": 2108.0,
    "C(HI)": 2108.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 519",
    "preemptions": " 9",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001702309",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.918005979",
    "avgresponsejitter": " 0.001066829",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 527",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  17

    
    "id": " 17",
    "basecpu": " 1",
    "priority": " 10",
    "period": 78750.0,
    "C(LO)": 1991.9999999999998,
    "C(HI)": 1991.9999999999998,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 356",
    "preemptions": " 23",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007670183",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.879439384",
    "avgresponsejitter": " 0.001208447",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 378",
    "timesonc2": " 0",
    "lockedtime": " 0.000000820"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 20",
    "period": 39375.0,
    "C(LO)": 847.0,
    "C(HI)": 847.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 711",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000446492",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.916881159",
    "avgresponsejitter": " 0.000428760",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 1",
    "timesonc1": " 710",
    "timesonc2": " 0",
    "lockedtime": " 0.000007574"




   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 19",
    "period": 45000.0,
    "C(LO)": 812.0,
    "C(HI)": 812.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 622",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000422258",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.900008802",
    "avgresponsejitter": " 0.000408940",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 1",
    "timesonc1": " 621",
    "timesonc2": " 0",
    "lockedtime": " 0.000013919"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 18",
    "period": 47250.0,
    "C(LO)": 794.0,
    "C(HI)": 794.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 592",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000414775",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.877945216",
    "avgresponsejitter": " 0.000401601",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 2",
    "timesonc1": " 590",
    "timesonc2": " 2",
    "lockedtime": " 0.000021426"




   Task:  20

    
    "id": " 20",
    "basecpu": " 1",
    "priority": " 8",
    "period": 90720.0,
    "C(LO)": 1332.0,
    "C(HI)": 1332.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 309",
    "preemptions": " 18",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002223447",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.851046003",
    "avgresponsejitter": " 0.000713556",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 326",
    "timesonc2": " 0",
    "lockedtime": " 0.000000631"




   Task:  18

    
    "id": " 18",
    "basecpu": " 1",
    "priority": " 9",
    "period": 84000.0,
    "C(LO)": 1159.0,
    "C(HI)": 1159.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 334",
    "preemptions": " 7",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001116069",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.888006072",
    "avgresponsejitter": " 0.000586694",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 340",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  9

    
    "id": " 9",
    "basecpu": " 1",
    "priority": " 17",
    "period": 50000.0,
    "C(LO)": 354.0,
    "C(HI)": 354.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 560",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000217898",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.900421135",
    "avgresponsejitter": " 0.000182607",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 559",
    "timesonc2": " 0",
    "lockedtime": " 0.000012871"




   Task:  14

    
    "id": " 14",
    "basecpu": " 1",
    "priority": " 13",
    "period": 70000.0,
    "C(LO)": 225.0,
    "C(HI)": 225.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 400",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000331498",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.860006937",
    "avgresponsejitter": " 0.000116589",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 400",
    "timesonc2": " 0",
    "lockedtime": " 0.000005063"




   Task:  29

    
    "id": " 29",
    "basecpu": " 2",
    "priority": " 3",
    "period": 157500.0,
    "C(LO)": 10672.0,
    "C(HI)": 21345.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 179",
    "preemptions": " 231",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.018238919",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.887743736",
    "avgresponsejitter": " 0.005968486",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 411",
    "lockedtime": " 0.000010835"




   Task:  32

    
    "id": " 32",
    "basecpu": " 2",
    "priority": " 1",
    "period": 180000.0,
    "C(LO)": 6409.0,
    "C(HI)": 12819.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 157",
    "preemptions": " 66",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.020234417",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.903363763",
    "avgresponsejitter": " 0.004004520",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 223",
    "lockedtime": " 0.000005033"




   Task:  31

    
    "id": " 31",
    "basecpu": " 2",
    "priority": " 2",
    "period": 175000.0,
    "C(LO)": 4738.0,
    "C(HI)": 9476.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 161",
    "preemptions": " 56",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.018448601",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.826130925",
    "avgresponsejitter": " 0.002812111",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 218",
    "lockedtime": " 0.000001462"




   Task:  27

    
    "id": " 27",
    "basecpu": " 2",
    "priority": " 5",
    "period": 135000.0,
    "C(LO)": 3194.0,
    "C(HI)": 6389.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 208",
    "preemptions": " 63",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004213610",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.813568396",
    "avgresponsejitter": " 0.001654949",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 271",
    "lockedtime": " 0.000003508"




   Task:  23

    
    "id": " 23",
    "basecpu": " 2",
    "priority": " 6",
    "period": 105000.0,
    "C(LO)": 2060.0,
    "C(HI)": 4120.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 267",
    "preemptions": " 7",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003148357",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.825007486",
    "avgresponsejitter": " 0.001060886",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 4",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 277",
    "lockedtime": " 0.000001111"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 8",
    "period": 25200.0,
    "C(LO)": 370.0,
    "C(HI)": 740.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1110",
    "preemptions": " 12",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001615330",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.921605967",
    "avgresponsejitter": " 0.000193135",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 9",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1130",
    "lockedtime": " 0.000024270"




   Task:  34

    
    "id": " 34",
    "basecpu": " 2",
    "priority": " 0",
    "period": 472500.0,
    "C(LO)": 4922.0,
    "C(HI)": 9844.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 61",
    "preemptions": " 56",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.015293444",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.892654697",
    "avgresponsejitter": " 0.004075465",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 116",
    "lockedtime": " 0.000004027"




   Task:  28

    
    "id": " 28",
    "basecpu": " 2",
    "priority": " 4",
    "period": 141750.0,
    "C(LO)": 12.0,
    "C(HI)": 25.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 198",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000028153",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.793675700",
    "avgresponsejitter": " 0.000016153",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 95",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 292",
    "lockedtime": " 0.000009450"




   Task:  21

    
    "id": " 21",
    "basecpu": " 2",
    "priority": " 7",
    "period": 94500.0,
    "C(LO)": 19741.0,
    "C(HI)": 19741.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 297",
    "preemptions": " 507",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.015778961",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.878898222",
    "avgresponsejitter": " 0.010831610",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 803",
    "lockedtime": " 0.000051559"




   Task:  3

    
    "id": " 3",
    "basecpu": " 2",
    "priority": " 11",
    "period": 22500.0,
    "C(LO)": 2809.0,
    "C(HI)": 2809.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1243",
    "preemptions": " 59",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001960694",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.922505778",
    "avgresponsejitter": " 0.001416030",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1301",
    "lockedtime": " 0.000053351"




   Task:  16

    
    "id": " 16",
    "basecpu": " 2",
    "priority": " 10",
    "period": 75600.0,
    "C(LO)": 4936.0,
    "C(HI)": 4936.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 371",
    "preemptions": " 129",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004632303",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.896698408",
    "avgresponsejitter": " 0.002603760",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 499",
    "lockedtime": " 0.000007240"




   Task:  19

    
    "id": " 19",
    "basecpu": " 2",
    "priority": " 9",
    "period": 90000.0,
    "C(LO)": 4048.9999999999995,
    "C(HI)": 4048.9999999999995,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 312",
    "preemptions": " 34",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005429802",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.901638949",
    "avgresponsejitter": " 0.002090700",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 345",
    "lockedtime": " 0.000002982"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 12",
    "period": 18900.0,
    "C(LO)": 496.0,
    "C(HI)": 496.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1479",
    "preemptions": " 28",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000339697",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.915305760",
    "avgresponsejitter": " 0.000250207",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1506",
    "lockedtime": " 0.000019252"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 13",
    "period": 10000.0,
    "C(LO)": 68.0,
    "C(HI)": 68.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2794",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000054453",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 28.920005940",
    "avgresponsejitter": " 0.000042547",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 9",
    "timesrestored": " 8",
    "timesonc1": " 1",
    "timesonc2": " 2792",
    "lockedtime": " 0.000076051"



   </details>



  22. Taskset **e4_semi2wf_t2245**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t2245",
    "size": "10",
    "utilization": "1.848",
    "realutilization": 1.9999990476190477,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 5",
    "period": 113400.0,
    "C(LO)": 19.0,
    "C(HI)": 19.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 11340000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 16,
    "util": 99.99994356261023




   CPU: 2

    
    "id": 2,
    "hyperperiod": 28350000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 11,
    "util": 99.99996119929453




   Real Utilization: 1.9999990476190477
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  9

    
    "id": " 9",
    "basecpu": " 1",
    "priority": " 1",
    "period": 708750.0,
    "C(LO)": 79399.0,
    "C(HI)": 158799.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  10

    
    "id": " 10",
    "basecpu": " 1",
    "priority": " 0",
    "period": 945000.0,
    "C(LO)": 60133.0,
    "C(HI)": 120266.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 2",
    "period": 141750.0,
    "C(LO)": 7144.0,
    "C(HI)": 14289.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 3",
    "period": 54000.0,
    "C(LO)": 1091.0,
    "C(HI)": 2182.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 4",
    "period": 126000.0,
    "C(LO)": 31188.0,
    "C(HI)": 31188.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  4

    
    "id": " 4",
    "basecpu": " 1",
    "priority": " 6",
    "period": 108000.0,
    "C(LO)": 11589.0,
    "C(HI)": 11589.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005394895",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000017712",
    "avgresponsejitter": " 0.005394895",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 5",
    "period": 113400.0,
    "C(LO)": 19.0,
    "C(HI)": 19.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  3

    
    "id": " 3",
    "basecpu": " 2",
    "priority": " 1",
    "period": 90000.0,
    "C(LO)": 20487.0,
    "C(HI)": 40975.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  8

    
    "id": " 8",
    "basecpu": " 2",
    "priority": " 0",
    "period": 175000.0,
    "C(LO)": 60059.0,
    "C(HI)": 60059.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000000000",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 0.000000000",
    "avgresponsejitter": " 0.000000000",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 2",
    "period": 28350.0,
    "C(LO)": 5725.0,
    "C(HI)": 5725.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002901180",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.000011766",
    "avgresponsejitter": " 0.002901180",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1",
    "lockedtime": " 0.000000219"



   </details>



  23. Taskset **e4_semi2wf_t2351**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t2351",
    "size": "10",
    "utilization": "1.86",
    "realutilization": 1.8911653703703704,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  3

    
    "id": " 3",
    "basecpu": " 2",
    "priority": " 4",
    "period": 26250.0,
    "C(LO)": 1791.0,
    "C(HI)": 1791.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 379",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000922865",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.922507946",
    "avgresponsejitter": " 0.000911183",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 2",
    "timesonc1": " 2",
    "timesonc2": " 376",
    "lockedtime": " 0.000014652"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 12600000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 6293963,
    "util": 94.4497680776014




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 2",
    "hightolow": " 2",
    "idletime": 6047884,
    "util": 94.66676895943563




   Real Utilization: 1.8911653703703704
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  1

    
    "id": " 1",
    "basecpu": " 1",
    "priority": " 4",
    "period": 10000.0,
    "C(LO)": 855.0,
    "C(HI)": 1711.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 994",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000522039",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.920005982",
    "avgresponsejitter": " 0.000428541",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 993",
    "timesonc2": " 0",
    "lockedtime": " 0.000006123"




   Task:  10

    
    "id": " 10",
    "basecpu": " 1",
    "priority": " 0",
    "period": 840000.0,
    "C(LO)": 50005.0,
    "C(HI)": 100011.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 13",
    "preemptions": " 53",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.063656682",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.240457264",
    "avgresponsejitter": " 0.034861342",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 65",
    "timesonc2": " 0",
    "lockedtime": " 0.000001679"




   Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 3",
    "period": 15750.0,
    "C(LO)": 811.0,
    "C(HI)": 1622.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 632",
    "preemptions": " 15",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000911913",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.922506018",
    "avgresponsejitter": " 0.000415763",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 646",
    "timesonc2": " 0",
    "lockedtime": " 0.000010970"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 2",
    "period": 75000.0,
    "C(LO)": 20139.0,
    "C(HI)": 20139.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 134",
    "preemptions": " 187",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.012951973",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.900488670",
    "avgresponsejitter": " 0.010710742",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 320",
    "timesonc2": " 0",
    "lockedtime": " 0.000004099"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 1",
    "period": 196875.0,
    "C(LO)": 49285.0,
    "C(HI)": 49285.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 52",
    "preemptions": " 236",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.043565222",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.844178174",
    "avgresponsejitter": " 0.030322721",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 287",
    "timesonc2": " 0",
    "lockedtime": " 0.000007595"




   Task:  9

    
    "id": " 9",
    "basecpu": " 2",
    "priority": " 0",
    "period": 200000.0,
    "C(LO)": 29155.0,
    "C(HI)": 58310.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 51",
    "preemptions": " 57",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.076327886",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.800006610",
    "avgresponsejitter": " 0.020188943",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 109",
    "lockedtime": " 0.000008204"




   Task:  7

    
    "id": " 7",
    "basecpu": " 2",
    "priority": " 1",
    "period": 120000.0,
    "C(LO)": 3979.0,
    "C(HI)": 7958.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 84",
    "preemptions": " 6",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.016365483",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.840007081",
    "avgresponsejitter": " 0.002531619",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 89",
    "lockedtime": " 0.000004877"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 3",
    "period": 39375.0,
    "C(LO)": 12340.0,
    "C(HI)": 12340.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 253",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007425318",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.883131147",
    "avgresponsejitter": " 0.006201925",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 252",
    "lockedtime": " 0.000004351"




   Task:  5

    
    "id": " 5",
    "basecpu": " 2",
    "priority": " 2",
    "period": 56700.0,
    "C(LO)": 11815.0,
    "C(HI)": 11815.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 176",
    "preemptions": " 56",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.014999862",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.865806682",
    "avgresponsejitter": " 0.007018393",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 231",
    "lockedtime": " 0.000010177"




   Task:  3

    
    "id": " 3",
    "basecpu": " 2",
    "priority": " 4",
    "period": 26250.0,
    "C(LO)": 1791.0,
    "C(HI)": 1791.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 379",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000922865",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.922507946",
    "avgresponsejitter": " 0.000911183",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 2",
    "timesonc1": " 2",
    "timesonc2": " 376",
    "lockedtime": " 0.000014652"



   </details>



  24. Taskset **e4_semi2wf_t2381**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t2381",
    "size": "10",
    "utilization": "1.86",
    "realutilization": 1.364373262786596,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 5",
    "period": 15750.0,
    "C(LO)": 2201.0,
    "C(HI)": 2201.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1968",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001130132",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.980006309",
    "avgresponsejitter": " 0.001116126",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 1",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 1",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 5",
    "timesrestored": " 5",
    "timesonc1": " 8",
    "timesonc2": " 1959",
    "lockedtime": " 0.000012492"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 22680000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 19110691,
    "util": 66.29507760141094




   CPU: 2

    
    "id": 2,
    "hyperperiod": 56700000,
    "lowtohigh": " 21",
    "hightolow": " 21",
    "idletime": 16929345,
    "util": 70.14224867724867




   Real Utilization: 1.364373262786596
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 3",
    "period": 20000.0,
    "C(LO)": 1606.0,
    "C(HI)": 3213.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1550",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000967081",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.960006078",
    "avgresponsejitter": " 0.000808538",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1549",
    "timesonc2": " 0",
    "lockedtime": " 0.000018835"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 1",
    "period": 56700.0,
    "C(LO)": 1858.0,
    "C(HI)": 3717.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 548",
    "preemptions": " 25",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002032997",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.958206874",
    "avgresponsejitter": " 0.000978571",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 572",
    "timesonc2": " 0",
    "lockedtime": " 0.000010865"




   Task:  10

    
    "id": " 10",
    "basecpu": " 1",
    "priority": " 0",
    "period": 648000.0,
    "C(LO)": 295113.0,
    "C(HI)": 295113.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 49",
    "preemptions": " 541",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.206426477",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.456006207",
    "avgresponsejitter": " 0.175329144",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 589",
    "timesonc2": " 0",
    "lockedtime": " 0.000050249"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 2",
    "period": 189000.0,
    "C(LO)": 33743.0,
    "C(HI)": 33743.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 165",
    "preemptions": " 140",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.021197456",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.807006204",
    "avgresponsejitter": " 0.017493748",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 304",
    "timesonc2": " 0",
    "lockedtime": " 0.000010922"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 3",
    "period": 37800.0,
    "C(LO)": 3339.0,
    "C(HI)": 6679.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 821",
    "preemptions": " 34",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006693727",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.958206529",
    "avgresponsejitter": " 0.001694667",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 857",
    "lockedtime": " 0.000020000"




   Task:  3

    
    "id": " 3",
    "basecpu": " 2",
    "priority": " 4",
    "period": 26250.0,
    "C(LO)": 437.0,
    "C(HI)": 875.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1182",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000698444",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.975006234",
    "avgresponsejitter": " 0.000224213",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 14",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1195",
    "lockedtime": " 0.000002147"




   Task:  7

    
    "id": " 7",
    "basecpu": " 2",
    "priority": " 1",
    "period": 168750.0,
    "C(LO)": 1038.0,
    "C(HI)": 2077.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 185",
    "preemptions": " 6",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002539129",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.881256823",
    "avgresponsejitter": " 0.000585856",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 4",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 194",
    "lockedtime": " 0.000000465"




   Task:  6

    
    "id": " 6",
    "basecpu": " 2",
    "priority": " 2",
    "period": 140000.0,
    "C(LO)": 79054.0,
    "C(HI)": 79054.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 223",
    "preemptions": " 1047",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.055755099",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.940005910",
    "avgresponsejitter": " 0.045658676",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1269",
    "lockedtime": " 0.000038357"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 5",
    "period": 15750.0,
    "C(LO)": 2201.0,
    "C(HI)": 2201.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1968",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001130132",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.980006309",
    "avgresponsejitter": " 0.001116126",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 1",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 1",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 5",
    "timesrestored": " 5",
    "timesonc1": " 8",
    "timesonc2": " 1959",
    "lockedtime": " 0.000012492"




   Task:  9

    
    "id": " 9",
    "basecpu": " 2",
    "priority": " 0",
    "period": 506250.0,
    "C(LO)": 36948.0,
    "C(HI)": 36948.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 63",
    "preemptions": " 153",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.072641799",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.881865694",
    "avgresponsejitter": " 0.027244514",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 215",
    "lockedtime": " 0.000002787"



   </details>



  25. Taskset **e4_semi2wf_t2578**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t2578",
    "size": "10",
    "utilization": "1.8840000000000001",
    "realutilization": 1.1632031305114638,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 5",
    "period": 52500.0,
    "C(LO)": 10160.0,
    "C(HI)": 10160.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1418",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005210171",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 75.390407042",
    "avgresponsejitter": " 0.005150249",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 2",
    "timesonc1": " 1416",
    "timesonc2": " 1",
    "lockedtime": " 0.000009559"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 12",
    "hightolow": " 12",
    "idletime": 45337930,
    "util": 60.01946208112875




   CPU: 2

    
    "id": 2,
    "hyperperiod": 11340000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 49554835,
    "util": 56.300850970017635




   Real Utilization: 1.1632031305114638
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 1",
    "period": 168000.0,
    "C(LO)": 22578.0,
    "C(HI)": 45156.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 444",
    "preemptions": " 219",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.055594901",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 75.256006757",
    "avgresponsejitter": " 0.014652565",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 5",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 667",
    "timesonc2": " 0",
    "lockedtime": " 0.000013904"




   Task:  10

    
    "id": " 10",
    "basecpu": " 1",
    "priority": " 0",
    "period": 900000.0,
    "C(LO)": 56811.0,
    "C(HI)": 113623.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 84",
    "preemptions": " 129",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.089546414",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 74.800006865",
    "avgresponsejitter": " 0.039834360",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 213",
    "timesonc2": " 0",
    "lockedtime": " 0.000005384"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 2",
    "period": 108000.0,
    "C(LO)": 3966.0,
    "C(HI)": 7932.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 690",
    "preemptions": " 29",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.026750544",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 75.304006877",
    "avgresponsejitter": " 0.002439132",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 6",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 724",
    "timesonc2": " 0",
    "lockedtime": " 0.000008222"




   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 3",
    "period": 131250.0,
    "C(LO)": 29452.0,
    "C(HI)": 29452.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 568",
    "preemptions": " 152",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.021676492",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 75.287507574",
    "avgresponsejitter": " 0.015696339",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 719",
    "timesonc2": " 0",
    "lockedtime": " 0.000015940"




   Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 5",
    "period": 52500.0,
    "C(LO)": 10160.0,
    "C(HI)": 10160.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1418",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005210171",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 75.390407042",
    "avgresponsejitter": " 0.005150249",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 2",
    "timesonc1": " 1416",
    "timesonc2": " 1",
    "lockedtime": " 0.000009559"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 4",
    "period": 56700.0,
    "C(LO)": 6720.0,
    "C(HI)": 6720.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1313",
    "preemptions": " 52",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.009176474",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 75.333706342",
    "avgresponsejitter": " 0.003568676",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1364",
    "timesonc2": " 0",
    "lockedtime": " 0.000007607"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 2",
    "period": 67500.0,
    "C(LO)": 10661.0,
    "C(HI)": 21323.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1104",
    "preemptions": " 125",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.011852093",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 75.385005787",
    "avgresponsejitter": " 0.005860973",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1228",
    "lockedtime": " 0.000010868"




   Task:  5

    
    "id": " 5",
    "basecpu": " 2",
    "priority": " 1",
    "period": 84000.0,
    "C(LO)": 4985.0,
    "C(HI)": 9971.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 887",
    "preemptions": " 56",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.013434048",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 75.340007601",
    "avgresponsejitter": " 0.002856652",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 942",
    "lockedtime": " 0.000022138"




   Task:  9

    
    "id": " 9",
    "basecpu": " 2",
    "priority": " 0",
    "period": 180000.0,
    "C(LO)": 42334.0,
    "C(HI)": 42334.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 415",
    "preemptions": " 366",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.039004799",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 75.342876988",
    "avgresponsejitter": " 0.025917402",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 780",
    "lockedtime": " 0.000016529"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 3",
    "period": 45360.0,
    "C(LO)": 9491.0,
    "C(HI)": 9491.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1642",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005693165",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 75.390406495",
    "avgresponsejitter": " 0.004754018",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1641",
    "lockedtime": " 0.000027757"



   </details>



  26. Taskset **e4_semi2wf_t2592**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t2592",
    "size": "10",
    "utilization": "1.8840000000000001",
    "realutilization": 1.8032315343915344,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 3",
    "period": 26250.0,
    "C(LO)": 2881.0,
    "C(HI)": 2881.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 305",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001474285",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 9.050007231",
    "avgresponsejitter": " 0.001460706",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 1",
    "timesonc1": " 3",
    "timesonc2": " 301",
    "lockedtime": " 0.000009736"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 56700000,
    "lowtohigh": " 2",
    "hightolow": " 2",
    "idletime": 5756397,
    "util": 89.84762433862434




   CPU: 2

    
    "id": 2,
    "hyperperiod": 56700000,
    "lowtohigh": " 1",
    "hightolow": " 1",
    "idletime": 5400375,
    "util": 90.4755291005291




   Real Utilization: 1.8032315343915344
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 1",
    "period": 162000.0,
    "C(LO)": 37120.0,
    "C(HI)": 74241.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 51",
    "preemptions": " 72",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.026279628",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.938007306",
    "avgresponsejitter": " 0.019854468",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 122",
    "timesonc2": " 0",
    "lockedtime": " 0.000000309"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 0",
    "period": 189000.0,
    "C(LO)": 19680.0,
    "C(HI)": 39361.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 44",
    "preemptions": " 25",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.014907174",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.954664568",
    "avgresponsejitter": " 0.010633294",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 68",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  4

    
    "id": " 4",
    "basecpu": " 1",
    "priority": " 2",
    "period": 87500.0,
    "C(LO)": 3029.0,
    "C(HI)": 6058.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 94",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005516027",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 9.050006123",
    "avgresponsejitter": " 0.001617279",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 96",
    "timesonc2": " 0",
    "lockedtime": " 0.000000438"




   Task:  1

    
    "id": " 1",
    "basecpu": " 1",
    "priority": " 5",
    "period": 22500.0,
    "C(LO)": 2635.0,
    "C(HI)": 2635.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 359",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001354796",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 9.032505979",
    "avgresponsejitter": " 0.001334309",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 358",
    "timesonc2": " 0",
    "lockedtime": " 0.000001150"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 3",
    "period": 108000.0,
    "C(LO)": 7443.0,
    "C(HI)": 7443.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 76",
    "preemptions": " 4",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004787802",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.992005979",
    "avgresponsejitter": " 0.003760826",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 79",
    "timesonc2": " 0",
    "lockedtime": " 0.000000240"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 4",
    "period": 65625.0,
    "C(LO)": 819.0,
    "C(HI)": 819.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 124",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000489970",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 9.006255979",
    "avgresponsejitter": " 0.000412826",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 123",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  9

    
    "id": " 9",
    "basecpu": " 2",
    "priority": " 1",
    "period": 453600.0,
    "C(LO)": 127937.0,
    "C(HI)": 255875.00000000003,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 19",
    "preemptions": " 57",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.195275372",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.716522255",
    "avgresponsejitter": " 0.080337625",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 76",
    "lockedtime": " 0.000005625"




   Task:  10

    
    "id": " 10",
    "basecpu": " 2",
    "priority": " 0",
    "period": 787500.0,
    "C(LO)": 44721.0,
    "C(HI)": 89442.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 12",
    "preemptions": " 9",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.103429282",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.911804072",
    "avgresponsejitter": " 0.030159063",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 20",
    "lockedtime": " 0.000000000"




   Task:  7

    
    "id": " 7",
    "basecpu": " 2",
    "priority": " 2",
    "period": 175000.0,
    "C(LO)": 28393.0,
    "C(HI)": 28393.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 47",
    "preemptions": " 15",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.017782417",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.875009787",
    "avgresponsejitter": " 0.015363414",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 61",
    "lockedtime": " 0.000003706"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 3",
    "period": 26250.0,
    "C(LO)": 2881.0,
    "C(HI)": 2881.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 305",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001474285",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 9.050007231",
    "avgresponsejitter": " 0.001460706",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 1",
    "timesonc1": " 3",
    "timesonc2": " 301",
    "lockedtime": " 0.000009736"



   </details>



  27. Taskset **e4_semi2wf_t261**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t261",
    "size": "8",
    "utilization": "1.872",
    "realutilization": 0.9048070546737214,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 4",
    "period": 39375.0,
    "C(LO)": 4544.0,
    "C(HI)": 4544.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 493",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002323589",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.372507012",
    "avgresponsejitter": " 0.002297559",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 2",
    "timesonc1": " 489",
    "timesonc2": " 3",
    "lockedtime": " 0.000000823"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 22680000,
    "lowtohigh": " 9",
    "hightolow": " 9",
    "idletime": 12104863,
    "util": 46.62758818342152




   CPU: 2

    
    "id": 2,
    "hyperperiod": 9450000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 12734113,
    "util": 43.85311728395062




   Real Utilization: 0.9048070546737214
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 0",
    "period": 567000.0,
    "C(LO)": 53705.0,
    "C(HI)": 107410.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 36",
    "preemptions": " 36",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.036998165",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.280226520",
    "avgresponsejitter": " 0.029507826",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 71",
    "timesonc2": " 0",
    "lockedtime": " 0.000002886"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 2",
    "period": 135000.0,
    "C(LO)": 5022.0,
    "C(HI)": 10045.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 145",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006885781",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.305007309",
    "avgresponsejitter": " 0.002626390",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 147",
    "timesonc2": " 0",
    "lockedtime": " 0.000001739"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 3",
    "period": 47250.0,
    "C(LO)": 1436.0,
    "C(HI)": 2873.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 411",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002214156",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.325256210",
    "avgresponsejitter": " 0.000735949",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 6",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 416",
    "timesonc2": " 0",
    "lockedtime": " 0.000000916"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 1",
    "period": 648000.0,
    "C(LO)": 311868.0,
    "C(HI)": 311868.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 31",
    "preemptions": " 234",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.204224700",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 19.792005979",
    "avgresponsejitter": " 0.164573195",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 264",
    "timesonc2": " 0",
    "lockedtime": " 0.000014796"




   Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 4",
    "period": 39375.0,
    "C(LO)": 4544.0,
    "C(HI)": 4544.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 493",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002323589",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.372507012",
    "avgresponsejitter": " 0.002297559",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 2",
    "timesonc1": " 489",
    "timesonc2": " 3",
    "lockedtime": " 0.000000823"




   Task:  6

    
    "id": " 6",
    "basecpu": " 2",
    "priority": " 0",
    "period": 175000.0,
    "C(LO)": 47400.0,
    "C(HI)": 94800.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 112",
    "preemptions": " 148",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.041908901",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.250005760",
    "avgresponsejitter": " 0.029281859",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 259",
    "lockedtime": " 0.000004447"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 2",
    "period": 25200.0,
    "C(LO)": 6314.0,
    "C(HI)": 6314.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 770",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003795471",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.353605760",
    "avgresponsejitter": " 0.003156243",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 769",
    "lockedtime": " 0.000005480"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 1",
    "period": 67500.0,
    "C(LO)": 10687.0,
    "C(HI)": 10687.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 288",
    "preemptions": " 56",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.010032769",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 20.308575802",
    "avgresponsejitter": " 0.005993865",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 343",
    "lockedtime": " 0.000011156"



   </details>



  28. Taskset **e4_semi2wf_t2850**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t2850",
    "size": "10",
    "utilization": "1.9200000000000002",
    "realutilization": 1.5484786243386246,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  1

    
    "id": " 1",
    "basecpu": " 1",
    "priority": " 5",
    "period": 20000.0,
    "C(LO)": 4087.9999999999995,
    "C(HI)": 4087.9999999999995,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 679",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002097102",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 14.575006973",
    "avgresponsejitter": " 0.002068649",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 1",
    "timesonc1": " 676",
    "timesonc2": " 2",
    "lockedtime": " 0.000002036"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 37800000,
    "lowtohigh": " 1",
    "hightolow": " 1",
    "idletime": 7727657,
    "util": 79.55646296296297




   CPU: 2

    
    "id": 2,
    "hyperperiod": 7560000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 9339851,
    "util": 75.29139947089948




   Real Utilization: 1.5484786243386246
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 2",
    "period": 135000.0,
    "C(LO)": 17998.0,
    "C(HI)": 35996.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 102",
    "preemptions": " 38",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.023135952",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 14.514381303",
    "avgresponsejitter": " 0.010425928",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 139",
    "timesonc2": " 0",
    "lockedtime": " 0.000000736"




   Task:  10

    
    "id": " 10",
    "basecpu": " 1",
    "priority": " 0",
    "period": 787500.0,
    "C(LO)": 73222.0,
    "C(HI)": 146444.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 19",
    "preemptions": " 58",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.144861946",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 14.387505979",
    "avgresponsejitter": " 0.058215393",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 77",
    "timesonc2": " 0",
    "lockedtime": " 0.000002246"




   Task:  9

    
    "id": " 9",
    "basecpu": " 1",
    "priority": " 1",
    "period": 504000.0,
    "C(LO)": 6790.0,
    "C(HI)": 13580.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 28",
    "preemptions": " 3",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.012744120",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 14.116236048",
    "avgresponsejitter": " 0.003877468",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 30",
    "timesonc2": " 0",
    "lockedtime": " 0.000001928"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 3",
    "period": 100000.0,
    "C(LO)": 22249.0,
    "C(HI)": 22249.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 137",
    "preemptions": " 19",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.015248811",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 14.505106541",
    "avgresponsejitter": " 0.011519033",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 155",
    "timesonc2": " 0",
    "lockedtime": " 0.000000426"




   Task:  1

    
    "id": " 1",
    "basecpu": " 1",
    "priority": " 5",
    "period": 20000.0,
    "C(LO)": 4087.9999999999995,
    "C(HI)": 4087.9999999999995,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 679",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002097102",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 14.575006973",
    "avgresponsejitter": " 0.002068649",
    "deadlinesmissed": " 1",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 1",
    "timesonc1": " 676",
    "timesonc2": " 2",
    "lockedtime": " 0.000002036"




   Task:  4

    
    "id": " 4",
    "basecpu": " 1",
    "priority": " 4",
    "period": 75000.0,
    "C(LO)": 12611.0,
    "C(HI)": 12611.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 182",
    "preemptions": " 45",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.009608778",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 14.500010063",
    "avgresponsejitter": " 0.006943108",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 226",
    "timesonc2": " 0",
    "lockedtime": " 0.000000498"




   Task:  6

    
    "id": " 6",
    "basecpu": " 2",
    "priority": " 1",
    "period": 118125.0,
    "C(LO)": 21946.0,
    "C(HI)": 43892.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 116",
    "preemptions": " 48",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.023484685",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 14.466255781",
    "avgresponsejitter": " 0.013399982",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 163",
    "lockedtime": " 0.000003432"




   Task:  7

    
    "id": " 7",
    "basecpu": " 2",
    "priority": " 0",
    "period": 120000.0,
    "C(LO)": 5572.0,
    "C(HI)": 11145.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 115",
    "preemptions": " 9",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.010862874",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 14.565203237",
    "avgresponsejitter": " 0.003200438",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 123",
    "lockedtime": " 0.000004526"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 3",
    "period": 50400.0,
    "C(LO)": 13743.0,
    "C(HI)": 13743.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 271",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.008267655",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 14.557605760",
    "avgresponsejitter": " 0.006906772",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 270",
    "lockedtime": " 0.000001604"




   Task:  3

    
    "id": " 3",
    "basecpu": " 2",
    "priority": " 2",
    "period": 60480.0,
    "C(LO)": 6545.0,
    "C(HI)": 6545.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 226",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003920586",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 14.547525760",
    "avgresponsejitter": " 0.003294051",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 225",
    "lockedtime": " 0.000000000"



   </details>



  29. Taskset **e4_semi2wf_t2872**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t2872",
    "size": "10",
    "utilization": "1.9200000000000002",
    "realutilization": 1.96684557319224,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the guilty task.</summary>

   Time values are expressed as **micro-seconds**.

Task:  8

    
    "id": " 8",
    "basecpu": " 2",
    "priority": " 2",
    "period": 189000.0,
    "C(LO)": 21803.0,
    "C(HI)": 21803.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 16",
    "preemptions": " 7",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.017231589",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.646006589",
    "avgresponsejitter": " 0.012083988",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 1",
    "budgetexceededaftermigration": " 1",
    "timesmigrated": " 1",
    "timesrestored": " 0",
    "timesonc1": " 3",
    "timesonc2": " 19",
    "lockedtime": " 0.000000928"



   </details>



   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 0",
    "hightolow": " 0",
    "idletime": 1930514,
    "util": 98.29760670194004




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 3",
    "hightolow": " 2",
    "idletime": 1829198,
    "util": 98.38695061728396




   Real Utilization: 1.96684557319224
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 1",
    "period": 81000.0,
    "C(LO)": 10689.0,
    "C(HI)": 21379.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 37",
    "preemptions": " 15",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.013190474",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.836101243",
    "avgresponsejitter": " 0.005981856",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 51",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 3",
    "period": 56250.0,
    "C(LO)": 4764.0,
    "C(HI)": 9528.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 53",
    "preemptions": " 5",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002834934",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.868756718",
    "avgresponsejitter": " 0.002398949",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 57",
    "timesonc2": " 0",
    "lockedtime": " 0.000000664"




   Task:  4

    
    "id": " 4",
    "basecpu": " 1",
    "priority": " 2",
    "period": 67500.0,
    "C(LO)": 1759.0,
    "C(HI)": 3518.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 44",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001049949",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.835094949",
    "avgresponsejitter": " 0.000866288",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 43",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  1

    
    "id": " 1",
    "basecpu": " 1",
    "priority": " 4",
    "period": 15750.0,
    "C(LO)": 183.0,
    "C(HI)": 367.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 185",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000112486",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.882256622",
    "avgresponsejitter": " 0.000096390",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 184",
    "timesonc2": " 0",
    "lockedtime": " 0.000001009"




   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 0",
    "period": 181440.0,
    "C(LO)": 48240.0,
    "C(HI)": 48240.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 17",
    "preemptions": " 37",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.042650477",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.721606048",
    "avgresponsejitter": " 0.029159258",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 53",
    "timesonc2": " 0",
    "lockedtime": " 0.000001099"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 5",
    "period": 87500.0,
    "C(LO)": 10782.0,
    "C(HI)": 10782.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 34",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006412778",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.800006048",
    "avgresponsejitter": " 0.005557940",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 33",
    "timesonc2": " 0",
    "lockedtime": " 0.000000408"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 3",
    "period": 30240.0,
    "C(LO)": 10323.0,
    "C(HI)": 20646.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 96",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.014859003",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.842566414",
    "avgresponsejitter": " 0.005482763",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 98",
    "lockedtime": " 0.000002381"




   Task:  9

    
    "id": " 9",
    "basecpu": " 2",
    "priority": " 1",
    "period": 200000.0,
    "C(LO)": 33862.0,
    "C(HI)": 33862.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 16",
    "preemptions": " 10",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.025913015",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.800006550",
    "avgresponsejitter": " 0.020148805",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 25",
    "lockedtime": " 0.000001339"




   Task:  8

    
    "id": " 8",
    "basecpu": " 2",
    "priority": " 2",
    "period": 189000.0,
    "C(LO)": 21803.0,
    "C(HI)": 21803.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 16",
    "preemptions": " 7",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.017231589",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.646006589",
    "avgresponsejitter": " 0.012083988",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 1",
    "budgetexceededaftermigration": " 1",
    "timesmigrated": " 1",
    "timesrestored": " 0",
    "timesonc1": " 3",
    "timesonc2": " 19",
    "lockedtime": " 0.000000928"




   Task:  10

    
    "id": " 10",
    "basecpu": " 2",
    "priority": " 0",
    "period": 405000.0,
    "C(LO)": 22138.0,
    "C(HI)": 22138.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 9",
    "preemptions": " 3",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.018044186",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 3.857001820",
    "avgresponsejitter": " 0.013208700",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 11",
    "lockedtime": " 0.000000000"



   </details>

</details>



### **Safe Boundary Exceeded**

<details><summary markdown="span">Click here to expand this section.</summary>

Ovvero quando un taskset ha troppi core (2 nel contesto dual-core) eseguenti in HI-crit mode.



  1. Taskset **e4_semi2wf_t11051**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t11051",
    "size": "25",
    "utilization": "1.848",
    "realutilization": 1.7456836155202824,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 34",
    "hightolow": " 33",
    "idletime": 14699425,
    "util": 87.03754409171076




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 8",
    "hightolow": " 7",
    "idletime": 14140053,
    "util": 87.53081746031746




   Real Utilization: 1.7456836155202824
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  24

    
    "id": " 24",
    "basecpu": " 1",
    "priority": " 0",
    "period": 200000.0,
    "C(LO)": 15165.0,
    "C(HI)": 30331.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 109",
    "preemptions": " 96",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.020580730",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.400214982",
    "avgresponsejitter": " 0.009343378",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 204",
    "timesonc2": " 0",
    "lockedtime": " 0.000004562"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 4",
    "period": 42000.0,
    "C(LO)": 2591.0,
    "C(HI)": 5183.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 514",
    "preemptions": " 34",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006248979",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.507232189",
    "avgresponsejitter": " 0.001382505",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 7",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 554",
    "timesonc2": " 0",
    "lockedtime": " 0.000001577"




   Task:  14

    
    "id": " 14",
    "basecpu": " 1",
    "priority": " 3",
    "period": 108000.0,
    "C(LO)": 5801.0,
    "C(HI)": 11603.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 201",
    "preemptions": " 29",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.012771946",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.492005979",
    "avgresponsejitter": " 0.003172754",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 231",
    "timesonc2": " 0",
    "lockedtime": " 0.000000333"




   Task:  22

    
    "id": " 22",
    "basecpu": " 1",
    "priority": " 1",
    "period": 180000.0,
    "C(LO)": 9124.0,
    "C(HI)": 18249.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 121",
    "preemptions": " 49",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.017423757",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.421707162",
    "avgresponsejitter": " 0.005534913",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 172",
    "timesonc2": " 0",
    "lockedtime": " 0.000003213"




   Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 7",
    "period": 20000.0,
    "C(LO)": 341.0,
    "C(HI)": 682.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1077",
    "preemptions": " 10",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003890297",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.500006532",
    "avgresponsejitter": " 0.000194273",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 10",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1096",
    "timesonc2": " 0",
    "lockedtime": " 0.000016006"




   Task:  21

    
    "id": " 21",
    "basecpu": " 1",
    "priority": " 2",
    "period": 162000.0,
    "C(LO)": 1892.0,
    "C(HI)": 3784.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 134",
    "preemptions": " 12",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.010603982",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.390380817",
    "avgresponsejitter": " 0.001106889",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 146",
    "timesonc2": " 0",
    "lockedtime": " 0.000000165"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 5",
    "period": 28350.0,
    "C(LO)": 51.0,
    "C(HI)": 103.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 761",
    "preemptions": " 3",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002273276",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.517656051",
    "avgresponsejitter": " 0.000038252",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 11",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 774",
    "timesonc2": " 0",
    "lockedtime": " 0.000005943"




   Task:  4

    
    "id": " 4",
    "basecpu": " 1",
    "priority": " 11",
    "period": 30240.0,
    "C(LO)": 4117.0,
    "C(HI)": 4117.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 713",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002118964",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.500647459",
    "avgresponsejitter": " 0.002084904",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 712",
    "timesonc2": " 0",
    "lockedtime": " 0.000010360"




   Task:  16

    
    "id": " 16",
    "basecpu": " 1",
    "priority": " 6",
    "period": 118125.0,
    "C(LO)": 10614.0,
    "C(HI)": 10614.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 184",
    "preemptions": " 105",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.012056399",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.498756030",
    "avgresponsejitter": " 0.006054550",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 288",
    "timesonc2": " 0",
    "lockedtime": " 0.000014598"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 10",
    "period": 56250.0,
    "C(LO)": 3869.0,
    "C(HI)": 3869.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 384",
    "preemptions": " 24",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004372727",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.487506069",
    "avgresponsejitter": " 0.002091565",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 407",
    "timesonc2": " 0",
    "lockedtime": " 0.000017057"




   Task:  13

    
    "id": " 13",
    "basecpu": " 1",
    "priority": " 8",
    "period": 90720.0,
    "C(LO)": 3051.0,
    "C(HI)": 3051.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 239",
    "preemptions": " 5",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003764324",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.502746336",
    "avgresponsejitter": " 0.001549282",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 243",
    "timesonc2": " 0",
    "lockedtime": " 0.000000886"




   Task:  9

    
    "id": " 9",
    "basecpu": " 1",
    "priority": " 9",
    "period": 56700.0,
    "C(LO)": 997.0,
    "C(HI)": 997.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 381",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002731601",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.489772763",
    "avgresponsejitter": " 0.000502186",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 382",
    "timesonc2": " 0",
    "lockedtime": " 0.000004399"




   Task:  25

    
    "id": " 25",
    "basecpu": " 2",
    "priority": " 0",
    "period": 648000.0,
    "C(LO)": 86464.0,
    "C(HI)": 172928.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 34",
    "preemptions": " 217",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.084002820",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 21.736006574",
    "avgresponsejitter": " 0.056454724",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 251",
    "lockedtime": " 0.000026321"




   Task:  23

    
    "id": " 23",
    "basecpu": " 2",
    "priority": " 1",
    "period": 181440.0,
    "C(LO)": 11039.0,
    "C(HI)": 22079.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 120",
    "preemptions": " 92",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.019751904",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.409927171",
    "avgresponsejitter": " 0.006863129",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 211",
    "lockedtime": " 0.000011745"




   Task:  18

    
    "id": " 18",
    "basecpu": " 2",
    "priority": " 3",
    "period": 131250.0,
    "C(LO)": 5890.0,
    "C(HI)": 11781.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 165",
    "preemptions": " 59",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.009633219",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.398097517",
    "avgresponsejitter": " 0.003241381",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 224",
    "lockedtime": " 0.000003048"




   Task:  20

    
    "id": " 20",
    "basecpu": " 2",
    "priority": " 2",
    "period": 157500.0,
    "C(LO)": 4360.0,
    "C(HI)": 8721.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 138",
    "preemptions": " 12",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006437964",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.422887721",
    "avgresponsejitter": " 0.002286075",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 150",
    "lockedtime": " 0.000000414"




   Task:  10

    
    "id": " 10",
    "basecpu": " 2",
    "priority": " 4",
    "period": 60000.0,
    "C(LO)": 537.0,
    "C(HI)": 1075.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 360",
    "preemptions": " 5",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005018985",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.481411601",
    "avgresponsejitter": " 0.000299817",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 5",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 369",
    "lockedtime": " 0.000010171"




   Task:  11

    
    "id": " 11",
    "basecpu": " 2",
    "priority": " 9",
    "period": 65625.0,
    "C(LO)": 7848.000000000001,
    "C(HI)": 7848.000000000001,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 329",
    "preemptions": " 94",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005279474",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.459381387",
    "avgresponsejitter": " 0.004053477",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 422",
    "lockedtime": " 0.000008727"




   Task:  7

    
    "id": " 7",
    "basecpu": " 2",
    "priority": " 10",
    "period": 52500.0,
    "C(LO)": 5277.0,
    "C(HI)": 5277.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 411",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003167535",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.472506432",
    "avgresponsejitter": " 0.002604219",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 410",
    "lockedtime": " 0.000007195"




   Task:  15

    
    "id": " 15",
    "basecpu": " 2",
    "priority": " 7",
    "period": 113400.0,
    "C(LO)": 6834.0,
    "C(HI)": 6834.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 191",
    "preemptions": " 55",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.009684631",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.432606435",
    "avgresponsejitter": " 0.003802532",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 245",
    "lockedtime": " 0.000012706"




   Task:  5

    
    "id": " 5",
    "basecpu": " 2",
    "priority": " 11",
    "period": 33750.0,
    "C(LO)": 1360.0,
    "C(HI)": 1360.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 639",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000822631",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.498756997",
    "avgresponsejitter": " 0.000683201",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 638",
    "lockedtime": " 0.000012036"




   Task:  19

    
    "id": " 19",
    "basecpu": " 2",
    "priority": " 5",
    "period": 141750.0,
    "C(LO)": 3944.9999999999995,
    "C(HI)": 3944.9999999999995,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 153",
    "preemptions": " 8",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006827916",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.404256444",
    "avgresponsejitter": " 0.002086015",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 160",
    "lockedtime": " 0.000003315"




   Task:  17

    
    "id": " 17",
    "basecpu": " 2",
    "priority": " 6",
    "period": 120000.0,
    "C(LO)": 3144.0,
    "C(HI)": 3144.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 181",
    "preemptions": " 19",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004776468",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.480007865",
    "avgresponsejitter": " 0.001639075",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 199",
    "lockedtime": " 0.000010664"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 12",
    "period": 15750.0,
    "C(LO)": 312.0,
    "C(HI)": 312.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 992",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000175435",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 16.592511096",
    "avgresponsejitter": " 0.000163850",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 1",
    "timesonc1": " 0",
    "timesonc2": " 991",
    "lockedtime": " 0.000012769"




   Task:  12

    
    "id": " 12",
    "basecpu": " 2",
    "priority": " 8",
    "period": 84375.0,
    "C(LO)": 901.0,
    "C(HI)": 901.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 257",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000538871",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.515631378",
    "avgresponsejitter": " 0.000449886",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 256",
    "lockedtime": " 0.000000000"



   </details>



  2. Taskset **e4_semi2wf_t11249**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t11249",
    "size": "25",
    "utilization": "1.872",
    "realutilization": 1.5595309171075837,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 27",
    "hightolow": " 26",
    "idletime": 25406093,
    "util": 77.59603791887125




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 24",
    "hightolow": " 23",
    "idletime": 24543101,
    "util": 78.35705379188713




   Real Utilization: 1.5595309171075837
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  4

    
    "id": " 4",
    "basecpu": " 1",
    "priority": " 7",
    "period": 39375.0,
    "C(LO)": 2075.0,
    "C(HI)": 4151.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 989",
    "preemptions": " 31",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003849498",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.863131826",
    "avgresponsejitter": " 0.001074646",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 7",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1026",
    "timesonc2": " 0",
    "lockedtime": " 0.000016156"




   Task:  20

    
    "id": " 20",
    "basecpu": " 1",
    "priority": " 1",
    "period": 135000.0,
    "C(LO)": 6950.0,
    "C(HI)": 13901.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 289",
    "preemptions": " 90",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.035893258",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.747910105",
    "avgresponsejitter": " 0.004642640",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 5",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 383",
    "timesonc2": " 0",
    "lockedtime": " 0.000004180"




   Task:  15

    
    "id": " 15",
    "basecpu": " 1",
    "priority": " 5",
    "period": 90000.0,
    "C(LO)": 4160.0,
    "C(HI)": 8320.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 434",
    "preemptions": " 34",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.030081973",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.881474517",
    "avgresponsejitter": " 0.002564081",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 5",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 472",
    "timesonc2": " 0",
    "lockedtime": " 0.000007225"




   Task:  24

    
    "id": " 24",
    "basecpu": " 1",
    "priority": " 0",
    "period": 196875.0,
    "C(LO)": 8314.0,
    "C(HI)": 16629.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 199",
    "preemptions": " 68",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.032116880",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.785506601",
    "avgresponsejitter": " 0.005011414",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 267",
    "timesonc2": " 0",
    "lockedtime": " 0.000007249"




   Task:  18

    
    "id": " 18",
    "basecpu": " 1",
    "priority": " 3",
    "period": 129600.0,
    "C(LO)": 3350.0,
    "C(HI)": 6701.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 302",
    "preemptions": " 41",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006163423",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.883851444",
    "avgresponsejitter": " 0.001908688",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 344",
    "timesonc2": " 0",
    "lockedtime": " 0.000012682"




   Task:  19

    
    "id": " 19",
    "basecpu": " 1",
    "priority": " 2",
    "period": 131250.0,
    "C(LO)": 1213.0,
    "C(HI)": 2426.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 298",
    "preemptions": " 11",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.028504090",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.851934805",
    "avgresponsejitter": " 0.000816468",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 310",
    "timesonc2": " 0",
    "lockedtime": " 0.000003129"




   Task:  17

    
    "id": " 17",
    "basecpu": " 1",
    "priority": " 4",
    "period": 120000.0,
    "C(LO)": 646.0,
    "C(HI)": 1293.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 326",
    "preemptions": " 6",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.030525369",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.883495303",
    "avgresponsejitter": " 0.000437856",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 5",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 336",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  23

    
    "id": " 23",
    "basecpu": " 1",
    "priority": " 6",
    "period": 181440.0,
    "C(LO)": 43258.0,
    "C(HI)": 43258.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 216",
    "preemptions": " 400",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.030642060",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.828746375",
    "avgresponsejitter": " 0.024699363",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 615",
    "timesonc2": " 0",
    "lockedtime": " 0.000080261"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 12",
    "period": 35000.0,
    "C(LO)": 3531.0,
    "C(HI)": 3531.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1113",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001816426",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.885006523",
    "avgresponsejitter": " 0.001788637",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 3",
    "timesrestored": " 3",
    "timesonc1": " 1110",
    "timesonc2": " 2",
    "lockedtime": " 0.000038934"




   Task:  9

    
    "id": " 9",
    "basecpu": " 1",
    "priority": " 9",
    "period": 60000.0,
    "C(LO)": 3512.0,
    "C(HI)": 3512.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 650",
    "preemptions": " 25",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002703511",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.880010276",
    "avgresponsejitter": " 0.001787553",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 674",
    "timesonc2": " 0",
    "lockedtime": " 0.000033808"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 11",
    "period": 45360.0,
    "C(LO)": 1134.0,
    "C(HI)": 1134.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 859",
    "preemptions": " 14",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002400414",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.873526168",
    "avgresponsejitter": " 0.000606790",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 872",
    "timesonc2": " 0",
    "lockedtime": " 0.000024087"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 10",
    "period": 56250.0,
    "C(LO)": 1100.0,
    "C(HI)": 1100.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 693",
    "preemptions": " 7",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001158829",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.868756111",
    "avgresponsejitter": " 0.000567955",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 699",
    "timesonc2": " 0",
    "lockedtime": " 0.000003495"




   Task:  13

    
    "id": " 13",
    "basecpu": " 1",
    "priority": " 8",
    "period": 70000.0,
    "C(LO)": 210.0,
    "C(HI)": 210.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 557",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000700946",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.851812943",
    "avgresponsejitter": " 0.000108255",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 557",
    "timesonc2": " 0",
    "lockedtime": " 0.000000165"




   Task:  22

    
    "id": " 22",
    "basecpu": " 2",
    "priority": " 1",
    "period": 162000.0,
    "C(LO)": 31576.0,
    "C(HI)": 63152.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 241",
    "preemptions": " 883",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.061086054",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.718005910",
    "avgresponsejitter": " 0.019886375",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1125",
    "lockedtime": " 0.000041450"




   Task:  7

    
    "id": " 7",
    "basecpu": " 2",
    "priority": " 4",
    "period": 50400.0,
    "C(LO)": 894.0,
    "C(HI)": 1789.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 773",
    "preemptions": " 51",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002917529",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.859348336",
    "avgresponsejitter": " 0.000479252",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 11",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 834",
    "lockedtime": " 0.000000000"




   Task:  25

    
    "id": " 25",
    "basecpu": " 2",
    "priority": " 0",
    "period": 900000.0,
    "C(LO)": 10854.0,
    "C(HI)": 21709.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 45",
    "preemptions": " 36",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.017573396",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.701283613",
    "avgresponsejitter": " 0.007277517",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 82",
    "lockedtime": " 0.000000670"




   Task:  10

    
    "id": " 10",
    "basecpu": " 2",
    "priority": " 3",
    "period": 60480.0,
    "C(LO)": 450.0,
    "C(HI)": 900.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 645",
    "preemptions": " 18",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001218955",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.888646336",
    "avgresponsejitter": " 0.000240694",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 7",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 669",
    "lockedtime": " 0.000004697"




   Task:  16

    
    "id": " 16",
    "basecpu": " 2",
    "priority": " 2",
    "period": 118125.0,
    "C(LO)": 452.0,
    "C(HI)": 904.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 331",
    "preemptions": " 4",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002598913",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.863131027",
    "avgresponsejitter": " 0.000236952",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 336",
    "lockedtime": " 0.000010895"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 10",
    "period": 28350.0,
    "C(LO)": 5033.0,
    "C(HI)": 5033.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1373",
    "preemptions": " 338",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003230411",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.867856030",
    "avgresponsejitter": " 0.002568817",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1710",
    "lockedtime": " 0.000012453"




   Task:  11

    
    "id": " 11",
    "basecpu": " 2",
    "priority": " 8",
    "period": 64800.0,
    "C(LO)": 7889.999999999999,
    "C(HI)": 7889.999999999999,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 602",
    "preemptions": " 315",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007814033",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.880208709",
    "avgresponsejitter": " 0.004372189",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 916",
    "lockedtime": " 0.000038468"




   Task:  5

    
    "id": " 5",
    "basecpu": " 2",
    "priority": " 9",
    "period": 42000.0,
    "C(LO)": 3520.0,
    "C(HI)": 3520.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 928",
    "preemptions": " 86",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004985132",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.892006357",
    "avgresponsejitter": " 0.001876976",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1013",
    "lockedtime": " 0.000002541"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 11",
    "period": 10000.0,
    "C(LO)": 381.0,
    "C(HI)": 381.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 3890",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000204931",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.880008474",
    "avgresponsejitter": " 0.000194057",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 9",
    "timesrestored": " 7",
    "timesonc1": " 12",
    "timesonc2": " 3877",
    "lockedtime": " 0.000054078"




   Task:  14

    
    "id": " 14",
    "basecpu": " 2",
    "priority": " 6",
    "period": 75600.0,
    "C(LO)": 2112.0,
    "C(HI)": 2112.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 516",
    "preemptions": " 72",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003180985",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.858406718",
    "avgresponsejitter": " 0.001113489",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 587",
    "lockedtime": " 0.000000000"




   Task:  12

    
    "id": " 12",
    "basecpu": " 2",
    "priority": " 7",
    "period": 65625.0,
    "C(LO)": 1688.0,
    "C(HI)": 1688.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 594",
    "preemptions": " 64",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007829592",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.851691874",
    "avgresponsejitter": " 0.001002928",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 657",
    "lockedtime": " 0.000024982"




   Task:  21

    
    "id": " 21",
    "basecpu": " 2",
    "priority": " 5",
    "period": 141750.0,
    "C(LO)": 1885.0,
    "C(HI)": 1885.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 276",
    "preemptions": " 35",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006938426",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 39.842592051",
    "avgresponsejitter": " 0.001023381",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 310",
    "lockedtime": " 0.000001033"



   </details>



  3. Taskset **e4_semi2wf_t11303**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t11303",
    "size": "25",
    "utilization": "1.8840000000000001",
    "realutilization": 1.6505231481481482,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 16",
    "hightolow": " 15",
    "idletime": 19291674,
    "util": 82.9879417989418




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 9",
    "hightolow": " 8",
    "idletime": 20339001,
    "util": 82.06437301587302




   Real Utilization: 1.6505231481481482
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  13

    
    "id": " 13",
    "basecpu": " 1",
    "priority": " 4",
    "period": 70875.0,
    "C(LO)": 6111.0,
    "C(HI)": 12223.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 434",
    "preemptions": " 153",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.016088342",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.618256096",
    "avgresponsejitter": " 0.003902315",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 588",
    "timesonc2": " 0",
    "lockedtime": " 0.000020658"




   Task:  18

    
    "id": " 18",
    "basecpu": " 1",
    "priority": " 1",
    "period": 126000.0,
    "C(LO)": 5625.0,
    "C(HI)": 11250.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 245",
    "preemptions": " 36",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.013662769",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.630533670",
    "avgresponsejitter": " 0.003127724",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 282",
    "timesonc2": " 0",
    "lockedtime": " 0.000002724"




   Task:  14

    
    "id": " 14",
    "basecpu": " 1",
    "priority": " 3",
    "period": 75600.0,
    "C(LO)": 2471.0,
    "C(HI)": 4943.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 407",
    "preemptions": " 31",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.010842420",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.629247604",
    "avgresponsejitter": " 0.001381231",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 440",
    "timesonc2": " 0",
    "lockedtime": " 0.000008237"




   Task:  23

    
    "id": " 23",
    "basecpu": " 1",
    "priority": " 0",
    "period": 196875.0,
    "C(LO)": 5021.0,
    "C(HI)": 10042.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 157",
    "preemptions": " 28",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.012967186",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.515631150",
    "avgresponsejitter": " 0.002788108",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 184",
    "timesonc2": " 0",
    "lockedtime": " 0.000002195"




   Task:  10

    
    "id": " 10",
    "basecpu": " 1",
    "priority": " 5",
    "period": 60000.0,
    "C(LO)": 1486.0,
    "C(HI)": 2973.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 512",
    "preemptions": " 15",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.008119931",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.601389793",
    "avgresponsejitter": " 0.000788772",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 5",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 531",
    "timesonc2": " 0",
    "lockedtime": " 0.000000165"




   Task:  17

    
    "id": " 17",
    "basecpu": " 1",
    "priority": " 2",
    "period": 105000.0,
    "C(LO)": 329.0,
    "C(HI)": 658.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 293",
    "preemptions": " 5",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.008173495",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.557691003",
    "avgresponsejitter": " 0.000213511",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 4",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 301",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  11

    
    "id": " 11",
    "basecpu": " 1",
    "priority": " 8",
    "period": 64800.0,
    "C(LO)": 13583.0,
    "C(HI)": 13583.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 474",
    "preemptions": " 277",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.011130973",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.585606811",
    "avgresponsejitter": " 0.007508853",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 750",
    "timesonc2": " 0",
    "lockedtime": " 0.000032147"




   Task:  4

    
    "id": " 4",
    "basecpu": " 1",
    "priority": " 12",
    "period": 35000.0,
    "C(LO)": 3446.0,
    "C(HI)": 3446.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 877",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001771511",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.625007384",
    "avgresponsejitter": " 0.001743916",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 0",
    "timesonc1": " 875",
    "timesonc2": " 1",
    "lockedtime": " 0.000015480"




   Task:  12

    
    "id": " 12",
    "basecpu": " 1",
    "priority": " 7",
    "period": 70000.0,
    "C(LO)": 4920.0,
    "C(HI)": 4920.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 439",
    "preemptions": " 57",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.011819604",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.594623640",
    "avgresponsejitter": " 0.002757387",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 495",
    "timesonc2": " 0",
    "lockedtime": " 0.000010054"




   Task:  15

    
    "id": " 15",
    "basecpu": " 1",
    "priority": " 6",
    "period": 87500.0,
    "C(LO)": 5187.0,
    "C(HI)": 5187.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 352",
    "preemptions": " 69",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.011538456",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.625007868",
    "avgresponsejitter": " 0.003050165",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 420",
    "timesonc2": " 0",
    "lockedtime": " 0.000005808"




   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 10",
    "period": 45000.0,
    "C(LO)": 1836.0,
    "C(HI)": 1836.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 682",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000948315",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.600459339",
    "avgresponsejitter": " 0.000932940",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 0",
    "timesonc1": " 681",
    "timesonc2": " 0",
    "lockedtime": " 0.000005009"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 11",
    "period": 40000.0,
    "C(LO)": 872.0,
    "C(HI)": 872.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 767",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000454234",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.600008814",
    "avgresponsejitter": " 0.000439892",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 0",
    "timesonc1": " 766",
    "timesonc2": " 0",
    "lockedtime": " 0.000006363"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 9",
    "period": 45360.0,
    "C(LO)": 549.0,
    "C(HI)": 549.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 677",
    "preemptions": " 7",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002065970",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.618009895",
    "avgresponsejitter": " 0.000287877",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 683",
    "timesonc2": " 0",
    "lockedtime": " 0.000006234"




   Task:  22

    
    "id": " 22",
    "basecpu": " 2",
    "priority": " 2",
    "period": 189000.0,
    "C(LO)": 19197.0,
    "C(HI)": 38394.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 163",
    "preemptions": " 243",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.031267700",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.433087847",
    "avgresponsejitter": " 0.011892414",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 406",
    "lockedtime": " 0.000008571"




   Task:  24

    
    "id": " 24",
    "basecpu": " 2",
    "priority": " 1",
    "period": 450000.0,
    "C(LO)": 18137.0,
    "C(HI)": 36275.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 70",
    "preemptions": " 75",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.047973318",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.600006015",
    "avgresponsejitter": " 0.012299414",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 146",
    "lockedtime": " 0.000005333"




   Task:  25

    
    "id": " 25",
    "basecpu": " 2",
    "priority": " 0",
    "period": 453600.0,
    "C(LO)": 14773.0,
    "C(HI)": 29547.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 69",
    "preemptions": " 63",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.027377300",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.391467901",
    "avgresponsejitter": " 0.009438697",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 132",
    "lockedtime": " 0.000003243"




   Task:  21

    
    "id": " 21",
    "basecpu": " 2",
    "priority": " 3",
    "period": 175000.0,
    "C(LO)": 4426.0,
    "C(HI)": 8852.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 176",
    "preemptions": " 36",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005492949",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.450005952",
    "avgresponsejitter": " 0.002409535",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 212",
    "lockedtime": " 0.000005420"




   Task:  19

    
    "id": " 19",
    "basecpu": " 2",
    "priority": " 5",
    "period": 129600.0,
    "C(LO)": 1738.0,
    "C(HI)": 3477.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 238",
    "preemptions": " 12",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006213423",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.585605955",
    "avgresponsejitter": " 0.001003186",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 252",
    "lockedtime": " 0.000007399"




   Task:  20

    
    "id": " 20",
    "basecpu": " 2",
    "priority": " 4",
    "period": 141750.0,
    "C(LO)": 708.0,
    "C(HI)": 1416.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 218",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000951949",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.623270324",
    "avgresponsejitter": " 0.000360345",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 220",
    "lockedtime": " 0.000000000"




   Task:  5

    
    "id": " 5",
    "basecpu": " 2",
    "priority": " 8",
    "period": 39375.0,
    "C(LO)": 6251.0,
    "C(HI)": 6251.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 779",
    "preemptions": " 130",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004129258",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.594380778",
    "avgresponsejitter": " 0.003184492",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 908",
    "lockedtime": " 0.000010802"




   Task:  3

    
    "id": " 3",
    "basecpu": " 2",
    "priority": " 9",
    "period": 33750.0,
    "C(LO)": 4341.0,
    "C(HI)": 4341.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 909",
    "preemptions": " 97",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003126303",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.611255787",
    "avgresponsejitter": " 0.002205468",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1005",
    "lockedtime": " 0.000010700"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 11",
    "period": 10000.0,
    "C(LO)": 729.0,
    "C(HI)": 729.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 592",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000378432",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.900006541",
    "avgresponsejitter": " 0.000368195",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 1",
    "timesonc1": " 2",
    "timesonc2": " 589",
    "lockedtime": " 0.000012483"




   Task:  16

    
    "id": " 16",
    "basecpu": " 2",
    "priority": " 6",
    "period": 94500.0,
    "C(LO)": 6381.0,
    "C(HI)": 6381.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 326",
    "preemptions": " 23",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004113733",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.619701012",
    "avgresponsejitter": " 0.003203961",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 348",
    "lockedtime": " 0.000001468"




   Task:  9

    
    "id": " 9",
    "basecpu": " 2",
    "priority": " 7",
    "period": 47250.0,
    "C(LO)": 2523.0,
    "C(HI)": 2523.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 650",
    "preemptions": " 29",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001891619",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.618294369",
    "avgresponsejitter": " 0.001286192",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 678",
    "lockedtime": " 0.000002318"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 10",
    "period": 25200.0,
    "C(LO)": 504.0,
    "C(HI)": 504.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1217",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000301258",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 31.618010574",
    "avgresponsejitter": " 0.000254237",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1216",
    "lockedtime": " 0.000024402"



   </details>



  4. Taskset **e4_semi2wf_t11768**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t11768",
    "size": "25",
    "utilization": "1.9320000000000002",
    "realutilization": 1.8805915079365079,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 24",
    "hightolow": " 23",
    "idletime": 6878972,
    "util": 93.93388712522045




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 20",
    "hightolow": " 19",
    "idletime": 6661951,
    "util": 94.12526366843034




   Real Utilization: 1.8805915079365079
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  19

    
    "id": " 19",
    "basecpu": " 1",
    "priority": " 2",
    "period": 140000.0,
    "C(LO)": 13152.0,
    "C(HI)": 26304.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 75",
    "preemptions": " 43",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.025696730",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.220006480",
    "avgresponsejitter": " 0.007564438",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 118",
    "timesonc2": " 0",
    "lockedtime": " 0.000001964"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 8",
    "period": 37800.0,
    "C(LO)": 2073.0,
    "C(HI)": 4147.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 274",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003505417",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.281606610",
    "avgresponsejitter": " 0.001082447",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 5",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 279",
    "timesonc2": " 0",
    "lockedtime": " 0.000006219"




   Task:  10

    
    "id": " 10",
    "basecpu": " 1",
    "priority": " 5",
    "period": 56700.0,
    "C(LO)": 2665.0,
    "C(HI)": 5331.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 183",
    "preemptions": " 10",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004265676",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.263060438",
    "avgresponsejitter": " 0.001429039",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 194",
    "timesonc2": " 0",
    "lockedtime": " 0.000001165"




   Task:  21

    
    "id": " 21",
    "basecpu": " 1",
    "priority": " 1",
    "period": 162000.0,
    "C(LO)": 4756.0,
    "C(HI)": 9512.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 65",
    "preemptions": " 15",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.012382258",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.213895937",
    "avgresponsejitter": " 0.002910688",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 81",
    "timesonc2": " 0",
    "lockedtime": " 0.000000676"




   Task:  4

    
    "id": " 4",
    "basecpu": " 1",
    "priority": " 7",
    "period": 40000.0,
    "C(LO)": 1131.0,
    "C(HI)": 2263.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 259",
    "preemptions": " 3",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001788015",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.280006682",
    "avgresponsejitter": " 0.000608724",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 5",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 266",
    "timesonc2": " 0",
    "lockedtime": " 0.000002000"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 6",
    "period": 45360.0,
    "C(LO)": 720.0,
    "C(HI)": 1440.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 228",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001114544",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.251366598",
    "avgresponsejitter": " 0.000384057",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 7",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 236",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  12

    
    "id": " 12",
    "basecpu": " 1",
    "priority": " 3",
    "period": 65625.0,
    "C(LO)": 413.0,
    "C(HI)": 826.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 158",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001240276",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.237507417",
    "avgresponsejitter": " 0.000220526",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 160",
    "timesonc2": " 0",
    "lockedtime": " 0.000002625"




   Task:  11

    
    "id": " 11",
    "basecpu": " 1",
    "priority": " 4",
    "period": 60000.0,
    "C(LO)": 157.0,
    "C(HI)": 314.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 173",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002504646",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.264619237",
    "avgresponsejitter": " 0.000096300",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 174",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  24

    
    "id": " 24",
    "basecpu": " 1",
    "priority": " 0",
    "period": 600000.0,
    "C(LO)": 116299.0,
    "C(HI)": 116299.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 18",
    "preemptions": " 146",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.081777910",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.604041396",
    "avgresponsejitter": " 0.069398018",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 163",
    "timesonc2": " 0",
    "lockedtime": " 0.000007994"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 10",
    "period": 54000.0,
    "C(LO)": 5515.0,
    "C(HI)": 5515.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 192",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003302985",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.260007721",
    "avgresponsejitter": " 0.002789129",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 191",
    "timesonc2": " 0",
    "lockedtime": " 0.000001514"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 11",
    "period": 45000.0,
    "C(LO)": 3438.0,
    "C(HI)": 3438.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 102",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001753862",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 5.500008706",
    "avgresponsejitter": " 0.001738997",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 4",
    "timesrestored": " 3",
    "timesonc1": " 98",
    "timesonc2": " 3",
    "lockedtime": " 0.000002568"




   Task:  17

    
    "id": " 17",
    "basecpu": " 1",
    "priority": " 9",
    "period": 120000.0,
    "C(LO)": 4009.0000000000005,
    "C(HI)": 4009.0000000000005,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 87",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002381153",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.200009937",
    "avgresponsejitter": " 0.002001784",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 86",
    "timesonc2": " 0",
    "lockedtime": " 0.000000577"




   Task:  22

    
    "id": " 22",
    "basecpu": " 2",
    "priority": " 1",
    "period": 168750.0,
    "C(LO)": 40534.0,
    "C(HI)": 81068.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 62",
    "preemptions": " 162",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.038714015",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.125783514",
    "avgresponsejitter": " 0.023730111",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 223",
    "lockedtime": " 0.000007282"




   Task:  9

    
    "id": " 9",
    "basecpu": " 2",
    "priority": " 3",
    "period": 56250.0,
    "C(LO)": 953.0,
    "C(HI)": 1907.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 184",
    "preemptions": " 4",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001430934",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.237717474",
    "avgresponsejitter": " 0.000493072",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 6",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 193",
    "lockedtime": " 0.000000622"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 6",
    "period": 26250.0,
    "C(LO)": 269.0,
    "C(HI)": 539.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 394",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000421586",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.290005757",
    "avgresponsejitter": " 0.000139523",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 4",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 397",
    "lockedtime": " 0.000003748"




   Task:  15

    
    "id": " 15",
    "basecpu": " 2",
    "priority": " 2",
    "period": 112500.0,
    "C(LO)": 716.0,
    "C(HI)": 1433.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 93",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007006652",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.238103922",
    "avgresponsejitter": " 0.000468784",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 96",
    "lockedtime": " 0.000000000"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 7",
    "period": 15750.0,
    "C(LO)": 70.0,
    "C(HI)": 141.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 655",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002834054",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.284756309",
    "avgresponsejitter": " 0.000047039",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 8",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 663",
    "lockedtime": " 0.000000381"




   Task:  7

    
    "id": " 7",
    "basecpu": " 2",
    "priority": " 12",
    "period": 50000.0,
    "C(LO)": 5433.0,
    "C(HI)": 5433.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 207",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002785523",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.250005775",
    "avgresponsejitter": " 0.002751156",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 1",
    "timesonc1": " 1",
    "timesonc2": " 205",
    "lockedtime": " 0.000006538"




   Task:  25

    
    "id": " 25",
    "basecpu": " 2",
    "priority": " 0",
    "period": 756000.0,
    "C(LO)": 77581.0,
    "C(HI)": 77581.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 15",
    "preemptions": " 83",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.078418219",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 10.838529126",
    "avgresponsejitter": " 0.051799492",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 97",
    "lockedtime": " 0.000003228"




   Task:  20

    
    "id": " 20",
    "basecpu": " 2",
    "priority": " 5",
    "period": 151200.0,
    "C(LO)": 14665.0,
    "C(HI)": 14665.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 70",
    "preemptions": " 51",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.011612967",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.281607174",
    "avgresponsejitter": " 0.007651922",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 120",
    "lockedtime": " 0.000005886"




   Task:  18

    
    "id": " 18",
    "basecpu": " 2",
    "priority": " 8",
    "period": 129600.0,
    "C(LO)": 4975.0,
    "C(HI)": 4975.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 81",
    "preemptions": " 9",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005749772",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.238406372",
    "avgresponsejitter": " 0.002730114",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 89",
    "lockedtime": " 0.000000532"




   Task:  14

    
    "id": " 14",
    "basecpu": " 2",
    "priority": " 10",
    "period": 94500.0,
    "C(LO)": 3358.0,
    "C(HI)": 3358.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 110",
    "preemptions": " 3",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004483529",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.206008495",
    "avgresponsejitter": " 0.001744258",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 112",
    "lockedtime": " 0.000003667"




   Task:  13

    
    "id": " 13",
    "basecpu": " 2",
    "priority": " 11",
    "period": 84000.0,
    "C(LO)": 1430.0,
    "C(HI)": 1430.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 124",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000732742",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.248005898",
    "avgresponsejitter": " 0.000727216",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 123",
    "lockedtime": " 0.000001420"




   Task:  23

    
    "id": " 23",
    "basecpu": " 2",
    "priority": " 4",
    "period": 200000.0,
    "C(LO)": 2112.0,
    "C(HI)": 2112.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 53",
    "preemptions": " 5",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003441357",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.202780066",
    "avgresponsejitter": " 0.001114168",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 57",
    "lockedtime": " 0.000000000"




   Task:  16

    
    "id": " 16",
    "basecpu": " 2",
    "priority": " 9",
    "period": 113400.0,
    "C(LO)": 366.0,
    "C(HI)": 366.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 92",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000225327",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.207419574",
    "avgresponsejitter": " 0.000185018",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 91",
    "lockedtime": " 0.000002141"



   </details>



  5. Taskset **e4_semi2wf_t13284**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t13284",
    "size": "30",
    "utilization": "1.848",
    "realutilization": 1.9546660405643739,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 5",
    "hightolow": " 4",
    "idletime": 2591360,
    "util": 97.71485008818343




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 7",
    "hightolow": " 6",
    "idletime": 2549511,
    "util": 97.75175396825396




   Real Utilization: 1.9546660405643739
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  27

    
    "id": " 27",
    "basecpu": " 1",
    "priority": " 1",
    "period": 180000.0,
    "C(LO)": 13925.0,
    "C(HI)": 27851.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 23",
    "preemptions": " 25",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.013034988",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.787211357",
    "avgresponsejitter": " 0.008176213",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 47",
    "timesonc2": " 0",
    "lockedtime": " 0.000001486"




   Task:  16

    
    "id": " 16",
    "basecpu": " 1",
    "priority": " 5",
    "period": 70875.0,
    "C(LO)": 3885.0,
    "C(HI)": 7771.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 56",
    "preemptions": " 12",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006963940",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.827256964",
    "avgresponsejitter": " 0.002505796",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 68",
    "timesonc2": " 0",
    "lockedtime": " 0.000001718"




   Task:  17

    
    "id": " 17",
    "basecpu": " 1",
    "priority": " 4",
    "period": 75600.0,
    "C(LO)": 3102.0,
    "C(HI)": 6205.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 53",
    "preemptions": " 8",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007715135",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.855732694",
    "avgresponsejitter": " 0.001915547",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 60",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  30

    
    "id": " 30",
    "basecpu": " 1",
    "priority": " 0",
    "period": 907200.0,
    "C(LO)": 30824.0,
    "C(HI)": 61648.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 6",
    "preemptions": " 15",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.054869688",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.632536604",
    "avgresponsejitter": " 0.028742063",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 21",
    "timesonc2": " 0",
    "lockedtime": " 0.000001027"




   Task:  21

    
    "id": " 21",
    "basecpu": " 1",
    "priority": " 3",
    "period": 129600.0,
    "C(LO)": 2944.0,
    "C(HI)": 5888.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 31",
    "preemptions": " 8",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006206090",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.758489565",
    "avgresponsejitter": " 0.001819042",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 40",
    "timesonc2": " 0",
    "lockedtime": " 0.000001643"




   Task:  24

    
    "id": " 24",
    "basecpu": " 1",
    "priority": " 2",
    "period": 157500.0,
    "C(LO)": 803.0,
    "C(HI)": 1606.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 26",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001262898",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.786779751",
    "avgresponsejitter": " 0.000434541",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 26",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  15

    
    "id": " 15",
    "basecpu": " 1",
    "priority": " 6",
    "period": 70000.0,
    "C(LO)": 207.0,
    "C(HI)": 414.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 57",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000122853",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.851404417",
    "avgresponsejitter": " 0.000102703",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 56",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  12

    
    "id": " 12",
    "basecpu": " 1",
    "priority": " 10",
    "period": 60000.0,
    "C(LO)": 8118.0,
    "C(HI)": 8118.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 66",
    "preemptions": " 17",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004881120",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.840006138",
    "avgresponsejitter": " 0.004070778",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 82",
    "timesonc2": " 0",
    "lockedtime": " 0.000006078"




   Task:  14

    
    "id": " 14",
    "basecpu": " 1",
    "priority": " 8",
    "period": 65625.0,
    "C(LO)": 6110.0,
    "C(HI)": 6110.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 61",
    "preemptions": " 17",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006326309",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.871881192",
    "avgresponsejitter": " 0.003305351",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 77",
    "timesonc2": " 0",
    "lockedtime": " 0.000001802"




   Task:  25

    
    "id": " 25",
    "basecpu": " 1",
    "priority": " 7",
    "period": 162000.0,
    "C(LO)": 12507.0,
    "C(HI)": 12507.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 26",
    "preemptions": " 23",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.014283943",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.888007231",
    "avgresponsejitter": " 0.007365201",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 48",
    "timesonc2": " 0",
    "lockedtime": " 0.000002252"




   Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 13",
    "period": 25200.0,
    "C(LO)": 1445.0,
    "C(HI)": 1445.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 5",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000739315",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 1.078881363",
    "avgresponsejitter": " 0.000731114",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 1",
    "timesonc1": " 3",
    "timesonc2": " 1",
    "lockedtime": " 0.000000000"




   Task:  10

    
    "id": " 10",
    "basecpu": " 1",
    "priority": " 11",
    "period": 50000.0,
    "C(LO)": 2017.9999999999998,
    "C(HI)": 2017.9999999999998,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 80",
    "preemptions": " 4",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001876514",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.900008459",
    "avgresponsejitter": " 0.001035661",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 83",
    "timesonc2": " 0",
    "lockedtime": " 0.000001177"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 12",
    "period": 35000.0,
    "C(LO)": 766.0,
    "C(HI)": 766.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 113",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000459075",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.885006889",
    "avgresponsejitter": " 0.000383670",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 112",
    "timesonc2": " 0",
    "lockedtime": " 0.000001405"




   Task:  13

    
    "id": " 13",
    "basecpu": " 1",
    "priority": " 9",
    "period": 60480.0,
    "C(LO)": 944.0,
    "C(HI)": 944.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 66",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001272315",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.870726811",
    "avgresponsejitter": " 0.000481676",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 66",
    "timesonc2": " 0",
    "lockedtime": " 0.000002931"




   Task:  1

    
    "id": " 1",
    "basecpu": " 1",
    "priority": " 14",
    "period": 18900.0,
    "C(LO)": 224.0,
    "C(HI)": 224.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 208",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000129802",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.893406694",
    "avgresponsejitter": " 0.000118727",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 1",
    "timesonc1": " 206",
    "timesonc2": " 1",
    "lockedtime": " 0.000002856"




   Task:  6

    
    "id": " 6",
    "basecpu": " 2",
    "priority": " 9",
    "period": 40000.0,
    "C(LO)": 4310.0,
    "C(HI)": 8620.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 99",
    "preemptions": " 19",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006769222",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.880005850",
    "avgresponsejitter": " 0.002361832",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 118",
    "lockedtime": " 0.000003748"




   Task:  11

    
    "id": " 11",
    "basecpu": " 2",
    "priority": " 6",
    "period": 56700.0,
    "C(LO)": 2464.0,
    "C(HI)": 4928.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 70",
    "preemptions": " 9",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006620255",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.855801039",
    "avgresponsejitter": " 0.001403847",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 78",
    "lockedtime": " 0.000003246"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 10",
    "period": 30240.0,
    "C(LO)": 1079.0,
    "C(HI)": 2158.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 131",
    "preemptions": " 4",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003690742",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.900967285",
    "avgresponsejitter": " 0.000596754",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 136",
    "lockedtime": " 0.000003114"




   Task:  9

    
    "id": " 9",
    "basecpu": " 2",
    "priority": " 7",
    "period": 47250.0,
    "C(LO)": 1293.0,
    "C(HI)": 2586.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 84",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003283363",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.874506991",
    "avgresponsejitter": " 0.000718868",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 86",
    "lockedtime": " 0.000002667"




   Task:  29

    
    "id": " 29",
    "basecpu": " 2",
    "priority": " 0",
    "period": 200000.0,
    "C(LO)": 2261.0,
    "C(HI)": 4523.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 21",
    "preemptions": " 4",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005515754",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.806831033",
    "avgresponsejitter": " 0.001435066",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 24",
    "lockedtime": " 0.000000000"




   Task:  8

    
    "id": " 8",
    "basecpu": " 2",
    "priority": " 8",
    "period": 45360.0,
    "C(LO)": 343.0,
    "C(HI)": 686.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 87",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000448021",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.855607982",
    "avgresponsejitter": " 0.000177249",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 89",
    "lockedtime": " 0.000000444"




   Task:  23

    
    "id": " 23",
    "basecpu": " 2",
    "priority": " 2",
    "period": 150000.0,
    "C(LO)": 632.0,
    "C(HI)": 1265.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 27",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000372186",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.750399348",
    "avgresponsejitter": " 0.000317697",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 26",
    "lockedtime": " 0.000000973"




   Task:  26

    
    "id": " 26",
    "basecpu": " 2",
    "priority": " 1",
    "period": 175000.0,
    "C(LO)": 54.0,
    "C(HI)": 109.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 24",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000088961",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.850006159",
    "avgresponsejitter": " 0.000035258",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 24",
    "lockedtime": " 0.000000826"




   Task:  20

    
    "id": " 20",
    "basecpu": " 2",
    "priority": " 5",
    "period": 118125.0,
    "C(LO)": 29641.0,
    "C(HI)": 29641.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 34",
    "preemptions": " 77",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.024890985",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.782314694",
    "avgresponsejitter": " 0.017469225",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 110",
    "lockedtime": " 0.000006778"




   Task:  19

    
    "id": " 19",
    "basecpu": " 2",
    "priority": " 11",
    "period": 84375.0,
    "C(LO)": 6122.0,
    "C(HI)": 6122.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 48",
    "preemptions": " 4",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003357724",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.881256231",
    "avgresponsejitter": " 0.003119420",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 51",
    "lockedtime": " 0.000000799"




   Task:  7

    
    "id": " 7",
    "basecpu": " 2",
    "priority": " 13",
    "period": 45000.0,
    "C(LO)": 1945.0,
    "C(HI)": 1945.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 88",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001004144",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.870005760",
    "avgresponsejitter": " 0.000986541",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 87",
    "lockedtime": " 0.000000664"




   Task:  18

    
    "id": " 18",
    "basecpu": " 2",
    "priority": " 12",
    "period": 81000.0,
    "C(LO)": 3086.0,
    "C(HI)": 3086.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 50",
    "preemptions": " 3",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001800354",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.888006577",
    "avgresponsejitter": " 0.001578114",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 52",
    "lockedtime": " 0.000001177"




   Task:  28

    
    "id": " 28",
    "basecpu": " 2",
    "priority": " 3",
    "period": 196875.0,
    "C(LO)": 4135.0,
    "C(HI)": 4135.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 21",
    "preemptions": " 7",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004137586",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.740631018",
    "avgresponsejitter": " 0.002396102",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 27",
    "lockedtime": " 0.000001273"




   Task:  3

    
    "id": " 3",
    "basecpu": " 2",
    "priority": " 14",
    "period": 26250.0,
    "C(LO)": 439.0,
    "C(HI)": 439.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 150",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000236679",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.885006384",
    "avgresponsejitter": " 0.000225517",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 149",
    "lockedtime": " 0.000005712"




   Task:  22

    
    "id": " 22",
    "basecpu": " 2",
    "priority": " 4",
    "period": 140000.0,
    "C(LO)": 177.0,
    "C(HI)": 177.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 29",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000107327",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 4.806725015",
    "avgresponsejitter": " 0.000089643",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 28",
    "lockedtime": " 0.000000165"



   </details>



  6. Taskset **e4_semi2wf_t13324**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t13324",
    "size": "30",
    "utilization": "1.86",
    "realutilization": 1.878521693121693,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 9",
    "hightolow": " 8",
    "idletime": 6753017,
    "util": 94.04495855379189




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 14",
    "hightolow": " 13",
    "idletime": 7022623,
    "util": 93.80721075837742




   Real Utilization: 1.878521693121693
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  22

    
    "id": " 22",
    "basecpu": " 1",
    "priority": " 4",
    "period": 126000.0,
    "C(LO)": 9621.0,
    "C(HI)": 19243.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 87",
    "preemptions": " 48",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.017212228",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.716274613",
    "avgresponsejitter": " 0.005565222",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 135",
    "timesonc2": " 0",
    "lockedtime": " 0.000002769"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 9",
    "period": 52500.0,
    "C(LO)": 3364.0,
    "C(HI)": 6729.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 206",
    "preemptions": " 11",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004896222",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.710009231",
    "avgresponsejitter": " 0.001810892",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 218",
    "timesonc2": " 0",
    "lockedtime": " 0.000000402"




   Task:  13

    
    "id": " 13",
    "basecpu": " 1",
    "priority": " 7",
    "period": 78750.0,
    "C(LO)": 3702.0,
    "C(HI)": 7404.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 138",
    "preemptions": " 12",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004269529",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.714352751",
    "avgresponsejitter": " 0.001921282",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 149",
    "timesonc2": " 0",
    "lockedtime": " 0.000003147"




   Task:  20

    
    "id": " 20",
    "basecpu": " 1",
    "priority": " 5",
    "period": 108000.0,
    "C(LO)": 1215.0,
    "C(HI)": 2430.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 101",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001856357",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.692730865",
    "avgresponsejitter": " 0.000651219",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 103",
    "timesonc2": " 0",
    "lockedtime": " 0.000000165"




   Task:  11

    
    "id": " 11",
    "basecpu": " 1",
    "priority": " 8",
    "period": 65625.0,
    "C(LO)": 729.0,
    "C(HI)": 1458.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 165",
    "preemptions": " 3",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002081420",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.696881048",
    "avgresponsejitter": " 0.000385030",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 168",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  23

    
    "id": " 23",
    "basecpu": " 1",
    "priority": " 3",
    "period": 131250.0,
    "C(LO)": 1281.0,
    "C(HI)": 2563.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 83",
    "preemptions": " 7",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007801847",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.635801799",
    "avgresponsejitter": " 0.000769006",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 90",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  26

    
    "id": " 26",
    "basecpu": " 1",
    "priority": " 2",
    "period": 181440.0,
    "C(LO)": 918.0,
    "C(HI)": 1836.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 61",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001330997",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.706619826",
    "avgresponsejitter": " 0.000479222",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 62",
    "timesonc2": " 0",
    "lockedtime": " 0.000000246"




   Task:  16

    
    "id": " 16",
    "basecpu": " 1",
    "priority": " 6",
    "period": 87500.0,
    "C(LO)": 353.0,
    "C(HI)": 706.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 124",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001845390",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.675006844",
    "avgresponsejitter": " 0.000197820",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 125",
    "timesonc2": " 0",
    "lockedtime": " 0.000001646"




   Task:  29

    
    "id": " 29",
    "basecpu": " 1",
    "priority": " 1",
    "period": 567000.0,
    "C(LO)": 94116.0,
    "C(HI)": 94116.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 20",
    "preemptions": " 115",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.078157204",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.212094021",
    "avgresponsejitter": " 0.059703982",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 134",
    "timesonc2": " 0",
    "lockedtime": " 0.000008387"




   Task:  15

    
    "id": " 15",
    "basecpu": " 1",
    "priority": " 11",
    "period": 84000.0,
    "C(LO)": 12061.0,
    "C(HI)": 12061.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 129",
    "preemptions": " 38",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.008921607",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.668006243",
    "avgresponsejitter": " 0.006236787",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 166",
    "timesonc2": " 0",
    "lockedtime": " 0.000003066"




   Task:  30

    
    "id": " 30",
    "basecpu": " 1",
    "priority": " 0",
    "period": 630000.0,
    "C(LO)": 40836.0,
    "C(HI)": 40836.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 19",
    "preemptions": " 36",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.032794174",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.720246799",
    "avgresponsejitter": " 0.023531601",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 54",
    "timesonc2": " 0",
    "lockedtime": " 0.000004360"




   Task:  9

    
    "id": " 9",
    "basecpu": " 1",
    "priority": " 13",
    "period": 60480.0,
    "C(LO)": 3270.0,
    "C(HI)": 3270.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 179",
    "preemptions": " 4",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002271967",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.704967291",
    "avgresponsejitter": " 0.001668742",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 4",
    "timesrestored": " 3",
    "timesonc1": " 179",
    "timesonc2": " 3",
    "lockedtime": " 0.000002931"




   Task:  4

    
    "id": " 4",
    "basecpu": " 1",
    "priority": " 15",
    "period": 40000.0,
    "C(LO)": 1131.0,
    "C(HI)": 1131.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 129",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000590369",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.080326700",
    "avgresponsejitter": " 0.000577048",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 3",
    "timesrestored": " 3",
    "timesonc1": " 125",
    "timesonc2": " 3",
    "lockedtime": " 0.000000967"




   Task:  10

    
    "id": " 10",
    "basecpu": " 1",
    "priority": " 12",
    "period": 64800.0,
    "C(LO)": 1369.0,
    "C(HI)": 1369.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 167",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000821994",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.692007772",
    "avgresponsejitter": " 0.000691012",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 166",
    "timesonc2": " 0",
    "lockedtime": " 0.000001628"




   Task:  27

    
    "id": " 27",
    "basecpu": " 1",
    "priority": " 10",
    "period": 196875.0,
    "C(LO)": 3512.0,
    "C(HI)": 3512.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 56",
    "preemptions": " 7",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003729964",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.631259279",
    "avgresponsejitter": " 0.001884114",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 62",
    "timesonc2": " 0",
    "lockedtime": " 0.000001949"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 14",
    "period": 56700.0,
    "C(LO)": 758.0,
    "C(HI)": 758.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 191",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000384532",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.725756105",
    "avgresponsejitter": " 0.000383153",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 1",
    "timesonc1": " 188",
    "timesonc2": " 2",
    "lockedtime": " 0.000005219"




   Task:  28

    
    "id": " 28",
    "basecpu": " 2",
    "priority": " 0",
    "period": 200000.0,
    "C(LO)": 26234.0,
    "C(HI)": 52469.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 55",
    "preemptions": " 113",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.043207724",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.600005760",
    "avgresponsejitter": " 0.016464435",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 167",
    "lockedtime": " 0.000006847"




   Task:  5

    
    "id": " 5",
    "basecpu": " 2",
    "priority": " 6",
    "period": 47250.0,
    "C(LO)": 2455.0,
    "C(HI)": 4910.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 228",
    "preemptions": " 4",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003883865",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.678506444",
    "avgresponsejitter": " 0.001256366",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 234",
    "lockedtime": " 0.000002925"




   Task:  18

    
    "id": " 18",
    "basecpu": " 2",
    "priority": " 2",
    "period": 90720.0,
    "C(LO)": 1246.0,
    "C(HI)": 2493.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 120",
    "preemptions": " 6",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.019132354",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.704966559",
    "avgresponsejitter": " 0.000856937",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 126",
    "lockedtime": " 0.000001706"




   Task:  17

    
    "id": " 17",
    "basecpu": " 2",
    "priority": " 3",
    "period": 90000.0,
    "C(LO)": 1010.0,
    "C(HI)": 2020.9999999999998,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 121",
    "preemptions": " 3",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003509030",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.710784429",
    "avgresponsejitter": " 0.000547901",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 124",
    "lockedtime": " 0.000000000"




   Task:  19

    
    "id": " 19",
    "basecpu": " 2",
    "priority": " 1",
    "period": 100800.0,
    "C(LO)": 1106.0,
    "C(HI)": 2213.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 108",
    "preemptions": " 4",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003104129",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.699676508",
    "avgresponsejitter": " 0.000610694",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 112",
    "lockedtime": " 0.000000387"




   Task:  12

    
    "id": " 12",
    "basecpu": " 2",
    "priority": " 4",
    "period": 67500.0,
    "C(LO)": 415.0,
    "C(HI)": 830.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 160",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.008598321",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.665637865",
    "avgresponsejitter": " 0.000261676",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 163",
    "lockedtime": " 0.000000000"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 7",
    "period": 25200.0,
    "C(LO)": 29.0,
    "C(HI)": 58.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 427",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000056252",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.710761943",
    "avgresponsejitter": " 0.000019156",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 6",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 432",
    "lockedtime": " 0.000004733"




   Task:  25

    
    "id": " 25",
    "basecpu": " 2",
    "priority": " 5",
    "period": 175000.0,
    "C(LO)": 31292.0,
    "C(HI)": 31292.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 63",
    "preemptions": " 156",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.026457679",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.675005949",
    "avgresponsejitter": " 0.018825799",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 218",
    "lockedtime": " 0.000011168"




   Task:  7

    
    "id": " 7",
    "basecpu": " 2",
    "priority": " 11",
    "period": 56250.0,
    "C(LO)": 4514.0,
    "C(HI)": 4514.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 192",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002700931",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.688145781",
    "avgresponsejitter": " 0.002276273",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 191",
    "lockedtime": " 0.000002081"




   Task:  14

    
    "id": " 14",
    "basecpu": " 2",
    "priority": " 10",
    "period": 81000.0,
    "C(LO)": 5892.0,
    "C(HI)": 5892.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 134",
    "preemptions": " 12",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005580447",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.692006405",
    "avgresponsejitter": " 0.003034562",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 145",
    "lockedtime": " 0.000001907"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 13",
    "period": 22500.0,
    "C(LO)": 1229.0,
    "C(HI)": 1229.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 478",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000641024",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.710009991",
    "avgresponsejitter": " 0.000627994",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 477",
    "lockedtime": " 0.000006345"




   Task:  21

    
    "id": " 21",
    "basecpu": " 2",
    "priority": " 9",
    "period": 113400.0,
    "C(LO)": 3302.0,
    "C(HI)": 3302.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 96",
    "preemptions": " 10",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004113904",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.659607456",
    "avgresponsejitter": " 0.001770880",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 105",
    "lockedtime": " 0.000006366"




   Task:  24

    
    "id": " 24",
    "basecpu": " 2",
    "priority": " 8",
    "period": 151200.0,
    "C(LO)": 2939.0,
    "C(HI)": 2939.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 72",
    "preemptions": " 8",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002321189",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.584008994",
    "avgresponsejitter": " 0.001505453",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 79",
    "lockedtime": " 0.000001865"




   Task:  3

    
    "id": " 3",
    "basecpu": " 2",
    "priority": " 12",
    "period": 39375.0,
    "C(LO)": 224.0,
    "C(HI)": 224.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 274",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000120270",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.710641189",
    "avgresponsejitter": " 0.000117363",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 273",
    "lockedtime": " 0.000004724"



   </details>



  7. Taskset **e4_semi2wf_t13371**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t13371",
    "size": "30",
    "utilization": "1.86",
    "realutilization": 1.2956386507936508,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 72",
    "hightolow": " 71",
    "idletime": 37280637,
    "util": 67.12465873015873




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 47",
    "hightolow": " 46",
    "idletime": 42593940,
    "util": 62.43920634920635




   Real Utilization: 1.2956386507936508
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  9

    
    "id": " 9",
    "basecpu": " 1",
    "priority": " 7",
    "period": 45360.0,
    "C(LO)": 3718.0,
    "C(HI)": 7437.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1288",
    "preemptions": " 267",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.009151568",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.332966072",
    "avgresponsejitter": " 0.002138090",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 16",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1570",
    "timesonc2": " 0",
    "lockedtime": " 0.000016847"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 8",
    "period": 28350.0,
    "C(LO)": 2221.0,
    "C(HI)": 4442.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 2060",
    "preemptions": " 193",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004805441",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.345907282",
    "avgresponsejitter": " 0.001214075",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 24",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 2276",
    "timesonc2": " 0",
    "lockedtime": " 0.000009021"




   Task:  27

    
    "id": " 27",
    "basecpu": " 1",
    "priority": " 2",
    "period": 175000.0,
    "C(LO)": 9039.0,
    "C(HI)": 18079.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 335",
    "preemptions": " 273",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.019954661",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.276897799",
    "avgresponsejitter": " 0.006091066",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 8",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 615",
    "timesonc2": " 0",
    "lockedtime": " 0.000007952"




   Task:  21

    
    "id": " 21",
    "basecpu": " 1",
    "priority": " 4",
    "period": 118125.0,
    "C(LO)": 5016.0,
    "C(HI)": 10033.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 496",
    "preemptions": " 81",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.012026766",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.354979892",
    "avgresponsejitter": " 0.002795796",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 578",
    "timesonc2": " 0",
    "lockedtime": " 0.000003045"




   Task:  15

    
    "id": " 15",
    "basecpu": " 1",
    "priority": " 5",
    "period": 84375.0,
    "C(LO)": 1229.0,
    "C(HI)": 2458.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 693",
    "preemptions": " 39",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007250859",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.303131003",
    "avgresponsejitter": " 0.000730709",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 10",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 741",
    "timesonc2": " 0",
    "lockedtime": " 0.000001156"




   Task:  13

    
    "id": " 13",
    "basecpu": " 1",
    "priority": " 6",
    "period": 75600.0,
    "C(LO)": 857.0,
    "C(HI)": 1714.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 774",
    "preemptions": " 60",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004325937",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.364360700",
    "avgresponsejitter": " 0.000477321",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 5",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 838",
    "timesonc2": " 0",
    "lockedtime": " 0.000001222"




   Task:  29

    
    "id": " 29",
    "basecpu": " 1",
    "priority": " 0",
    "period": 840000.0,
    "C(LO)": 3095.0,
    "C(HI)": 6191.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 71",
    "preemptions": " 13",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004704288",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 58.964266553",
    "avgresponsejitter": " 0.001846285",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 83",
    "timesonc2": " 0",
    "lockedtime": " 0.000000402"




   Task:  23

    
    "id": " 23",
    "basecpu": " 1",
    "priority": " 3",
    "period": 131250.0,
    "C(LO)": 285.0,
    "C(HI)": 570.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 446",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001620444",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.276730904",
    "avgresponsejitter": " 0.000153907",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 7",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 454",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  1

    
    "id": " 1",
    "basecpu": " 1",
    "priority": " 17",
    "period": 18900.0,
    "C(LO)": 2278.0,
    "C(HI)": 2278.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 3090",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001172727",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.363207165",
    "avgresponsejitter": " 0.001153817",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 11",
    "timesrestored": " 11",
    "timesonc1": " 3085",
    "timesonc2": " 4",
    "lockedtime": " 0.000010796"




   Task:  30

    
    "id": " 30",
    "basecpu": " 1",
    "priority": " 1",
    "period": 907200.0,
    "C(LO)": 58822.0,
    "C(HI)": 58822.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 66",
    "preemptions": " 440",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.055379775",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.067330790",
    "avgresponsejitter": " 0.039291264",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 505",
    "timesonc2": " 0",
    "lockedtime": " 0.000016381"




   Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 16",
    "period": 26250.0,
    "C(LO)": 1649.0,
    "C(HI)": 1649.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2225",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000853216",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.353758138",
    "avgresponsejitter": " 0.000836129",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 4",
    "timesrestored": " 4",
    "timesonc1": " 2219",
    "timesonc2": " 5",
    "lockedtime": " 0.000045420"




   Task:  24

    
    "id": " 24",
    "basecpu": " 1",
    "priority": " 9",
    "period": 135000.0,
    "C(LO)": 5132.0,
    "C(HI)": 5132.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 434",
    "preemptions": " 74",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005568048",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.323274387",
    "avgresponsejitter": " 0.002850973",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 507",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 15",
    "period": 33750.0,
    "C(LO)": 861.0,
    "C(HI)": 861.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1731",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000512477",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.354609258",
    "avgresponsejitter": " 0.000426363",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1730",
    "timesonc2": " 0",
    "lockedtime": " 0.000012090"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 14",
    "period": 35000.0,
    "C(LO)": 877.0,
    "C(HI)": 877.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1669",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000527664",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.345476288",
    "avgresponsejitter": " 0.000436526",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1668",
    "timesonc2": " 0",
    "lockedtime": " 0.000009258"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 13",
    "period": 45000.0,
    "C(LO)": 995.9999999999999,
    "C(HI)": 995.9999999999999,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1299",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000599832",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.365006012",
    "avgresponsejitter": " 0.000492378",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1298",
    "timesonc2": " 0",
    "lockedtime": " 0.000001757"




   Task:  16

    
    "id": " 16",
    "basecpu": " 1",
    "priority": " 12",
    "period": 90000.0,
    "C(LO)": 1984.9999999999998,
    "C(HI)": 1984.9999999999998,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 650",
    "preemptions": " 31",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002310748",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.320861129",
    "avgresponsejitter": " 0.001052318",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 680",
    "timesonc2": " 0",
    "lockedtime": " 0.000000390"




   Task:  22

    
    "id": " 22",
    "basecpu": " 1",
    "priority": " 10",
    "period": 120000.0,
    "C(LO)": 2606.0,
    "C(HI)": 2606.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 488",
    "preemptions": " 47",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003665751",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.321867387",
    "avgresponsejitter": " 0.001453372",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 534",
    "timesonc2": " 0",
    "lockedtime": " 0.000001111"




   Task:  20

    
    "id": " 20",
    "basecpu": " 1",
    "priority": " 11",
    "period": 113400.0,
    "C(LO)": 2020.9999999999998,
    "C(HI)": 2020.9999999999998,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 516",
    "preemptions": " 76",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002729670",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.288778486",
    "avgresponsejitter": " 0.001105568",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 591",
    "timesonc2": " 0",
    "lockedtime": " 0.000002778"




   Task:  11

    
    "id": " 11",
    "basecpu": " 2",
    "priority": " 5",
    "period": 54000.0,
    "C(LO)": 4571.0,
    "C(HI)": 9142.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1082",
    "preemptions": " 146",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.008135399",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.332730018",
    "avgresponsejitter": " 0.002407132",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 12",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1239",
    "lockedtime": " 0.000025706"




   Task:  17

    
    "id": " 17",
    "basecpu": " 2",
    "priority": " 3",
    "period": 100800.0,
    "C(LO)": 7622.0,
    "C(HI)": 15244.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 581",
    "preemptions": " 151",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.012575477",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.363207673",
    "avgresponsejitter": " 0.004083661",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 6",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 737",
    "lockedtime": " 0.000032766"




   Task:  26

    
    "id": " 26",
    "basecpu": " 2",
    "priority": " 0",
    "period": 162000.0,
    "C(LO)": 11321.0,
    "C(HI)": 22642.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 362",
    "preemptions": " 176",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.018908571",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.335081952",
    "avgresponsejitter": " 0.006188423",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 4",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 541",
    "lockedtime": " 0.000026219"




   Task:  25

    
    "id": " 25",
    "basecpu": " 2",
    "priority": " 1",
    "period": 151200.0,
    "C(LO)": 3625.0,
    "C(HI)": 7251.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 387",
    "preemptions": " 47",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006156468",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.227279823",
    "avgresponsejitter": " 0.001882207",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 436",
    "lockedtime": " 0.000009216"




   Task:  7

    
    "id": " 7",
    "basecpu": " 2",
    "priority": " 6",
    "period": 39375.0,
    "C(LO)": 926.0,
    "C(HI)": 1853.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1484",
    "preemptions": " 4",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001469339",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.353756577",
    "avgresponsejitter": " 0.000467568",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 10",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1497",
    "lockedtime": " 0.000040387"




   Task:  18

    
    "id": " 18",
    "basecpu": " 2",
    "priority": " 2",
    "period": 101250.0,
    "C(LO)": 497.00000000000006,
    "C(HI)": 995.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 578",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003557853",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.334787132",
    "avgresponsejitter": " 0.000258243",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 5",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 584",
    "lockedtime": " 0.000031150"




   Task:  14

    
    "id": " 14",
    "basecpu": " 2",
    "priority": " 4",
    "period": 84000.0,
    "C(LO)": 295.0,
    "C(HI)": 591.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 696",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000478096",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.296005964",
    "avgresponsejitter": " 0.000153168",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 7",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 702",
    "lockedtime": " 0.000000387"




   Task:  19

    
    "id": " 19",
    "basecpu": " 2",
    "priority": " 8",
    "period": 108000.0,
    "C(LO)": 22667.0,
    "C(HI)": 22667.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 542",
    "preemptions": " 183",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.014405559",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.320009529",
    "avgresponsejitter": " 0.011431303",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 724",
    "lockedtime": " 0.000062441"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 11",
    "period": 30240.0,
    "C(LO)": 1709.0,
    "C(HI)": 1709.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 258",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000882736",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 8.741445892",
    "avgresponsejitter": " 0.000868105",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 257",
    "lockedtime": " 0.000009114"




   Task:  12

    
    "id": " 12",
    "basecpu": " 2",
    "priority": " 9",
    "period": 70000.0,
    "C(LO)": 1011.0,
    "C(HI)": 1011.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 835",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000520580",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.310006556",
    "avgresponsejitter": " 0.000514763",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 2",
    "timesonc1": " 2",
    "timesonc2": " 832",
    "lockedtime": " 0.000048456"




   Task:  28

    
    "id": " 28",
    "basecpu": " 2",
    "priority": " 7",
    "period": 200000.0,
    "C(LO)": 1690.0,
    "C(HI)": 1690.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 293",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001259547",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.200006565",
    "avgresponsejitter": " 0.000851357",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 293",
    "lockedtime": " 0.000006637"




   Task:  10

    
    "id": " 10",
    "basecpu": " 2",
    "priority": " 10",
    "period": 52500.0,
    "C(LO)": 287.0,
    "C(HI)": 287.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1113",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001319964",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 59.327507102",
    "avgresponsejitter": " 0.000148961",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 2",
    "timesonc1": " 2",
    "timesonc2": " 1111",
    "lockedtime": " 0.000059303"



   </details>



  8. Taskset **e4_semi2wf_t15544**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t15544",
    "size": "35",
    "utilization": "1.86",
    "realutilization": 1.8544047707231042,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 8",
    "hightolow": " 7",
    "idletime": 8206845,
    "util": 92.76292328042328




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 24",
    "hightolow": " 23",
    "idletime": 8303654,
    "util": 92.67755379188712




   Real Utilization: 1.8544047707231042
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  35

    
    "id": " 35",
    "basecpu": " 1",
    "priority": " 0",
    "period": 472500.0,
    "C(LO)": 42439.0,
    "C(HI)": 84879.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 28",
    "preemptions": " 70",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.048921508",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.290070399",
    "avgresponsejitter": " 0.023756538",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 98",
    "timesonc2": " 0",
    "lockedtime": " 0.000012568"




   Task:  34

    
    "id": " 34",
    "basecpu": " 1",
    "priority": " 1",
    "period": 200000.0,
    "C(LO)": 11754.0,
    "C(HI)": 23509.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 66",
    "preemptions": " 42",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.026763363",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.800291910",
    "avgresponsejitter": " 0.007617183",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 107",
    "timesonc2": " 0",
    "lockedtime": " 0.000005162"




   Task:  32

    
    "id": " 32",
    "basecpu": " 1",
    "priority": " 2",
    "period": 168000.0,
    "C(LO)": 5988.0,
    "C(HI)": 11977.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 78",
    "preemptions": " 16",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005672706",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.768006670",
    "avgresponsejitter": " 0.003135595",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 93",
    "timesonc2": " 0",
    "lockedtime": " 0.000001237"




   Task:  25

    
    "id": " 25",
    "basecpu": " 1",
    "priority": " 6",
    "period": 129600.0,
    "C(LO)": 2004.0000000000002,
    "C(HI)": 4009.0000000000005,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 100",
    "preemptions": " 10",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003857895",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.702407459",
    "avgresponsejitter": " 0.001119498",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 111",
    "timesonc2": " 0",
    "lockedtime": " 0.000002739"




   Task:  26

    
    "id": " 26",
    "basecpu": " 1",
    "priority": " 5",
    "period": 135000.0,
    "C(LO)": 1463.0,
    "C(HI)": 2926.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 97",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002447514",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.825299904",
    "avgresponsejitter": " 0.000785544",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 100",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  27

    
    "id": " 27",
    "basecpu": " 1",
    "priority": " 4",
    "period": 140000.0,
    "C(LO)": 903.0,
    "C(HI)": 1806.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 93",
    "preemptions": " 3",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001616462",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.742251610",
    "avgresponsejitter": " 0.000469622",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 95",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  20

    
    "id": " 20",
    "basecpu": " 1",
    "priority": " 7",
    "period": 101250.0,
    "C(LO)": 344.0,
    "C(HI)": 689.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 128",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000430192",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.763642976",
    "avgresponsejitter": " 0.000177402",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 129",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  28

    
    "id": " 28",
    "basecpu": " 1",
    "priority": " 3",
    "period": 141750.0,
    "C(LO)": 407.0,
    "C(HI)": 815.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 92",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001804766",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.763802045",
    "avgresponsejitter": " 0.000229327",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 94",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  24

    
    "id": " 24",
    "basecpu": " 1",
    "priority": " 8",
    "period": 126000.0,
    "C(LO)": 21252.0,
    "C(HI)": 21252.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 103",
    "preemptions": " 100",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.016981117",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.726006045",
    "avgresponsejitter": " 0.011094321",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 202",
    "timesonc2": " 0",
    "lockedtime": " 0.000017426"




   Task:  18

    
    "id": " 18",
    "basecpu": " 1",
    "priority": " 12",
    "period": 94500.0,
    "C(LO)": 6327.0,
    "C(HI)": 6327.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 137",
    "preemptions": " 30",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006694405",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.758341610",
    "avgresponsejitter": " 0.003321568",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 166",
    "timesonc2": " 0",
    "lockedtime": " 0.000000408"




   Task:  21

    
    "id": " 21",
    "basecpu": " 1",
    "priority": " 11",
    "period": 108000.0,
    "C(LO)": 7148.0,
    "C(HI)": 7148.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 120",
    "preemptions": " 10",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005832814",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.744006156",
    "avgresponsejitter": " 0.003634601",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 129",
    "timesonc2": " 0",
    "lockedtime": " 0.000002655"




   Task:  14

    
    "id": " 14",
    "basecpu": " 1",
    "priority": " 13",
    "period": 70000.0,
    "C(LO)": 4487.0,
    "C(HI)": 4487.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 185",
    "preemptions": " 16",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004050781",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.810006598",
    "avgresponsejitter": " 0.002324664",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 200",
    "timesonc2": " 0",
    "lockedtime": " 0.000009532"




   Task:  11

    
    "id": " 11",
    "basecpu": " 1",
    "priority": " 15",
    "period": 60480.0,
    "C(LO)": 3161.0,
    "C(HI)": 3161.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 214",
    "preemptions": " 18",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002442276",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.825291033",
    "avgresponsejitter": " 0.001629676",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 0",
    "timesonc1": " 230",
    "timesonc2": " 1",
    "lockedtime": " 0.000009679"




   Task:  1

    
    "id": " 1",
    "basecpu": " 1",
    "priority": " 17",
    "period": 20000.0,
    "C(LO)": 546.0,
    "C(HI)": 546.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 643",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000289393",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.825006895",
    "avgresponsejitter": " 0.000277399",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 0",
    "timesonc1": " 641",
    "timesonc2": " 1",
    "lockedtime": " 0.000008601"




   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 16",
    "period": 47250.0,
    "C(LO)": 1035.0,
    "C(HI)": 1035.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 273",
    "preemptions": " 8",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000825925",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.804756637",
    "avgresponsejitter": " 0.000537204",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 0",
    "timesonc1": " 280",
    "timesonc2": " 0",
    "lockedtime": " 0.000004679"




   Task:  22

    
    "id": " 22",
    "basecpu": " 1",
    "priority": " 10",
    "period": 118125.0,
    "C(LO)": 1554.0,
    "C(HI)": 1554.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 110",
    "preemptions": " 10",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002791216",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.762901538",
    "avgresponsejitter": " 0.000841628",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 119",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  13

    
    "id": " 13",
    "basecpu": " 1",
    "priority": " 14",
    "period": 67500.0,
    "C(LO)": 490.0,
    "C(HI)": 490.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 192",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000293261",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.825008051",
    "avgresponsejitter": " 0.000247547",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 191",
    "timesonc2": " 0",
    "lockedtime": " 0.000004441"




   Task:  23

    
    "id": " 23",
    "basecpu": " 1",
    "priority": " 9",
    "period": 120000.0,
    "C(LO)": 522.0,
    "C(HI)": 522.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 108",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000311802",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.720290946",
    "avgresponsejitter": " 0.000257162",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 107",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  31

    
    "id": " 31",
    "basecpu": " 2",
    "priority": " 1",
    "period": 157500.0,
    "C(LO)": 15260.0,
    "C(HI)": 30521.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 83",
    "preemptions": " 106",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.022791429",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.762498165",
    "avgresponsejitter": " 0.009580072",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 189",
    "lockedtime": " 0.000003673"




   Task:  29

    
    "id": " 29",
    "basecpu": " 2",
    "priority": " 3",
    "period": 150000.0,
    "C(LO)": 6102.0,
    "C(HI)": 12205.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 87",
    "preemptions": " 54",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.012184120",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.750005898",
    "avgresponsejitter": " 0.003610640",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 142",
    "lockedtime": " 0.000002024"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 9",
    "period": 22500.0,
    "C(LO)": 895.0,
    "C(HI)": 1791.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 572",
    "preemptions": " 13",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002212610",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.826919312",
    "avgresponsejitter": " 0.000460634",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 6",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 590",
    "lockedtime": " 0.000008144"




   Task:  30

    
    "id": " 30",
    "basecpu": " 2",
    "priority": " 2",
    "period": 151200.0,
    "C(LO)": 3924.9999999999995,
    "C(HI)": 7849.999999999999,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 86",
    "preemptions": " 25",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.010261877",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.711134204",
    "avgresponsejitter": " 0.002442910",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 112",
    "lockedtime": " 0.000000000"




   Task:  15

    
    "id": " 15",
    "basecpu": " 2",
    "priority": " 5",
    "period": 87500.0,
    "C(LO)": 791.0,
    "C(HI)": 1583.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 148",
    "preemptions": " 6",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001102393",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.775161489",
    "avgresponsejitter": " 0.000410093",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 155",
    "lockedtime": " 0.000000000"




   Task:  12

    
    "id": " 12",
    "basecpu": " 2",
    "priority": " 6",
    "period": 64800.0,
    "C(LO)": 380.0,
    "C(HI)": 761.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 199",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.013164979",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.765606345",
    "avgresponsejitter": " 0.000259189",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 201",
    "lockedtime": " 0.000005405"




   Task:  17

    
    "id": " 17",
    "basecpu": " 2",
    "priority": " 4",
    "period": 90720.0,
    "C(LO)": 261.0,
    "C(HI)": 523.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 143",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000361529",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.791525760",
    "avgresponsejitter": " 0.000137342",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 144",
    "lockedtime": " 0.000001489"




   Task:  3

    
    "id": " 3",
    "basecpu": " 2",
    "priority": " 8",
    "period": 25200.0,
    "C(LO)": 40.0,
    "C(HI)": 81.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 510",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000077682",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.801606342",
    "avgresponsejitter": " 0.000026901",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 7",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 517",
    "lockedtime": " 0.000006168"




   Task:  33

    
    "id": " 33",
    "basecpu": " 2",
    "priority": " 0",
    "period": 181440.0,
    "C(LO)": 233.0,
    "C(HI)": 466.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 72",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000316730",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.713625015",
    "avgresponsejitter": " 0.000124240",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 73",
    "lockedtime": " 0.000000000"




   Task:  19

    
    "id": " 19",
    "basecpu": " 2",
    "priority": " 7",
    "period": 100000.0,
    "C(LO)": 14778.0,
    "C(HI)": 14778.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 130",
    "preemptions": " 158",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.015839444",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.800005925",
    "avgresponsejitter": " 0.008377066",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 287",
    "lockedtime": " 0.000010213"




   Task:  9

    
    "id": " 9",
    "basecpu": " 2",
    "priority": " 12",
    "period": 52500.0,
    "C(LO)": 7245.0,
    "C(HI)": 7245.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 246",
    "preemptions": " 35",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005266435",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.810162225",
    "avgresponsejitter": " 0.003635075",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 280",
    "lockedtime": " 0.000003084"




   Task:  16

    
    "id": " 16",
    "basecpu": " 2",
    "priority": " 10",
    "period": 90000.0,
    "C(LO)": 5939.0,
    "C(HI)": 5939.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 144",
    "preemptions": " 20",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003687943",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.780006970",
    "avgresponsejitter": " 0.003027486",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 163",
    "lockedtime": " 0.000004667"




   Task:  10

    
    "id": " 10",
    "basecpu": " 2",
    "priority": " 11",
    "period": 54000.0,
    "C(LO)": 3151.0,
    "C(HI)": 3151.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 239",
    "preemptions": " 29",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006226766",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.798005760",
    "avgresponsejitter": " 0.001674967",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 267",
    "lockedtime": " 0.000009393"




   Task:  8

    
    "id": " 8",
    "basecpu": " 2",
    "priority": " 13",
    "period": 50000.0,
    "C(LO)": 1809.0,
    "C(HI)": 1809.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 206",
    "preemptions": " 6",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001154619",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 11.200008904",
    "avgresponsejitter": " 0.000925105",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 211",
    "lockedtime": " 0.000006411"




   Task:  5

    
    "id": " 5",
    "basecpu": " 2",
    "priority": " 15",
    "period": 28350.0,
    "C(LO)": 429.0,
    "C(HI)": 429.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 454",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000226709",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.814205760",
    "avgresponsejitter": " 0.000217021",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 1",
    "timesonc1": " 0",
    "timesonc2": " 453",
    "lockedtime": " 0.000003342"




   Task:  6

    
    "id": " 6",
    "basecpu": " 2",
    "priority": " 14",
    "period": 35000.0,
    "C(LO)": 284.0,
    "C(HI)": 284.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 368",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000149799",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 13.810007550",
    "avgresponsejitter": " 0.000147841",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 1",
    "timesonc1": " 0",
    "timesonc2": " 367",
    "lockedtime": " 0.000007198"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 16",
    "period": 26250.0,
    "C(LO)": 90.0,
    "C(HI)": 90.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 243",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000061174",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 7.326256267",
    "avgresponsejitter": " 0.000050315",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 242",
    "lockedtime": " 0.000001372"



   </details>



  9. Taskset **e4_semi2wf_t15546**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t15546",
    "size": "35",
    "utilization": "1.86",
    "realutilization": 1.9322569312169313,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 11",
    "hightolow": " 10",
    "idletime": 3643739,
    "util": 96.78682627865962




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 7",
    "hightolow": " 6",
    "idletime": 4038325,
    "util": 96.43886684303351




   Real Utilization: 1.9322569312169313
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  13

    
    "id": " 13",
    "basecpu": " 1",
    "priority": " 6",
    "period": 56700.0,
    "C(LO)": 4706.0,
    "C(HI)": 9413.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 102",
    "preemptions": " 27",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.008337279",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.679469763",
    "avgresponsejitter": " 0.002645435",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 128",
    "timesonc2": " 0",
    "lockedtime": " 0.000002781"




   Task:  12

    
    "id": " 12",
    "basecpu": " 1",
    "priority": " 7",
    "period": 54000.0,
    "C(LO)": 3523.0,
    "C(HI)": 7047.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 107",
    "preemptions": " 17",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005815556",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.677501778",
    "avgresponsejitter": " 0.001958192",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 4",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 127",
    "timesonc2": " 0",
    "lockedtime": " 0.000000838"




   Task:  26

    
    "id": " 26",
    "basecpu": " 1",
    "priority": " 3",
    "period": 118125.0,
    "C(LO)": 4723.0,
    "C(HI)": 9447.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 50",
    "preemptions": " 12",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004005417",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.682972823",
    "avgresponsejitter": " 0.002528201",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 61",
    "timesonc2": " 0",
    "lockedtime": " 0.000002724"




   Task:  30

    
    "id": " 30",
    "basecpu": " 1",
    "priority": " 2",
    "period": 140000.0,
    "C(LO)": 4448.0,
    "C(HI)": 8897.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 42",
    "preemptions": " 18",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007044790",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.601405691",
    "avgresponsejitter": " 0.002754282",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 59",
    "timesonc2": " 0",
    "lockedtime": " 0.000002246"




   Task:  11

    
    "id": " 11",
    "basecpu": " 1",
    "priority": " 8",
    "period": 52500.0,
    "C(LO)": 1293.0,
    "C(HI)": 2587.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 110",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001989222",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.675505514",
    "avgresponsejitter": " 0.000669156",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 111",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  9

    
    "id": " 9",
    "basecpu": " 1",
    "priority": " 9",
    "period": 47250.0,
    "C(LO)": 883.0,
    "C(HI)": 1766.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 122",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001334532",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.675059018",
    "avgresponsejitter": " 0.000460039",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 124",
    "timesonc2": " 0",
    "lockedtime": " 0.000002324"




   Task:  25

    
    "id": " 25",
    "basecpu": " 1",
    "priority": " 4",
    "period": 113400.0,
    "C(LO)": 1743.0,
    "C(HI)": 3487.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 52",
    "preemptions": " 8",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002728153",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.682178177",
    "avgresponsejitter": " 0.001010811",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 59",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  20

    
    "id": " 20",
    "basecpu": " 1",
    "priority": " 5",
    "period": 84000.0,
    "C(LO)": 1111.0,
    "C(HI)": 2223.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 69",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001908240",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.628005979",
    "avgresponsejitter": " 0.000653369",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 4",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 74",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  31

    
    "id": " 31",
    "basecpu": " 1",
    "priority": " 1",
    "period": 141750.0,
    "C(LO)": 132.0,
    "C(HI)": 264.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 42",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000084931",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.685780126",
    "avgresponsejitter": " 0.000067195",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 41",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  35

    
    "id": " 35",
    "basecpu": " 1",
    "priority": " 0",
    "period": 810000.0,
    "C(LO)": 118782.0,
    "C(HI)": 118782.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 8",
    "preemptions": " 104",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.091076297",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 5.864963105",
    "avgresponsejitter": " 0.077604796",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 111",
    "timesonc2": " 0",
    "lockedtime": " 0.000010922"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 18",
    "period": 25200.0,
    "C(LO)": 2225.0,
    "C(HI)": 2225.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 228",
    "preemptions": " 9",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001401084",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.695552018",
    "avgresponsejitter": " 0.001137168",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 1",
    "timesonc1": " 234",
    "timesonc2": " 2",
    "lockedtime": " 0.000001556"




   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 17",
    "period": 35000.0,
    "C(LO)": 1446.0,
    "C(HI)": 1446.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 165",
    "preemptions": " 6",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000842087",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.707900303",
    "avgresponsejitter": " 0.000737970",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 0",
    "timesonc1": " 169",
    "timesonc2": " 1",
    "lockedtime": " 0.000001075"




   Task:  21

    
    "id": " 21",
    "basecpu": " 1",
    "priority": " 14",
    "period": 84375.0,
    "C(LO)": 2403.0,
    "C(HI)": 2403.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 69",
    "preemptions": " 7",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003258258",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.653131096",
    "avgresponsejitter": " 0.001282114",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 75",
    "timesonc2": " 0",
    "lockedtime": " 0.000000646"




   Task:  4

    
    "id": " 4",
    "basecpu": " 1",
    "priority": " 19",
    "period": 22500.0,
    "C(LO)": 478.0,
    "C(HI)": 478.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 255",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000248991",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.695301817",
    "avgresponsejitter": " 0.000246802",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 2",
    "timesrestored": " 1",
    "timesonc1": " 253",
    "timesonc2": " 1",
    "lockedtime": " 0.000000255"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 16",
    "period": 45000.0,
    "C(LO)": 793.0,
    "C(HI)": 793.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 128",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000470721",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.672236661",
    "avgresponsejitter": " 0.000399541",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 127",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  34

    
    "id": " 34",
    "basecpu": " 1",
    "priority": " 10",
    "period": 189000.0,
    "C(LO)": 3235.0,
    "C(HI)": 3235.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 32",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001915378",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.673137318",
    "avgresponsejitter": " 0.001601709",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 31",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  19

    
    "id": " 19",
    "basecpu": " 1",
    "priority": " 15",
    "period": 72000.0,
    "C(LO)": 875.0,
    "C(HI)": 875.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 81",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000519688",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.688007186",
    "avgresponsejitter": " 0.000440429",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 80",
    "timesonc2": " 0",
    "lockedtime": " 0.000000396"




   Task:  23

    
    "id": " 23",
    "basecpu": " 1",
    "priority": " 12",
    "period": 100000.0,
    "C(LO)": 1199.0,
    "C(HI)": 1199.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 59",
    "preemptions": " 4",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001853961",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.700008027",
    "avgresponsejitter": " 0.000639396",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 62",
    "timesonc2": " 0",
    "lockedtime": " 0.000001402"




   Task:  22

    
    "id": " 22",
    "basecpu": " 1",
    "priority": " 13",
    "period": 90000.0,
    "C(LO)": 917.0,
    "C(HI)": 917.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 65",
    "preemptions": " 3",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000603048",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.672690580",
    "avgresponsejitter": " 0.000450721",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 67",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  2

    
    "id": " 2",
    "basecpu": " 1",
    "priority": " 20",
    "period": 18900.0,
    "C(LO)": 169.0,
    "C(HI)": 169.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 304",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000098426",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.707805937",
    "avgresponsejitter": " 0.000088366",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 1",
    "timesrestored": " 0",
    "timesonc1": " 301",
    "timesonc2": " 2",
    "lockedtime": " 0.000001898"




   Task:  33

    
    "id": " 33",
    "basecpu": " 1",
    "priority": " 11",
    "period": 180000.0,
    "C(LO)": 1160.0,
    "C(HI)": 1160.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 33",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000697598",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.581119862",
    "avgresponsejitter": " 0.000591255",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 32",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  32

    
    "id": " 32",
    "basecpu": " 2",
    "priority": " 0",
    "period": 168000.0,
    "C(LO)": 19704.0,
    "C(HI)": 39409.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 35",
    "preemptions": " 73",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.018007526",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.553211363",
    "avgresponsejitter": " 0.011338084",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 107",
    "lockedtime": " 0.000005832"




   Task:  18

    
    "id": " 18",
    "basecpu": " 2",
    "priority": " 2",
    "period": 70875.0,
    "C(LO)": 3246.0,
    "C(HI)": 6493.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 82",
    "preemptions": " 10",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004273973",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.676852775",
    "avgresponsejitter": " 0.001700835",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 91",
    "lockedtime": " 0.000000372"




   Task:  16

    
    "id": " 16",
    "basecpu": " 2",
    "priority": " 4",
    "period": 64800.0,
    "C(LO)": 2111.0,
    "C(HI)": 4222.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 90",
    "preemptions": " 12",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003811378",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.702406652",
    "avgresponsejitter": " 0.001151820",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 103",
    "lockedtime": " 0.000000000"




   Task:  17

    
    "id": " 17",
    "basecpu": " 2",
    "priority": " 3",
    "period": 65625.0,
    "C(LO)": 2027.9999999999998,
    "C(HI)": 4057.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 88",
    "preemptions": " 12",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003865640",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.643755760",
    "avgresponsejitter": " 0.001097318",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 100",
    "lockedtime": " 0.000001084"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 10",
    "period": 15750.0,
    "C(LO)": 387.0,
    "C(HI)": 774.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 364",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000523976",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.701505859",
    "avgresponsejitter": " 0.000196601",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 364",
    "lockedtime": " 0.000007138"




   Task:  3

    
    "id": " 3",
    "basecpu": " 2",
    "priority": " 9",
    "period": 20000.0,
    "C(LO)": 365.0,
    "C(HI)": 731.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 287",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000510081",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.700006904",
    "avgresponsejitter": " 0.000189411",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 288",
    "lockedtime": " 0.000004093"




   Task:  6

    
    "id": " 6",
    "basecpu": " 2",
    "priority": " 6",
    "period": 28350.0,
    "C(LO)": 392.0,
    "C(HI)": 785.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 203",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000543078",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.699327955",
    "avgresponsejitter": " 0.000200387",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 205",
    "lockedtime": " 0.000001964"




   Task:  14

    
    "id": " 14",
    "basecpu": " 2",
    "priority": " 5",
    "period": 60000.0,
    "C(LO)": 434.0,
    "C(HI)": 869.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 97",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000434958",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.700215252",
    "avgresponsejitter": " 0.000219429",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 97",
    "lockedtime": " 0.000000000"




   Task:  28

    
    "id": " 28",
    "basecpu": " 2",
    "priority": " 1",
    "period": 129600.0,
    "C(LO)": 833.0,
    "C(HI)": 1667.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 46",
    "preemptions": " 6",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001312841",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.703605619",
    "avgresponsejitter": " 0.000454559",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 51",
    "lockedtime": " 0.000000000"




   Task:  10

    
    "id": " 10",
    "basecpu": " 2",
    "priority": " 13",
    "period": 50400.0,
    "C(LO)": 5205.0,
    "C(HI)": 5205.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 115",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002669565",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.696679514",
    "avgresponsejitter": " 0.002636910",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 114",
    "lockedtime": " 0.000010309"




   Task:  27

    
    "id": " 27",
    "basecpu": " 2",
    "priority": " 8",
    "period": 126000.0,
    "C(LO)": 12587.0,
    "C(HI)": 12587.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 47",
    "preemptions": " 17",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007718147",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.670612474",
    "avgresponsejitter": " 0.006550736",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 63",
    "lockedtime": " 0.000001754"




   Task:  24

    
    "id": " 24",
    "basecpu": " 2",
    "priority": " 11",
    "period": 108000.0,
    "C(LO)": 5740.0,
    "C(HI)": 5740.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 54",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003438673",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.616006009",
    "avgresponsejitter": " 0.002864868",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 53",
    "lockedtime": " 0.000001943"




   Task:  15

    
    "id": " 15",
    "basecpu": " 2",
    "priority": " 12",
    "period": 63000.0,
    "C(LO)": 702.0,
    "C(HI)": 702.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 92",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000360997",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.670011216",
    "avgresponsejitter": " 0.000354961",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 91",
    "lockedtime": " 0.000000408"




   Task:  29

    
    "id": " 29",
    "basecpu": " 2",
    "priority": " 7",
    "period": 135000.0,
    "C(LO)": 292.0,
    "C(HI)": 292.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 44",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000172006",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 6.676519673",
    "avgresponsejitter": " 0.000143261",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 43",
    "lockedtime": " 0.000001132"



   </details>



  10. Taskset **e4_semi2wf_t15922**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t15922",
    "size": "35",
    "utilization": "1.9080000000000001",
    "realutilization": 1.6231884038800706,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 113400000,
    "lowtohigh": " 35",
    "hightolow": " 34",
    "idletime": 21512960,
    "util": 81.02913580246914




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 48",
    "hightolow": " 47",
    "idletime": 21217475,
    "util": 81.28970458553792




   Real Utilization: 1.6231884038800706
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  11

    
    "id": " 11",
    "basecpu": " 1",
    "priority": " 7",
    "period": 50400.0,
    "C(LO)": 2616.0,
    "C(HI)": 5233.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 647",
    "preemptions": " 71",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.008700847",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.509301297",
    "avgresponsejitter": " 0.001520817",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 10",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 727",
    "timesonc2": " 0",
    "lockedtime": " 0.000004556"




   Task:  33

    
    "id": " 33",
    "basecpu": " 1",
    "priority": " 1",
    "period": 196875.0,
    "C(LO)": 10219.0,
    "C(HI)": 20439.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 167",
    "preemptions": " 151",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.017130420",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.484381225",
    "avgresponsejitter": " 0.006091255",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 317",
    "timesonc2": " 0",
    "lockedtime": " 0.000010877"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 8",
    "period": 45360.0,
    "C(LO)": 2058.0,
    "C(HI)": 4116.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 718",
    "preemptions": " 67",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007092526",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.477768051",
    "avgresponsejitter": " 0.001223985",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 9",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 793",
    "timesonc2": " 0",
    "lockedtime": " 0.000006060"




   Task:  34

    
    "id": " 34",
    "basecpu": " 1",
    "priority": " 0",
    "period": 405000.0,
    "C(LO)": 14630.0,
    "C(HI)": 29260.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 82",
    "preemptions": " 106",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.017394324",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.403936946",
    "avgresponsejitter": " 0.009239009",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 187",
    "timesonc2": " 0",
    "lockedtime": " 0.000004288"




   Task:  26

    
    "id": " 26",
    "basecpu": " 1",
    "priority": " 5",
    "period": 131250.0,
    "C(LO)": 4549.0,
    "C(HI)": 9098.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 249",
    "preemptions": " 87",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007257276",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.421204228",
    "avgresponsejitter": " 0.002605769",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 337",
    "timesonc2": " 0",
    "lockedtime": " 0.000003249"




   Task:  28

    
    "id": " 28",
    "basecpu": " 1",
    "priority": " 4",
    "period": 151200.0,
    "C(LO)": 3827.0,
    "C(HI)": 7655.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 217",
    "preemptions": " 41",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007378595",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.510769874",
    "avgresponsejitter": " 0.002299036",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 258",
    "timesonc2": " 0",
    "lockedtime": " 0.000003369"




   Task:  32

    
    "id": " 32",
    "basecpu": " 1",
    "priority": " 2",
    "period": 181440.0,
    "C(LO)": 2025.0,
    "C(HI)": 4051.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 181",
    "preemptions": " 26",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005497529",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.478983321",
    "avgresponsejitter": " 0.001252658",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 209",
    "timesonc2": " 0",
    "lockedtime": " 0.000001931"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 9",
    "period": 28350.0,
    "C(LO)": 223.0,
    "C(HI)": 446.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1149",
    "preemptions": " 9",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003871264",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.517455997",
    "avgresponsejitter": " 0.000124345",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 5",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1162",
    "timesonc2": " 0",
    "lockedtime": " 0.000004604"




   Task:  31

    
    "id": " 31",
    "basecpu": " 1",
    "priority": " 3",
    "period": 175000.0,
    "C(LO)": 919.0,
    "C(HI)": 1838.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 187",
    "preemptions": " 11",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001815060",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.375006312",
    "avgresponsejitter": " 0.000494216",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 198",
    "timesonc2": " 0",
    "lockedtime": " 0.000000366"




   Task:  24

    
    "id": " 24",
    "basecpu": " 1",
    "priority": " 6",
    "period": 108000.0,
    "C(LO)": 548.0,
    "C(HI)": 1096.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 303",
    "preemptions": " 4",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003111471",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.510459102",
    "avgresponsejitter": " 0.000303595",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 4",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 310",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  5

    
    "id": " 5",
    "basecpu": " 1",
    "priority": " 17",
    "period": 26250.0,
    "C(LO)": 4448.0,
    "C(HI)": 4448.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1241",
    "preemptions": " 114",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002904763",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.523756574",
    "avgresponsejitter": " 0.002250393",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 1354",
    "timesonc2": " 0",
    "lockedtime": " 0.000024306"




   Task:  12

    
    "id": " 12",
    "basecpu": " 1",
    "priority": " 14",
    "period": 52500.0,
    "C(LO)": 2677.0,
    "C(HI)": 2677.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 621",
    "preemptions": " 46",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003117231",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.500636384",
    "avgresponsejitter": " 0.001389222",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 666",
    "timesonc2": " 0",
    "lockedtime": " 0.000001018"




   Task:  27

    
    "id": " 27",
    "basecpu": " 1",
    "priority": " 10",
    "period": 150000.0,
    "C(LO)": 6010.0,
    "C(HI)": 6010.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 218",
    "preemptions": " 59",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007964868",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.401008492",
    "avgresponsejitter": " 0.003340174",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 276",
    "timesonc2": " 0",
    "lockedtime": " 0.000007441"




   Task:  7

    
    "id": " 7",
    "basecpu": " 1",
    "priority": " 16",
    "period": 37800.0,
    "C(LO)": 1289.0,
    "C(HI)": 1289.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 862",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000774069",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.508257168",
    "avgresponsejitter": " 0.000642736",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 861",
    "timesonc2": " 0",
    "lockedtime": " 0.000000847"




   Task:  14

    
    "id": " 14",
    "basecpu": " 1",
    "priority": " 12",
    "period": 56700.0,
    "C(LO)": 1917.0,
    "C(HI)": 1917.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 575",
    "preemptions": " 39",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005415384",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.489354120",
    "avgresponsejitter": " 0.001070925",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 613",
    "timesonc2": " 0",
    "lockedtime": " 0.000001562"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 18",
    "period": 18900.0,
    "C(LO)": 473.0,
    "C(HI)": 473.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1723",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000250922",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.526906453",
    "avgresponsejitter": " 0.000239550",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 3",
    "timesrestored": " 3",
    "timesonc1": " 1721",
    "timesonc2": " 1",
    "lockedtime": " 0.000010892"




   Task:  10

    
    "id": " 10",
    "basecpu": " 1",
    "priority": " 15",
    "period": 50000.0,
    "C(LO)": 1150.0,
    "C(HI)": 1150.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 652",
    "preemptions": " 23",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004038709",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.500030793",
    "avgresponsejitter": " 0.000601420",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 674",
    "timesonc2": " 0",
    "lockedtime": " 0.000017625"




   Task:  13

    
    "id": " 13",
    "basecpu": " 1",
    "priority": " 13",
    "period": 54000.0,
    "C(LO)": 605.0,
    "C(HI)": 605.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 604",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000579192",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.509036285",
    "avgresponsejitter": " 0.000305949",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 604",
    "timesonc2": " 0",
    "lockedtime": " 0.000014354"




   Task:  18

    
    "id": " 18",
    "basecpu": " 1",
    "priority": " 11",
    "period": 67500.0,
    "C(LO)": 142.0,
    "C(HI)": 142.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 483",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000093135",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.467506745",
    "avgresponsejitter": " 0.000075465",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 482",
    "timesonc2": " 0",
    "lockedtime": " 0.000004009"




   Task:  35

    
    "id": " 35",
    "basecpu": " 2",
    "priority": " 0",
    "period": 450000.0,
    "C(LO)": 63826.99999999999,
    "C(HI)": 127654.99999999999,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 73",
    "preemptions": " 508",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.061767631",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 32.952403937",
    "avgresponsejitter": " 0.040664619",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 580",
    "lockedtime": " 0.000023033"




   Task:  15

    
    "id": " 15",
    "basecpu": " 2",
    "priority": " 5",
    "period": 60480.0,
    "C(LO)": 2510.0,
    "C(HI)": 5021.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 539",
    "preemptions": " 110",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.010153420",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.477766502",
    "avgresponsejitter": " 0.001440255",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 5",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 653",
    "lockedtime": " 0.000010495"




   Task:  30

    
    "id": " 30",
    "basecpu": " 2",
    "priority": " 1",
    "period": 168000.0,
    "C(LO)": 5999.0,
    "C(HI)": 11998.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 195",
    "preemptions": " 84",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.010440129",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.424006351",
    "avgresponsejitter": " 0.003271877",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 279",
    "lockedtime": " 0.000001489"




   Task:  20

    
    "id": " 20",
    "basecpu": " 2",
    "priority": " 4",
    "period": 81000.0,
    "C(LO)": 2099.0,
    "C(HI)": 4198.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 403",
    "preemptions": " 70",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005324772",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.481006468",
    "avgresponsejitter": " 0.001178760",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 474",
    "lockedtime": " 0.000004033"




   Task:  1

    
    "id": " 1",
    "basecpu": " 2",
    "priority": " 10",
    "period": 10000.0,
    "C(LO)": 236.0,
    "C(HI)": 472.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 3254",
    "preemptions": " 11",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003825733",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.520586438",
    "avgresponsejitter": " 0.000124529",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 35",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 3299",
    "lockedtime": " 0.000029862"




   Task:  25

    
    "id": " 25",
    "basecpu": " 2",
    "priority": " 2",
    "period": 120000.0,
    "C(LO)": 627.0,
    "C(HI)": 1254.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 273",
    "preemptions": " 18",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003394210",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.520729964",
    "avgresponsejitter": " 0.000393342",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 292",
    "lockedtime": " 0.000000384"




   Task:  23

    
    "id": " 23",
    "basecpu": " 2",
    "priority": " 3",
    "period": 100000.0,
    "C(LO)": 271.0,
    "C(HI)": 542.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 327",
    "preemptions": " 5",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007811823",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.500693441",
    "avgresponsejitter": " 0.000175979",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 334",
    "lockedtime": " 0.000000541"




   Task:  9

    
    "id": " 9",
    "basecpu": " 2",
    "priority": " 13",
    "period": 47250.0,
    "C(LO)": 5114.0,
    "C(HI)": 5114.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 690",
    "preemptions": " 84",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003584273",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.508008060",
    "avgresponsejitter": " 0.002632778",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 773",
    "lockedtime": " 0.000015682"




   Task:  29

    
    "id": " 29",
    "basecpu": " 2",
    "priority": " 6",
    "period": 162000.0,
    "C(LO)": 15701.0,
    "C(HI)": 15701.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 202",
    "preemptions": " 271",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.013035009",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.404665183",
    "avgresponsejitter": " 0.008949682",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 472",
    "lockedtime": " 0.000013483"




   Task:  4

    
    "id": " 4",
    "basecpu": " 2",
    "priority": " 14",
    "period": 20000.0,
    "C(LO)": 977.0,
    "C(HI)": 977.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 1628",
    "preemptions": " 27",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000846919",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.520008348",
    "avgresponsejitter": " 0.000492904",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1654",
    "lockedtime": " 0.000018078"




   Task:  22

    
    "id": " 22",
    "basecpu": " 2",
    "priority": " 7",
    "period": 90000.0,
    "C(LO)": 3530.0,
    "C(HI)": 3530.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 363",
    "preemptions": " 17",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005913345",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.490116447",
    "avgresponsejitter": " 0.001824637",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 379",
    "lockedtime": " 0.000001225"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 15",
    "period": 15750.0,
    "C(LO)": 494.0,
    "C(HI)": 494.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 1374",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000266754",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.609007369",
    "avgresponsejitter": " 0.000254571",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 7",
    "timesrestored": " 6",
    "timesonc1": " 11",
    "timesonc2": " 1362",
    "lockedtime": " 0.000024150"




   Task:  21

    
    "id": " 21",
    "basecpu": " 2",
    "priority": " 8",
    "period": 84375.0,
    "C(LO)": 2309.0,
    "C(HI)": 2309.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 387",
    "preemptions": " 57",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002362814",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.484382291",
    "avgresponsejitter": " 0.001210553",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 443",
    "lockedtime": " 0.000009081"




   Task:  17

    
    "id": " 17",
    "basecpu": " 2",
    "priority": " 11",
    "period": 64800.0,
    "C(LO)": 1400.0,
    "C(HI)": 1400.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 503",
    "preemptions": " 15",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001390784",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.464806399",
    "avgresponsejitter": " 0.000710348",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 517",
    "lockedtime": " 0.000002544"




   Task:  19

    
    "id": " 19",
    "basecpu": " 2",
    "priority": " 9",
    "period": 75000.0,
    "C(LO)": 1607.0,
    "C(HI)": 1607.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 435",
    "preemptions": " 17",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003994709",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.475006535",
    "avgresponsejitter": " 0.000851631",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 451",
    "lockedtime": " 0.000002315"




   Task:  16

    
    "id": " 16",
    "basecpu": " 2",
    "priority": " 12",
    "period": 63000.0,
    "C(LO)": 1304.0,
    "C(HI)": 1304.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 518",
    "preemptions": " 8",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001351345",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 33.510599363",
    "avgresponsejitter": " 0.000661625",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 525",
    "lockedtime": " 0.000003402"



   </details>



  11. Taskset **e4_semi2wf_t16141**

    Taskset execution params:
	 
    "id": "e4_semi2wf_t16141",
    "size": "35",
    "utilization": "1.9320000000000002",
    "realutilization": 1.7519806613756612,
    "criticality_factor": "2",
    "hicrit_proportion": "0.5"


   <details> <summary markdown="span">Click here to see the CPUs log.</summary>

   Idle time is expressed as **seconds**.

   Util values are expressed as **percentage** %.



   CPU: 1

    
    "id": 1,
    "hyperperiod": 56700000,
    "lowtohigh": " 31",
    "hightolow": " 30",
    "idletime": 14135313,
    "util": 87.53499735449735




   CPU: 2

    
    "id": 2,
    "hyperperiod": 113400000,
    "lowtohigh": " 28",
    "hightolow": " 27",
    "idletime": 13990080,
    "util": 87.66306878306878




   Real Utilization: 1.7519806613756612
   </details>

   <details> <summary markdown="span">Click here to see the whole tasksets.</summary>

   Time values are expressed as **micro-seconds**.



   Task:  34

    
    "id": " 34",
    "basecpu": " 1",
    "priority": " 0",
    "period": 540000.0,
    "C(LO)": 45504.0,
    "C(HI)": 91008.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 41",
    "preemptions": " 220",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.048666345",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.061140694",
    "avgresponsejitter": " 0.030463300",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 260",
    "timesonc2": " 0",
    "lockedtime": " 0.000006333"




   Task:  33

    
    "id": " 33",
    "basecpu": " 1",
    "priority": " 1",
    "period": 196875.0,
    "C(LO)": 13854.0,
    "C(HI)": 27708.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 109",
    "preemptions": " 141",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.018419568",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.065631766",
    "avgresponsejitter": " 0.008405405",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 249",
    "timesonc2": " 0",
    "lockedtime": " 0.000010568"




   Task:  11

    
    "id": " 11",
    "basecpu": " 1",
    "priority": " 4",
    "period": 52500.0,
    "C(LO)": 2367.0,
    "C(HI)": 4734.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 407",
    "preemptions": " 69",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007524210",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.265259523",
    "avgresponsejitter": " 0.001386105",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 7",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 482",
    "timesonc2": " 0",
    "lockedtime": " 0.000004258"




   Task:  8

    
    "id": " 8",
    "basecpu": " 1",
    "priority": " 7",
    "period": 45360.0,
    "C(LO)": 1677.0,
    "C(HI)": 3355.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 470",
    "preemptions": " 56",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006112177",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.229520282",
    "avgresponsejitter": " 0.000972700",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 528",
    "timesonc2": " 0",
    "lockedtime": " 0.000000718"




   Task:  12

    
    "id": " 12",
    "basecpu": " 1",
    "priority": " 3",
    "period": 60000.0,
    "C(LO)": 1824.0,
    "C(HI)": 3649.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 356",
    "preemptions": " 32",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004213489",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.240132231",
    "avgresponsejitter": " 0.001007649",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 389",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  9

    
    "id": " 9",
    "basecpu": " 1",
    "priority": " 6",
    "period": 50000.0,
    "C(LO)": 717.0,
    "C(HI)": 1434.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 427",
    "preemptions": " 18",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003775282",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.250131435",
    "avgresponsejitter": " 0.000419438",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 447",
    "timesonc2": " 0",
    "lockedtime": " 0.000000402"




   Task:  10

    
    "id": " 10",
    "basecpu": " 1",
    "priority": " 5",
    "period": 50400.0,
    "C(LO)": 572.0,
    "C(HI)": 1144.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 424",
    "preemptions": " 16",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004861538",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.269915847",
    "avgresponsejitter": " 0.000314538",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 6",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 445",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  6

    
    "id": " 6",
    "basecpu": " 1",
    "priority": " 8",
    "period": 35000.0,
    "C(LO)": 204.0,
    "C(HI)": 408.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 609",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000965862",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.245006009",
    "avgresponsejitter": " 0.000106252",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 6",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 615",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  28

    
    "id": " 28",
    "basecpu": " 1",
    "priority": " 2",
    "period": 135000.0,
    "C(LO)": 278.0,
    "C(HI)": 557.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 159",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000384907",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.195006069",
    "avgresponsejitter": " 0.000149072",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 4",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 162",
    "timesonc2": " 0",
    "lockedtime": " 0.000000309"




   Task:  20

    
    "id": " 20",
    "basecpu": " 1",
    "priority": " 12",
    "period": 100000.0,
    "C(LO)": 7651.0,
    "C(HI)": 7651.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 214",
    "preemptions": " 54",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006638703",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.200134243",
    "avgresponsejitter": " 0.004105793",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 267",
    "timesonc2": " 0",
    "lockedtime": " 0.000001766"




   Task:  3

    
    "id": " 3",
    "basecpu": " 1",
    "priority": " 15",
    "period": 25200.0,
    "C(LO)": 1877.0,
    "C(HI)": 1877.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 846",
    "preemptions": " 61",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001240339",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.268807868",
    "avgresponsejitter": " 0.000953381",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 906",
    "timesonc2": " 0",
    "lockedtime": " 0.000026883"




   Task:  4

    
    "id": " 4",
    "basecpu": " 1",
    "priority": " 14",
    "period": 30240.0,
    "C(LO)": 2137.0,
    "C(HI)": 2137.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 705",
    "preemptions": " 75",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001414420",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.258726186",
    "avgresponsejitter": " 0.001088757",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 779",
    "timesonc2": " 0",
    "lockedtime": " 0.000006492"




   Task:  21

    
    "id": " 21",
    "basecpu": " 1",
    "priority": " 11",
    "period": 105000.0,
    "C(LO)": 4489.0,
    "C(HI)": 4489.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 204",
    "preemptions": " 22",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.003861565",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.210134480",
    "avgresponsejitter": " 0.002359054",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 225",
    "timesonc2": " 0",
    "lockedtime": " 0.000001532"




   Task:  18

    
    "id": " 18",
    "basecpu": " 1",
    "priority": " 13",
    "period": 87500.0,
    "C(LO)": 3247.0,
    "C(HI)": 3247.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 245",
    "preemptions": " 27",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.004026024",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.262509402",
    "avgresponsejitter": " 0.001742646",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 271",
    "timesonc2": " 0",
    "lockedtime": " 0.000003150"




   Task:  1

    
    "id": " 1",
    "basecpu": " 1",
    "priority": " 16",
    "period": 10000.0,
    "C(LO)": 219.0,
    "C(HI)": 219.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 2128",
    "preemptions": " 1",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000130048",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.260005979",
    "avgresponsejitter": " 0.000118309",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 6",
    "timesrestored": " 4",
    "timesonc1": " 2122",
    "timesonc2": " 6",
    "lockedtime": " 0.000006955"




   Task:  26

    
    "id": " 26",
    "basecpu": " 1",
    "priority": " 9",
    "period": 126000.0,
    "C(LO)": 2400.0,
    "C(HI)": 2400.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 170",
    "preemptions": " 26",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005803670",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.169927661",
    "avgresponsejitter": " 0.001287526",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 195",
    "timesonc2": " 0",
    "lockedtime": " 0.000000000"




   Task:  25

    
    "id": " 25",
    "basecpu": " 1",
    "priority": " 10",
    "period": 118125.0,
    "C(LO)": 1707.0,
    "C(HI)": 1707.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 182",
    "preemptions": " 18",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006252255",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.264283375",
    "avgresponsejitter": " 0.000949201",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 199",
    "timesonc2": " 0",
    "lockedtime": " 0.000004471"




   Task:  35

    
    "id": " 35",
    "basecpu": " 2",
    "priority": " 0",
    "period": 945000.0,
    "C(LO)": 82887.0,
    "C(HI)": 165775.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 24",
    "preemptions": " 179",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.076905081",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 21.794418390",
    "avgresponsejitter": " 0.054370700",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 202",
    "lockedtime": " 0.000007736"




   Task:  5

    
    "id": " 5",
    "basecpu": " 2",
    "priority": " 9",
    "period": 33750.0,
    "C(LO)": 2075.0,
    "C(HI)": 4150.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 632",
    "preemptions": " 11",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.007173910",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.264611171",
    "avgresponsejitter": " 0.001103447",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 9",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 651",
    "lockedtime": " 0.000006273"




   Task:  23

    
    "id": " 23",
    "basecpu": " 2",
    "priority": " 2",
    "period": 112500.0,
    "C(LO)": 5376.0,
    "C(HI)": 10753.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 191",
    "preemptions": " 59",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.016527132",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.265768366",
    "avgresponsejitter": " 0.003297111",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 3",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 252",
    "lockedtime": " 0.000002781"




   Task:  2

    
    "id": " 2",
    "basecpu": " 2",
    "priority": " 10",
    "period": 18900.0,
    "C(LO)": 839.0,
    "C(HI)": 1678.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 1127",
    "preemptions": " 13",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001622081",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.264172694",
    "avgresponsejitter": " 0.000432646",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 10",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 1149",
    "lockedtime": " 0.000008078"




   Task:  32

    
    "id": " 32",
    "basecpu": " 2",
    "priority": " 1",
    "period": 157500.0,
    "C(LO)": 3789.0,
    "C(HI)": 7579.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 136",
    "preemptions": " 22",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006867541",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.105738291",
    "avgresponsejitter": " 0.002114315",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 159",
    "lockedtime": " 0.000000751"




   Task:  15

    
    "id": " 15",
    "basecpu": " 2",
    "priority": " 5",
    "period": 72000.0,
    "C(LO)": 1213.0,
    "C(HI)": 2426.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 297",
    "preemptions": " 7",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006480622",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.240005892",
    "avgresponsejitter": " 0.000648769",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 2",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 305",
    "lockedtime": " 0.000000607"




   Task:  22

    
    "id": " 22",
    "basecpu": " 2",
    "priority": " 3",
    "period": 108000.0,
    "C(LO)": 1129.0,
    "C(HI)": 2259.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 198",
    "preemptions": " 6",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.006607784",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.169571841",
    "avgresponsejitter": " 0.000640129",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 204",
    "lockedtime": " 0.000000387"




   Task:  17

    
    "id": " 17",
    "basecpu": " 2",
    "priority": " 4",
    "period": 75600.0,
    "C(LO)": 559.0,
    "C(HI)": 1119.0,
    "criticality": "HIGH",
    "migrable": "False",
    "completedruns": " 283",
    "preemptions": " 4",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001592348",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.244079583",
    "avgresponsejitter": " 0.000294658",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 1",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 287",
    "lockedtime": " 0.000000387"




   Task:  29

    
    "id": " 29",
    "basecpu": " 2",
    "priority": " 8",
    "period": 140000.0,
    "C(LO)": 15231.0,
    "C(HI)": 15231.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 153",
    "preemptions": " 160",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.015678646",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.140940183",
    "avgresponsejitter": " 0.008689916",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 312",
    "lockedtime": " 0.000017982"




   Task:  31

    
    "id": " 31",
    "basecpu": " 2",
    "priority": " 6",
    "period": 150000.0,
    "C(LO)": 10912.0,
    "C(HI)": 10912.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 143",
    "preemptions": " 117",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.013027357",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.150704336",
    "avgresponsejitter": " 0.006297405",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 259",
    "lockedtime": " 0.000009982"




   Task:  19

    
    "id": " 19",
    "basecpu": " 2",
    "priority": " 13",
    "period": 90720.0,
    "C(LO)": 5403.0,
    "C(HI)": 5403.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 236",
    "preemptions": " 33",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.005305432",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.228486021",
    "avgresponsejitter": " 0.002809342",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 268",
    "lockedtime": " 0.000013721"




   Task:  14

    
    "id": " 14",
    "basecpu": " 2",
    "priority": " 15",
    "period": 65625.0,
    "C(LO)": 2546.0,
    "C(HI)": 2546.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 326",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001529619",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.262947276",
    "avgresponsejitter": " 0.001275718",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 325",
    "lockedtime": " 0.000003468"




   Task:  16

    
    "id": " 16",
    "basecpu": " 2",
    "priority": " 14",
    "period": 75000.0,
    "C(LO)": 1679.0,
    "C(HI)": 1679.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 285",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001011417",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.225006258",
    "avgresponsejitter": " 0.000841390",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 284",
    "lockedtime": " 0.000003517"




   Task:  24

    
    "id": " 24",
    "basecpu": " 2",
    "priority": " 12",
    "period": 113400.0,
    "C(LO)": 2528.0,
    "C(HI)": 2528.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 189",
    "preemptions": " 8",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002917306",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.205806835",
    "avgresponsejitter": " 0.001305183",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 196",
    "lockedtime": " 0.000002366"




   Task:  7

    
    "id": " 7",
    "basecpu": " 2",
    "priority": " 17",
    "period": 39375.0,
    "C(LO)": 843.0,
    "C(HI)": 843.0,
    "criticality": "LOW",
    "migrable": "True",
    "completedruns": " 542",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000436462",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.262512694",
    "avgresponsejitter": " 0.000424832",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 541",
    "lockedtime": " 0.000024027"




   Task:  27

    
    "id": " 27",
    "basecpu": " 2",
    "priority": " 11",
    "period": 129600.0,
    "C(LO)": 2119.0,
    "C(HI)": 2119.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 166",
    "preemptions": " 8",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.002412438",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.254406210",
    "avgresponsejitter": " 0.001101180",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 173",
    "lockedtime": " 0.000001015"




   Task:  13

    
    "id": " 13",
    "basecpu": " 2",
    "priority": " 16",
    "period": 63000.0,
    "C(LO)": 492.99999999999994,
    "C(HI)": 492.99999999999994,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 339",
    "preemptions": " 0",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.000300183",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.231006426",
    "avgresponsejitter": " 0.000252447",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 338",
    "lockedtime": " 0.000001781"




   Task:  30

    
    "id": " 30",
    "basecpu": " 2",
    "priority": " 7",
    "period": 141750.0,
    "C(LO)": 412.0,
    "C(HI)": 412.0,
    "criticality": "LOW",
    "migrable": "False",
    "completedruns": " 152",
    "preemptions": " 2",
    "minresponsejitter": " 0.000000000",
    "maxresponsejitter": " 0.001440829",
    "minreleasejitter": " 0.000000000",
    "maxreleasejitter": " 22.265533778",
    "avgresponsejitter": " 0.000222474",
    "deadlinesmissed": " 0",
    "deadlinemissedtargetcore": " 0",
    "deadlinemissedaftermigration": " 0",
    "budgetexceeded": " 0",
    "budgetexceededtargetcore": " 0",
    "budgetexceededaftermigration": " 0",
    "timesmigrated": " 0",
    "timesrestored": " 0",
    "timesonc1": " 0",
    "timesonc2": " 153",
    "lockedtime": " 0.000000000"



   </details>

</details></details>



## Focus for each Taskset size level.

<details><summary markdown="span">Click here to expand this section.</summary>

### Level 8

   Tasksets executed: 33

   - Tasksets actually schedulable: 26/33 = 78.78787878787878 %

   - Tasksets **not** schedulable: 0/33 = 0.0 %

   - Tasksets exceeding level-criticality budget: 7/33 = 21.21212121212121 %

   - Tasksets exceeding safe boundary: 0/33 = 0.0 %

### Level 10

   Tasksets executed: 45

   - Tasksets actually schedulable: 38/45 = 84.44444444444444 %

   - Tasksets **not** schedulable: 0/45 = 0.0 %

   - Tasksets exceeding level-criticality budget: 7/45 = 15.555555555555555 %

   - Tasksets exceeding safe boundary: 0/45 = 0.0 %

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

   Tasksets executed: 20

   - Tasksets actually schedulable: 8/20 = 40.0 %

   - Tasksets **not** schedulable: 0/20 = 0.0 %

   - Tasksets exceeding level-criticality budget: 8/20 = 40.0 %

   - Tasksets exceeding safe boundary: 4/20 = 20.0 %

### Level 30

   Tasksets executed: 12

   - Tasksets actually schedulable: 4/12 = 33.33333333333333 %

   - Tasksets **not** schedulable: 0/12 = 0.0 %

   - Tasksets exceeding level-criticality budget: 5/12 = 41.66666666666667 %

   - Tasksets exceeding safe boundary: 3/12 = 25.0 %

### Level 35

   Tasksets executed: 6

   - Tasksets actually schedulable: 1/6 = 16.666666666666664 %

   - Tasksets **not** schedulable: 0/6 = 0.0 %

   - Tasksets exceeding level-criticality budget: 1/6 = 16.666666666666664 %

   - Tasksets exceeding safe boundary: 4/6 = 66.66666666666666 %

</details>


