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

## Executing Ada application targetting RTEMS over XtratuM
If you want to execute Ada tasksets on the TSP Platform, you need to install both [XtratuM](https://fentiss.com/products/hypervisor/) 2.0.5 and [RTEMS](https://www.rtems.org/) 4.9 (including its toolchain to compile Ada programs targetting RTEMS) targetting XtratuM itself. XtratuM is open-source, but you need to contact the [FentISS](https://fentiss.com/company/contact/) team if you want to get it. You also need a Board Support Package (BSP) in order to execute RTEMS over XtratuM. FentISS has developed one for their applications, but you need to ask them if they are willing to share it with you.

## Collecting data coming from the target HW to the host
The transition between automatic execution of Ada applications and analysis of log data is not automated. Before running the bash script, be sure that you have properly opened a terminal monitor (such as cutecom or HTerm) and connected to the target. 

# How to use the whole infrastructure
If you have not already, read the disclaimer [below](#disclaimer). Really.
 
This section is still **work in progress**. Meanwhile, read the disclaimer [below](#disclaimer) :upside_down_face:
## Configuration

## Schedulability Analysis and tasksets generation
## Execution on real target

## Off-line data analysis
# Disclaimer

This work is a continuation of my master's thesis work in [Computer Science](http://informatica.math.unipd.it/laureamagistrale/indexen.html) at the [University of Padua](https://www.unipd.it/en/). In the rush to get my degree, a lot of the code I wrote (system configuration, taskset generation, schedulability analysis, and off-line data analysis) is _really_ ugly :sob:. Some things I’m ashamed of, but I think you’ll understand. I decided to publish the source code of my work anyway, both to facilitate any subsequent work to mine and because there may be someone in the community who one day decides to re-engineer the source code.
