/* 
 *  COPYRIGHT (c) 1989-2007.
 *  On-Line Applications Research Corporation (OAR).
 *
 *  The license and distribution terms for this file may be
 *  found in the file LICENSE in this distribution or at
 *  http://www.rtems.com/license/LICENSE.
 *
 *  $Id$
 */
/*  updated for triple test, 20003/11/06, Erik Adli */

#include "system.h"
#include <stdio.h>
#include <stdlib.h>

/* CPU usage and Rate monotonic manger statistics */
#include "rtems/cpuuse.h"

// Periods for the various tasks [seconds]
#define PERIOD_TASK_ABSOLUTE           1
#define PERIOD_TASK_RATE_MONOTONIC     2
#define PERIOD_TASK_RELATIVE           3



// TASK 1

rtems_task Task_Periodic(
  rtems_task_argument unused
)
{
    rtems_name        name;
    rtems_id          period;
    rtems_status_code status;
    name = rtems_build_name( 'P', 'E', 'R', 'D' );
    status = rtems_rate_monotonic_create( name, &period );

    while ( 1 ) {
        //  1 tick are 500 microseconds. Check CONFIGURE_MICROSECONDS_PER_TICK in system.h
        rtems_rate_monotonic_period( period, 2000 );  //  2000 ticks = 1000000 microseconds = 1000 milliseconds

        /* Perform some periodic actions */
        //  XmConsolePutChar ('X');  //  warning: implicit declaration of function 'XmConsolePutChar' [-Wimplicit-function-declaration]
        //  XM_write_console ("XM_write_console"); //  warning: implicit declaration of function 'XM_write_console' [-Wimplicit-function-declaration]
        printf("printf");
        printk("printk");
    }

};
