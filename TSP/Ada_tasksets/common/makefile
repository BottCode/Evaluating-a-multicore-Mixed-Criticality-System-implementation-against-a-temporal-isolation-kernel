.DEFAULT_GOAL := all

###
## XtratuM definitions
#

include rules.mk

CONTAINER=container.bin
RSW=resident_sw
XCF_XEF=xm_cf.xef.xmc
XCF_BIN=xm_cf.bin.xmc
PART1=first_partition
PART1_BIN=$(PART1).bin
PART1_XEF=$(PART1).xef

PART2=second_partition
PART2_BIN=$(PART2).bin
PART2_XEF=$(PART2).xef


###
## XM Application Rules
#

all: $(RSW)
	# arm-rtems4.11-objdump -D $(RSW) > $(RSW)_DUMP.S

APP_PATH1=First_Partition/app
APP1=first_partition

APP_PATH2=Second_Partition/app
APP2=second_partition

$(PART1):
	RAM_AREA_START=0x10000000 make -C $(APP_PATH1)
	find ${APP_PATH1} -name ${APP1} -exec cp {} $@ \;

$(PART2):
	RAM_AREA_START=0x14000000 make -C $(APP_PATH2)
	find ${APP_PATH2} -name ${APP2} -exec cp {} $@ \;

clean:
	rm -f resident_sw *.S
	make clean -C $(APP_PATH1)
	make clean -C $(APP_PATH2)

PACK_ARGS=-h $(XMCORE):$(XCF_XEF) -p 1:$(PART1_XEF) -p 2:$(PART2_XEF)

$(CONTAINER): $(PART1_XEF) $(PART2_XEF) $(XCF_XEF)
	$(XMPACK) check $(XCF_XEF) $(PACK_ARGS)
	$(XMPACK) build $(PACK_ARGS) $@

.INTERMEDIATE: $(PART1) $(PART1_XEF) $(PART2) $(PART2_XEF) $(XCF_BIN) $(XCF_XEF) $(CONTAINER)