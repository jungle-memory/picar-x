
from picarx import Picarx
import time
import picamera

if __name__ == "__main__":
    try:
        px = Picarx()
        camera = picamera.PiCamera()
        camera.resolution = (640, 480)
        camera.start_recording('forward.h264')
        
        counter = 0
        threshold = 4
        px.set_dir_servo_angle(0)
        px.forward(20)
        time.sleep(4)

        camera.stop_recording()

    finally:
        px.set_dir_servo_angle(0)
        px.forward(0)
