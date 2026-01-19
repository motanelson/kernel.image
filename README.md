kernel linux

Attention, version 6 this project can only be used for educational and non-commercial purposes; it cannot be sold. It is only for young people to learn how Linux works. The vmlinuz and initrd.img files are part of an operating system and must be compiled from scratch to be distributed commercially.


Linux Kernel 2.x – Overview and Advantages
The Linux Kernel 2.x series, released between 1996 and 2011, represents one of the most important eras in the history of Linux. During this long-lived branch, Linux evolved from a simple Unix-like kernel into a mature, stable, and highly scalable operating system core, suitable for desktops, servers, and embedded systems.
Key Advantages
One of the main strengths of the 2.x kernel series is its stability. Many versions of the 2.x kernel were widely adopted in production environments and remained in use for years. This makes it an excellent choice for systems that prioritize reliability over constant change.
Another major advantage is its low hardware requirements. Kernel 2.x runs efficiently on older computers, making it ideal for lightweight Linux distributions, recovery systems, educational projects, and legacy hardware.
Core Properties and Features
Monolithic kernel design with loadable modules
Strong process and memory management
Support for multiple architectures (x86, ARM, PowerPC, MIPS, and more)
Mature network stack with IPv4 and IPv6 support
Extensive filesystem support (ext2, ext3, FAT, ISO9660, NFS, etc.)
Highly configurable through compile-time options
Proven security model based on Unix permissions
Why Kernel 2.x Still Matters
The Linux 2.x kernel represents the golden era of classic Linux systems. It is well-documented, predictable, and ideal for custom Linux builders who want full control over the system, minimal abstraction, and a deep understanding of how Linux works internally.
For projects focused on simplicity, transparency, and education, the 2.x kernel remains a solid and respected foundation.
 👍


.
Boot Process Overview: ISOLINUX, vmlinuz and initrd
This project is designed as an educational Linux builder, allowing users to observe, experiment and understand how a Linux system boots and how a distribution is constructed.
This section explains the role of ISOLINUX, vmlinuz, initrd.gz and linuxrd, which are fundamental components of the boot process.
ISOLINUX
ISOLINUX is a bootloader used mainly for bootable ISO images (CD/DVD/USB).
It is part of the SYSLINUX bootloader family.
ISOLINUX is responsible for:
Starting the boot process
Presenting a boot menu (if configured)
Loading the Linux kernel and the initial RAM disk into memory
ISOLINUX does not run Linux itself.
Its only job is to prepare the system and pass control to the Linux kernel.
Typical ISOLINUX configuration files:
isolinux.cfg
menu.cfg
These files define:
Which kernel to boot
Which initrd to load
Kernel parameters (boot options)
vmlinuz (Linux Kernel)
vmlinuz is the compressed Linux kernel.
The kernel is the core of the operating system and is responsible for:
Hardware detection
CPU and memory management
Device drivers
Starting the first user-space process
When ISOLINUX loads vmlinuz, the kernel:
Decompresses itself into memory
Initializes hardware
Looks for an initial root filesystem (initrd / initramfs)
Without a kernel, Linux cannot exist.
initrd.gz / linuxrd (Initial RAM Disk)
initrd.gz (sometimes named linuxrd) is a compressed temporary root filesystem loaded into RAM.
Its purpose is to:
Prepare the system before the real root filesystem is mounted
Load necessary kernel modules (storage, filesystem, USB, etc.)
Locate and mount the real system image
Hand over control to the main system
The initrd usually contains:
A minimal filesystem
BusyBox or similar tools
Boot scripts (init)
Mount logic and hardware detection
After its job is done, the system switches from the initrd to the real root filesystem.
Boot Flow Summary
The boot process works in this order:
BIOS / UEFI starts the bootloader
ISOLINUX loads:
vmlinuz (Linux kernel)
initrd.gz or linuxrd
Linux kernel starts and initializes hardware
initrd runs early boot scripts
The real Linux system is mounted and started
This separation allows experimentation, modular design and educational exploration.
Educational Purpose
By separating:
Bootloader
Kernel
Initial RAM filesystem
System and data images
This builder encourages users to:
Observe how Linux starts
Modify and experiment safely
Create their own Linux distributions
Learn Linux internals through practice
Linux is not a black box — it is a system meant to be studied.
