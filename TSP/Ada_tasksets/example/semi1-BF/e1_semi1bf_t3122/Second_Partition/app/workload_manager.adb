package body Workload_Manager is

	type Workloads is array (Natural range <>) of Positive;
	type Workloads_Access is access all Workloads;

	Workloads_T10 : aliased Workloads := (1822, 1528, 1340, 1301, 1779, 1329, 1476, 1446);
    Workloads_T11 : aliased Workloads := (5573, 5040, 4476, 5035, 5448, 4614, 4688, 3934, 5008);
	Workloads_T7 : aliased Workloads := (808, 754, 643, 823, 891, 794, 627, 836, 835);
    Workloads_T6 : aliased Workloads := (620, 556, 581, 632, 546, 582, 590, 586);
	
    Overall_Workloads : constant array (1 .. 12) of Workloads_Access := (
		10 => Workloads_T10'Access,
		11 => Workloads_T11'Access,
		7 => Workloads_T7'Access,
		6 => Workloads_T6'Access,
        others => Workloads_T6'Access
	);

	--  Get task "ID" 's workload for its I-th job release.
	function Get_Workload(ID : Natural; I : Natural) return Positive is
	begin
		if I in Overall_Workloads (ID)'Range then
			return Overall_Workloads (ID)(I);
		else
			return Overall_Workloads (ID)(0);
		end if;
	end Get_Workload;

end Workload_Manager;