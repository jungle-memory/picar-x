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

