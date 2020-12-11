pragma Profile (Ravenscar);

with System;

with Ada.Real_Time;
use Ada.Real_Time;

with Ada.Text_IO;
with Gnat.IO;

--  with print_utilities_h;

--  with Periodic_Tasks;

--  with taskset_e1_semi1bf_t3122;
--  pragma Unreferenced (taskset_e1_semi1bf_t3122);

procedure main_e1_semi1bf_t3122_p0 is
   Next_Wakeup : Ada.Real_Time.Time;
   Period      : constant Ada.Real_Time.Time_Span :=
                    Ada.Real_Time.Nanoseconds (2_000_000_000);
                    --   Ada.Real_Time.Nanoseconds (20000);

   Iterations : constant := 1000;
   Actual_Span : array (1..Iterations) of Ada.Real_Time.Time_Span;
   Average_Span : Ada.Real_Time.Time_Span := Ada.Real_Time.Time_Span_Zero;
   Max_Span     : Ada.Real_Time.Time_Span := Ada.Real_Time.Time_Span_First;
   Min_Span     : Ada.Real_Time.Time_Span := Ada.Real_Time.Time_Span_Last;

   pragma Priority (System.Priority'Last);

begin
   GNAT.IO.Put_Line ("AA");
   GNAT.IO.Put ("BB");
   Ada.Text_Io.Put_Line ("*** Delay Until Variation Test ***");
   Ada.Text_Io.Put_Line (
      Integer'Image (Iterations) & " iterations with " &
      Duration'Image (Ada.Real_Time.To_Duration(Period)) &
      "s period"
   );
   
   Next_Wakeup := Ada.Real_Time.Clock + Period;
   for Count in 1..Iterations loop
   
      delay until Next_Wakeup;

      Next_Wakeup := Next_Wakeup + Period;
   end loop;

   Ada.Text_Io.Put_Line (
      "Average delay is" &
      Duration'Image (Ada.Real_Time.To_Duration (Average_Span)) &
      "s"
   );
   Ada.Text_Io.Put_Line (
      "Maximum delay is" &
      Duration'Image (Ada.Real_Time.To_Duration (Max_Span)) &
      "s"
   );
   Ada.Text_Io.Put_Line (
      "Minimum delay is" &
       Duration'Image (Ada.Real_Time.To_Duration (Min_Span)) &
       "s"
   );
   Ada.Text_Io.Put_Line ("*** END OF Delay Until Variation Test ***");
end main_e1_semi1bf_t3122_p0;