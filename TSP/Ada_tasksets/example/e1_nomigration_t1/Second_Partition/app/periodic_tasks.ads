with System;

package Periodic_Tasks is

  --  CPU_A  : constant CPU := CPU'First;
  --  CPU_B  : constant CPU := CPU'Last; 

  --  Periodic LO-CRIT task
  task type Low_Crit
      (Id                              : Natural;
      Pri                              : System.Priority;
      Low_Critical_Budget              : Natural;
      Workload                         : Positive;
      Period                           : Positive)
  is
      pragma Priority (Pri);
  end Low_Crit;

  --  Periodic HI-CRIT task
  task type High_Crit
      (Id                              : Natural;
      Pri                              : System.Priority;
      Low_Critical_Budget              : Natural;
      High_Critical_Budget             : Natural;
      Workload                         : Positive;
      Period                           : Positive) 
  is
      pragma Priority (Pri);
  end High_Crit;

  procedure Init;
  pragma No_Return (Init);

end Periodic_Tasks;