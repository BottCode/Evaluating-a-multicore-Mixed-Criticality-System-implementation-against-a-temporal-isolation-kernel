with RTEMS.TASKS;

package Set_Of_Procedures is

    procedure T_5_Body (ARGUMENT : in RTEMS.TASKS.ARGUMENT);
    pragma Convention (C, T_5_Body);

    procedure T_10_Body (ARGUMENT : in RTEMS.TASKS.ARGUMENT);
    pragma Convention (C, T_10_Body);

    procedure T_11_Body (ARGUMENT : in RTEMS.TASKS.ARGUMENT);
    pragma Convention (C, T_11_Body);

    procedure T_7_Body (ARGUMENT : in RTEMS.TASKS.ARGUMENT);
    pragma Convention (C, T_7_Body);
    
    procedure T_9_Body (ARGUMENT : in RTEMS.TASKS.ARGUMENT);
    pragma Convention (C, T_9_Body);

    procedure LAST (ARGUMENT : in RTEMS.TASKS.ARGUMENT);
    pragma Convention (C, LAST);

end Set_Of_Procedures;