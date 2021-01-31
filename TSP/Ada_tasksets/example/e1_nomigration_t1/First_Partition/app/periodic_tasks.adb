with Ada.Real_Time; use Ada.Real_Time;
with Ada.Text_IO;

with System.Multiprocessors;
use System.Multiprocessors;

with Single_Execution_Data;
with Production_Workload;
with Set_Of_Procedures;
with Workload_Manager;
with Initial_Delay;

with RTEMS;
with RTEMS.TASKS;
with RTEMS.CPU_Usage;

package body Periodic_Tasks is

   function Get_Longest_Hyperperiod return Natural is
   begin
      if Single_Execution_Data.Experiment_Hyperperiods (1) > Single_Execution_Data.Experiment_Hyperperiods (2) then
         return Single_Execution_Data.Experiment_Hyperperiods (1);
      end if;

      return Single_Execution_Data.Experiment_Hyperperiods (2);
   end Get_Longest_Hyperperiod;

   ------------
   --  Init  --
   ------------

   procedure Init is
      Next_Period : constant Ada.Real_Time.Time := Ada.Real_Time.Time_First + Ada.Real_Time.Microseconds (Initial_Delay.Delay_Time);
      Period_To_Add : constant Ada.Real_Time.Time_Span := Ada.Real_Time.Microseconds (Get_Longest_Hyperperiod);

      ID_T_5 : RTEMS.ID;
      ID_T_10 : RTEMS.ID;
      ID_T_11 : RTEMS.ID;
      ID_T_7 : RTEMS.ID;
      ID_T_9 : RTEMS.ID;
      ID_T_LAST : RTEMS.ID;

      STATUS_T_5 : RTEMS.STATUS_CODES;
      STATUS_T_10 : RTEMS.STATUS_CODES;
      STATUS_T_11 : RTEMS.STATUS_CODES;
      STATUS_T_7 : RTEMS.STATUS_CODES;
      STATUS_T_9 : RTEMS.STATUS_CODES;
      STATUS_T_LAST : RTEMS.STATUS_CODES;
   begin
      --  Stuck until someone states that experiment is over.
      --  Ada.Text_IO.Put_Line ("----------------------");
      --  Ada.Text_IO.Put_Line ("--  END EXPERIMENT  --");
      --  Ada.Text_IO.Put_Line ("----------------------");

      --  Tasksets allocation

      RTEMS.TASKS.CREATE(
         RTEMS.BUILD_NAME('T', '_', '0', '5'),
         139,
         RTEMS.MINIMUM_STACK_SIZE,
         RTEMS.PREEMPT,
         RTEMS.DEFAULT_ATTRIBUTES,
         ID_T_5,
         STATUS_T_5
      );

      RTEMS.TASKS.CREATE(
         RTEMS.BUILD_NAME('T', '_', '0', '7'),
         140,
         RTEMS.MINIMUM_STACK_SIZE,
         RTEMS.PREEMPT,
         RTEMS.DEFAULT_ATTRIBUTES,
         ID_T_7,
         STATUS_T_7
      );

      RTEMS.TASKS.CREATE(
         RTEMS.BUILD_NAME('T', '_', '1', '1'),
         142,
         RTEMS.MINIMUM_STACK_SIZE,
         RTEMS.PREEMPT,
         RTEMS.DEFAULT_ATTRIBUTES,
         ID_T_11,
         STATUS_T_11
      );         

      --  RTEMS.TASKS.CREATE( RTEMS.BUILD_NAME('T', '_', '1', '0'), 141, RTEMS.MINIMUM_STACK_SIZE, RTEMS.PREEMPT, RTEMS.DEFAULT_ATTRIBUTES, ID_T_10, STATUS_T_10);    

      Ada.Text_IO.Put_Line ("START");

      RTEMS.TASKS.START( ID_T_7, Set_Of_Procedures.T_7_Body'ACCESS, 0, STATUS_T_7);

      RTEMS.TASKS.START(
         ID_T_5,
         Set_Of_Procedures.T_5_Body'ACCESS,
         0,
         STATUS_T_5
      );
   
      --  RTEMS.TASKS.START( ID_T_10, Set_Of_Procedures.T_10_Body'ACCESS, 0, STATUS_T_10);

      RTEMS.TASKS.START(
         ID_T_11,
         Set_Of_Procedures.T_11_Body'ACCESS,
         0,
         STATUS_T_11
      );

      Ada.Text_IO.Put_Line ("T5 started");

      delay 20.0;

      --  Ada.Text_IO.Put_Line ("End");
      RTEMS.CPU_Usage.report;

      loop
         null; 
      end loop;
   end Init;

end Periodic_Tasks;
