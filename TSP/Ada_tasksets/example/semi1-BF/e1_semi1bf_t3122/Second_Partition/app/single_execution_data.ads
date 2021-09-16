package Single_Execution_Data is
	pragma Preelaborate;

	Numb_Of_Partitions : Positive := 2;

	Experiment_Hyperperiods : array (1 .. Numb_Of_Partitions) of Natural := (1 => 113400000, 2 => 37800000);

	Id_Experiment : Integer := 1;
	Approach : String := "SEMI2BF";
	Taskset_Id : Integer := 7;
	Partition_Id : String := "P2";

	Id_Execution : String := "e1_semi2bf_t3122";

	--  Needed to plot diagrams. These data are stored as strings in order to avoid issue related
	--  to differents types representations in differents languages (Python and Ada).
	Taskset_Size : String := "12";
	Taskset_Utilization : String := "1.8";
	Criticality_Factor : String := "2";
	HI_Crit_Proportion : String := "0.5";

end Single_Execution_Data;