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

## Circle

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


