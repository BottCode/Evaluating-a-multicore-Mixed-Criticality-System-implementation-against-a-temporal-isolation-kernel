#include <string.h>
#include <stdio.h>
#include <xm.h>

#define ITER 30

#define PRINT(...) do { \
        printf("[P%d] ", XM_PARTITION_SELF); \
        printf(__VA_ARGS__); \
} while (0)

void print_to_c ()
{
    PRINT ("HEELLOO");
}