with Ada.Text_IO;

package body worker is

  task body T1 is
  begin
    loop
      Ada.Text_IO.Put_Line("T1");
    end loop;
  end T1;

  task body T2 is
  begin
    loop
      Ada.Text_IO.Put_Line("T2");
    end loop;
  end T2;

end worker;
