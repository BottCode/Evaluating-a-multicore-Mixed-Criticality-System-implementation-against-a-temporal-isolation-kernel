with Ada.Real_Time; use Ada.Real_Time;

with Single_Execution_Data;
with Production_Workload;
with Workload_Manager;
with Initial_Delay;
with RTEMS.INTERRUPT;

with Ada.Text_IO;
with System.Task_Primitives.Operations;

package body Set_Of_Procedures is

    package STPO renames System.Task_Primitives.Operations;

    procedure Work (Period : Positive; ID : Natural; Fake_Period : Duration);
    pragma No_Return (Work);

    procedure Work (Period : Positive; ID : Natural; Fake_Period : Duration) is
      Next_Period : Ada.Real_Time.Time := Ada.Real_Time.Time_First + Ada.Real_Time.Microseconds (Initial_Delay.Delay_Time);
      Period_To_Add : constant Ada.Real_Time.Time_Span := Ada.Real_Time.Microseconds (1_000_000); --  Ada.Real_Time.Microseconds (Period);
      I : Natural := 0;
      P : Duration := Fake_Period + 2.0;
      Time_Left : Ada.Real_Time.Time_Span;
      Delayed_At : Ada.Real_Time.Time;
      Waked_At : Ada.Real_Time.Time;
      Deadline : Ada.Real_Time.Time;
      ISRL : RTEMS.ISR_Level := 0;
      Time_To_Sleep : Duration := 0.0;
      Now : Ada.Real_Time.Time;
    begin

      delay 2.0;

      loop
         Deadline := Ada.Real_Time.Clock + To_Time_Span (Fake_Period);
         --  Ada.Text_IO.Put_Line (Duration'Image(To_Duration (Ada.Real_Time.Time_Span_Unit)));
         --  Time_Left := Ada.Real_Time.Clock + To_Time (Ada.Real_Time.Time_Unit);
         --  Ada.Text_IO.Put_Line ()
         --  Ada.Text_IO.Put_Line (Duration'Image (Fake_Period));

         Production_Workload.Small_Whetstone (Workload_Manager.Get_Workload (ID, I));

         I := I + 1;

         Now := Ada.Real_Time.Clock;

         --  ISRL := RTEMS.INTERRUPT.DISABLE;
         --  Ada.Text_IO.Put_Line (RTEMS.ISR_Level'Image (ISRL));
         
         if Now <= Deadline then
            
            ISRL := RTEMS.INTERRUPT.DISABLE;
            Ada.Text_IO.Put_Line ("T " & Natural'Image (ID) & " has disabled interr");
            Time_To_Sleep := To_Duration (Deadline - Ada.Real_Time.Clock);
            Ada.Text_IO.Put_Line ("T " & Natural'Image (ID) & " is going to enable interr");
            RTEMS.INTERRUPT.ENABLE (144);
            Ada.Text_IO.Put_Line ("T " & Natural'Image (ID) & " has enabled interr");

            --  Ada.Text_IO.Put_Line ( "Task: " & Natural'Image (ID) & ": sleep for: " & Duration'Image (Time_To_Sleep));
            Delayed_At := Ada.Real_Time.Clock;
            delay Time_To_Sleep;
            Waked_At := Ada.Real_Time.Clock;

            Ada.Text_IO.Put_Line ("Error Task " & Natural'Image (ID) & ": " & Duration'Image (Abs (Time_To_Sleep - (To_Duration (Waked_At - Delayed_At))) * 1_000) & " milliseconds");
         end if;

         
      end loop;
    end Work;

    procedure T_5_Body (ARGUMENT : in RTEMS.TASKS.ARGUMENT) is
        pragma Unreferenced (ARGUMENT);
        Period : Positive := 2_000_000;
        ID : Natural := 5;
    begin
        Work (Period, ID, 2.0);
    end T_5_Body;

    procedure T_10_Body (ARGUMENT : in RTEMS.TASKS.ARGUMENT) is
        pragma Unreferenced (ARGUMENT);
        Period : Positive := 131250;
        ID : Natural := 10;
    begin
        Work (Period, ID, 1.0);
    end T_10_Body;

    procedure T_11_Body (ARGUMENT : in RTEMS.TASKS.ARGUMENT) is
        pragma Unreferenced (ARGUMENT);
        Period : Positive := 600000;
        ID : Natural := 11;
    begin
        Work (Period, ID, 4.0);
    end T_11_Body;

    procedure T_7_Body (ARGUMENT : in RTEMS.TASKS.ARGUMENT) is
        pragma Unreferenced (ARGUMENT);
        Period : Positive := 101250;
        ID : Natural := 7;
    begin
        Work (Period, ID, 5.0);
    end T_7_Body;

    procedure T_9_Body (ARGUMENT : in RTEMS.TASKS.ARGUMENT) is
        pragma Unreferenced (ARGUMENT);
        Period : Positive := 118125;
        ID : Natural := 9;
    begin
        Work (Period, ID, 1.0);
    end T_9_Body;

    procedure LAST (ARGUMENT : in RTEMS.TASKS.ARGUMENT) is
        pragma Unreferenced (ARGUMENT);
        Next_Period : Ada.Real_Time.Time := Ada.Real_Time.Time_First + Ada.Real_Time.Nanoseconds (1_000_000_000);
        Period_To_Add : constant Ada.Real_Time.Time_Span := Ada.Real_Time.Nanoseconds (1_000_000_000);
    begin
        delay until (Next_Period) + (Period_To_Add * 10);
        loop
            null;
            Ada.Text_IO.Put_Line ("end?");
        end loop;
    end LAST;

end Set_Of_Procedures;