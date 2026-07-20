all: build_dir compile_kernel compile_shell compile_desktop bundle_kernel

build_dir:
	mkdir -p build

compile_kernel:
	$(MAKE) -C kernel

compile_shell:
	$(MAKE) -C shell

compile_desktop:
	$(MAKE) -C python

bundle_kernel: build_dir
	cat kernel/boot/boot.bin build/kernel.bin > build/avocet.bin

run: build_dir compile_kernel compile_shell bundle_kernel
	qemu-system-i386 -drive format=raw,file=build/avocet.bin

desktop: build_dir compile_desktop
	./build/avocet_desktop.exe

clean:
	$(MAKE) -C kernel clean
	$(MAKE) -C shell clean
	$(MAKE) -C python clean
	rm -rf build
