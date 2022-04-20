# Start Here

One of the things that makes the PiCar-X so extraordinary is that the setup is as fun and educational as working with the finished product. Sunfounder has made it really easy to follow their instructions and get started. 

Below you will find a roadmap to getting started with their instructions and a few tips from us based on our experience. 

## Get Car

Sunfounder sells the [PiCar-X AI Car kit](https://amzn.to/3uKSQp1) on Amazon. 

The kit comes with everything you need except the Raspberry Pi, batteries, and battery charger. It comes with all the parts for the car and even a few spare parts. Plus, the kit has a screw driver and allen wrench.

## Get Raspberry Pi

The Raspberry Pi is sold separately. You can buy it on Amazon too. Look for Rasperry Pi 4 starter kits, like [this one](https://amzn.to/3L1feA7) and [this one](https://amzn.to/3jP7NQL). 

[![raspberry-pi-kit-1](//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B09W7P91SP&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=jungle-memory-20&language=en_US)](https://amzn.to/3L1feA7) [![raspberry-pi-kit-2](//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B09LYP7QH3&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=jungle-memory-20&language=en_US)](https://amzn.to/3jP7NQL)

These kits come with the essentials you need to work with the car. Specifically, a Raspberry Pi 4 with Wifi and an SD card. 

They also come with a charging cord and case. Although you do not need the power cord and case for the car, they are good to have. 

## Get Batteries

The batteries power the Raspberry Pi and the Sunfounder robot sensor hat that comes with the PiCar-X kit. You can buy the batteries online. They need to be 18650 rechargeable lithium batteries, [like this example](https://amzn.to/36rkspL).

[![rechargeable-lithium-battery](//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B09PFVPS7J&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=jungle-memory-20&language=en_US)](https://amzn.to/36rkspL)

The PiCar-X requries two batteries to run. Consider buying at least 4 batteries so that you can charge two while using two.

You can get a [battery charger like this one](https://amzn.to/385Qf05).

[![lithium-battery-charger](//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B08XQSSRZK&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=jungle-memory-20&language=en_US)](https://amzn.to/385Qf05)

## Build Car

Sunfounder makes it really easy to assemble the car with their amazing instructions. 

The [instructions are online](https://docs.sunfounder.com/projects/picar-x/en/latest/list_and_assembly.html) and the kit comes a written copy.

They walk you through how to connect the parts and wire the car. 

You do things like add the Raspberry Pi, robot HAT, battery pack, motors, servos, wheels, sensors, and camera to the car's frame. You also wire the car. If it is your first time building something like this, expect it to take a couple of hours. 

When assembling the car, pay close attention to detail. We encourage you to disassemble and reassemble the parts if you need to or if you just want to learn more about the parts.

Here are a few tips. 

- put one battery ribbon under each battery so that you can use the ribbon to remove the battery
- the camera FFC cable needs to twist so that it can make the proper connections on both ends
- try to align the servo motors so that they are pointing in correct angle to start
- remember to zero the servos using P11 before installing and running the code
- when you test the car, if the rear-wheel motors run in the wrong direction, take them off and switch sides

## Install Software

Sunfounder has excellent instructions for installing the software. 

You have two options.

You can install [Ezblock](https://docs.sunfounder.com/projects/picar-x/en/latest/ezblock/play_with_ezblock.html). It is Sunfounder's software for helping beginners program on a Raspberry Pi and offers two environments. You can use the Ezblock Graphical User Interface environment and a command-line Python environment.

Instead, you can install [the Python environment](https://docs.sunfounder.com/projects/picar-x/en/latest/python/play_with_python.html). It is Sunfounder's Python setup for programming on a Raspberry Pi with the robot HAT and PiCar-X.

Regardless, to install the software, you need to turn on the Raspberry Pi and access its operating system as explained in the instructions.

## Test Car

Test the car by running the Sunfounder code examples for either [Ezblock](https://docs.sunfounder.com/projects/picar-x/en/latest/ezblock/play_with_ezblock.html) or [Python](https://docs.sunfounder.com/projects/picar-x/en/latest/python/play_with_python.html).

You need to access the Raspberry Pi operating system to access the code examples as explained in the Sunfounder instructions.

Start with the `calibration` example to make sure the motors work and spin in the right direction. Also check the servos to make sure they work.

Finally, have fun running the other examples!
