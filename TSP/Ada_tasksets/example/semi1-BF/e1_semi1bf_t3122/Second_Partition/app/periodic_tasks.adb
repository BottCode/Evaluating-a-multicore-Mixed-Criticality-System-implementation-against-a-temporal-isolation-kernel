with Ada.Real_Time; use Ada.Real_Time;
with Ada.Text_IO;

with System.Multiprocessors;
use System.Multiprocessors;

with Single_Execution_Data;
with Production_Workload;
with Workload_Manager;
with Initial_Delay;

package body Periodic_Tasks is

   function Get_Longest_Hyperperiod return Natural is
   begin
      if Single_Execution_Data.Experiment_Hyperperiods (1) > Single_Execution_Data.Experiment_Hyperperiods (2) then
         return Single_Execution_Data.Experiment_Hyperperiods (1);
      end if;

      return Single_Execution_Data.Experiment_Hyperperiods (2);
   end Get_Longest_Hyperperiod;

   ---------------------
   --  type Low_Crit  --
   ---------------------

   task body Low_Crit is
      Next_Period : Ada.Real_Time.Time := Ada.Real_Time.Time_First + Ada.Real_Time.Microseconds (Initial_Delay.Delay_Time);
      Period_To_Add : constant Ada.Real_Time.Time_Span := Ada.Real_Time.Microseconds (Period);
      I : Natural := 0;
   begin
      loop
         delay until Next_Period;

         --  Ada.Text_IO.Put_Line ("CPU: " & CPU'Image(System.OS_Interface.Current_CPU) & Integer'Image(ID) & Integer'Image (I));
         Production_Workload.Small_Whetstone (Workload_Manager.Get_Workload (ID, I));
         
         I := I + 1;

         Next_Period := Next_Period + Period_To_Add;
      end loop;
   end Low_Crit;

   ----------------------
   --  type High_Crit  --
   ----------------------

   task body High_Crit is
      Next_Period : Ada.Real_Time.Time := Ada.Real_Time.Time_First + Ada.Real_Time.Microseconds (Initial_Delay.Delay_Time);
      Period_To_Add : constant Ada.Real_Time.Time_Span := Ada.Real_Time.Microseconds (Period);
      I : Natural := 0;
   begin
      loop
         delay until Next_Period;
         
         --  Ada.Text_IO.Put_Line ("CPU: " & CPU'Image(System.OS_Interface.Current_CPU) & Integer'Image(ID) & Integer'Image (I));
         Production_Workload.Small_Whetstone (Workload_Manager.Get_Workload (ID, I));

         I := I + 1;

         Next_Period := Next_Period + Period_To_Add;
      end loop;
   end High_Crit;

   ------------
   --  Init  --
   ------------

   procedure Init is
   begin
      --  Stuck until someone states that experiment is over.
      --  Ada.Text_IO.Put_Line ("----------------------");
      --  Ada.Text_IO.Put_Line ("--  END EXPERIMENT  --");
      --  Ada.Text_IO.Put_Line ("----------------------");

      Ada.Text_IO.Put_Line ("<execution>");

      Ada.Text_IO.Put_Line ("<executionid>" & Single_Execution_Data.Id_Execution & "</executionid>");
      Ada.Text_IO.Put_Line ("<experimentid>" & Integer'Image (Single_Execution_Data.Id_Experiment) & "</experimentid>");
      Ada.Text_IO.Put_Line ("<approach>" & Single_Execution_Data.Approach & "</approach>");
      Ada.Text_IO.Put_Line ("<tasksetid>" & Integer'Image (Single_Execution_Data.Taskset_Id) & "</tasksetid>");
      Ada.Text_IO.Put_Line ("<tasksetsize>" & Single_Execution_Data.Taskset_Size & "</tasksetsize>");
      Ada.Text_IO.Put_Line ("<tasksetutilization>" & Single_Execution_Data.Taskset_Utilization & "</tasksetutilization>");
      Ada.Text_IO.Put_Line ("<criticalityfactor>" & Single_Execution_Data.Criticality_Factor & "</criticalityfactor>");
      Ada.Text_IO.Put_Line ("<perc>" & Single_Execution_Data.HI_Crit_Proportion & "</perc>");
      Ada.Text_IO.Put_Line ("<hyperperiodp1>" & Natural'Image (Single_Execution_Data.Experiment_Hyperperiods (1)) & "</hyperperiodp1>");
      Ada.Text_IO.Put_Line ("<hyperperiodp2>" & Natural'Image (Single_Execution_Data.Experiment_Hyperperiods (2)) & "</hyperperiodp2>");

      --  Print tasks/partition log

      Ada.Text_IO.Put_Line ("</execution>");
      Ada.Text_IO.Put_Line("");
      --  System.BB.Threads.Queues.Print_Queues;

      loop
         null;
      end loop;
   end Init;

   ----------------------------
   --  End_Task_Second_Core  --
   ----------------------------
   
   --  This task stucks second core's execution when current experiment should stops.
   task End_Task_Second_Core with 
         Priority => System.Priority'Last,
         CPU      => CPU'Last;

   task body End_Task_Second_Core is
   begin
      loop
         null;
      end loop;
   end End_Task_Second_Core;

   task Notify_Major_Hyperperiod_Has_Been_Expired with 
         Priority => System.Priority'Last - 1,
         CPU      => CPU'Last;
   
   task body Notify_Major_Hyperperiod_Has_Been_Expired is
      Next_Period : constant Ada.Real_Time.Time := Ada.Real_Time.Time_First + Ada.Real_Time.Microseconds (Initial_Delay.Delay_Time);
      Period_To_Add : constant Ada.Real_Time.Time_Span := Ada.Real_Time.Microseconds (Get_Longest_Hyperperiod);
   begin

      delay until Next_Period + Period_To_Add;

   end Notify_Major_Hyperperiod_Has_Been_Expired;

end Periodic_Tasks;
