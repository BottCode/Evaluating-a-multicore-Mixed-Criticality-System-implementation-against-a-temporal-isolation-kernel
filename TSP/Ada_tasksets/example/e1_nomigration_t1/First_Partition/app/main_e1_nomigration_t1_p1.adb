with System;
with Periodic_Tasks;
with Ada.Text_IO;

procedure main_e1_nomigration_t1_p1 is
	pragma Priority (114);
begin
	Ada.Text_IO.Put_Line ("MAIN!");
	Periodic_Tasks.Init;
end main_e1_nomigration_t1_p1;