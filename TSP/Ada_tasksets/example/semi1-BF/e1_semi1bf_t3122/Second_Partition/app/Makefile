PROGRAM=main_e1_semi1bf_t3122_p2

#
#  Makefile for Empty Ada program example
#
#  See README.Makefiles in the main ada-examples directory.
#
#  $Id: Makefile,v 1.2 2009/09/17 18:13:40 joel Exp $
#

BUILD_DIR=o-optimize

include $(RTEMS_MAKEFILE_PATH)/Makefile.inc
include $(RTEMS_CUSTOM)
include $(PROJECT_ROOT)/make/leaf.cfg

# stack size for the first Ada thread
CFLAGS +=-DGNAT_MAIN_STACKSPACE=100

# initialize the network stack -- assumes existence of networkconfig.h
# CFLAGS +=-DMAIN_USE_NETWORKING=1

# Should we prompt for command line arguments?
# DEFINES +=-DMAIN_USE_REQUIRES_COMMAND_LINE

# If you want to hard-code the command line, define this to a string
# DEFINES += -DMAIN_COMMAND_LINE="ARGS"

#
#  Subdirectory makefiles do some setup, then we get here
#
#  $Id: Makefile.shared,v 1.15 2011/02/08 16:53:23 joel Exp $
#

# Tool helpers
SPECFLAGS = -B${RTEMS_MAKEFILE_PATH}/lib/ -specs=bsp_specs -qrtems
CFLAGS =


# Some tests need to be able to do a gethostbyname
ifeq ($(NEED_ROOTFS_FOR_HOST_INFO),yes)
  CLEAN_ADDITIONS += FilesystemImage FilesystemImage.c FilesystemImage.h
  FILESYSTEM_OBJS  = FilesystemImage.o
  FILESYSTEM_SRCS  = FilesystemImage.h
  CFLAGS          += -DENABLE_UNTAR_ROOT_FILESYSTEM -I.
endif

ifeq ($(NEED_NETWORK),yes)
#NETWORK_HFILE= ../networkconfig_$(RTEMS_BSP).h 
#NETWORK_HFILE= ../networkconfig.h
endif


DEFINES += -D$(RTEMS_BSP)
CFLAGS += $(DEFINES)
LINKARGS += -Wl,--defsym=_RAM_START=0x14000000

RTS= --RTS=$(shell $(CC) -print-multi-directory $(CFLAGS))

all:  $(PROGRAM)
		#$(RTEMS_MAKEFILE_PATH)
		arm-rtems4.11-nm -g -n $(PROGRAM) > $(PROGRAM).num
		cp $(PROGRAM) $(PROGRAM).ralf
		#arm-rtems4.11-objdump $(PROGRAM) -D > $(PROGRAM)_DUMP.S
		arm-rtems4.11-size $(PROGRAM)
		rm -rf $(BUILD_DIR)
		mkdir $(BUILD_DIR)
		#mv *".num" *".exe" *".obj" *".bin" *".bt" *".gba" *".ralf" "b~"*"."*  *".o" *".ali" *".S" $(PROGRAM) $(BUILD_DIR)


joel:
	@echo CFLAGS=$(CFLAGS)
	@echo CC=$(CC)
	@echo RTS=$(RTS)
	$(CC) -print-multi-directory $(CFLAGS)
	$(CC) -mcpu=403 -print-multi-directory

$(PROGRAM): rtems_init.o $(FILESYSTEM_OBJS) $(EXTRA_OBJS)
	$(AS:as=gnatmake) $(CPU_CFLAGS) $(RTS) -g -v $(EXTRA_GNATFLAGS) \
            -I$(RTEMS_MAKEFILE_PATH)/lib/include/adainclude \
 	    -O -gnata -gnatE -gnato -g $(PROGRAM) -o $(@) \
	    -bargs -Mgnat_main \
	    -largs $(SPECFLAGS) $(CFLAGS) $(LINKARGS) \
		rtems_init.o $(FILESYSTEM_OBJS) \
	     $(EXTRA_OBJS)
ifeq ($(RTEMS_BSP_FAMILY),pc386)
	$(OBJCOPY) -O binary $(@) $(@).bin
	$(RTEMS_MAKEFILE_PATH)/build-tools/bin2boot -v $(@).bt $(HEADERADDR) \
          $(START16FILE) $(START16ADDR) 0 $(@).bin $(RELOCADDR) 0
endif
ifeq ($(RTEMS_BSP),icecube)
	$(OBJCOPY) -R -S -O binary obj/$(PROGRAM) obj/$(PROGRAM).bin
	cat obj/$(PROGRAM).bin | gzip -9 >obj/$(PROGRAM).gz
	mkimage \
	  -A ppc -O rtems -T kernel -a 0x40000 -e 0x40000 -n "RTEMS" \
	  -d obj/$(PROGRAM).gz obj/$(PROGRAM).img 
	cp obj/$(PROGRAM).img ../../../../tftpboot/main.img
	rm -f obj/$(PROGRAM).gz obj/$(PROGRAM).img
endif

rtems_init.o: ../rtems_init.c $(FILESYSTEM_SRCS) $(NETWORK_HFILE)
	$(CC) $(CFLAGS) -g -I. $(CPU_CFLAGS) -c $<

ifeq ($(NEED_ROOTFS_FOR_HOST_INFO),yes)
FilesystemImage: ../rootfs/etc/host.conf ../rootfs/etc/hosts
	(cd ../rootfs ; tar cf - \
	  --exclude CVS --exclude .cvsignore --exclude .svn .) >$(@)

FilesystemImage.c FilesystemImage.h: FilesystemImage
	$(PROJECT_ROOT)/bin/rtems-bin2c FilesystemImage FilesystemImage

FilesystemImage.o: FilesystemImage.c
	$(CC) $(CFLAGS) $(CPU_CFLAGS) -c $<
endif

clean:
	rm -f obj/*
	rm -f b~*.*  *.o *.ali $(PROGRAM)
	rm -f *.num *.exe *.obj *.bin *.bt *.gba *.ralf *.S
	#rm $(BUILD_DIR)
	

