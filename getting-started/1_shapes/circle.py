
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
