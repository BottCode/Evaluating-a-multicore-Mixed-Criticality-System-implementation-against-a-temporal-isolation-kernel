#!/bin/sh
REPO_ROOT=$PWD

RUNTIME_PROJ_DIR="$REPO_ROOT/ada-ravenscar-runtime-for-zynq7000-dual-core-supporting-mixed-criticality-systems/"
RUNTIME_INSTALLATION_DIR="$RUNTIME_PROJ_DIR/runtime/arm-eabi/lib/gnat/ravenscar_full_zynq7000"
RTA_DIR="$REPO_ROOT/py-xu-burns-2019-rta/dual-core-version"
PATH_TO_XSDB="/home/mattia/opt/XilinxSDK/SDK/2016.4/bin"

cd $RUNTIME_PROJ_DIR
sh build_runtime_zynq.sh
cd $REPO_ROOT

ADA_TASKSETS_DIR="$RTA_DIR/Ada_tasksets"

Execute_E1=$1
Execute_E2=$2
Execute_E3=$3
Execute_E4=$4

# Tasksets related to experiment 1
ADA_TASKSETS_E_1="$ADA_TASKSETS_DIR/experiment_1"
# Tasksets related to experiment 2
ADA_TASKSETS_E_2="$ADA_TASKSETS_DIR/experiment_2"
# Tasksets related to experiment 3
ADA_TASKSETS_E_3="$ADA_TASKSETS_DIR/experiment_3"
# Tasksets related to experiment 4
ADA_TASKSETS_E_4="$ADA_TASKSETS_DIR/experiment_4"

if [ "$Execute_E1" = True ]
then
    for approach_dir in $ADA_TASKSETS_E_1/*/
    do
        for taskset_dir in $approach_dir*/
        do
            [ -d "$taskset_dir" ] && make -C $taskset_dir && cd $taskset_dir && "$PATH_TO_XSDB/xsdb" cora_xsdb.ini && make clean -C $taskset_dir
        done
    done
fi

cd $REPO_ROOT

if [ "$Execute_E2" = True ]
then
    for approach_dir in $ADA_TASKSETS_E_2/*/
    do
        for taskset_dir in $approach_dir*/
        do
            [ -d "$taskset_dir" ] && make -C $taskset_dir && cd $taskset_dir && "$PATH_TO_XSDB/xsdb" cora_xsdb.ini && make clean -C $taskset_dir
        done
    done
fi

cd $REPO_ROOT

if [ "$Execute_E3" = True ]
then
    for approach_dir in $ADA_TASKSETS_E_3/*/
    do
        for taskset_dir in $approach_dir*/
        do
            [ -d "$taskset_dir" ] && make -C $taskset_dir && cd $taskset_dir && "$PATH_TO_XSDB/xsdb" cora_xsdb.ini && make clean -C $taskset_dir
        done
    done
fi

cd $REPO_ROOT

if [ "$Execute_E4" = True ]
then
    for approach_dir in $ADA_TASKSETS_E_4/*/
    do
        for taskset_dir in $approach_dir*/
        do
            [ -d "$taskset_dir" ] && make -C $taskset_dir && cd $taskset_dir && "$PATH_TO_XSDB/xsdb" cora_xsdb.ini && make clean -C $taskset_dir
        done
    done
fi

cd $REPO_ROOT