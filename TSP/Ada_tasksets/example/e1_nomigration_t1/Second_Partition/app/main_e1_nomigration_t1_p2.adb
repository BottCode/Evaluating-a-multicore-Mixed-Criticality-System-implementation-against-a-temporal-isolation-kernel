with System;
with Periodic_Tasks;
with Ada.Text_IO;

with taskset_e1_nomigration_t1_p2;
pragma Unreferenced (taskset_e1_nomigration_t1_p2);

procedure main_e1_nomigration_t1_p2 is
	pragma Priority (System.Priority'Last);
begin
	Ada.Text_IO.Put_Line ("P2");
	Periodic_Tasks.Init;
end main_e1_nomigration_t1_p2;