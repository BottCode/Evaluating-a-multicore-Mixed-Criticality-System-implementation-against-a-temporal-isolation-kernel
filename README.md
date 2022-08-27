# Evaluating a multicore Mixed-Criticality System implementation against a temporal isolation kernel

This repository is the main reference for the article that [Professor T. Vardanega](https://orcid.org/0000-0002-0089-0889) and I published with the above title: https://doi.org/10.1016/j.sysarc.2022.102688

The role of this repository is:
- contain and execute some [bash scripts](https://github.com/BottCode/Exploring-the-viability-of-a-MCS-multicore-runtime-demonstrator-a-comparison-with-a-/blob/master/execute_comparison_xuburns.sh) that allow you to configure and execute python scripts correctly
  - actually, the configuration is badly splitted into two different files (the aforementioned one and [this](https://github.com/BottCode/synthetic-Ada-tasksets-generation-for-a-MCS-semi-partitioned-model-or-RTEMS-on-XtratuM/blob/8745de417a2851d7b41dafb6b447c25f2bcfdab5/dual-core-version/config.py) one). Read the disclaimer [below](#disclaimer).
- aggregate two more repositories
  -  the [former](https://github.com/BottCode/Ada-RTE-supporting-semi-partitioned-model) contains the Ada runtime environment implementing the semi-partitioned model by Xu & Burns.
  -  the [latter](https://github.com/BottCode/synthetic-Ada-tasksets-generation-for-a-MCS-semi-partitioned-model-or-RTEMS-on-XtratuM) contains some python scripts implementing the schedulability analysis (both for the RTE Platform and TSP Platform), synthetic tasksets generation (both for RTE Platform and TSP Platform) and storing the *interesting* Ada tasksets to be executed on the RTE Platform. Such tasksets are saved in XML format too.
-  contains some python scripts that implement off-line data analysis resulting from real executions on the target HW.


# Requirements
First of all, **check each submodules' requirements**.

Then, for RTA and tasksets generation, you need:
1. Ubuntu (any Linux distro should be Ok)
2. Python3
3. pip3 
4. git (>= 2)

For the RTE Platform, you need:
1. ... work in progress

## Executing Ada application targetting RTEMS over XtratuM
If you want to execute Ada tasksets on the TSP Platform, you need to install both [XtratuM](https://fentiss.com/products/hypervisor/) 2.0.5 and [RTEMS](https://www.rtems.org/) 4.9 (including its toolchain to compile Ada programs targetting RTEMS) targetting XtratuM itself. XtratuM is open-source, but you need to contact the [FentISS](https://fentiss.com/company/contact/) team if you want to get it. You also need a Board Support Package (BSP) in order to execute RTEMS over XtratuM. FentISS has developed one for their applications, but you need to ask them if they are willing to share it with you.

## Collecting data coming from the target HW to the host
The transition between automatic execution of Ada applications and analysis of log data is not automated. Before running the bash script, be sure that you have properly opened a terminal monitor (such as cutecom or HTerm) and connected to the target. 

# How to use the whole infrastructure
If you have not already, read the disclaimer [below](#disclaimer). Really.
 
This section is still **work in progress**. Meanwhile, read the disclaimer [below](#disclaimer) :upside_down_face:
## Configuration
You can manipulate the input data via the [configuration.ini](./configuration.ini) file. The following is an explanation for each file section.

### ```[Experiments]```
In this section you can choose which experiments you want to execute. Use `yes` to execute an experiment. For instance, the following configuration executes only experiments 1, 3 and 4.
```
exp_1 = yes
exp_2 = no
exp_3 = yes
exp_4 = yes
```

### ```[Tasksets for each UL]```
_This parameter is **across all experiments.**_

In this section you can set how many tasksets to generate for each utilization level (see next section). We call this number $n$. For instance, if your utilizations range is $[1.6, 1.648]$ stepping $0.012$, you have $(1.648-1.6) / 0.012 = 4$ utilizations levels ($\{1.6, 1.612, 1.624, 1.636, 1.648\}$). If you set $n=10$, then you will generate $4 * 10=40$ tasksets.
```
n = 10
```


### ```[Utilization Levels]```
_This parameter is **across all experiments.**_

In this section you can set the utilizations range (explained above) you want to explore. For instance, the following configuration sets $[1.11, 1.875]$ range stepping $0.012$. This range is 
```
lower_bound = 1.11
upper_bound = 1.875
step        = 0.012
```

### ```[Criticality Factor Levels]```
_This parameter is for **experiment 2**_

In this section you can set the criticality factors range you want to explore. You can set this range as explained above. For instance, the following configuration generates $n$ tasksets for each criticality factor level in $\{1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4\}$.
```
lower_bound = 1.5
upper_bound = 4
step        = 0.25
```
_Please Note_: the _criticality factor_ concept does not apply to a tasksets thought for the TSP approach, since a (TSP) task can have only one criticality level.

### ```[HI-crit Proportion Levels]```
_This parameter is for **experiment 3**_

In this section you can set the HI-crit proportions range you want to explore. You can set this range as explained above. For instance, the following configuration generates $n$ tasksets for each HI-crit proportion level in $\{0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8\}$.
```
lower_bound = 0.2
upper_bound = 0.8
step        = 0.1
```

### ```[Tasksets Size]```
_This parameter is for **experiment 4**_

In this section you can set the tasksets cardinality.  For instance, the following configuration generates $n$ tasksets for each taskset cardinality in $\{15, 20, 25, 30, 35\}$.
```
size_list = 15, 20, 25, 30, 35
```

### ```[Per-tasks utilization range]```
_This parameter is **across all experiments.**_

In this section you can set the Per-tasks **nominal** utilization range.
```
lower_bound = 0.048
upper_bound = 0.6
```

## Schedulability Analysis and tasksets generation
## Execution on real target

## Off-line data analysis
# Disclaimer

This work is a continuation of my master's thesis work in [Computer Science](http://informatica.math.unipd.it/laureamagistrale/indexen.html) at the [University of Padua](https://www.unipd.it/en/). In the rush to get my degree, a lot of the code I wrote (system configuration, taskset generation, schedulability analysis, and off-line data analysis) is _really_ ugly :sob:. Some things I’m ashamed of, but I think you’ll understand. I decided to publish the source code of my work anyway, both to facilitate any subsequent work to mine and because there may be someone in the community who one day decides to re-engineer the source code.
