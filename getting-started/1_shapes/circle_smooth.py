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
