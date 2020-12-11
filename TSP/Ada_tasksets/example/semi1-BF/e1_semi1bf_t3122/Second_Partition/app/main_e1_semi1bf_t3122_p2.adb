with System;
with Periodic_Tasks;

with taskset_e1_semi1bf_t3122;
pragma Unreferenced (taskset_e1_semi1bf_t3122);

procedure main_e1_semi1bf_t3122_p1 is
    pragma Priority (System.Priority'Last);
begin
    Periodic_Tasks.Init;
end main_e1_semi1bf_t3122_p1;