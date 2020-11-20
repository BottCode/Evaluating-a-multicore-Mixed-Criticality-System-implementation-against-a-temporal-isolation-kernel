#!/bin/sh
REPO_ROOT=$PWD

RUNTIME_PROJ_DIR="$REPO_ROOT/ada-ravenscar-runtime-for-zynq7000-dual-core-supporting-mixed-criticality-systems/"
RUNTIME_INSTALLATION_DIR="$RUNTIME_PROJ_DIR/runtime/arm-eabi/lib/gnat/ravenscar_full_zynq7000"
RTA_DIR="$REPO_ROOT/py-xu-burns-2019-rta/dual-core-version"

ADA_TASKSETS_DIR="$RTA_DIR/Ada_tasksets"

Execute_E1=true
Execute_E2=true
Execute_E3=true
Execute_E4=true

# Tasksets related to experiment 1
ADA_TASKSETS_E_1="$ADA_TASKSETS_DIR/experiment_1"
# Tasksets related to experiment 2
ADA_TASKSETS_E_2="$ADA_TASKSETS_DIR/experiment_2"
# Tasksets related to experiment 3
ADA_TASKSETS_E_3="$ADA_TASKSETS_DIR/experiment_3"
# Tasksets related to experiment 4
ADA_TASKSETS_E_4="$ADA_TASKSETS_DIR/experiment_4"

if [ "$Execute_E1" = true ]
then
    for approach_dir in $ADA_TASKSETS_E_1/*/
    do
        for taskset_dir in $approach_dir*/
        do
            [ -d "$taskset_dir" ] && make -C $taskset_dir && make clean -C $taskset_dir
        done
    done
fi

if [ "$Execute_E2" = true ]
then
    for approach_dir in $ADA_TASKSETS_E_2/*/
    do
        for taskset_dir in $approach_dir*/
        do
            [ -d "$taskset_dir" ] && make -C $taskset_dir && make clean -C $taskset_dir
        done
    done
fi

if [ "$Execute_E3" = true ]
then
    for approach_dir in $ADA_TASKSETS_E_3/*/
    do
        for taskset_dir in $approach_dir*/
        do
            [ -d "$taskset_dir" ] && make -C $taskset_dir && make clean -C $taskset_dir
        done
    done
fi

if [ "$Execute_E4" = true ]
then
    for approach_dir in $ADA_TASKSETS_E_4/*/
    do
        for taskset_dir in $approach_dir*/
        do
            [ -d "$taskset_dir" ] && make -C $taskset_dir && make clean -C $taskset_dir
        done
    done
fi