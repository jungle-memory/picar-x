
from picarx import Picarx
import time
import picamera

if __name__ == "__main__":
    try:
        px = Picarx()
        camera = picamera.PiCamera()
        camera.resolution = (640, 480)
        camera.start_recording('my_video.h264')
        
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

        camera.stop_recording()

    finally:
        px.set_dir_servo_angle(0)
        px.forward(0)
