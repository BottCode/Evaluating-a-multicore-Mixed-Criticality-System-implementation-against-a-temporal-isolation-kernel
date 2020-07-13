pragma Profile (Ravenscar);

with worker;

with System.Multiprocessors;

with System.BB.Parameters;

procedure Main is
 Is_Multi : Boolean := System.BB.Parameters.Multiprocessor;
 No_CPU : System.Multiprocessors.CPU := System.Multiprocessors.Number_Of_CPUs;
begin
  loop
    null;
  end loop;
end Main;
