with System.Multiprocessors; use System.Multiprocessors;

package worker is

  task type T1 with CPU => CPU'First;
  task type T2 with CPU => CPU'Last;

  WORK_1 : T1;
  WORK_2 : T2;

end worker;
