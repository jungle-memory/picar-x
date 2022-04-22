# Sensors

The PiCar-X has an ultrasonic sensor and a grayscale sensor.

The ultrasonic sensor detects distance from objects within its range. You can use it with PiCar-X to avoid crashing into objects or know when something approaches the car.

[![ultrasonic-sensor-raspberry-pi](//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B01JG09DCK&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=jungle-memory-20&language=en_US)](https://amzn.to/3L1feA7)

The grayscale sensor can detect black, white, and shades of gray. You can use it with PiCar-X to make the car follow a black or white line.

[![grayscale-sensor-raspberry-pi](//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07VY254N8&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=jungle-memory-20&language=en_US)](https://amzn.to/3jP7NQL)

Starting with the code examples in the [Ezblock](https://docs.sunfounder.com/projects/picar-x/en/latest/ezblock/play_with_ezblock.html) and [Python](https://docs.sunfounder.com/projects/picar-x/en/latest/python/play_with_python.html), you can use their sensor code to understand how you can program the car to use the sensors.

## Starting With Examples

A great way to learn how to program the PiCar-X to use the ultrasonic sensor is to start with [the `obstacle avoidance` example](https://docs.sunfounder.com/projects/picar-x/en/latest/python/python_avoid.html). 

A great way to learn how to program the PiCar-X to use the grayscale sensor is to start with [the `line tracking` example](https://docs.sunfounder.com/projects/picar-x/en/latest/python/python_line_track.html). 

Read the code to understand how it works. Then run it!

To help you get started and to inspire you to create your own scripts for the car, this project folder contains additional code examples for programming the PiCar-X to drive in various shapes or patterns.

When reading and writing the code, think about the interaction of the sensor data with what the motors and servers are doing. Also consider what limitations the sensors have, like how far and wide the ultrasonic sensors can detect signals and the sensitivity of the grayscale sensor.

Feel free to use and modify the code below.

Post videos on Instagram and YouTube and tag us or hashtag #junglememory!

## Avoid Left Right

```python
from picarx import Picarx
import time


def main():
    try:
        px = Picarx()
        # px = Picarx(ultrasonic_pins=['D2','D3']) # tring, echo
        px.forward(30)
        time.sleep(0.3)
        readjust = False
        while True:
            distance = px.ultrasonic.read()
            print("distance: ",distance)
            if distance > 0 and distance < 300:
                if distance < 50:
                    px.set_dir_servo_angle(-35)
                    readjust = True
                elif readjust == True:
                    px.set_dir_servo_angle(0)
                    time.sleep(1)
                    px.set_dir_servo_angle(35)
                    time.sleep(1)
                    px.set_dir_servo_angle(-35)
                    time.sleep(1)
                    px.set_dir_servo_angle(0)
                    readjust = False
                else:
                    px.set_dir_servo_angle(0)
            
    finally:
        px.forward(0)
```

###### https://www.youtube.com/embed/zvEG26c9SHY

###### https://www.youtube.com/embed/1AjgXbDf1DI
