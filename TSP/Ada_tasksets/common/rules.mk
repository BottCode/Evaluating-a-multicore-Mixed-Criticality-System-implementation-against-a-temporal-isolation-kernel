XTRATUM_PATH=/opt/sdk-xm-arm-205-cora/xm

include $(XTRATUM_PATH)/lib/dot.config

include $(XTRATUM_PATH)/xmconfig
include $(XTRATUM_PATH)/version
include $(XTRATUM_PATH)/lib/rules.mk

#PATHS
XMBIN_PATH=$(XTRATUM_PATH)/bin
XMCORE_PATH=$(XTRATUM_PATH)/lib

# APPLICATIONS
XMCPARSER=$(XMBIN_PATH)/xmcparser
XMPACK=$(XMBIN_PATH)/xmpack
RSWBUILD=$(XMBIN_PATH)/rswbuild
XEF=$(XMBIN_PATH)/xmeformat build

# XM CORE
XMCORE_ELF=$(XMCORE_PATH)/xm_core
XMCORE_BIN=$(XMCORE_PATH)/xm_core.bin
XMCORE=$(XMCORE_PATH)/xm_core.xef

# LIBRARIES
LIB_XM=-lxm

#XM_CF
XMCF ?= xm_cf.$(ARCH).xml

ifdef CONFIG_XEF_COMPRESSION
XEF_FLAGS += -c
endif

# RULES
%.xef: %
	$(XEF) $< $(XEF_FLAGS) -o $@

%.xef.xmc: %.bin.xmc
	$(XEF) -m $< $(XEF_FLAGS) -o $@

xm_cf.bin.xmc: $(XMCF)
	$(XMCPARSER) -o $@ $^

xm_cf.c.xmc: $(XMCF)
	$(XMCPARSER) -c -o $@ $^

resident_sw: container.bin
	$(RSWBUILD) $^ $@
	chmod +x $@

distclean: clean
	@$(RM) ∗~

clean:
	@$(RM) container.bin resident_sw xm_cf xm_cf.bin xm_cf.∗.xmc
	@$(RM) ∗.o ∗.∗.xmc dep.mk