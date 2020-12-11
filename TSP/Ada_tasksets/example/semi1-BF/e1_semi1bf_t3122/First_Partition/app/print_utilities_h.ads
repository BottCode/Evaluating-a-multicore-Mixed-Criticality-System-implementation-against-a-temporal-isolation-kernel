pragma Ada_2005;
pragma Style_Checks (Off);

with Interfaces.C; use Interfaces.C;

package print_utilities_h is

   procedure print_to_c;  -- ./print_utilities.h:1
   pragma Import (C, print_to_c, "print_to_c");

end print_utilities_h;
