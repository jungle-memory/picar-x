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
