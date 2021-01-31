with Periodic_Tasks;
use Periodic_Tasks;

package taskset_e1_nomigration_t1_p2 is

  T_2 : High_Crit (Id => 2, Pri => 4, Low_Critical_Budget => 2886, High_Critical_Budget => 5772, Workload => 761, Period => 25200);
  T_12 : High_Crit (Id => 12, Pri => 0, Low_Critical_Budget => 68836, High_Critical_Budget => 137672, Workload => 18252, Period => 945000);
  T_1 : High_Crit (Id => 1, Pri => 5, Low_Critical_Budget => 1091, High_Critical_Budget => 2183, Workload => 288, Period => 15750);
  T_4 : Low_Crit (Id => 4, Pri => 3, Low_Critical_Budget => 15522, Workload => 2056, Period => 84375);
  T_6 : Low_Crit (Id => 6, Pri => 2, Low_Critical_Budget => 11048, Workload => 1463, Period => 94500);
  T_3 : Low_Crit (Id => 3, Pri => 6, Low_Critical_Budget => 5263, Workload => 694, Period => 70000);
  T_8 : Low_Crit (Id => 8, Pri => 1, Low_Critical_Budget => 6655, Workload => 878, Period => 113400);

end taskset_e1_nomigration_t1_p2;