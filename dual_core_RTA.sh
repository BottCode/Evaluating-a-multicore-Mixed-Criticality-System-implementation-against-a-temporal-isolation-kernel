#!/bin/sh

REPO_ROOT=$PWD

RUNTIME_PROJ_DIR="$REPO_ROOT/ada-ravenscar-runtime-for-zynq7000-dual-core-supporting-mixed-criticality-systems/"
RUNTIME_INSTALLATION_DIR="$RUNTIME_PROJ_DIR/runtime/arm-eabi/lib/gnat/ravenscar_full_zynq7000"
RTA_DIR="$REPO_ROOT/py-xu-burns-2019-rta/dual-core-version/"

cd $RUNTIME_PROJ_DIR
sh build_runtime_zynq.sh
cd $REPO_ROOT

cd $RTA_DIR
python3 run.py --runtime-dir $RUNTIME_INSTALLATION_DIR --util-low $1 --util-high $2 --util-step $3 --criticality-low $4 --criticality-high $5 --criticality-step $6 --proportion-low $7 --proportion-high $8 --proportion-step $9 --exp-1 ${10} --exp-2 ${11} --exp-3 ${12} --exp-4 ${13} --numb-tests ${14}

