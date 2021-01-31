with Periodic_Tasks;
use Periodic_Tasks;

package taskset_e1_nomigration_t1_p1 is

  T_5 : High_Crit (Id => 5, Pri => 2, Low_Critical_Budget => 9434, High_Critical_Budget => 18868, Workload => 2500, Period => 90720);
  T_10 : High_Crit (Id => 10, Pri => 1, Low_Critical_Budget => 11431, High_Critical_Budget => 22862, Workload => 3029, Period => 131250);
  T_11 : High_Crit (Id => 11, Pri => 0, Low_Critical_Budget => 22280, High_Critical_Budget => 44560, Workload => 5904, Period => 600000);
  T_7 : Low_Crit (Id => 7, Pri => 4, Low_Critical_Budget => 34545, Workload => 4577, Period => 101250);
  T_9 : Low_Crit (Id => 9, Pri => 3, Low_Critical_Budget => 12074, Workload => 1599, Period => 118125);

end taskset_e1_nomigration_t1_p1;