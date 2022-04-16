
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
