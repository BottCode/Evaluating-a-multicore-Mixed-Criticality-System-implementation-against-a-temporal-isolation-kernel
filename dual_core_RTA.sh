#!/bin/sh
REPO_ROOT=$PWD

RUNTIME_PROJ_DIR="$REPO_ROOT/ada-ravenscar-runtime-for-zynq7000-dual-core-supporting-mixed-criticality-systems/"
RUNTIME_INSTALLATION_DIR="$RUNTIME_PROJ_DIR/runtime/arm-eabi/lib/gnat/ravenscar_full_zynq7000"
RTA_DIR="$REPO_ROOT/py-xu-burns-2019-rta/dual-core-version/"

cd $RUNTIME_PROJ_DIR
sh build_runtime_zynq.sh
cd $REPO_ROOT

cd $RTA_DIR
python3 run.py $RUNTIME_INSTALLATION_DIR

