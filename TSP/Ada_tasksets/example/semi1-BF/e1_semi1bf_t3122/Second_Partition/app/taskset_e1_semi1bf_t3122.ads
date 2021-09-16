with Periodic_Tasks;
use Periodic_Tasks;

package taskset_e1_semi1bf_t3122 is

  T_4 : Low_Crit (Id => 4, Pri => 2, Low_Critical_Budget => 1, Workload => 1, Period => 100);
  T_5 : High_Crit (Id => 5, Pri => 9, Low_Critical_Budget => 1, High_Critical_Budget => 1, Workload => 1, Period => 4_000_000);
  T_1 : Low_Crit (Id => 1, Pri => 5, Low_Critical_Budget => 1, Workload => 1, Period => 10);
  T_9 : Low_Crit (Id => 9, Pri => 1, Low_Critical_Budget => 1, Workload => 1, Period => 350);
  T_8 : Low_Crit (Id => 8, Pri => 6, Low_Critical_Budget => 1, Workload => 1, Period => 50);
  T_6 : Low_Crit (Id => 6, Pri => 4, Low_Critical_Budget => 1, Workload => 1, Period => 20);

end taskset_e1_semi1bf_t3122;
