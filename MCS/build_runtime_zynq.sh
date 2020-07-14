git submodule update --init --recursive

cd ada-ravenscar-runtime-for-zynq7000-dual-core-supporting-mixed-criticality-systems
mkdir cortex-ar/zynq7000/ravenscar-full/adalib/ -p
mkdir cortex-ar/zynq7000/ravenscar-full/obj -p
mkdir cortex-ar/zynq7000/ravenscar-full/user_srcs

gprbuild -P ravenscar_full_zynq7000.gpr -j0 -f 
mkdir ../runtime/arm-eabi/lib/gnat/ravenscar_full_zynq7000 -p
gprinstall -P ravenscar_full_zynq7000.gpr -p -f -XPREFIX=$PWD/../runtime/arm-eabi/lib/gnat/ravenscar_full_zynq7000 --install-name=ravenscar_full_zynq7000

cd ..


