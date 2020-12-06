UTIL_STEP=0.012
UTIL_LOWER_BOUND=1.8
UTIL_HIGHER_BOUND=2.1

CRITICALITY_STEP=0.25
CRITICALITY_LOWER_BOUND=1.5
CRITICALITY_HIGHER_BOUND=4

PROPORTION_STEP=0.1
PROPORTION_LOWER_BOUND=0.1
PROPORTION_HIGHER_BOUND=0.9

E1=True
E2=False
E3=False
E4=False

NUMBER_OF_TESTS=100

#sh dual_core_RTA.sh $UTIL_LOWER_BOUND $UTIL_HIGHER_BOUND $UTIL_STEP $CRITICALITY_LOWER_BOUND $CRITICALITY_HIGHER_BOUND $CRITICALITY_STEP $PROPORTION_LOWER_BOUND $PROPORTION_HIGHER_BOUND $PROPORTION_STEP $E1 $E2 $E3 $E4 $NUMBER_OF_TESTS
sh execute_ada_xu_burns.sh $E1 $E2 $E3 $E4 > log_execution.txt
#sh perform_analysys_sim_vs_real.sh $UTIL_LOWER_BOUND $UTIL_HIGHER_BOUND $UTIL_STEP $CRITICALITY_LOWER_BOUND $CRITICALITY_HIGHER_BOUND $CRITICALITY_STEP $PROPORTION_LOWER_BOUND $PROPORTION_HIGHER_BOUND $PROPORTION_STEP $E1 $E2 $E3 $E4 $NUMBER_OF_TESTS