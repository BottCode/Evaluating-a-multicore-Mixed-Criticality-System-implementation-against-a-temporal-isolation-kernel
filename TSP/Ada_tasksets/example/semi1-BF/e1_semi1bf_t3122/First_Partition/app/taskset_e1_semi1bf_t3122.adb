with Single_Execution_Data;
with Production_Workload;

with Ada.Real_Time;
use Ada.Real_Time;

with RTEMS;
with RTEMS.TASKS;

package body taskset_e1_semi1bf_t3122 is

  task body T_9 is
      Next_Period : Ada.Real_Time.Time := Ada.Real_Time.Time_First + Ada.Real_Time.Microseconds (Single_Execution_Data.Delay_Time);
      Period_To_Add : constant Ada.Real_Time.Time_Span := Ada.Real_Time.Nanoseconds (2_000_000_000);
      I : Natural := 0;
  begin

    loop
        delay until Next_Period;
        if I rem 2 = 0 then
          Production_Workload.Small_Whetstone (1);
        end if;
        I := I + 1;
        Next_Period := Next_Period + Period_To_Add;
    end loop;

  end T_9;

  task body T_10 is
      Next_Period : Ada.Real_Time.Time := Ada.Real_Time.Time_First + Ada.Real_Time.Microseconds (Single_Execution_Data.Delay_Time);
      Period_To_Add : constant Ada.Real_Time.Time_Span := Ada.Real_Time.Nanoseconds (1_000_000_000);
      I : Natural := 0;
  begin

    loop
        delay until Next_Period;
        if I rem 2 = 0 then
          Production_Workload.Small_Whetstone (1);
        end if;
        I := I + 1;
        Next_Period := Next_Period + Period_To_Add;
    end loop;

  end T_10;

end taskset_e1_semi1bf_t3122;