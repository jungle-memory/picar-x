# Driving Shapes

Programming the PiCar-X to drive is really fun.

The example code for [Ezblock](https://docs.sunfounder.com/projects/picar-x/en/latest/ezblock/play_with_ezblock.html) and [Python](https://docs.sunfounder.com/projects/picar-x/en/latest/python/play_with_python.html) comes with some that make the car drive.

Star with the `move` example.

Here is a video showing it.

###### https://www.youtube.com/embed/rK63L7JGiEs

# Additional Examples

This project folder contains code for programming the PiCar-X to drive in various shapes or patterns.

Feel free to use and modify the code.

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


