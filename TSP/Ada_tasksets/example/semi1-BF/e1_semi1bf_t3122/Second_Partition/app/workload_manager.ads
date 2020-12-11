package Workload_Manager is

    --  Get task "ID" 's workload for its I-th job release. 
    function Get_Workload (ID : Natural; I : Natural) return Positive;

end Workload_Manager;