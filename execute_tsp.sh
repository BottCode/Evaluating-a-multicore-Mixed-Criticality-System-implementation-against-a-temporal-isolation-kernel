#!/bin/sh
REPO_ROOT=$PWD

TSP_DIR="$REPO_ROOT/TSP/"

PATH_TO_XSDB="/home/mattia/opt/XilinxSDK/SDK/2016.4/bin"

# sh build_runtime_zynq.sh
cd $REPO_ROOT

ADA_TASKSETS_DIR="$TSP_DIR/Ada_tasksets"

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
            echo "Executing \n"
            echo $taskset_dir
            [ -d "$taskset_dir" ] && if make -C $taskset_dir ; then
                cd $taskset_dir && "$PATH_TO_XSDB/xsdb" cora_xsdb.ini && make clean -C $taskset_dir && cd $approach_dir && rm -rf $taskset_dir
            else
                echo "\n### Compilation failed! ###\n"
                cd $approach_dir && rm -rf $taskset_dir
            fi
            # [ -d "$taskset_dir" ] && make -C $taskset_dir && cd $taskset_dir && "$PATH_TO_XSDB/xsdb" cora_xsdb.ini && make clean -C $taskset_dir
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
            echo "Executing \n"
            echo $taskset_dir
            [ -d "$taskset_dir" ] && if make -C $taskset_dir ; then
                cd $taskset_dir && "$PATH_TO_XSDB/xsdb" cora_xsdb.ini && make clean -C $taskset_dir && cd $approach_dir && rm -rf $taskset_dir
            else
                echo "\n### Compilation failed! ###\n"
                cd $approach_dir && rm -rf $taskset_dir
            fi
            # [ -d "$taskset_dir" ] && make -C $taskset_dir && cd $taskset_dir && "$PATH_TO_XSDB/xsdb" cora_xsdb.ini && make clean -C $taskset_dir
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
            echo "Executing \n"
            echo $taskset_dir
            [ -d "$taskset_dir" ] && if make -C $taskset_dir ; then
                cd $taskset_dir && "$PATH_TO_XSDB/xsdb" cora_xsdb.ini && make clean -C $taskset_dir && cd $approach_dir && rm -rf $taskset_dir
            else
                echo "\n### Compilation failed! ###\n"
                cd $approach_dir && rm -rf $taskset_dir
            fi
            # [ -d "$taskset_dir" ] && make -C $taskset_dir && cd $taskset_dir && "$PATH_TO_XSDB/xsdb" cora_xsdb.ini && make clean -C $taskset_dir
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
            echo "Executing \n"
            echo $taskset_dir
            [ -d "$taskset_dir" ] && if make -C $taskset_dir ; then
                cd $taskset_dir && "$PATH_TO_XSDB/xsdb" cora_xsdb.ini && make clean -C $taskset_dir && cd $approach_dir && rm -rf $taskset_dir
            else
                echo "\n### Compilation failed! ###\n"
                cd $approach_dir && rm -rf $taskset_dir
            fi
            # [ -d "$taskset_dir" ] && make -C $taskset_dir && cd $taskset_dir && "$PATH_TO_XSDB/xsdb" cora_xsdb.ini && make clean -C $taskset_dir
        done
    done
fi

cd $REPO_ROOT
