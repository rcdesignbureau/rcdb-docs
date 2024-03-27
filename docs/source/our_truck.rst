#########
Our Truck
#########

**This project seeks to take an RC offroad race truck and make it drive itself!**


Software
########

Python
______
The main driving portion of the code, the one which interacts with the GPIO is written in Python.
This is due to the fact that Python is well-supported with GPIO libraries. Python is also used to write the logs to the web server page.

Rust
_____
Rust is used to write nearly everything else on the car, namely the server software and the vision, the two things that
need to be well-optimized. These things could not be written in Python, so they are written in Rust with FFI bindings that
allows them to be called in the main Python code.

OS
_____
Our SBC (Single-Board Computer) for this project runs Ubuntu 22.04 Minimal with Linux kernel 5.10-rockchip. It has KDE plasma installed on
it if plugging a monitor in would ever be necessary. Running Linux on a robot controller versus another operating system such as Android
(present on REV Robotics Control Hubs) has many advantages, such as being able to compile Rust code on the SBC itself, rather than having to
upload pre-compiled binaries and thus have to install bulky GNU ARM toolchains to an x86_64 PC.



Hardware
########

Truck
_____

For this project, our choice of RC platform was different from most comparable projects, since we did not build
on top of a `Traxxas Slash 4x4 <https://traxxas.com/products/showroom?f[0]=field_type%3A250>`_ variant, instead choosing a kit-only race chassis,
the `Tekno RC SCT410.3 <https://www.teknorc.com/shop/tkr5507-sct410-3-110th-4wd-competition-short-course-truck>`_. This chassis, although belonging
to the same 4wd SCT category as the Traxxas Slash 4x4, has a much lower center of gravity, larger bore oil-filled shocks, coarser gear pitch to handle
much more motor load and power, and has much more rigid bumpers and crash bars.

Compute Element
_______________

Here, we used a `Radxa ROCK 5B <https://radxa.com/products/rock5/5b/>`_ (8GB RAM) as our robot controller. This single-board computer has plenty of
processing power, possessing an 8-core CPU, 1 TFLOPS GPU, and 6 TOPS NPU for AI processing. In order to be able to efficiently run two OpenCV camera
streams in tandem, we had to pick a board that had the highest performance per watt in its category. The ROCK 5B's GPIO pins make it easy to control
the PWM motor controller and servo on the truck, allowing us to directly modify the throttle or steering position from code.

3D Printed Parts
________________

Naturally, for such a project, next to none of the custom parts we needed were already designed by others. Due to this project, to our knowledge, being
the only one of its kind to not utilize a Traxxas chassis, we had to design all the brackets and mounts for the webcams and compute element ourselves.