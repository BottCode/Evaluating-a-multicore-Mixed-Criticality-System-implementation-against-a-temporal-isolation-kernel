#!/bin/sh
REPO_ROOT=$PWD

REPO_ANALYSIS="$REPO_ROOT/analysis"

cd $REPO_ANALYSIS && python3 tsp_results.py --util-low $1 --util-high $2 --util-step $3 --criticality-low $4 --criticality-high $5 --criticality-step $6 --proportion-low $7 --proportion-high $8 --proportion-step $9 --exp-1 ${10} --exp-2 ${11} --exp-3 ${12} --exp-4 ${13} --numb-tests ${14}

cd $REPO_ROOT