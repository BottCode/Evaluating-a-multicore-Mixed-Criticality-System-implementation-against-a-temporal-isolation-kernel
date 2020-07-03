cd bb-runtimes
exec ./build_rts.py --output=temp --bsps-only zynq7000

gprbuild -P temp/BSPs/ravenscar_full_zynq7000.gpr -j0 -f 
mkdir ../runtime/arm-eabi/lib/gnat/ravenscar_full_zynq7000 -p
gprinstall -P temp/BSPs/ravenscar_full_zynq7000.gpr -p -f -XPREFIX=$PWD/../runtime/arm-eabi/lib/gnat/ravenscar_full_zynq7000

cd ..

mv runtime/arm-eabi/lib/gnat/ravenscar_full_zynq7000/adalib/ravenscar_full_zynq7000/* runtime/arm-eabi/lib/gnat/ravenscar_full_zynq7000/adalib/
rm -rf runtime/arm-eabi/lib/gnat/ravenscar_full_zynq7000/adalib/ravenscar_full_zynq7000/

mv runtime/arm-eabi/lib/gnat/ravenscar_full_zynq7000/gnat/ravenscar_full_zynq7000/* runtime/arm-eabi/lib/gnat/ravenscar_full_zynq7000/gnat/
rm -rf runtime/arm-eabi/lib/gnat/ravenscar_full_zynq7000/gnat/ravenscar_full_zynq7000/

