#!/bin/sh
REPO_ROOT=$PWD

REPO_ANALYSIS="$REPO_ROOT/analysis"

cd $REPO_ANALYSIS && python3 simulation_vs_real_execution.py

cd $REPO_ROOT