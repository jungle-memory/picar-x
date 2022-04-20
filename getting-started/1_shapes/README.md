# Driving Shapes

Programming the PiCar-X to drive is really fun.

Sunfounder makes it easy to learn how to program the car to move.

Starting with the code examples in the [Ezblock](https://docs.sunfounder.com/projects/picar-x/en/latest/ezblock/play_with_ezblock.html) and [Python](https://docs.sunfounder.com/projects/picar-x/en/latest/python/play_with_python.html), you can use their code that makes the car drive to understand how you can program the car to drive.

Start with the `move` example.

Here is a video showing it.

###### https://www.youtube.com/embed/rK63L7JGiEs

## Starting With Examples

Starting with this example is a great way to learn how to program the PiCar-X to move.

To help you get started and to inspire you to create, this project folder contains additional code examples for programming the PiCar-X to drive in various shapes or patterns.

When reading and writing the code, think about how the speed and servo angles impact one another and the car's behavior. Also consider what limitations the car has, like turning radius, acceleration, top speed, and others.

Feel free to use and modify the code below.

Post videos on Instagram and YouTube and tag us or hashtag #junglememory!

## Circle Smooth

```python
from picarx import Picarx
import time


if __name__ == "__main__":
    try:
        px = Picarx()
        counter = 0
        threshold = 12
        px.forward(27)
        px.set_dir_servo_angle(30)

        while counter < threshold:
            time.sleep(4)
            counter = counter + 1

    finally:
        px.forward(0)
```

###### https://www.youtube.com/embed/L6SAVV-i7IA

## Circle Right Turns

```python

from picarx import Picarx
import time


if __name__ == "__main__":
    try:
        px = Picarx()
        counter = 0
        threshold = 6

        while counter < threshold:

            px.forward(20)
            time.sleep(0.1)

            for angle in range(0,45):
                px.set_dir_servo_angle(angle)
                time.sleep(0.02)

            for angle in range(0,45):
                px.set_dir_servo_angle(angle)
                time.sleep(0.02)

            for angle in range(0,45):
                px.set_dir_servo_angle(angle)
                time.sleep(0.02)
            
            for angle in range(0,45):
                px.set_dir_servo_angle(angle)
                time.sleep(0.02)

            counter = counter + 1

    finally:
        px.forward(0)
```

###### https://www.youtube.com/embed/oCXH_EwoArQ

## Oval

```python

from picarx import Picarx
import time


if __name__ == "__main__":
    try:
        px = Picarx()
        counter = 0
        threshold = 4
        px.set_dir_servo_angle(0)
        px.forward(20)
        time.sleep(2)

        while counter < threshold:
            px.forward(23)

            for angle in range(0,38):
                px.set_dir_servo_angle(angle)
                time.sleep(0.0275)

            for angle in range(0,38):
                px.set_dir_servo_angle(angle)
                time.sleep(0.0275)

            for angle in range(0,38):
                px.set_dir_servo_angle(angle)
                time.sleep(0.0275)

            px.set_dir_servo_angle(0)
            px.forward(20)
            time.sleep(2)
            counter = counter + 1

    finally:
        px.set_dir_servo_angle(0)
        px.forward(0)
```
###### https://www.youtube.com/embed/_YTO8IhbrhY

## U-Turn

```python

from picarx import Picarx
import time


if __name__ == "__main__":
    try:
        px = Picarx()
        counter = 0
        threshold = 1
        px.set_dir_servo_angle(0)
        px.forward(30)
        time.sleep(0.5)
        px.forward(60)
        time.sleep(3)
        px.forward(30)
        time.sleep(0.2)

        while counter < threshold:
            px.forward(23)

            for angle in range(0,38):
                px.set_dir_servo_angle(angle)
                time.sleep(0.0275)

            for angle in range(0,38):
                px.set_dir_servo_angle(angle)
                time.sleep(0.0275)

            for angle in range(0,38):
                px.set_dir_servo_angle(angle)
                time.sleep(0.0275)

            px.set_dir_servo_angle(0)
            px.forward(20)
            time.sleep(2)
            counter = counter + 1

    finally:
        px.set_dir_servo_angle(0)
        px.forward(0)
```

## Zig Zag

```python
from picarx import Picarx
import time


if __name__ == "__main__":
    try:
        px = Picarx()
        px.set_dir_servo_angle(0)
        px.forward(30)
        time.sleep(0.5)
        for angle in range(0,50):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        for angle in range(-50,0):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        px.forward(0)
        time.sleep(0.01)
         
        px.forward(30)
        time.sleep(0.5)
        for angle in range(-50,0):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        for anlge in range(0,50):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        px.forward(0)
        time.sleep(0.01)

        px.forward(30)
        time.sleep(0.5)
        for angle in range(-50,0):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        for angle in range(-50,0):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        px.forward(0)
        time.sleep(0.01)
         
        px.set_dir_servo_angle(0)
        px.forward(30)
        time.sleep(0.5)
        for angle in range(0,50):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        for anlge in range(0,50):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        px.forward(0)
        time.sleep(0.01)

        for angle in range(0,35):
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(35,-35,-1):
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(-35,0):
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(0,35):
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)
        for angle in range(35,-35,-1):
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)        
        for angle in range(-35,0):
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)
            
    finally:
        px.forward(0)
```

###### https://www.youtube.com/embed/xl5kr4h9m3s
