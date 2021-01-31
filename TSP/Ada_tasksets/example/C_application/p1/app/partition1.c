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
    
    while ( 1 ) {
      ;
    }

};
