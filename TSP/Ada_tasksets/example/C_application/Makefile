.DEFAULT_GOAL := all

###
## XtratuM definitions
#

include rules.mk

CONTAINER=container.bin
RSW=resident_sw
XCF_XEF=xm_cf.xef.xmc
XCF_BIN=xm_cf.bin.xmc
PART0=partition0
PART0_BIN=$(PART0).bin
PART0_XEF=$(PART0).xef

PART1=partition1
PART1_BIN=$(PART1).bin
PART1_XEF=$(PART1).xef


###
## XM Application Rules
#

all: $(RSW)
	# arm-rtems4.11-objdump -D $(RSW) > $(RSW)_DUMP.S

APP_PATH0=p0/app
APP0=partition0

APP_PATH1=p1/app
APP1=partition1

$(PART0):
	RAM_AREA_START=0x10000000 make -C $(APP_PATH0)
	find ${APP_PATH0} -name ${APP0} -exec cp {} $@ \;

$(PART1):
	RAM_AREA_START=0x14000000 make -C $(APP_PATH1)
	find ${APP_PATH1} -name ${APP1} -exec cp {} $@ \;

clean:
	rm -f resident_sw *.S
	make clean -C $(APP_PATH0)
	make clean -C $(APP_PATH1)

PACK_ARGS=-h $(XMCORE):$(XCF_XEF) -p 0:$(PART0_XEF) -p 1:$(PART1_XEF)

$(CONTAINER): $(PART0_XEF) $(PART1_XEF) $(XCF_XEF)
	$(XMPACK) check $(XCF_XEF) $(PACK_ARGS)
	$(XMPACK) build $(PACK_ARGS) $@

.INTERMEDIATE: $(PART0) $(PART0_XEF) $(PART1) $(PART1_XEF) $(XCF_BIN) $(XCF_XEF) $(CONTAINER)